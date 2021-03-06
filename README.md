# PySOFT

[![Build Status](https://travis-ci.org/kpj/PySOFT.png)](https://travis-ci.org/kpj/PySOFT)
[![Latest Version](https://img.shields.io/pypi/v/pysoft.svg)](https://pypi.python.org/pypi/pysoft/)
[![Downloads](https://img.shields.io/pypi/dm/PySOFT.svg)](https://pypi.python.org/pypi/PySOFT/)


Parser for the SOFT (Simple Omnibus Format in Text) file format.


## Installation
### Using pip

```
$ pip install pysoft
```


## Usage

Exemplary usage as python module:
```python

import pysoft

soft = pysoft.SOFTFile('GDSxxxx.soft')
print('Data retrieved from %s' % soft.header['database']['database_name'])
```


## Bug Reports

Please submit any bugs you find to https://github.com/kpj/PySOFT/issues.


## Links

- Github: https://github.com/kpj/PySOFT
- PyPi Homepage: https://pypi.python.org/pypi/pysoft
