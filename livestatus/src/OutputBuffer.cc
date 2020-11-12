// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "OutputBuffer.h"
<<<<<<< HEAD
#include <unistd.h>
#include <chrono>
#include <cstddef>
#include <iomanip>
#include "Logger.h"
#include "Poller.h"

OutputBuffer::OutputBuffer(int fd, const bool &termination_flag, Logger *logger)
    : _fd(fd)
    , _termination_flag(termination_flag)
    , _logger(logger)
    // TODO(sp) This is really the wrong default because it hides some early
    // errors, e.g. an unknown command. But we can't change this easily because
    // of legacy reasons... :-/
    , _response_header(ResponseHeader::off)
    , _response_code(ResponseCode::ok) {}

OutputBuffer::~OutputBuffer() { flush(); }

=======

#include <chrono>
#include <cstddef>
#include <iomanip>
#include <string_view>

#include "Logger.h"
#include "POSIXUtils.h"

using namespace std::chrono_literals;

OutputBuffer::OutputBuffer(int fd, const bool &termination_flag, Logger *logger)
    : _fd(fd)
    , _termination_flag(termination_flag)
    , _logger(logger)
    // TODO(sp) This is really the wrong default because it hides some early
    // errors, e.g. an unknown command. But we can't change this easily because
    // of legacy reasons... :-/
    , _response_header(ResponseHeader::off)
    , _response_code(ResponseCode::ok) {}

OutputBuffer::~OutputBuffer() { flush(); }

>>>>>>> upstream/master
void OutputBuffer::flush() {
    if (_response_header == ResponseHeader::fixed16) {
        if (_response_code != ResponseCode::ok) {
            _os.clear();
            _os.str("");
            _os << _error_message;
        }
        auto code = static_cast<unsigned>(_response_code);
        size_t size = _os.tellp();
        std::ostringstream header;
        header << std::setw(3) << std::setfill('0') << code << " "  //
               << std::setw(11) << std::setfill(' ') << size << "\n";
        writeData(header);
    }
    writeData(_os);
}

<<<<<<< HEAD
void OutputBuffer::writeData(std::ostringstream &os) {
    // TODO(sp) This cruel and slightly non-portable hack avoids copying (which
    // is important). We could do better by e.g. using boost::asio::streambuf.
    struct Hack : public std::stringbuf {
        [[nodiscard]] const char *base() const { return pbase(); }
    };
    const char *buffer = static_cast<Hack *>(os.rdbuf())->base();
    size_t bytes_to_write = os.tellp();
    while (!shouldTerminate() && bytes_to_write > 0) {
        Poller poller;
        poller.addFileDescriptor(_fd, PollEvents::out);
        int retval = poller.poll(std::chrono::milliseconds(100));
        if (retval > 0 && poller.isFileDescriptorSet(_fd, PollEvents::out)) {
            ssize_t bytes_written = write(_fd, buffer, bytes_to_write);
            if (bytes_written == -1) {
                generic_error ge("could not write " +
                                 std::to_string(bytes_to_write) +
                                 " bytes to client socket");
                Informational(_logger) << ge;
                break;
            }
            buffer += bytes_written;
            bytes_to_write -= bytes_written;
        }
=======
namespace {
// TODO(sp) This cruel and slightly non-portable hack avoids copying, which
// is important. Note that UBSan rightly complains about it. We could do
// better with C++20 via os.view().
std::string_view toStringView(std::ostringstream &os) {
    struct Hack : public std::stringbuf {
        [[nodiscard]] const char *base() const { return pbase(); }
    };
    return {static_cast<Hack *>(os.rdbuf())->base(),
            static_cast<size_t>(os.tellp())};
}
}  // namespace

void OutputBuffer::writeData(std::ostringstream &os) {
    if (writeWithTimeoutWhile(_fd, toStringView(os), 100ms,
                              [this]() { return !shouldTerminate(); }) == -1) {
        generic_error ge{"cannot write to client socket"};
        Informational(_logger) << ge;
>>>>>>> upstream/master
    }
}

void OutputBuffer::setError(ResponseCode code, const std::string &message) {
    Warning(_logger) << "error: " << message;
    // only the first error is being returned
    if (_error_message.empty()) {
        _error_message = message + "\n";
        _response_code = code;
    }
}

std::string OutputBuffer::getError() const { return _error_message; }
