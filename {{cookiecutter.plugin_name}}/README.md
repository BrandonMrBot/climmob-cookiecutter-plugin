{{ cookiecutter.plugin_description }}
==============

Getting Started
---------------

- Activate the FormShare environment.
```
$ . ./path/to/FormShare/bin/activate
```

- Change directory into your newly created plugin.
```
$ cd {{ cookiecutter.plugin_name }}
```

- Build the plugin
```
$ python setup.py develop
```

- Add the plugin to the FormShare list of plugins by editing the following line in development.ini or production.ini
```
    #formshare.plugins = examplePlugin
    formshare.plugins = {{ cookiecutter.plugin_name }}
```

- Run FormShare again
