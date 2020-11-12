<<<<<<< HEAD
#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2016             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master
"""This module contains functions that transform Python values into
text representations optimized for human beings - with optional localization.
The resulting strings are not ment to be parsed into values again later. They
are just for optical output purposes."""
<<<<<<< HEAD
from __future__ import division
=======
>>>>>>> upstream/master

# THIS IS STILL EXPERIMENTAL

import time
import math
from datetime import timedelta
<<<<<<< HEAD
from typing import Tuple, Union  # pylint: disable=unused-import
=======
from typing import Optional, Tuple, Union
>>>>>>> upstream/master

from cmk.utils.i18n import _

#.
#   .--Date/Time-----------------------------------------------------------.
#   |           ____        _          _______ _                           |
#   |          |  _ \  __ _| |_ ___   / /_   _(_)_ __ ___   ___            |
#   |          | | | |/ _` | __/ _ \ / /  | | | | '_ ` _ \ / _ \           |
#   |          | |_| | (_| | ||  __// /   | | | | | | | | |  __/           |
#   |          |____/ \__,_|\__\___/_/    |_| |_|_| |_| |_|\___|           |
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def date(timestamp):
    return time.strftime(_("%Y-%m-%d"), time.localtime(timestamp))


def date_and_time(timestamp):
    return "%s %s" % (date(timestamp), time_of_day(timestamp))


def time_of_day(timestamp):
    return time.strftime(_("%H:%M:%S"), time.localtime(timestamp))


def timespan(seconds):
    # type: (Union[float, int]) -> str
    return str(timedelta(seconds=int(seconds)))


def time_since(timestamp):
    # type: (int) -> str
    return timespan(time.time() - timestamp)


class Age(object):
    """Format time difference seconds into approximated human readable text"""
    def __init__(self, secs):
        super(Age, self).__init__()
        self.__secs = secs

    def __str__(self):
        secs = self.__secs

        if secs < 0:
            return "- " + approx_age(-secs)
        elif secs > 0 and secs < 1:  # ms
            return physical_precision(secs, 3, _("s"))
        elif secs < 10:
            return "%.2f %s" % (secs, _("s"))
        elif secs < 60:
            return "%.1f %s" % (secs, _("s"))
        elif secs < 240:
=======
# NOTE: strftime's format *must* be of type str, both in Python 2 and 3.
def date(timestamp: Optional[float]) -> str:
    return time.strftime(str(_("%Y-%m-%d")), time.localtime(timestamp))


def date_and_time(timestamp: Optional[float]) -> str:
    return "%s %s" % (date(timestamp), time_of_day(timestamp))


# NOTE: strftime's format *must* be of type str, both in Python 2 and 3.
def time_of_day(timestamp: Optional[float]) -> str:
    return time.strftime(str(_("%H:%M:%S")), time.localtime(timestamp))


def timespan(seconds: Union[float, int]) -> str:
    return str(timedelta(seconds=int(seconds)))


def time_since(timestamp: int) -> str:
    return timespan(time.time() - timestamp)


class Age:
    """Format time difference seconds into approximated human readable text"""
    def __init__(self, secs: float) -> None:
        super(Age, self).__init__()
        self.__secs = secs

    def __str__(self) -> str:
        secs = self.__secs

        if secs < 0:
            return "-" + approx_age(-secs)
        if 0 < secs < 1:  # ms
            return physical_precision(secs, 3, _("s"))
        if secs < 10:
            return "%.2f %s" % (secs, _("s"))
        if secs < 60:
            return "%.1f %s" % (secs, _("s"))
        if secs < 240:
>>>>>>> upstream/master
            return "%d %s" % (secs, _("s"))

        mins = int(secs / 60.0)
        if mins < 360:
            return "%d %s" % (mins, _("m"))

        hours = int(mins / 60.0)
        if hours < 48:
            return "%d %s" % (hours, _("h"))

        days = hours / 24.0
        if days < 6:
            d = ("%.1f" % days).rstrip("0").rstrip(".")
            return "%s %s" % (d, _("d"))
