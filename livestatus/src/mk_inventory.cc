// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "mk_inventory.h"

<<<<<<< HEAD
=======
#include <sys/stat.h>

>>>>>>> upstream/master
time_t mk_inventory_last(const std::string &path) {
    struct stat st;
    return stat(path.c_str(), &st) != 0 ? 0 : st.st_mtime;
}
