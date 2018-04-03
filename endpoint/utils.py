import subprocess

def get_image_name():
    pass

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
    imagename = ''
    test_pull_image(imagename)