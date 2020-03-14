Installation
============

Basic Installation
------------------
Install juntagrico-polling with :command:`pip`::

    $ pip install juntagrico-polling

Django Settings
---------------
You have to add the app to your installed apps in your Django settings

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'juntagrico',
        'juntagrico_polling',
    ]


You also have to configure caching so that the app works correctly, and you have to execute the django createcachetable command (during the command juntagrico and all juntagrico apps have to be removed from the INSTALLED_APPS).

.. code-block:: python

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'juntagrico_app_cache_table',
            'TIMEOUT': None,
        }
    }
