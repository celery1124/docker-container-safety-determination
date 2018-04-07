import subprocess

def get_image_name(js):
    names = []
    for event in js['events']:
        if even['action'] == 'push':
            repo = event['target']['repository']
            url = event["target"]["url"]
            tag = event['target']['tag']
            ip, port = get_registry_url(url)

def get_registry_url(link):
    # to-do
    ip = ''
    port = ''
    return ip, port

def pull_image(imagename):
    print('pulling image.....')
    cmd = ['docker', 'pull', imagename]
    p = subprocess.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)

def untar_image(tarfile):
    print('untar image.....')
    cmd = ['tar', '-xvf', tarfile]
    p = subprocess.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)

def test_pull_image(imagename):
    pull_image(imagename)

if __name__ == '__main__':
    imagename = 'my-ubuntu'
    test_pull_image(imagename)
