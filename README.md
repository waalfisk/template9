
### template9 -- PSQL client
The `template9` docker example 

* belongs to bridge network and has a static ip
* runs an initial `install.sql` on a remote PSQL server container 
* runs `script.sh` file as a cron job (e.g. data cleaning SQL scripts)
* have a mounting point to a host directory,

### Purpose
* run bash scripts (`script.sh`) in cron
* read, store, process data on a host directory via a mounting point,
* communicate with a PSQL server container with the docker network via IP address

### Commands
Use the following commands to install, start, or uninstall the images or container.

| command | description |
|:-------:|:-----------:|
| `./config uninstall` | Cleanup previous installations |
| `vi config.conf` | Increment the version |
| `./config.sh build run` | Build the Image and instantiate the Container |
| `./config.sh start` | Start the Container again |

Requires execution rights for `config.sh`.
For example, run `chmod u+x config.sh` to call `./config.sh ...`.
Otherwise call `bash config.sh ...`.

### script.sh
Is executed as cron job.
Edit the file `script.sh` for the stuff you want to do.

## crontab
Edit in `crontab` the schedule when to execute `script.sh`. 

For debugging check the log file

```
docker exec -it mytempl9 tail -f /var/log/cron.log
```

## network settings
Requires a bridge network, e.g.

```
docker network create \
    --subnet=172.64.0.0/16 \
    --driver=bridge \
    mynet
```

what is specified in `config.conf` as 

```
netname=mynet
ipaddr4=172.64.0.9  # pick an IP within the subnet of mynet
```

### Dockerfile
Nothing to say about it.

## Related templates
* [template5](https://github.com/waalfisk/template5) -- Postgres Database
* [template9](https://github.com/waalfisk/template9) -- Process with access to Postgres DB

### Links
* [template9](https://github.com/waalfisk/template9)
* [Run a cron job with Docker](https://www.ekito.fr/people/run-a-cron-job-with-docker/)