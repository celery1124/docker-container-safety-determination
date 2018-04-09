import commands
import pyclamd

class clamav:
	def __init__(self):
		try:
			self.cd = pyclamd.ClamdAgnostic()
			self.cd.ping()
		except pyclamd.ConnectionError:
			print "clamav initialize error"
	def scan_file(self, filename):
		ret = self.cd.scan_file(filename)
		if ret is not None:
			return False
		else:
			return True

	def parse_multiscan_ret(self, output):
		malwarelist = []
		if output is not None:
			results = output.keys()
			for line in results:
				malwarelist.append(line)
		return malwarelist

	def scan_dir(self, directory):
		ret = self.cd.multiscan_file(directory)
		return self.parse_multiscan_ret(ret)

	

# Deprecated API
'''
def parse_clamscan_ret(output):
	whitelist = []
	blacklist = []
	results = output[1].splitlines()
	for line in results:
		status = line.split()
		status = status[len(status)-1]
		if(status == 'OK'):
			whitelist.append(line.split(':')[0])
		elif(status == 'FOUND'):
			blacklist.append(line.split(':')[0])
	return {'whitelist': whitelist, 'blacklist':blacklist}


def call_clamscan(cmd):
	ret = commands.getstatusoutput(cmd);
	return ret

def scan_file(filename):
	basic_cmd = 'clamscan --no-summary '
	ret = call_clamscan(basic_cmd + filename)
	result = parse_clamscan_ret(ret)
	if not result['blacklist']:
		return True
	else:
		return False

def scan_dir(path):
	basic_cmd = 'clamscan -r --no-summary '
	ret = call_clamscan(basic_cmd + path)
	return parse_clamscan_ret(ret)
'''