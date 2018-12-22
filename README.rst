=============================
Blogging-for-Humans
=============================

.. image:: https://badge.fury.io/py/blogging_for_humans.svg
    :target: https://badge.fury.io/py/blogging_for_humans

.. image:: https://travis-ci.org/jhselvik/blogging_for_humans.svg?branch=master
    :target: https://travis-ci.org/jhselvik/blogging_for_humans

.. image:: https://codecov.io/gh/jhselvik/blogging_for_humans/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jhselvik/blogging_for_humans

A sample Django package

Documentation
-------------

The full documentation is at https://blogging_for_humans.readthedocs.io.

Quickstart
----------

Install Blogging-for-Humans::

    pip install blogging_for_humans

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'blogging_for_humans.apps.BloggingForHumansConfig',
        ...
    )

Add Blogging-for-Humans's URL patterns:

.. code-block:: python

    from blogging_for_humans import urls as blogging_for_humans_urls


    urlpatterns = [
        ...
        url(r'^', include(blogging_for_humans_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