<<<<<<< HEAD
        elif days < 999:
            return "%.0f %s" % (days, _("d"))
        else:
            years = days / 365.0
            if years < 10:
                return "%.1f %s" % (years, _("y"))

            return "%.0f %s" % (years, _("y"))

    def __float__(self):
=======
        if days < 999:
            return "%.0f %s" % (days, _("d"))
        years = days / 365.0
        if years < 10:
            return "%.1f %s" % (years, _("y"))

        return "%.0f %s" % (years, _("y"))

    def __float__(self) -> float:
>>>>>>> upstream/master
        return float(self.__secs)


# TODO: Make call sites use Age() directly?
<<<<<<< HEAD
def approx_age(secs):
=======
def approx_age(secs: float) -> str:
>>>>>>> upstream/master
    return "%s" % Age(secs)


#.
#   .--Bits/Bytes----------------------------------------------------------.
#   |            ____  _ _          ______        _                        |
#   |           | __ )(_) |_ ___   / / __ ) _   _| |_ ___  ___             |
#   |           |  _ \| | __/ __| / /|  _ \| | | | __/ _ \/ __|            |
#   |           | |_) | | |_\__ \/ / | |_) | |_| | ||  __/\__ \            |
#   |           |____/|_|\__|___/_/  |____/ \__, |\__\___||___/            |
#   |                                       |___/                          |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def scale_factor_prefix(value, base, prefixes=('', 'k', 'M', 'G', 'T', 'P')):
    # type: (int, float, Tuple[str, ...]) -> Tuple[float, str]
=======
def scale_factor_prefix(
    value: float, base: float,
    prefixes: Tuple[str, ...] = ('', 'k', 'M', 'G', 'T', 'P')) -> Tuple[float, str]:
>>>>>>> upstream/master
    base = float(base)

    prefix = prefixes[-1]
    factor = base
    for unit_prefix in prefixes[:-1]:
        if abs(value) < factor:
            prefix = unit_prefix
            break
        factor *= base
    return factor / base, prefix  # fixed: true-division


<<<<<<< HEAD
def drop_dotzero(v, digits=2):
    # type: (float, int) -> str
=======
def drop_dotzero(v: float, digits: int = 2) -> str:
>>>>>>> upstream/master
    """Renders a number as a floating point number and drops useless
    zeroes at the end of the fraction

    45.1 -> "45.1"
    45.0 -> "45"
    """
    t = '%.*f' % (digits, v)
    if "." in t:
        return t.rstrip("0").rstrip(".")
    return t


<<<<<<< HEAD
def fmt_number_with_precision(v, *args, **kwargs):
    factor, prefix = scale_factor_prefix(v, base=kwargs.get('base', 1000.0))
    value = float(v) / factor
    precision = kwargs.get("precision", 2)
    if kwargs.get("drop_zeroes", False):
        number = drop_dotzero(value, precision)
    else:
        number = '%.*f' % (precision, value)

    unit = kwargs.get("unit", "")
    return '%s %s' % (number, prefix + unit)


def fmt_bytes(b, base=1024.0, precision=2, unit="B"):
    # type: (int, float, int, str) -> str
=======
def fmt_number_with_precision(v: float,
                              base: float = 1000.0,
                              precision: int = 2,
                              drop_zeroes: bool = False,
                              unit: str = "") -> str:
    factor, prefix = scale_factor_prefix(v, base)
    value = float(v) / factor
    number = drop_dotzero(value, precision) if drop_zeroes else '%.*f' % (precision, value)
    return '%s %s' % (number, prefix + unit)


def fmt_bytes(b: int, base: float = 1024.0, precision: int = 2, unit: str = "B") -> str:
>>>>>>> upstream/master
    """Formats byte values to be used in texts for humans.

    Takes bytes as integer and returns a string which represents the bytes in a
    more human readable form scaled to TB/GB/MB/KB. The unit parameter simply
    changes the returned string, but does not interfere with any calculations."""
    return fmt_number_with_precision(b, base=base, precision=precision, unit=unit)


