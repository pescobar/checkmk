<<<<<<< HEAD
#!/usr/bin/env python
# encoding: utf-8

import os
import subprocess
import pytest


def test_01_python_interpreter_exists(site):
    assert os.path.exists(site.root + "/bin/python")


def test_02_python_interpreter_path(site):
    p = site.execute(["which", "python"], stdout=subprocess.PIPE)
    path = p.stdout.read().strip()
    assert path == "/omd/sites/%s/bin/python" % site.id


def test_03_python_interpreter_version(site):
    p = site.execute(["python", "-V"], stderr=subprocess.PIPE)
    version = p.stderr.read()
    assert version.startswith("Python 2.7.16")


def test_03_python_path(site):
    p = site.execute(["python", "-c", "import sys ; print(sys.path)"], stdout=subprocess.PIPE)
    sys_path = eval(p.stdout.read())
    assert sys_path[0] == ""
    assert site.root + "/local/lib/python" in sys_path
    assert site.root + "/lib/python" in sys_path
    assert site.root + "/lib/python2.7" in sys_path
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# flake8: noqa

import os
import subprocess
import pytest  # type: ignore[import]


def test_01_python_interpreter_exists(site):
    assert os.path.exists(site.root + "/bin/python3")


def test_02_python_interpreter_path(site):
    p = site.execute(["which", "python3"], stdout=subprocess.PIPE)
    path = p.stdout.read().strip()
    assert path == "/omd/sites/%s/bin/python3" % site.id


def test_03_python_interpreter_version(site):
    p = site.execute(["python3", "-V"], stdout=subprocess.PIPE)
    version = p.stdout.read()
    assert version.startswith("Python 3.8.6")


def test_03_python_path(site):
    p = site.execute(["python3", "-c", "import sys ; print(sys.path)"], stdout=subprocess.PIPE)
    sys_path = eval(p.stdout.read())
    assert sys_path[0] == ""
    assert site.root + "/local/lib/python3" in sys_path
    assert site.root + "/lib/python3" in sys_path
    assert site.root + "/lib/python3.8" in sys_path
>>>>>>> upstream/master

    for p in sys_path:
        if p != "" and not p.startswith(site.root):
            raise Exception("Found non site path %s in sys.path" % p)


def test_01_pip_exists(site):
<<<<<<< HEAD
    assert os.path.exists(site.root + "/bin/pip")


def test_02_pip_path(site):
    p = site.execute(["which", "pip"], stdout=subprocess.PIPE)
    path = p.stdout.read().strip()
    assert path == "/omd/sites/%s/bin/pip" % site.id


def test_03_pip_interpreter_version(site):
    p = site.execute(["pip", "-V"], stdout=subprocess.PIPE)
    version = p.stdout.read()
    assert version.startswith("pip 18.1")
=======
    assert os.path.exists(site.root + "/bin/pip3")


def test_02_pip_path(site):
    p = site.execute(["which", "pip3"], stdout=subprocess.PIPE)
    path = p.stdout.read().strip()
    assert path == "/omd/sites/%s/bin/pip3" % site.id


def test_03_pip_interpreter_version(site):
    p = site.execute(["pip3", "-V"], stdout=subprocess.PIPE)
    version = p.stdout.read()
    assert version.startswith("pip 20.2.1")
>>>>>>> upstream/master


# TODO: Improve this test to automatically adapt the expected modules from our Pipfile
@pytest.mark.parametrize("module_name", [
    "netsnmp",
<<<<<<< HEAD
    "pysphere",
=======
>>>>>>> upstream/master
    "ldap",
    "OpenSSL",
    "cryptography",
    "pysmi",
    "pysnmp",
<<<<<<< HEAD
    "pymssql",
    "ldap",
    "MySQLdb",
=======
    "ldap",
    "pymysql",
>>>>>>> upstream/master
    "psycopg2",
    "dicttoxml",
    "enum",
    "PIL",
    "reportlab",
    "PyPDF2",
    "psutil",
    "ipaddress",
<<<<<<< HEAD
    "netifaces",
=======
>>>>>>> upstream/master
    "requests",
    "paramiko",
    "pyghmi",
    "typing",
<<<<<<< HEAD
    "pathlib2",
=======
>>>>>>> upstream/master
    "dateutil",
    "snap7",
    "rrdtool",
    "werkzeug",
    "boto3",
    "kubernetes",
<<<<<<< HEAD
])
def test_python_modules(site, module_name):
    import importlib
=======
    "numpy",
])
def test_python_modules(site, module_name):
    import importlib  # pylint: disable=import-outside-toplevel
>>>>>>> upstream/master
    module = importlib.import_module(module_name)
    assert module.__file__.startswith(site.root)


<<<<<<< HEAD
@pytest.mark.skip("Skip until 2019-09-11")
def test_python_preferred_encoding():
    import locale
=======
def test_python_preferred_encoding():
    import locale  # pylint: disable=import-outside-toplevel
>>>>>>> upstream/master
    assert locale.getpreferredencoding() == "UTF-8"
