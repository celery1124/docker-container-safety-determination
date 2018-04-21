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


### Specify IP and PORT


In `endpoint/constants.py`, specify following fields with respect to your server. Also change `notification:endpoint:url` field in `registry/config.yml` to be `http://REGISTRY_IP:WEB_PORT/check_image`.


- `REGISTRY_IP`
- `REGISTRY_PORT`
- `WEB_PORT`


### Launch Registry


1. `$ cd registry/`
2. `$ docker-compose up`


### Launch Endpoint


1. `$ cd endpoint`
2. `$ python endpoint.py`


## On client side


### Run background_scanner


```shell
$ python background_scanner.py
```

### Dokcer pull image from private registry


```shell
$ docker pull REGISTRY_IP:REGISTRY_PORT/image_name
```

### Docker build image


1. See [this link](https://docs.docker.com/engine/reference/builder/#escape)  
2. Use `COPY` to copy files in context directory to the new image.  
3. See the reference link for `RUN` and `CMD` command.  
4. Build with following command. Note the dot at the end, as context directory.


```shell
$ docker build -t your_container_name:version_tag dir.
```

### Docker push image


#### Enable push to insecure registry  


Add configuration file to the server host to connect to insecure private registry.  


```shell
$ sudo vim /etc/docker/daemon.json
```


Add below to the configuration file:


```
{
"insecure-registries": ["REGISTRY_IP:REGISTRY_PORT"]
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
$ docker tag image_name:tag REGISTRY_IP:REGISTRY_PORT/container_name
$ docker push REGISTRY_IP:REGISTRY_PORT/image_name
```


### Docker save image


```shell
$ docker save -o a.tar container_name:version_tag
```


### Docker run container


```shell
$ docker run image_name:tag
```

### Docker list all containers


```shell
$ docker ps -a
```


### Docker list all images


```shell
$ docker image ls
```


## View push results


Push results can be viewed through browser at `REGISTRY_IP:WEB_PORT/results`. Successful pushes are marked with OK. Failed pushes lists those suspicious files.