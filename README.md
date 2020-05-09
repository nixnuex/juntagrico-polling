# juntagrico-polling
juntagrico-polling is an extension for juntagrico that allows you to set up polls in order to let qualified members (having with shares) submit their vote.

You can find more information about juntagrico on [github](https://github.com/juntagrico/juntagrico) or [juntagrico.org](https://juntagrico.org).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [juntagrico](https://github.com/juntagrico/juntagrico)

## Installing juntagrico-polling

To install juntagrico-polling, follow these steps:

	pip install git+https://github.com/nixnuex/juntagrico-polling

## Using juntagrico-polling

To use juntagrico-polling, follow these steps:

First install the package into your project (see above).

Open settings.py of your juntagrico instance and add juntagrico-polling to your INSTALLED_APPS:

	INSTALLED_APPS = (
	    ...
	    'juntagrico_polling',
	)
	
Open urls.py of your juntagrico instance and add juntagrico-polling:

	url(r'^', include('juntagrico_polling.urls')),
	
Once you've added juntagrico-polling to your INSTALLED_APPS, run the migrations to create the tables needed:

	python manage.py migrate

Navigate to your django admin site and set up your first poll.