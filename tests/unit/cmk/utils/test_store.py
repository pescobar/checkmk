<<<<<<< HEAD
# encoding: utf-8

import sys
import threading
import time
import os
import six

import pytest
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import enum
import threading
import queue
import os
import stat
import errno
from pathlib import Path

from six import ensure_binary
import pytest  # type: ignore[import]
from testlib import import_module, wait_until
>>>>>>> upstream/master

import cmk.utils.store as store
from cmk.utils.exceptions import MKGeneralException


<<<<<<< HEAD
def test_load_data_from_file_not_existing(tmp_path):
    data = store.load_data_from_file(str(tmp_path / "x"))
    assert data is None

    data = store.load_data_from_file(str(tmp_path / "x"), "DEFAULT")
    assert data == "DEFAULT"


def test_load_data_from_file_empty(tmp_path):
    locked_file = tmp_path / "test"
    locked_file.write_text(u"", encoding="utf-8")
    data = store.load_data_from_file(str(tmp_path / "x"), "DEF")
    assert data == "DEF"


def test_load_data_not_locked(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"[1, 2]", encoding="utf-8")

    store.load_data_from_file(str(locked_file))
    assert store.have_lock(str(locked_file)) is False


def test_load_data_from_file_locking(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"[1, 2]", encoding="utf-8")

    data = store.load_data_from_file(str(locked_file), lock=True)
    assert data == [1, 2]
    assert store.have_lock(str(locked_file)) is True


def test_load_data_from_not_permitted_file(tmp_path):
=======
@pytest.mark.parametrize("path_type", [str, Path])
def test_mkdir(tmp_path, path_type):
    test_dir = tmp_path / "abc"
    store.mkdir(path_type(test_dir))
    store.mkdir(path_type(test_dir))


@pytest.mark.parametrize("path_type", [str, Path])
def test_mkdir_mode(tmp_path, path_type):
    test_dir = tmp_path / "bla"
    store.mkdir(path_type(test_dir), mode=0o750)
    assert stat.S_IMODE(os.stat(str(test_dir)).st_mode) == 0o750


@pytest.mark.parametrize("path_type", [str, Path])
def test_mkdir_parent_not_exists(tmp_path, path_type):
    test_dir = tmp_path / "not-existing/xyz"
    with pytest.raises(OSError, match="No such file or directory"):
        store.mkdir(path_type(test_dir))


@pytest.mark.parametrize("path_type", [str, Path])
def test_makedirs(tmp_path, path_type):
    test_dir = tmp_path / "not-existing/xyz"
    store.makedirs(path_type(test_dir))
    store.makedirs(path_type(test_dir))


@pytest.mark.parametrize("path_type", [str, Path])
def test_makedirs_mode(tmp_path, path_type):
    test_dir = tmp_path / "whee/blub"
    store.makedirs(path_type(test_dir), mode=0o750)
    assert stat.S_IMODE(os.stat(str(test_dir)).st_mode) == 0o750


@pytest.mark.parametrize("path_type", [str, Path])
def test_load_data_from_file_not_existing(tmp_path, path_type):
    data = store.load_object_from_file(path_type(tmp_path / "x"))
    assert data is None

    data = store.load_object_from_file(path_type(tmp_path / "x"), default="DEFAULT")
    assert data == "DEFAULT"


@pytest.mark.parametrize("path_type", [str, Path])
def test_load_data_from_file_empty(tmp_path, path_type):
    locked_file = tmp_path / "test"
    locked_file.write_text(u"", encoding="utf-8")
    data = store.load_object_from_file(path_type(tmp_path / "x"), default="DEF")
    assert data == "DEF"


@pytest.mark.parametrize("path_type", [str, Path])
def test_load_data_not_locked(tmp_path, path_type):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"[1, 2]", encoding="utf-8")

    store.load_object_from_file(path_type(locked_file))
    assert store.have_lock(path_type(locked_file)) is False