# Precise size of a file - separated decimal separator
# 1234 -> "1234"
# 12345 => "12,345"
<<<<<<< HEAD
def filesize(size):
    dec_sep = ","
    if size < 10000:
        return str(size)
    elif size < 1000000:
        return str(size)[:-3] + dec_sep + str(size)[-3:]
    elif size < 1000000000:
=======
def filesize(size: float) -> str:
    dec_sep = ","
    if size < 10000:
        return str(size)
    if size < 1000000:
        return str(size)[:-3] + dec_sep + str(size)[-3:]
    if size < 1000000000:
>>>>>>> upstream/master
        return str(size)[:-6] + dec_sep + str(size)[-6:-3] + dec_sep + str(size)[-3:]

    return str(size)[:-9] + dec_sep + str(size)[-9:-6] + dec_sep + str(size)[-6:-3] + dec_sep + str(
        size)[-3:]


#.
#   .--Misc.Numbers--------------------------------------------------------.
#   |    __  __ _            _   _                 _                       |
#   |   |  \/  (_)___  ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ ___     |
#   |   | |\/| | / __|/ __| |  \| | | | | '_ ` _ \| '_ \ / _ \ '__/ __|    |
#   |   | |  | | \__ \ (__ _| |\  | |_| | | | | | | |_) |  __/ |  \__ \    |
#   |   |_|  |_|_|___/\___(_)_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |___/    |
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def percent(perc, scientific_notation=False):
=======
def percent(perc: float, scientific_notation: bool = False) -> str:
>>>>>>> upstream/master
    """Renders a given number as percentage string"""
    # 0 / 0.0 -> 0%
    # 9.0e-05 -> 0.00009%
    # 0.00009 -> 0.00009%
    # 0.00103 -> 0.001%
    # 0.0019  -> 0.002%
    # 0.129   -> 0.13%
    # 8.25752 -> 8.26%
    # 8       -> 8.0%
    # 80      -> 80.0%
    # 100.123 -> 100%
    # 200.123 -> 200%
    # 1234567 -> 1234567%
    #
    # with scientific_notation:
    # 0.00009 -> 9.0e-05%
    # 0.00019 -> 0.0002%
    # 12345 -> 12345%
    # 1234567 -> 1.2e+06%

    # 0 and 0.0 is a special case
    if perc == 0:
        return "0%"

    # 1000 < oo
    if abs(perc) > 999.5:
        if scientific_notation and abs(perc) >= 100000:
            result = "%1.e" % perc
        else:
            # TODO: in python3 change to >= 999.5
            # the way python rounds x.5 changed between py2 and py3
            result = "%d" % perc
    # 100 < 1000
    elif abs(perc) >= 100:
        result = "%d" % perc
    # 0.0 < 0.001
    elif 0.0 < abs(perc) < 0.01:
        result = "%.7f" % round(perc, -int(math.floor(math.log10(abs(perc)))))
        # for super small numbers < 0.0000001%, just return 0%
        if float(result) == 0:
            return "0%"
        if scientific_notation and perc < 0.0001:
            result = "%1.e" % float(result)
        else:
            result = result.rstrip("0")
    # 0.001 < 100
    else:
        result = "%.2f" % perc
        result = result.rstrip("0").rstrip(".")

    # add .0 to all integers < 100
    if float(result).is_integer() and float(result) < 100:
        result += ".0"

    return result + "%"


<<<<<<< HEAD
def scientific(v, precision=3):
    """Renders a given number in scientific notation (E-notation)"""
    if v == 0:
        return "0"
    elif v < 0:
=======
def scientific(v: float, precision: int = 3) -> str:
    """Renders a given number in scientific notation (E-notation)"""
    if v == 0:
        return "0"
    if v < 0:
>>>>>>> upstream/master
        return "-" + scientific(v * -1, precision)

    mantissa, exponent = _frexp10(float(v))
    # Render small numbers without exponent
<<<<<<< HEAD
    if exponent >= -3 and exponent <= 4:
