<<<<<<< HEAD
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.

>>>>>>> upstream/master
    // EXAMPLES
void v()
    {
// nice lambda
        auto z = [](auto&... Str) { return std::vector{Str...}; };

        auto zx = z(kDefaultDevConfigFileName, kDefaultConfigFileName);
    }
