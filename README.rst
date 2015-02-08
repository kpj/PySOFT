PySOFT
======
.. image:: https://pypip.in/v/pysoft/badge.png
    :target: https://crate.io/packages/pysoft/
    :alt: Latest version

.. image:: https://api.travis-ci.org/kpj/PySOFT.png?branch=master
    :target: https://travis-ci.org/kpj/PySOFT
    :alt: Travis-CI

.. image:: https://pypip.in/d/pysoft/badge.png
    :target: https://crate.io/packages/pysoft/
    :alt: Number of PyPI downloads

Parser for the SOFT (Simple Omnibus Format in Text) file format.


Installation
------------
Using pip
+++++++++
::

  $ pip install pysoft


Usage
-----
Exemplary usage as python module:
::

  import pysoft


  soft = pysoft.SOFTFile('GDSxxxx.soft')
  print('Data retrieved from %s' % soft.header['database']['database_name'])


Bug Reports
-----------
Please submit any bugs you find to https://github.com/kpj/PySOFT/issues.


Links
-----
- Github: https://github.com/kpj/PySOFT
- PyPi Homepage: https://pypi.python.org/pypi/pysoft
