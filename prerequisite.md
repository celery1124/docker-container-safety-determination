## fuzzy_hash


### Installation


`sudo python -m pip install fuzzyhashlib`


## MongoDB


### Installation


run following command:


1. `sudo apt-get install -y mongodb-org`
2. `cd ~; mkdir data`
3. `echo 'mongod --bind_ip=$IP --dbpath=data --nojournal' > mongod`
4. `chmod a+x mongod`


### Run service


Simply by `~/mongod`


### Mongo shell


Run local Mongo shell by `mongo`
Connect a remote MongoDB: `mongo --host 34.233.78.56`


### Install pymongo


Run `sudo python -m pip install pymongo`


### Create db and collection


- Create db: `use sdhash_db`
- Create collection: `db.createCollection("good_files")`


## Docker


### Installation


Test on a Ubuntu 16.04 virtual machine


<https://docs.docker.com/install/linux/docker-ce/ubuntu/>


### Create the registry


In the `registry` directory, run following command to create a registry. Here we bind port 5000 on localhost to port 5000 in container. 


```
sudo docker run -d --restart=always --name registry -p 5000:5000 -v 'pwd'/config.yml:/etc/docker/registry/config.yml registry:2
```


### Forward requests


1. First, enable firewall on host with `sudo iptables -A INPUT -i docker0 -j ACCEPT`
2. Bind local flask server on `0.0.0.0:portA`
3. Use `ip addr show docker0` to check the ip address `ipLocal` for the host inside container
4. Use `ipLocal:portA` for requests inside container


### Push images to registry


1. Start local flask server
2. Push images to the registry like `sudo docker push localhost:5000/my-container`

