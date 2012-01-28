
Introduction
============

.. Note:: 

    Transmogrifier itself includes a similarly scoped blueprint for codecs: http://pypi.python.org/pypi/collective.transmogrifier/1.3#codec-section

This `Transmogrifier`_ blueprint extracts text from within the specified CSS
id.

Installation
============

Sample installation via `mr.migrator`_::

    [buildout]
    extends = http://build.pythonpackages.com/buildout/plone/4.1.x-dev

    [plone]
    eggs += 
        mr.migrator
        transmogrify.extract
        transmogrify.filesystem
        transmogrify.ploneremote
        transmogrify.pathsorter
        transmogrify.print

Usage
=====

Sample usage in ``pipeline.cfg``::

    [transmogrifier]
    pipeline =
        source
        extract
        constructor
        schemaupdater
        print

    [source]
    blueprint = transmogrify.filesystem
    directory = docs/sample_content
    file-type = Document
    file-field = text
    wrap-data = false

    [extract]
    blueprint = transmogrify.extract

    [constructor]
    blueprint = transmogrify.ploneremote.remoteconstructor
    target = http://admin:admin@localhost:8080/Plone

    [schemaupdater]
    blueprint = transmogrify.ploneremote.remoteschemaupdater
    target = http://admin:admin@localhost:8080/Plone

    [print]
    blueprint = transmogrify.print

Specify id
~~~~~~~~~~

By default, the ``content`` id is used; specify an alternative with ``id``::

    [extract]
    blueprint = transmogrify.extract
    id = wrapper

Encoding and decoding charsets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, UTF-8 is used for both. But you can specify an alternative via::

    [extract]
    blueprint = transmogrify.extract
    decode = ascii
    encode = ascii

.. _`mr.migrator`: http://pypi.python.org/pypi/mr.migrator
.. _`Transmogrifier`: http://pypi.python.org/pypi/collective.transmogrifier
