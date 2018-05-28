
# ckanext-statsd

ckanext-statsd is a simple plugin that writes statistics to a graphite backend via a statsd server.

You can use this plugin to obtain counts for dataset modifications and creation, as well as timers for the various requests to your CKAN server.

> This plugin can generate a LOT of data


Requirements
------------

This plugin has only been tested with CKAN 2.7.3


------------
Installation
------------

To install ckanext-statsd:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-statsd Python package into your virtual environment::

     pip install git+https://github.com/rossjones/ckanext-statsd.git

3. Add ``statsd`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Add statsd configuration to your config file.  You may or may not need the prefix (see your statsd configuration for info)

```
ckanext.statsd.host = 10.0.2.2
ckanext.statsd.port = 8125
ckanext.statsd.prefix =
ckanext.statsd.logtimes = true
```

If you wish to not send timing information, then set `ckanext.statsd.logtimes = false`



5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

6. Use CKAN

7. Check your statsd server to see the metrics it is writing

