<<<<<<< HEAD
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

// Wrapping asio.hpp to hook socket creation with
// internal control of the options and mode
//

// Reasons:
// asio gives us no access to native handles before completion routines
// asio
// installed we have to set native handle as NOT INHERITABLE immediately upon
// creation

#ifndef asio_h__
#define asio_h__

<<<<<<< HEAD
#if defined(_WIN32) // Windows MSDN 32/64 bits for ARM/x86
=======
#if defined(_WIN32)  // Windows MSDN 32/64 bits for ARM/x86
>>>>>>> upstream/master
#include <WinSock2.h>

// asio will call this function instead of the WSASocketW
// we will modify behavior of the socket
SOCKET WSASocketW_Hook(int af, int type, int protocol,
                       LPWSAPROTOCOL_INFOW lpProtocolInfo, GROUP g,
                       DWORD dwFlags);

#define WSASocketW WSASocketW_Hook
<<<<<<< HEAD
#include "asio.hpp"
=======
#include <asio.hpp>
>>>>>>> upstream/master
#undef WSASocketW
#else
#error \
    "Please, double check, that your handles are not kept by spawning processes"
<<<<<<< HEAD
#include "asio.hpp"
=======
#include <asio.hpp>
>>>>>>> upstream/master
#endif
#endif  // asio_h__
