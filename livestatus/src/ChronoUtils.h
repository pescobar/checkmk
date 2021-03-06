// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef ChronoUtils_h
#define ChronoUtils_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <chrono>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <ratio>
#include <string>
#include <utility>
<<<<<<< HEAD

using minutes_d = std::chrono::duration<double, std::ratio<60>>;

=======

using minutes_d = std::chrono::duration<double, std::ratio<60>>;

>>>>>>> upstream/master
inline double elapsed_ms_since(std::chrono::steady_clock::time_point then) {
    return std::chrono::duration_cast<
               std::chrono::duration<double, std::milli>>(
               std::chrono::steady_clock::now() - then)
        .count();
}

inline tm to_tm(std::chrono::system_clock::time_point tp) {
    time_t t = std::chrono::system_clock::to_time_t(tp);
    struct tm ret;
// NOTE: A brilliant example of how to make a simple API function a total
// chaos follows...
#if defined(__STDC_LIB_EXT1__)
    // C11 function, only guaranteed to be available when a
    //    #define __STDC_WANT_LIB_EXT1_ 1
    // is done before including <time.h>. Signature:
    //    struct tm *localtime_s(const time_t *restrict timer,
    //                           struct tm *restrict result)
    localtime_s(&t, &ret);
#elif defined(__WIN32)
    // Win32 variant, it keeps us entertained with swapped parameters and a
    // different return value, yay! Signature:
    //    errno_t localtime_s(struct tm* _tm, const time_t *time)
    // We have to de-confuse cppcheck:
    // cppcheck-suppress uninitvar
    localtime_s(&ret, &t);
#else
    // POSIX.1-2008 variant, available under MinGW64 only under obscure
    // circumstances, so better avoid it there. Signature:
    //    struct tm *localtime_r(const time_t *restrict timer,
    //                           struct tm *restrict result);
    localtime_r(&t, &ret);
#endif
    // Reason: see Win32 section above
    // cppcheck-suppress uninitvar
    return ret;
}

inline std::chrono::system_clock::time_point from_tm(tm tp) {
    return std::chrono::system_clock::from_time_t(mktime(&tp));
}

template <typename Rep, typename Period>
inline timeval to_timeval(std::chrono::duration<Rep, Period> dur) {
<<<<<<< HEAD
=======
    using namespace std::chrono_literals;
>>>>>>> upstream/master
    timeval tv;
    // NOTE: The static_casts below are needed to avoid warning on e.g. some
    // 32bit platforms, because the underlying types might be larger than the
    // timeval fields. We can't use the correct POSIX types time_t and
    // suseconds_t because of the broken MinGW cross compiler, so we revert to
    // decltype.
    tv.tv_sec = static_cast<decltype(tv.tv_sec)>(
        std::chrono::duration_cast<std::chrono::seconds>(dur).count());
    tv.tv_usec = static_cast<decltype(tv.tv_usec)>(
<<<<<<< HEAD
        std::chrono::duration_cast<std::chrono::microseconds>(
            dur % std::chrono::seconds(1))
=======
        std::chrono::duration_cast<std::chrono::microseconds>(dur % 1s)
>>>>>>> upstream/master
            .count());
    return tv;
}

inline std::chrono::system_clock::time_point from_timeval(const timeval &tv) {
    return std::chrono::system_clock::time_point(
        std::chrono::seconds(tv.tv_sec) +
        std::chrono::microseconds(tv.tv_usec));
}

inline std::chrono::system_clock::time_point parse_time_t(
    const std::string &str) {
    return std::chrono::system_clock::from_time_t(atoi(str.c_str()));
}

template <typename Dur>
typename Dur::rep time_point_part(std::chrono::system_clock::time_point &tp) {
    return std::chrono::duration_cast<Dur>(tp.time_since_epoch() % Dur(1000))
        .count();
}

class FormattedTimePoint {
public:
    explicit FormattedTimePoint(std::chrono::system_clock::time_point tp,
                                std::string format = default_format)
        : _tp(tp), _format(std::move(format)) {}
    explicit FormattedTimePoint(time_t t, std::string format = default_format)
        : _tp(std::chrono::system_clock::from_time_t(t))
        , _format(std::move(format)) {}

    friend std::ostream &operator<<(std::ostream &os,
                                    const FormattedTimePoint &f) {
        tm local = to_tm(f._tp);
        return os << std::put_time(&local, f._format.c_str());
    }

private:
    std::chrono::system_clock::time_point _tp;
    std::string _format;

    // NOTE: In a perfect world we would simply use "%F %T" below, but the "%F"
    // format is a C99 addition, and the "%T" format is part of The Single Unix
    // Specification. Both formats should be available in any C++11-compliant
    // compiler, but the MinGW cross compiler doesn't get this right. So let's
    // use their ancient expansions...
    static constexpr auto default_format = "%Y-%m-%d %H:%M:%S";
};

#endif  // ChronoUtils_h
