<<<<<<< HEAD
# pylint: disable=redefined-outer-name

import pytest  # type: ignore
import docker  # type: ignore
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# pylint: disable=redefined-outer-name

from pathlib import Path

import pytest  # type: ignore[import]
import docker  # type: ignore[import]
>>>>>>> upstream/master

import testlib
import testlib.pylint_cmk


@pytest.fixture(scope="module")
def docker_client():
<<<<<<< HEAD
    return docker.DockerClient(base_url="tcp://127.0.0.1:2376")
=======
    return docker.DockerClient()
>>>>>>> upstream/master


@pytest.fixture(scope="module")
def python_container(request, docker_client):
    c = docker_client.containers.run(
        image="shimizukawa/python-all",
        command=["python2.5", "-c", "import time; time.sleep(9999)"],
        detach=True,
        volumes={
            testlib.cmk_path(): {
                'bind': '/cmk',
                'mode': 'ro'
            },
        },
    )
    yield c
    c.remove(force=True)


def _get_python_plugins():
    return [
<<<<<<< HEAD
        "agents/plugins/%s" % f
        for f in testlib.pylint_cmk.get_pylint_files("%s/agents/plugins" % testlib.cmk_path(), "*")
=======
        "agents/plugins/%s" % p.name
        for p in Path(testlib.cmk_path(), "agents", "plugins").iterdir()
        if testlib.pylint_cmk.is_python_file(str(p), "python") or
        testlib.pylint_cmk.is_python_file(str(p), "python3")
>>>>>>> upstream/master
    ]


@pytest.mark.parametrize("plugin_path", _get_python_plugins())
<<<<<<< HEAD
@pytest.mark.parametrize("python_version", ["2.5", "2.6", "2.7"])
def test_agent_plugin_syntax_compatibility(python_container, plugin_path, python_version):
    _exit_code, output = python_container.exec_run(
        ["python%s" % python_version,
         "%s/%s" % (testlib.cmk_path(), plugin_path)],
        workdir="/cmk",
    )

    assert "SyntaxError: " not in output
=======
@pytest.mark.parametrize("python_version", ["2.5", "2.6", "2.7", "3.7"])
def test_agent_plugin_syntax_compatibility(python_container, plugin_path, python_version):
    if plugin_path.endswith(".py2") and not python_version.startswith("2"):
        pytest.skip("Do not test .py2 with Python 3 "
                    "(Plugins are needed for compatibilit with 2.5 and newer)")

    if not plugin_path.endswith(".py2") and python_version in ["2.5", "2.6"]:
        pytest.skip("Do not test .py with Python 2 "
                    "(Plugins are needed for compatibilit with 2.5 and newer)")

    _exit_code, output = python_container.exec_run(
        ["python%s" % python_version, ("/cmk/%s" % plugin_path)],
        workdir="/cmk",
    )

    assert "SyntaxError: " not in output.decode("utf-8")
>>>>>>> upstream/master
