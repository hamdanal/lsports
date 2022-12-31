from __future__ import annotations

from lsports import PortInfo, comports


def test_comports():
    ports = comports()
    assert isinstance(ports, list)
    for port in ports:
        assert isinstance(port, PortInfo)
        assert isinstance(port.device, str)
        assert isinstance(port.name, str)
        assert isinstance(port.description, str)
        assert isinstance(port.hwid, str)
        if port.vid is not None:  # USB
            assert isinstance(port.vid, int)
            assert isinstance(port.pid, int)
            assert isinstance(port.location, str)
        if port.serial_number is not None:
            assert isinstance(port.serial_number, str)
        if port.manufacturer is not None:
            assert isinstance(port.manufacturer, str)
        if port.product is not None:
            assert isinstance(port.product, str)
        if port.interface is not None:
            assert isinstance(port.interface, str)
