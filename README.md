## Introduction


This is a service associated with a docker registry that can inspect pushed docker containers and figure out whether they are safe.


1. ClamAV is used to detect virus files
2. sdhash values are calculated for each file for caching purpose
3. MongoDB is used to store sdhashes, allow faster examination of previously checked files 


## Installation and pre-configuration


See [prerequisites](./prerequisite.md) for details.


## Run the service


### Start helper service


1. Start MongoDB: `$ ~/mongod`
2. Update clamAV DB: `$ sudo freshclam`
3. Start clamAV: `$ sudo service clamav-daemon start`


### Launch Registry


1. `$ cd registry/`
2. `$ docker-compose up`


### Launch Endpoint


1. `$ cd endpoint`
2. `$ python endpoint.py`


## On client side


### Docker build container


1. See [this link](https://docs.docker.com/engine/reference/builder/#escape)  
2. Use `COPY` to copy files in context directory to the new image.  
3. See the reference link for `RUN` and `CMD` command.  
4. Build with following command. Note the dot at the end, as context directory.


```shell
$ docker build -t your_container_name:version_tag .
```

### Docker push container


#### Enable push to insecure registry  


Add configuration file to the server host to connect to insecure private registry.  


```shell
$ sudo vim /etc/docker/daemon.json
```


Add below to the configuration file:


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

Here is a [reference](https://github.com/docker/distribution/issues/1874).


#### Push to registry


```shell
$ docker tag image_name:tag 159.65.238.188:5001/container_name
$ docker push 159.65.238.188:5001/container_name
```

### Docker save image


```shell
$ docker save -o a.tar container_name:version_tag
```


## View push results


Push results can be viewed through browser at `server_ip:web_port/results`. Substitute the ip and port field with your server info.