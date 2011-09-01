
Introduction
============

This simple `Transmogrifier`_ blueprint extracts text (including HTML) from within the specified CSS id ("content" id by default, e.g. <div id="content">EXTRACT ME</div>).

Installation
============

Sample installation (via `mr.migrator`_)::

    [buildout]
    develop = .
    extends = http://x.aclark.net/plone/4.1.x/develop.cfg
    parts += migrate

    [migrate]
    recipe = mr.migrator
    eggs =
        transmogrify.extract
        transmogrify.filesystem
        transmogrify.ploneremote
        transmogrify.pathsorter
        transmogrify.print
    pipeline = pipeline.cfg

Usage
=====

Sample usage::

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
    #blueprint = collective.transmogrifier.sections.folders
    blueprint = transmogrify.ploneremote.remoteconstructor
    target = http://admin:admin@localhost:8080/Plone

    [schemaupdater]
    blueprint = transmogrify.ploneremote.remoteschemaupdater
    target = http://admin:admin@localhost:8080/Plone

    [print]
    blueprint = transmogrify.print

Specify id
~~~~~~~~~~

By default, the "content" id is used. But you can specify an alternative via::

    [extract]
    blueprint = transmogrify.extract
    id = ALTERNATE CSS ID e.g. wrapper, container, whatever

Encoding and decoding charsets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, UTF-8 is used for both. But you can specify an alternative via::

    [extract]
    blueprint = transmogrify.extract
    decode = ALTERNATE CHARSET e.g. ascii, big5, gb2312, euc_kr, etc.
    encode = ALTERNATE CHARSET e.g. ascii, big5, gb2312, euc_kr, etc.

.. _`mr.migrator`: http://pypi.python.org/pypi/mr.migrator
.. _`Transmogrifier`: http://pypi.python.org/pypi/collective.transmogrifier