@pytest.mark.parametrize("path_type", [str, Path])
def test_load_data_from_file_locking(tmp_path, path_type):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"[1, 2]", encoding="utf-8")

    data = store.load_object_from_file(path_type(locked_file), lock=True)
    assert data == [1, 2]
    assert store.have_lock(path_type(locked_file)) is True


@pytest.mark.parametrize("path_type", [str, Path])
def test_load_data_from_not_permitted_file(tmp_path, path_type):
>>>>>>> upstream/master
    locked_file = tmp_path / "test"
    locked_file.write_text(u"[1, 2]", encoding="utf-8")
    os.chmod(str(locked_file), 0o200)

    with pytest.raises(MKGeneralException) as e:
<<<<<<< HEAD
        store.load_data_from_file(str(locked_file))
=======
        store.load_object_from_file(path_type(locked_file))
>>>>>>> upstream/master
    assert str(locked_file) in "%s" % e
    assert "Permission denied" in "%s" % e


<<<<<<< HEAD
def test_load_data_from_file_dict(tmp_path):
    locked_file = tmp_path / "test"
    locked_file.write_bytes(repr({"1": 2, "ä": u"ß"}))

    data = store.load_data_from_file(str(locked_file))
    assert isinstance(data, dict)
    assert data["1"] == 2
    assert isinstance(data["ä"], six.text_type)
    assert data["ä"] == u"ß"


def test_save_data_to_file(tmp_path):
    path = str(tmp_path / "test")

    store.save_data_to_file(path, [2, 3])
    assert store.load_data_from_file(path) == [2, 3]


def test_save_data_to_file_pretty(tmp_path):
    path = str(tmp_path / "test")
=======
@pytest.mark.parametrize("path_type", [str, Path])
def test_load_data_from_file_dict(tmp_path, path_type):
    locked_file = tmp_path / "test"
    locked_file.write_bytes(ensure_binary(repr({"1": 2, "ä": u"ß"})))

    data = store.load_object_from_file(path_type(locked_file))
    assert isinstance(data, dict)
    assert data["1"] == 2
    assert isinstance(data["ä"], str)
    assert data["ä"] == u"ß"


@pytest.mark.parametrize("path_type", [str, Path])
def test_load_mk_file(tmp_path, path_type):
    locked_file = tmp_path / "test"
    locked_file.write_bytes(b"# encoding: utf-8\nabc = '\xc3\xa4bc'\n")

    config = store.load_mk_file(path_type(locked_file), default={})
    assert config["abc"] == "äbc"


@pytest.mark.parametrize("path_type", [str, Path])
def test_save_data_to_file_pretty(tmp_path, path_type):
    path = path_type(tmp_path / "test")
>>>>>>> upstream/master

    data = {
        "asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "1asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "2asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "3asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "4asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "5asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
    }
<<<<<<< HEAD
    store.save_data_to_file(path, data)
    assert open(path).read().count("\n") > 4
    assert store.load_data_from_file(path) == data


def test_save_data_to_file_not_pretty(tmp_path):
    path = str(tmp_path / "test")
=======
    store.save_object_to_file(path, data, pretty=True)
    assert open(str(path)).read().count("\n") > 4
    assert store.load_object_from_file(path) == data


@pytest.mark.parametrize("path_type", [str, Path])
def test_save_data_to_file_not_pretty(tmp_path, path_type):
    path = path_type(tmp_path / "test")
>>>>>>> upstream/master

    data = {
        "asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "1asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "2asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "3asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "4asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
        "5asdasaaaaaaaaaaaaaaaaaaaad": "asbbbbbbbbbbbbbbbbbbd",
    }
<<<<<<< HEAD
    store.save_data_to_file(path, data, pretty=False)
    assert open(path).read().count("\n") == 1
    assert store.load_data_from_file(path) == data


