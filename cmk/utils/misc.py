<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
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
"""This is an unsorted collection of small unrelated helper functions which are
usable in all components of Check_MK

Please try to find a better place for the things you want to put here."""

<<<<<<< HEAD
import six


def make_utf8(x):
    if isinstance(x, six.text_type):
        return x.encode('utf-8')
    return x


def quote_shell_string(s):
=======
from contextlib import contextmanager
import inspect
import itertools
import os
from pathlib import Path
import sys
import time
from typing import Any, Iterator, Callable, Dict, List, Optional, Set, Tuple, Union

from cmk.utils.exceptions import MKGeneralException


def quote_shell_string(s: str) -> str:
>>>>>>> upstream/master
    """Quote string for use as arguments on the shell"""
    return "'" + s.replace("'", "'\"'\"'") + "'"


# TODO: Change to better name like: quote_pnp_string()
<<<<<<< HEAD
def pnp_cleanup(s):
    """Quote a string (host name or service description) in PNP4Nagios format"""
=======
def pnp_cleanup(s: str) -> str:
    """Quote a string (host name or service description) in PNP4Nagios format

    Because it is used as path element, this needs to be handled as "str" in Python 2 and 3
    """
>>>>>>> upstream/master
    return s \
        .replace(' ', '_') \
        .replace(':', '_') \
        .replace('/', '_') \
        .replace('\\', '_')


<<<<<<< HEAD
def key_config_paths(a):
=======
def key_config_paths(a: Path) -> Tuple[Tuple[str, ...], int, Tuple[str, ...]]:
>>>>>>> upstream/master
    """Key function for Check_MK configuration file paths

    Helper functions that determines the sort order of the
    configuration files. The following two rules are implemented:

    1. *.mk files in the same directory will be read
       according to their lexical order.
    2. subdirectories in the same directory will be
       scanned according to their lexical order.
    3. subdirectories of a directory will always be read *after*
       the *.mk files in that directory.
    """
    pa = a.parts
    return pa[:-1], len(pa), pa
<<<<<<< HEAD
=======


def total_size(o: Any, handlers: Optional[Dict] = None) -> int:
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    if handlers is None:
        handlers = {}

    dict_handler = lambda d: itertools.chain.from_iterable(d.items())
    all_handlers = {
        tuple: iter,
        list: iter,
        dict: dict_handler,
        set: iter,
        frozenset: iter,
    }
    all_handlers.update(handlers)  # user handlers take precedence
    seen: Set[int] = set()
    default_size = sys.getsizeof(0)  # estimate sizeof object without __sizeof__

    def sizeof(o: Any) -> int:
        if id(o) in seen:  # do not double count the same object
            return 0
        seen.add(id(o))
        s = sys.getsizeof(o, default_size)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


# Works with Checkmk version (without tailing .cee and/or .demo)
def is_daily_build_version(v: str) -> bool:
    return len(v) == 10 or '-' in v


# Works with Checkmk version (without tailing .cee and/or .demo)
def branch_of_daily_build(v: str) -> str:
    if len(v) == 10:
        return "master"
    return v.split('-')[0]


def cachefile_age(path: Union[Path, str]) -> float:
    if not isinstance(path, Path):
        path = Path(path)

    try:
        return time.time() - path.stat().st_mtime
    except Exception as e:
        raise MKGeneralException("Cannot determine age of cache file %s: %s" % (path, e))


def getfuncargs(func: Callable) -> List[str]:
    return list(inspect.signature(func).parameters)


def make_kwargs_for(function: Callable, **kwargs: Any) -> Dict[str, Any]:
    return {
        arg_indicator: arg  #
        for arg_name in getfuncargs(function)
        for arg_indicator, arg in kwargs.items()
        if arg_name == arg_indicator
    }


def with_umask(mask: int) -> Callable:
    def umask_wrapper(fun: Callable) -> Callable:
        def fun_wrapper(*args: Any, **kwargs: Any) -> Any:
            with umask(mask):
                return fun(*args, **kwargs)

        return fun_wrapper

    return umask_wrapper


@contextmanager
def umask(mask: int) -> Iterator[None]:
    old_mask = os.umask(mask)
    try:
        yield None
    finally:
        os.umask(old_mask)
>>>>>>> upstream/master
