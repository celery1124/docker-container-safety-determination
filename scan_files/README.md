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
--no-summary emit summary output  


## Python interface
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