def test_acquire_lock_not_existing(tmp_path):
    store.aquire_lock(str(tmp_path / "asd"))


def test_acquire_lock(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"", encoding="utf-8")

    path = str(locked_file)
=======
    store.save_object_to_file(path, data)
    assert open(str(path)).read().count("\n") == 1
    assert store.load_object_from_file(path) == data


@pytest.mark.parametrize("path_type", [str, Path])
@pytest.mark.parametrize("data", [
    None,
    [2, 3],
    [u"föö"],
    [b'foob\xc3\xa4r'],
])
def test_save_data_to_file(tmp_path, path_type, data):
    path = path_type(tmp_path / "lala")
    store.save_object_to_file(path, data)
    assert store.load_object_from_file(path) == data


@pytest.mark.parametrize("path_type", [str, Path])
@pytest.mark.parametrize("data", [
    u"föö",
])
def test_save_text_to_file(tmp_path, path_type, data):
    path = path_type(tmp_path / "lala")
    store.save_text_to_file(path, data)
    assert store.load_text_from_file(path) == data


@pytest.mark.parametrize("path_type", [str, Path])
@pytest.mark.parametrize("data", [
    None,
    b'foob\xc3\xa4r',
])
def test_save_text_to_file_bytes(tmp_path, path_type, data):
    path = path_type(tmp_path / "lala")
    with pytest.raises(TypeError) as e:
        store.save_text_to_file(path, data)
    assert "content argument must be Text, not bytes" in "%s" % e


@pytest.mark.parametrize("path_type", [str, Path])
@pytest.mark.parametrize("data", [
    b'foob\xc3\xa4r',
])
def test_save_bytes_to_file(tmp_path, path_type, data):
    path = path_type(tmp_path / "lala")
    store.save_bytes_to_file(path, data)
    assert store.load_bytes_from_file(path) == data


@pytest.mark.parametrize("path_type", [str, Path])
@pytest.mark.parametrize("data", [
    None,
    u"föö",
])
def test_save_bytes_to_file_unicode(tmp_path, path_type, data):
    path = path_type(tmp_path / "lala")
    with pytest.raises(TypeError) as e:
        store.save_bytes_to_file(path, data)
    assert "content argument must be bytes, not Text" in "%s" % e


@pytest.mark.parametrize("path_type", [str, Path])
def test_save_mk_file(tmp_path, path_type):
    path = path_type(tmp_path / "lala")
    store.save_mk_file(path, "x = 1")
    assert store.load_mk_file(path, default={}) == {"x": 1}


@pytest.mark.parametrize("path_type", [str, Path])
def test_save_to_mk_file(tmp_path, path_type):
    path = path_type(tmp_path / "huhu")
    store.save_to_mk_file(path, "x", {"a": 1})
    assert store.load_mk_file(path, default={"x": {"a": 2, "y": 1}}) == {"x": {"a": 1, "y": 1}}


@pytest.mark.parametrize("path_type", [str, Path])
def test_aquire_lock_not_existing(tmp_path, path_type):
    store.aquire_lock(path_type(tmp_path / "asd"))


@pytest.mark.parametrize("path_type", [str, Path])
def test_locked(locked_file, path_type):
    path = path_type(locked_file)

    assert store.have_lock(path) is False

    with store.locked(path):
        assert store.have_lock(path) is True

    assert store.have_lock(path) is False


@pytest.fixture(name="locked_file")
def fixture_locked_file(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"", encoding="utf-8")
    return locked_file


@pytest.mark.parametrize("path_type", [str, Path])
def test_try_locked(locked_file, path_type):
    path = path_type(locked_file)

    assert store.have_lock(path) is False

    with store.try_locked(path) as result:
        assert result is True
        assert store.have_lock(path) is True

    assert store.have_lock(path) is False


