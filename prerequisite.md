## fuzzy_hash


### Installation


`$ sudo python -m pip install fuzzyhashlib`


## MongoDB


### Installation


run following command:


1. `$ sudo apt-get install -y mongodb-org`
2. `$ cd ~; mkdir data`
3. `$ echo 'mongod --bind_ip=$IP --dbpath=data --nojournal' > mongod`
4. `$ chmod a+x mongod`


### Run service


Simply by `~/mongod`


### Mongo shell


Run local Mongo shell by `mongo`
Connect a remote MongoDB: `mongo --host 34.233.78.56`


### Install pymongo


Run `sudo python -m pip install pymongo`


### Create db and collection


In mongo shell,

- Create db: `use sdhash_db`
- Create collection: `db.createCollection("good_files")`


## Docker


### Installation


Test on a Ubuntu 16.04 virtual machine.


<https://docs.docker.com/install/linux/docker-ce/ubuntu/>


Install `docker-compose` according to <https://docs.docker.com/compose/install/#install-compose>


### Enable HTTP request


Add configuration file to the server host to connect to insecure private registry.  


```shell
$ sudo vim /etc/docker/daemon.json
```


Add below to the configuration file::  


```
{
"insecure-registries": ["ip:port"]
}
```


Restart docker daemon: 


```shell
$ sudo service docker stop
$ dockerd &
```


### Launch Registry


1. `cd registry/`
2. `docker-compose up`


### Launch Endpoint


1. `cd endpoint`
2. `python endpoint.py`


## ClamAV


### Installation

```shell
$ sudo apt-get install clamav clamav-daemon
```


### Run


1. Update clamAV DB: `sudo freshclam`
2. Start clamAV: `sudo service clamav-daemon start`


### pyclamd


```shell
$ sudo pip install pyclamd
```
