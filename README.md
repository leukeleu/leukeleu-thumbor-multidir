# thumbor_multidir
Thumbor file loader that checks multiple paths

## Config

Set the following configuration (or enviroment variable) before running Thumbor:
```
## List of paths to check for file to load
# defaults to empty list which is an error so all requests will return 404
TC_MULTIDIR_PATHS = ['/home/media', '/mnt/media']
```

## Running Thumbor

See [Thumbor repo](https://github.com/thumbor/thumbor)
or use the Docker container maintaned by [MinimalCompact](https://github.com/MinimalCompact/thumbor/tree/master/thumbor) as a base image... see [/docker/Dockerfile](https://github.com/benneic/thumbor_multidir/tree/master/docker) for an example.
