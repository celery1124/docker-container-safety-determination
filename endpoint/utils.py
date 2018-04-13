import subprocess as sub

def get_image_name(js):
	pushed = []
	for event in js['events']:
		if event['action'] == 'push':
			repo=event['target']['repository']
			url=event['request']['host']
			tag=event['target']['tag']
			path=url+'/'+repo+':'+tag
			print(path)
			pushed.append(path)
	return pushed

def pull_image(p):
	print('pulling images....')
	cmd=['docker', 'pull', p]
	s=sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
#	print(s.communicate())

def save_image(p):
	print('saving image...')
	cmd=['docker', 'save', '-o', 'test.tar', p]
	s=sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
#	print(s.communicate())

def export_image(p):
	print('running the container....')
	print('exporting image....')
	cmd=['docker', 'export', '--output=test.tar', p]
	s=sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
#	print(s.communicate())

def untar_image(p):
	print('untaring image....')
	cmd=['tar', '-xvf', 'test.tar', '-C', 'test/']
	sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
#	print(s.communicate())