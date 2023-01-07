# Originally sourced from pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net> BSD-3-Clause
# Modified by Ali Hamdan <ali.hamdan.dev@gmail.com> MIT License
from __future__ import annotations

import os

from lsports._common import PortInfo as PortInfo

__all__ = ["comports", "PortInfo"]

if os.name == "nt":
    from lsports._windows import comports as comports  # type: ignore[attr-defined]
elif os.name == "posix":
    from lsports._posix import comports as comports
else:
    raise ImportError(f"No implementation available for '{os.name}' platforms.")
