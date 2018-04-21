import subprocess as sub
import os
import constants

def get_image_name(js):
	pushed, names, digests = [], [], []
	for event in js['events']:
		if event['action'] == 'push':
			repo=event['target']['repository']
			print(repo)
			url=event['request']['host']
			print(url)
			digest=event['target']['digest']
			#tag=event['target']['tag']
			#print(tag)
			#path=url+'/'+repo+':'+tag
			path=url+'/'+repo
			print(path)
			pushed.append(path)
			names.append(repo)
			digests.append(digest)
	return pushed, names, digests

def pull_image(p):
	print('pulling images....')
	cmd=['docker', 'pull', p]
	s=sub.call(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
#	print(s.communicate())

def save_image(p):
	print('saving image...')
	cmd=['docker', 'save', '-o', 'test.tar', p]
	print(cmd)
	s=sub.call(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
#	print(s.communicate())

def export_image(p):
	print('running the container....')
	print('exporting image....')
	cmd=['docker', 'export', '--output=test.tar', p]
	s=sub.call(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
#	print(s.communicate())

def untar_image(p):
	print('untaring image....')
	cmd=['tar', '-xvf', 'test.tar', '-C', 'test/']
	print(cmd)
	sub.call(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
	for root, dirs, files in os.walk('./test'):
		for name in files:
			if name.endswith('.tar'):
				untar_layer=['tar', '-xvf', os.path.join(root, name), '-C', 'test/']
				print(untar_layer)
				sub.call(untar_layer, stdout=sub.PIPE, stderr=sub.PIPE)

def delete_malwares(malwares):
	if len(malwares) != 0:
		print('deleting malwares....')
	for m in malwares:
		name=m[0]
		digest=m[1]
		cmd=['curl', '-X', 'DELETE', REGISTRY_IP + ":"  + REGISTRY_PORT + '/v2/'+name+'/manifests/'+digest]
		print(cmd)
		sub.call(cmd, stdout=sub.PIPE, stderr=sub.PIPE)