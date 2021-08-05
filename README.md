# simpleTODO


### Local development
To start project with docker-compose
```
$ docker-compose -f docker-compose.yml up -d
```
To stop project with docker-compose
```
$ docker-compose -f docker-compose.yml stop
```
To check if project up and running correctly(State column should have `Up` for all services)
```
$ docker-compose -f docker-compose.yml ps
                    Name                          Command               State                    Ports
---------------------------------------------------------------------------------------------------------------
simpletodo_postgres_1         docker-entrypoint.sh postgres    Up      0.0.0.0:5532->5432/tcp,:::5532->5432/tcp
simpletodo_redis_1            docker-entrypoint.sh redis ...   Up      6379/tcp
simpletodo_simpletodo_1       bash -c python manage.py c ...   Up      0.0.0.0:8000->8000/tcp,:::8000->8000/tcp
simpletodo_simpletodo_run_1   python /opt/.pycharm_helpe ...   Up      0.0.0.0:38351->38351/tcp
```
To rebuild python project if requirements.txt was changed
```
$ docker-compose -f docker-compose.yml stop
$ docker-compose -f docker-compose.yml build simpletodo
$ docker-compose -f docker-compose.yml up -d
```
To check logs in selected service
```
$ docker-compose -f docker-compose.yml logs -f simpletodo
```

To exec command on selected service
```
$ docker-compose -f docker-compose.yml exec simpletodo bash

```