@pytest.mark.parametrize("path_type", [str, Path])
def test_try_locked_fails(locked_file, path_type, monkeypatch):
    path = path_type(locked_file)

    def _is_already_locked(path, blocking):
        raise IOError(errno.EAGAIN, "%s is already locked" % path)

    monkeypatch.setattr(store, "aquire_lock", _is_already_locked)

    assert store.have_lock(path) is False

    with store.try_locked(path) as result:
        assert result is False
        assert store.have_lock(path) is False

    assert store.have_lock(path) is False


@pytest.mark.parametrize("path_type", [str, Path])
def test_aquire_lock(locked_file, path_type):
    path = path_type(locked_file)
>>>>>>> upstream/master

    assert store.have_lock(path) is False
    store.aquire_lock(path)
    assert store.have_lock(path) is True


<<<<<<< HEAD
def test_acquire_lock_twice(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"", encoding="utf-8")

    path = str(locked_file)
=======
@pytest.mark.parametrize("path_type", [str, Path])
def test_aquire_lock_twice(locked_file, path_type):
    path = path_type(locked_file)
>>>>>>> upstream/master

    assert store.have_lock(path) is False
    store.aquire_lock(path)
    assert store.have_lock(path) is True
    store.aquire_lock(path)
    assert store.have_lock(path) is True


<<<<<<< HEAD
def test_release_lock_not_locked():
    store.release_lock("/asdasd/aasdasd")


def test_release_lock(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"", encoding="utf-8")

    path = str(locked_file)
=======
@pytest.mark.parametrize("path_type", [str, Path])
def test_release_lock_not_locked(path_type):
    store.release_lock(path_type("/asdasd/aasdasd"))


@pytest.mark.parametrize("path_type", [str, Path])
def test_release_lock(locked_file, path_type):
    path = path_type(locked_file)
>>>>>>> upstream/master

    assert store.have_lock(path) is False
    store.aquire_lock(path)
    assert store.have_lock(path) is True
    store.release_lock(path)
    assert store.have_lock(path) is False


<<<<<<< HEAD
def test_release_lock_already_closed(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"", encoding="utf-8")

    path = str(locked_file)
=======
@pytest.mark.parametrize("path_type", [str, Path])
def test_release_lock_already_closed(locked_file, path_type):
    path = path_type(locked_file)
>>>>>>> upstream/master

    assert store.have_lock(path) is False
    store.aquire_lock(path)
    assert store.have_lock(path) is True

<<<<<<< HEAD
    os.close(store._acquired_locks[path])
=======
    os.close(store._acquired_locks[str(path)])
>>>>>>> upstream/master

    store.release_lock(path)
    assert store.have_lock(path) is False


<<<<<<< HEAD
def test_release_all_locks(tmp_path):
=======
@pytest.mark.parametrize("path_type", [str, Path])
def test_release_all_locks(tmp_path, path_type):
>>>>>>> upstream/master
    locked_file1 = tmp_path / "locked_file1"
    locked_file1.write_text(u"", encoding="utf-8")
    locked_file2 = tmp_path / "locked_file2"
    locked_file2.write_text(u"", encoding="utf-8")

<<<<<<< HEAD
    path1 = str(locked_file1)
    path2 = str(locked_file2)
=======
    path1 = path_type(locked_file1)
    path2 = path_type(locked_file2)
>>>>>>> upstream/master

    assert store.have_lock(path1) is False
    store.aquire_lock(path1)
    assert store.have_lock(path1) is True

    assert store.have_lock(path2) is False
    store.aquire_lock(path2)
    assert store.have_lock(path2) is True

    store.release_all_locks()
    assert store.have_lock(path1) is False
    assert store.have_lock(path2) is False


<<<<<<< HEAD
def test_release_all_locks_already_closed(tmp_path):
    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"", encoding="utf-8")

    path = str(locked_file)
=======
@pytest.mark.parametrize("path_type", [str, Path])
def test_release_all_locks_already_closed(locked_file, path_type):
    path = path_type(locked_file)
