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

import os
import glob
import importlib


def load_plugins(init_file_path, package_name):
    plugin_files = sorted(glob.glob(os.path.join(os.path.dirname(init_file_path), "*.py")))
    plugins = [
        os.path.basename(f)[:-3]
        for f in plugin_files
        if not os.path.basename(f)[:-3] in ["__init__", "utils"]
    ]

    for plugin_name in plugins:
        importlib.import_module(package_name + '.' + plugin_name)
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import importlib
import pkgutil
import sys
from typing import Tuple, Optional, List, Generator


def load_plugins_with_exceptions(package_name: str) -> Generator[Tuple[str, Exception], None, None]:
    """Load all specified packages

    This function accepts a package name in Python's dotted syntax (e.g.
    requests.exceptions).

    Args:
        package_name:
            A valid module path in Python's dotted syntax.

    Returns:
        A generator of 2-tuples of plugin-name and exception, when a plugin failed to
        import. An empty generator if everything succeeded.

    Raises:
        Nothing explicit. Possibly ImportErrors.

    Example:
        >>> for mod_name, exc in load_plugins_with_exceptions("urllib"):
        ...     print("Importing %s failed: %s" % (mod_name, exc))

    """
    __import__(package_name)
    package = sys.modules[package_name]
    module_path: List[str] = getattr(package, '__path__', [])
    for _loader, plugin_name, _is_pkg in pkgutil.walk_packages(module_path):
        try:
            importlib.import_module("%s.%s" % (package_name, plugin_name))
        except Exception as exc:
            yield plugin_name, exc


def load_plugins(
    init_file_path: str,
    package_name: str,
) -> None:
    """Import all submodules of a module, recursively

    This works reliably even with relative imports happening along the chain.

    Args:
        init_file_path: Package name
        package_name: The name of the package.

    Returns:
        Nothing.

    """
    # This is duplicated because it somehow obscures the exceptions being raised by
    # errors while compiling modules. This implemention explicitly doesn't catch any exceptions
    # occurring while compiling.
    __import__(package_name)
    package = sys.modules[package_name]
    module_path: Optional[List[str]] = getattr(package, '__path__')
    if module_path:
        for _loader, plugin_name, _is_pkg in pkgutil.walk_packages(module_path):
            importlib.import_module("%s.%s" % (package_name, plugin_name))

    for _loader, plugin_name, _is_pkg in pkgutil.walk_packages([init_file_path]):
        importlib.import_module("%s.%s" % (package_name, plugin_name))
>>>>>>> upstream/master
