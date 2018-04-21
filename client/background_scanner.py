import commands
import time
import datetime
import os.path
from virus_check import clamav

def time_print(arg):
	timestamp = datetime.datetime.now()
	print "["+str(timestamp)+"] "+arg

def parse_docker_ps(output):
	image_dict = {}
	results = output[1].splitlines()
	# pop the attr line
	results.pop(0)
	for line in results:
		image_name = line.split()[1]
		container_id = line.split()[0]
		if image_name not in image_dict:
			image_dict[image_name] = [container_id]
		else:
			image_dict[image_name].append(container_id)
	# remove redundancy image
	return image_dict

def main():
	vc = clamav()

	while True:
		malware_flag = False
		time_print("do scanning")
		# step 1 list all the image of the running container
		ps_ret = commands.getstatusoutput("docker ps -a")
		image_list = parse_docker_ps(ps_ret)

		## step 2 save tar for each image
		temp_filename = "temp.tar"
		temp_dir = "temp"
		for k, v in image_list.items():
			commands.getoutput("docker save -o " + temp_filename + " "+ k)
			# create temp dir
			commands.getoutput("mkdir -p "+temp_dir)
			# un tar image to temp dir
			commands.getoutput("tar -xvf "+temp_filename+ " -C "+temp_dir)
			# step scan the dir using clamav
			full_path = os.path.abspath(temp_dir)
			malware_list = vc.scan_dir(full_path)
			if len(malware_list) != 0:
				malware_flag = True
				for malware in malware_list:
					time_print("found malware "+ malware)
				# rm container
				for container in v:
					commands.getoutput("docker rm "+container)
					time_print("delete container: "+container)
				# delete docker image
				commands.getoutput("docker image rm -f " + k)
				time_print("remove image: "+k)
			# clean up
			commands.getoutput("rm " + temp_filename)
			commands.getoutput("rm -r " + temp_dir)
		if malware_flag == False:
			time_print("no malicious container/image found")

		# scan every 10 minutes
		time.sleep(1*60)

if __name__ == "__main__":
    main()
