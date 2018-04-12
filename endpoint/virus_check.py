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

# return True for ok file, False for virus file
def virus_check_file(file_path):
	md = clamav();
	ret = md.scan_file(file_path)
	return ret