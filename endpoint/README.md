# Endpoint Manual

## Prerequisite
### ClamAV
#### Install ClamAV (On Ubuntu 16.04)
```shell
$ sudo apt-get install clamAV clamav-daemon
```
#### Update database
```shell
$ sudo freshclam
``` 
#### enable clamd 
```shell
$ sudo service clamav-daemon start
```

### pyclamd
#### install pyclamd 
```shell
$ sudo pip install pyclamd
```