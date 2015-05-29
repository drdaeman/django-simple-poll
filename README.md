Simple Django poll application
==============================

Installation
------------

This is a fork, that incorporates changes by myself and other various users.
First of all, you should check the original project to see if it will fit your needs.

If you want to use this one, you can install it from GitHub:

    pip install -e git+https://github.com/drdaeman/django-simple-poll.git#egg=django-simple-poll

Usage
-----

1. Add 'poll' application in the ``INSTALLED_APPS`` settings:

	```
	INSTALLED_APPS = (
    	# ...
    	'poll',
	)
	```

2. Add the poll's URL to your `urls.py`.

	```
	urlpatterns = patterns('',
		# ...
    	url(r'^poll/', include('poll.urls')),
	)
	```

3. Run `python manage.py syncdb` (or `python manage.py migrate poll` if you use South).

   Please beware that if you're using custom user model (with `AUTH_USER_MODEL` setting),
   while South migrations will correctly honor that, changing this setting at a later time
   may cause all sort of problems.
   
   There is no support for Django 1.7+ built-in database migrations for now. Sorry about this.

4. Add this tags in your template file to show poll:

	```
	{% load poll_tags %}
	{% poll %}                  {# will show the latest poll among all known ones #}
	{% poll user=user %}        {# will show the latest poll from the specific user #}
	{% poll poll_id=poll_id #}  {# will show the specific poll #}
	```

-----
Based on https://github.com/applecat/django-simple-poll and its derivatives.
