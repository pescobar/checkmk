// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef EventConsoleConnection_h
#define EventConsoleConnection_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <boost/asio/local/stream_protocol.hpp>
=======

#include <asio/local/stream_protocol.hpp>
>>>>>>> upstream/master
#include <iosfwd>
#include <string>
class Logger;

class EventConsoleConnection {
public:
    EventConsoleConnection(Logger *logger, std::string path);
    ~EventConsoleConnection();
    void run();

private:
    virtual void sendRequest(std::ostream &os) = 0;
    virtual void receiveReply(std::istream &is) = 0;

<<<<<<< HEAD
    std::string prefix(const std::string &message) const;
    void check(boost::asio::local::stream_protocol::iostream &stream,
=======
    [[nodiscard]] std::string prefix(const std::string &message) const;
    void check(asio::local::stream_protocol::iostream &stream,
>>>>>>> upstream/master
               const std::string &what) const;

    Logger *const _logger;
    const std::string _path;
};

#endif  // EventConsoleConnection_h
