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