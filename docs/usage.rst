=====
Usage
=====

To use Blogging-for-Humans in a project, add it to your `INSTALLED_APPS`:

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
