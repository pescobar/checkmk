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
// tails. You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.
>>>>>>> upstream/master

#ifndef Poller_h
#define Poller_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <poll.h>
=======

#include <poll.h>

#include <asio/basic_socket.hpp>
>>>>>>> upstream/master
#include <cerrno>
#include <chrono>
#include <string>
#include <unordered_map>
#include <vector>
<<<<<<< HEAD
#include "BitMask.h"
=======

#include "BitMask.h"
#include "Logger.h"
>>>>>>> upstream/master

enum class PollEvents { in = 1 << 0, out = 1 << 1, hup = 1 << 2 };
IS_BIT_MASK(PollEvents);

<<<<<<< HEAD
=======
namespace {
template <class Protocol, class SocketService>
int native_handle(const asio::basic_socket<Protocol, SocketService>& sock) {
    // socket::native_handle is not const but we just want
    // the copy of an int here.
    return const_cast<asio::basic_socket<Protocol, SocketService>&>(sock)
        .native_handle();
}
}  // namespace

>>>>>>> upstream/master
class Poller {
public:
    template <typename Rep, typename Period>
    int poll(std::chrono::duration<Rep, Period> timeout) {
        int retval;
        // I/O primitives can fail when interrupted by a signal, so we should
        // retry the operation. In the plain C world, this is already
        // encapsulated in e.g. glibc's TEMP_FAILURE_RETRY macro, see:
        // https://www.gnu.org/software/libc/manual/html_node/Interrupted-Primitives.html
        do {
            auto millis =
                std::chrono::duration_cast<std::chrono::milliseconds>(timeout);
            // The cast below is OK because int has at least 32 bits on all
            // platforms we care about: The timeout is then limited to 24.85
            // days, which should be more than enough for our needs.
<<<<<<< HEAD
            retval = ::poll(&_pollfds[0], _pollfds.size(),
                            static_cast<int>(millis.count()));
        } while (retval == -1 && errno == EINTR);
        return retval;
    }

    void addFileDescriptor(int fd, PollEvents e) {
=======
            retval = ::poll(_pollfds.data(), _pollfds.size(),
                            static_cast<int>(millis.count()));
        } while (retval == -1 && errno == EINTR);

        return retval;
    }

    template <typename Rep, typename Period>
    [[nodiscard]] bool wait(std::chrono::duration<Rep, Period> timeout,
                            const int fd, const PollEvents e,
                            Logger* const logger) {
        addFileDescriptor(fd, e);
        const int retval = poll(timeout);
        if (retval == -1) {
            generic_error ge{"Polling failed"};
            Error(logger) << ge;
            return false;
        }
        if (retval == 0) {
            errno = ETIMEDOUT;
            generic_error ge{"Polling failed"};
            Debug(logger) << ge;
            return false;
        }
        if (!isFileDescriptorSet(fd, e)) {
            errno = EBADF;
            generic_error ge{"Polling failed"};
            Error(logger) << ge;
            return false;
        }
        return true;
    }

    template <typename Rep, typename Period>
    [[nodiscard]] bool wait(std::chrono::duration<Rep, Period> timeout,
                            const int fd, const PollEvents e) {
        this->addFileDescriptor(fd, e);
        const int retval = this->poll(timeout);
        if (retval == -1) {
            return false;
        }
        if (retval == 0) {
            errno = ETIMEDOUT;
            return false;
        }
        if (!this->isFileDescriptorSet(fd, e)) {
            errno = EBADF;
            return false;
        }
        return true;
    }

    void addFileDescriptor(int fd, PollEvents e) {
        // TODO (ml): potential problem with same fd
>>>>>>> upstream/master
        _fd_to_pollfd[fd] = _pollfds.size();
        _pollfds.push_back({fd, toMask(e), 0});
    }

<<<<<<< HEAD
=======
    template <class Protocol, class SocketService>
    void addFileDescriptor(
        const asio::basic_socket<Protocol, SocketService>& sock, PollEvents e) {
        addFileDescriptor(native_handle(sock), e);
    }

>>>>>>> upstream/master
    bool isFileDescriptorSet(int fd, PollEvents e) const {
        auto it = _fd_to_pollfd.find(fd);
        return it != _fd_to_pollfd.end() &&
               (_pollfds[it->second].revents & toMask(e)) != 0;
    }

<<<<<<< HEAD
private:
=======
    template <class Protocol, class SocketService>
    bool isFileDescriptorSet(
        const asio::basic_socket<Protocol, SocketService>& sock,
        PollEvents e) const {
        return isFileDescriptorSet(native_handle(sock), e);
    }

private:
    friend class PollerFixture_ToMask_Test;       // CONTEXT: Google-Fuchsia
    friend class PollerFixture_Descriptors_Test;  // whitebox style testing

>>>>>>> upstream/master
    std::vector<pollfd> _pollfds;
    std::unordered_map<int, size_t> _fd_to_pollfd;

    static short toMask(PollEvents e) {
        // The cast below is OK because all POLLFOO values are within the
        // guaranteed short value range.
        return static_cast<short>(
            (is_empty_bit_mask(e & PollEvents::in) ? 0 : POLLIN) |
            (is_empty_bit_mask(e & PollEvents::out) ? 0 : POLLOUT) |
            (is_empty_bit_mask(e & PollEvents::hup) ? 0 : POLLHUP));
    }
};
<<<<<<< HEAD

=======
>>>>>>> upstream/master
#endif  // Poller_h
