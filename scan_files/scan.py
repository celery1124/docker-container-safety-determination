import commands

def call_clamscan(cmd):
	ret = commands.getstatusoutput(cmd);
	return ret

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