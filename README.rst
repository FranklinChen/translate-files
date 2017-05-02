Translate text files using Google Translate
===========================================

|Build Status|

Developer token
---------------

You need to use a Google API developer token in order to pay for use of
the Google Translate API. We check for the environment variable
``GOOGLE_API_TOKEN`` so in your ``.bash_profile`` (or other shell init
script) you should have

::

    export GOOGLE_API_TOKEN=...

Prerequisites
-------------

Make sure to have Python 3 installed, e.g., on macOS, you can use
Homebrew with

::

    $ brew install python3

Install
-------

Clone this repo and ``cd`` into it, then run

::

    $ python3 setup.py install

to install the executable ``translate-files``.

Usage
-----

Example usage, to convert from traditional (``zh-TW``) to simplified
(``zh-CN``):

::

    $ translate-files --source zh-TW --target zh-CN test/tw/*.txt

converts each of the input files from traditional to simplified output
files with an extra extension ``.output`` added to the original files'
paths.

Note: as usual, if you want to do something like convert an entire
directory tree, using the shell to generate all the paths:

::

    $ find rootDir -name '*.txt' -print0 | xargs -0 translate-files --source zh-TW --target zh-CN

will run ``translate-files`` on all ``.txt`` files under ``rootDir``
recursively.

.. |Build Status| image:: https://travis-ci.org/TalkBank/translate-files.png
   :target: https://travis-ci.org/TalkBank/translate-files