>>>>>>> upstream/master

    assert store.have_lock(path) is False
    store.aquire_lock(path)
    assert store.have_lock(path) is True

<<<<<<< HEAD
    os.close(store._acquired_locks[path])
=======
    os.close(store._acquired_locks[str(path)])
>>>>>>> upstream/master

    store.release_all_locks()
    assert store.have_lock(path) is False


<<<<<<< HEAD
class LockTestThread(threading.Thread):
    def __init__(self, store, path):
        self.store = store
        self.path = path
        self.do = None
        self.is_locked = False
        super(LockTestThread, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            if self.do == "lock":
                assert self.store.have_lock(self.path) is False
                self.store.aquire_lock(self.path)
                assert self.store.have_lock(self.path) is True
                self.do = None

            elif self.do == "unlock":
                assert self.store.have_lock(self.path) is True
                self.store.release_lock(self.path)
                assert self.store.have_lock(self.path) is False
                self.do = None

            else:
                time.sleep(0.1)


def test_locking(tmp_path):
    # HACK: We abuse modules as data containers, so we have to do this Kung Fu...
    store1 = sys.modules["cmk.utils.store"]
    del sys.modules["cmk.utils.store"]
    import cmk.utils.store as _store  # pylint: disable=reimported
    store2 = sys.modules["cmk.utils.store"]

    assert store1 != store2

    locked_file = tmp_path / "locked_file"
    locked_file.write_text(u"", encoding="utf-8")
    path = str(locked_file)

    t1 = LockTestThread(store1, path)
    t1.start()
    t2 = LockTestThread(store2, path)
    t2.start()

    # Take lock with store1
    t1.do = "lock"
    while range(20):
        if store1.have_lock(path):
            break
        time.sleep(0.01)
    assert store1.have_lock(path) is True

    # Now try to get lock with store2
    t2.do = "lock"
    time.sleep(0.2)
    assert store1.have_lock(path) is True
    assert store2.have_lock(path) is False

    # And now unlock store1 and check whether store2 has the lock now
    t1.do = "unlock"
    while range(20):
        if not store1.have_lock(path):
            break
        time.sleep(0.01)
    assert store1.have_lock(path) is False
    time.sleep(0.2)
    assert store2.have_lock(path) is True
=======
class LockTestJob(enum.Enum):
    TERMINATE = enum.auto()
    LOCK = enum.auto()
    UNLOCK = enum.auto()


class LockTestThread(threading.Thread):
    def __init__(self, store_mod, path):
        super(LockTestThread, self).__init__()
        self.daemon = True

        self.store = store_mod
        self.path = path

        self._jobs: queue.Queue[LockTestJob] = queue.Queue()

    def run(self):
        while True:
            try:
                job = self._jobs.get(block=True, timeout=0.1)
            except queue.Empty:
                continue

            try:
                if job is LockTestJob.TERMINATE:
                    break

                if job is LockTestJob.LOCK:
                    assert self.store.have_lock(self.path) is False
                    self.store.aquire_lock(self.path)
                    assert self.store.have_lock(self.path) is True
                    continue

                if job is LockTestJob.UNLOCK:
                    assert self.store.have_lock(self.path) is True
                    self.store.release_lock(self.path)
                    assert self.store.have_lock(self.path) is False
                    continue
            finally:
                self._jobs.task_done()

    def terminate(self):
        """Send terminate command to thread from outside and wait for completion"""
        self._jobs.put(LockTestJob.TERMINATE)
        self.join()

    def lock(self):
        """Send lock command to thread from outside and wait for completion"""
        self.lock_nowait()
        self._jobs.join()

    def unlock(self):
        """Send unlock command to thread from outside and wait for completion"""
        self._jobs.put(LockTestJob.UNLOCK)
        self._jobs.join()

    def lock_nowait(self):
        """Send lock command to thread from outside without waiting for completion"""
        self._jobs.put(LockTestJob.LOCK)

    def join_jobs(self):
        self._jobs.join()


@pytest.fixture(name="t1")
def fixture_test_thread_1(locked_file):
    # HACK: We abuse modules as data containers, so we have to do this Kung Fu...
    t_store = import_module("cmk/utils/store.py")

    t = LockTestThread(t_store, locked_file)
    t.start()

    yield t

    t.store.release_all_locks()
    t.terminate()


@pytest.fixture(name="t2")
def fixture_test_thread_2(locked_file):
    # HACK: We abuse modules as data containers, so we have to do this Kung Fu...
    t_store = store

    t = LockTestThread(t_store, locked_file)
    t.start()

    yield t

    t.store.release_all_locks()
    t.terminate()


def _wait_for_waiting_lock():
    """Use /proc/locks to wait until one lock is in waiting state

    https://man7.org/linux/man-pages/man5/proc.5.html
    """
    def has_waiting_lock():
        pid = os.getpid()
        with Path("/proc/locks").open() as f:
            for line in f:
                p = line.strip().split()
                if p[1] == "->" and p[2] == "FLOCK" and p[4] == "WRITE" and p[5] == str(pid):
                    return True
        return False

    wait_until(has_waiting_lock, timeout=1, interval=0.01)


@pytest.mark.parametrize("path_type", [str, Path])
def test_blocking_lock_while_other_holds_the_lock(locked_file, path_type, t1, t2, monkeypatch):
    assert t1.store != t2.store

    path = path_type(locked_file)

    assert t1.store.have_lock(path) is False
    assert t2.store.have_lock(path) is False

    try:
        # Take lock with t1
        t1.lock()

        assert t1.store.have_lock(path) is True
        assert t2.store.have_lock(path) is False

        # Now request the lock in t2, but don't wait for the successful locking. Only wait until we
        # start waiting for the lock.
        t2.lock_nowait()
        _wait_for_waiting_lock()

        assert t1.store.have_lock(path) is True
        assert t2.store.have_lock(path) is False
    finally:
        t1.unlock()

    t2.join_jobs()

    assert t1.store.have_lock(path) is False
    assert t2.store.have_lock(path) is True


@pytest.mark.parametrize("path_type", [str, Path])
def test_non_blocking_locking_without_previous_lock(locked_file, path_type, t1):
    assert t1.store != store
    path = path_type(locked_file)

    # Try to lock first
    assert store.try_aquire_lock(path) is True
    assert store.have_lock(path) is True
    store.release_lock(path)
    assert store.have_lock(path) is False


@pytest.mark.parametrize("path_type", [str, Path])
def test_non_blocking_locking_while_already_locked(locked_file, path_type, t1):
    assert t1.store != store
    path = path_type(locked_file)

    # Now take lock with t1.store
    t1.lock()
    assert t1.store.have_lock(path) is True

    # And now try to get the lock (which should not be possible)
    assert store.try_aquire_lock(path) is False
    assert t1.store.have_lock(path) is True
    assert store.have_lock(path) is False


@pytest.mark.parametrize("path_type", [str, Path])
def test_non_blocking_decorated_locking_without_previous_lock(locked_file, path_type, t1):
    assert t1.store != store
    path = path_type(locked_file)

    with store.try_locked(path) as result:
        assert result is True
        assert store.have_lock(path) is True
    assert store.have_lock(path) is False


@pytest.mark.parametrize("path_type", [str, Path])
def test_non_blocking_decorated_locking_while_already_locked(locked_file, path_type, t1):
    assert t1.store != store
    path = path_type(locked_file)

    # Take lock with t1.store
    t1.lock()
    assert t1.store.have_lock(path) is True

    # And now try to get the lock (which should not be possible)
    with store.try_locked(path) as result:
        assert result is False
        assert store.have_lock(path) is False
    assert store.have_lock(path) is False
>>>>>>> upstream/master
