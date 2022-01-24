{{ cookiecutter.plugin_description }}
==============

Getting Started
---------------

- Activate the ClimMob environment.
```
$ . ./path/to/ClimMob/bin/activate
```

- Change directory into your newly created plugin.
```
$ cd {{ cookiecutter.plugin_name }}
```

- Build the plugin
```
$ python setup.py develop
```

- Alembic configuration for extra tables
```
$ mv alembic.example.ini alembic.ini
```
- Edit the alembic.ini an replace sqlalchemy.url with the one in the FormShare ini file
```    
$ alembic revision --autogenerate -m "Initial version"
$ alembic upgrade head
```

- Add the plugin to the ClimMob list of plugins by editing the following line in development.ini or production.ini
```
    #climmob.plugins = examplePlugin
    climmob.plugins = {{ cookiecutter.plugin_name }}
```

- Run ClimMob again
