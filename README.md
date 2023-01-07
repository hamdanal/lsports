# lsports

A simple Python 3.7+ module to list serial ports on Windows, Linux, and macOS.

This is a modified version of `serial.tools.list_ports` from
[pySerial](https://github.com/pyserial/pyserial) by Chris Liechti.

The goal of this project is to integrate some fixes and improvements to the original *list_ports*
functionality with a faster release cycle.

## Installation

```bash
pip install lsports
```

## Usage

The module provides a single function `comports` that returns a list of `PortInfo` objects.
Each `PortInfo` object contains information about a connected serial port.
```python
from lsports import comports

for port in comports():
    print(port.device, port.product, port.hwid)
```
For a full list of available attributes, see the `PortInfo` class. Only `comports` and `PortInfo`
are considered public API.


## Notable changes from `serial.tools.list_ports`

* The information class name is `PortInfo` instead of `ListPortInfo`.
* On Linux, the objects returned by `comports()` are now instances of `PortInfo`, the same as
  other operating systems. Previously, Linux returned a subclass `SysFS` instead.
* On windows, the *"Bus Reported Device Name"* is used as the `product` attribute which was not
  previously used. This brings the Windows implementation closer to the POSIX ones.
* On Windows, increase the location path buffer size to 500 characters to support longer paths.
* On MacOS, the internal functions have been changed to use `bytes` instead of `str` as the
  project only supports python3.