=======
    if -3 <= exponent <= 4:
>>>>>>> upstream/master
        return "%%.%df" % max(0, precision - exponent) % v

    return "%%.%dfe%%d" % precision % (mantissa, exponent)


# Render a physical value with a precision of p
# digits. Use K (kilo), M (mega), m (milli), µ (micro)
# p is the number of non-zero digits - not the number of
# decimal places.
# Examples for p = 3:
# a: 0.0002234   b: 4,500,000  c: 137.56
# Result:
# a: 223 µ       b: 4.50 M     c: 138
#
# Note if the type of v is integer, then the precision cut
# down to the precision of the actual number
<<<<<<< HEAD
def physical_precision(v, precision, unit_symbol):
=======
def physical_precision(v: float, precision: int, unit_symbol: str) -> str:
>>>>>>> upstream/master
    if v < 0:
        return "-" + physical_precision(-v, precision, unit_symbol)

    scale_symbol, places_after_comma, scale_factor = calculate_physical_precision(v, precision)

    scaled_value = float(v) / scale_factor
    return (u"%%.%df %%s%%s" % places_after_comma) % (scaled_value, scale_symbol, unit_symbol)


<<<<<<< HEAD
def calculate_physical_precision(v, precision):
=======
def calculate_physical_precision(v: float, precision: int) -> Tuple[str, int, int]:
>>>>>>> upstream/master
    if v == 0:
        return "", precision - 1, 1

    # Splitup in mantissa (digits) an exponent to the power of 10
    # -> a: (2.23399998, -2)  b: (4.5, 6)    c: (1.3756, 2)
    _mantissa, exponent = _frexp10(float(v))

    if isinstance(v, int):
        precision = min(precision, exponent + 1)

    # Choose a power where no artifical zero (due to rounding) needs to be
    # placed left of the decimal point.
    scale_symbols = {
        -5: "f",
        -4: "p",
        -3: "n",
        -2: u"µ",
        -1: "m",
        0: "",
<<<<<<< HEAD
        1: "K",
=======
        1: "k",
>>>>>>> upstream/master
        2: "M",
        3: "G",
        4: "T",
        5: "P",
    }
    scale = 0

    while exponent < 0 and scale > -5:
        scale -= 1
        exponent += 3

    # scale, exponent = divmod(exponent, 3)
    places_before_comma = exponent + 1
    places_after_comma = precision - places_before_comma
    while places_after_comma < 0 and scale < 5:
        scale += 1
        exponent -= 3
        places_before_comma = exponent + 1
        places_after_comma = precision - places_before_comma

    return scale_symbols[scale], places_after_comma, 1000**scale


<<<<<<< HEAD
def fmt_nic_speed(speed):
=======
def fmt_nic_speed(speed: str) -> str:
>>>>>>> upstream/master
    """Format network speed (bit/s) for humans."""
    try:
        speedi = int(speed)
    except ValueError:
        return speed

    return fmt_number_with_precision(speedi,
                                     base=1000.0,
                                     precision=2,
                                     unit="bit/s",
                                     drop_zeroes=True)


#.
#   .--helper--------------------------------------------------------------.
#   |                    _          _                                      |
#   |                   | |__   ___| |_ __   ___ _ __                      |
#   |                   | '_ \ / _ \ | '_ \ / _ \ '__|                     |
#   |                   | | | |  __/ | |_) |  __/ |                        |
#   |                   |_| |_|\___|_| .__/ \___|_|                        |
#   |                                |_|                                   |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def _frexp10(x):
    return _frexpb(x, 10)


def _frexpb(x, base):
    # type: (float, int) -> Tuple[float, int]
=======
def _frexp10(x: float) -> Tuple[float, int]:
    return _frexpb(x, 10)


def _frexpb(x: float, base: int) -> Tuple[float, int]:
>>>>>>> upstream/master
    exp = int(math.log(x, base))
    mantissa = x / base**exp
    if mantissa < 1:
        mantissa *= base
        exp -= 1
    return mantissa, exp
