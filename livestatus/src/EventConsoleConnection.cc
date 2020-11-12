// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "EventConsoleConnection.h"
<<<<<<< HEAD
#include <boost/asio/basic_socket_streambuf.hpp>
#include <boost/asio/socket_base.hpp>
#include <boost/system/error_code.hpp>
#include <boost/system/system_error.hpp>
#include <chrono>
#include <ostream>
=======

#include <asio/basic_socket_streambuf.hpp>
#include <asio/error.hpp>
#include <asio/error_code.hpp>
#include <asio/socket_base.hpp>
#include <asio/system_error.hpp>
#include <chrono>
#include <ostream>
#include <system_error>  // IWYU pragma: keep
>>>>>>> upstream/master
#include <thread>
#include <utility>
#include "Logger.h"

<<<<<<< HEAD
EventConsoleConnection::EventConsoleConnection(Logger *logger, std::string path)
    : _logger(logger), _path(std::move(path)) {}

=======
#include "Logger.h"

using namespace std::chrono_literals;

EventConsoleConnection::EventConsoleConnection(Logger *logger, std::string path)
    : _logger(logger), _path(std::move(path)) {}

>>>>>>> upstream/master
EventConsoleConnection::~EventConsoleConnection() {
    Debug(_logger) << prefix("closing connection");
}

void EventConsoleConnection::run() {
<<<<<<< HEAD
    boost::asio::local::stream_protocol::endpoint ep(_path);
    // Attention, tricky timing-dependent stuff ahead: When we connect very
    // rapidly, a no_buffer_space (= ENOBUFS) error can happen. This is probably
    // caused by some internal Boost Kung Fu, remapping EGAIN to ENOBUFS, and
    // looks like a bug in Boost, but that's a bit unclear. So instead of
    // relying on Boost to retry under these circumstances, we do it ourselves.
    boost::asio::local::stream_protocol::iostream stream;
    while (true) {
        stream.connect(ep);
        if (stream.error() !=
            boost::system::error_code(boost::system::errc::no_buffer_space,
                                      boost::system::system_category())) {
=======
    asio::local::stream_protocol::endpoint ep(_path);
    // Attention, tricky timing-dependent stuff ahead: When we connect very
    // rapidly, a no_buffer_space (= ENOBUFS) error can happen. This is probably
    // caused by some internal asio Kung Fu, remapping EGAIN to ENOBUFS, and
    // looks like a bug in asio, but that's a bit unclear. So instead of
    // relying on asio to retry under these circumstances, we do it ourselves.
    asio::local::stream_protocol::iostream stream;
    while (true) {
        stream.connect(ep);
        if (stream.error() != asio::error_code(asio::error::no_buffer_space,
                                               asio::system_category())) {
>>>>>>> upstream/master
            break;
        }
        Debug(_logger) << "retrying to connect";
        stream.clear();
<<<<<<< HEAD
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
=======
        std::this_thread::sleep_for(1ms);
>>>>>>> upstream/master
    }

    check(stream, "connect");
    Debug(_logger) << prefix("successfully connected");

    stream << std::nounitbuf;
    sendRequest(stream);
    stream.flush();
<<<<<<< HEAD
    stream.rdbuf()->shutdown(boost::asio::socket_base::shutdown_send);
=======
    stream.rdbuf()->shutdown(asio::socket_base::shutdown_send);
>>>>>>> upstream/master
    check(stream, "send request");

    receiveReply(stream);
    check(stream, "receive reply");
}

std::string EventConsoleConnection::prefix(const std::string &message) const {
    return "[mkeventd at " + _path + "] " + message;
}

void EventConsoleConnection::check(
<<<<<<< HEAD
    boost::asio::local::stream_protocol::iostream &stream,
    const std::string &what) const {
    if (!stream && !stream.eof()) {
        // NOTE: Boost's system_error has a mutable string member for lazy
        // construction of what(), this screws up cert-err60-cpp. :-P
        throw boost::system::system_error(stream.error(),
                                          prefix("cannot " + what));  // NOLINT
=======
    asio::local::stream_protocol::iostream &stream,
    const std::string &what) const {
    if (!stream && !stream.eof()) {
        throw asio::system_error(stream.error(), prefix("cannot " + what));
>>>>>>> upstream/master
    }
}
