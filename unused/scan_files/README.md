# Scan files with ClamAV

## Install ClamAV (On Ubuntu 16.04)
```shell
$ sudo apt-get install clamAV
```
## Update database
```shell
$ sudo freshclam
```
## Scan directory in command line
```shell
$ clamscan -r --no-summary [dir]
```
-r recursively  
--no-summary omit summary output  

## Python module
1. install pyclamd 
```shell
$ sudo pip install pyclamd
```

2. install and enable clamd 
```shell
$ sudo apt-get install clamav-daemon clamav-freshclam clamav-unofficial-sigs
$ sudo freshclam
$ sudo service clamav-daemon start
```

## Python interface
```python
from scan import clamav
cd = clamav()
cd.scan_file(filname)
cd.scan_dir(directory)
```
1. scan directory
// input directory
// output dictionary {'blacklist':listofbadfiles, 'whitelist':listofgoodfiles}
```python
scan_dir(dir)
```
2. scan single file
// input filename
// output Ture - legal, False - Not legal
```python
scan_dir(filename)
``
