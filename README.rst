A Symphony Python Module
========================

.. image:: https://cdn.jsdelivr.net/gh/finos/contrib-toolbox@master/images/badge-archived.svg
      :target: https://finosfoundation.atlassian.net/wiki/display/FINOS/Archived

.. image:: https://img.shields.io/pypi/v/python-symphony.svg
      :target: https://pypi.python.org/pypi/python-symphony/

.. image:: https://img.shields.io/pypi/pyversions/python-symphony.svg
      :target: https://pypi.python.org/pypi/python-symphony/

.. image:: https://img.shields.io/pypi/format/python-symphony.svg
      :target: https://pypi.python.org/pypi/python-symphony/

.. image:: https://img.shields.io/badge/license-Apache%202-blue.svg
      :target: https://github.com/symphonyoss/python-symphony/blob/master/LICENSE

.. image:: https://travis-ci.org/symphonyoss/python-symphony.svg?branch=master
      :target: https://travis-ci.org/symphonyoss/python-symphony

.. image:: https://www.versioneye.com/user/projects/584f26435d8a55003f2782a7/badge.svg?style=flat-square
      :target: https://www.versioneye.com/user/projects/584f26435d8a55003f2782a7

The Symphony python client module provides a real-time wrapper around the Symphony REST API's to simplify the creation of chat sessions, room access, presence, messaging and more... The client provides a set of logical services representing supported features of the Symphony platform. Services support real-time events through feature based listeners and communication objects. Access is not limited to the services as all underlying Symphony client implementations are exposed for advanced use or creation of your own service.

Or it will once it's completely finished =P

Features
--------

* Parsing of p12 certificates
* Authentication
* Sending Messages
* Receiving Messages
* MessageML Parsing ( basic functionality )
* User Lookup

Requirements
------------

python-pip
openssl-dev
libgnutls-dev

Dependencies
------------

This project uses the following libraries:

* pip
* requests
* pytz
* lxml
* configparser
* bs4
* pyopenssl

Using the module
----------------

This module is still in VERY early stages.  It's not full feature yet.
However I have one bot up that makes use of it, and may be useful for
you to look at as an example:

`metronome bot <https://github.com/symphonyoss/metronome>`_


Contributing
------------

.. _hacking guide: HACKING.rst
Start by checking out the `hacking guide`_.

Next fork the repo, make your commits locally.
You can run CI / CD checks by doing:

First I recommend doing your work in a venv:

.. code:: text

    virtualenv symphony-test
    ./symphony-test/bin/activate

Then run tox

.. code:: text

    cd python-symphony
    pip install --upgrade tox
    tox

Once you are happy with your code, open a pull request.
Try to limit pull requests to signle specific changes.
If you want to make a major change hit me up via symphony, 
I am Matt Joyce ( symphony corporate ).  I am glad to hear
ideas.  And I'd love to see this project take on a life of
it's own.
