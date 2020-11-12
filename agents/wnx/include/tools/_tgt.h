<<<<<<< HEAD
// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2017             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// ails.  You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

// C++ cross platform support for OS and compilers and targets
#pragma once
#if !defined(___TGT_H)
#define ___TGT_H

#if defined(DEBUG) || defined(DBG) || defined(_DEBUG)
#define DEBUG_TARGET 1
#endif

#if defined(_MSC_VER)
#define WINDOWS_OS 1
#define MSC_COMPILER 1
#endif

namespace tgt {
constexpr bool IsDebug() {
#if defined(DEBUG_TARGET)
    return true;
#else
    return false;
#endif
}

constexpr bool Is64bit() {
#if defined(_WIN64)
    return true;
#else
    return false;
#endif
}

constexpr bool IsRelease() { return !IsDebug(); }

constexpr bool IsWindows() {
#if defined(WINDOWS_OS)
    return true;
#else
    return false;
#endif
}

}  // namespace tgt

#endif  // ___TGT_H
