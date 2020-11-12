
// provides basic api to start and stop service
#include "stdafx.h"

#include "providers/mem.h"

#include <iostream>
#include <string>

#include "tools/_raii.h"
#include "tools/_xlog.h"

<<<<<<< HEAD
namespace cma {

namespace provider {
=======
namespace cma::provider {
>>>>>>> upstream/master

std::string Mem::makeBody() {
    // the log output disabled because it
    // may be quite annoying during realtime monitoring
    // XLOG::t(XLOG_FUNC + " entering");

    // windows
    MEMORYSTATUSEX stat;
    stat.dwLength = sizeof(stat);
    ::GlobalMemoryStatusEx(&stat);
<<<<<<< HEAD
=======
    constexpr uint32_t kKilobyte = 1024;
>>>>>>> upstream/master

    auto string = fmt::format(
        "MemTotal:      {} kB\n"
        "MemFree:       {} kB\n"
        "SwapTotal:     {} kB\n"
        "SwapFree:      {} kB\n"
        "PageTotal:     {} kB\n"
        "PageFree:      {} kB\n"
        "VirtualTotal:  {} kB\n"
        "VirtualFree:   {} kB\n",
<<<<<<< HEAD
        stat.ullTotalPhys / 1024,                            // total
        stat.ullAvailPhys / 1024,                            // free
        (stat.ullTotalPageFile - stat.ullTotalPhys) / 1024,  // swap total
        (stat.ullAvailPageFile - stat.ullAvailPhys) / 1024,  // swap free
        stat.ullTotalPageFile / 1024,                        // paged total
        stat.ullAvailPageFile / 1024,                        // paged free
        stat.ullTotalVirtual / 1024,                         // virtual total
        stat.ullAvailVirtual / 1024);                        // virtual avail
=======
        stat.ullTotalPhys / kKilobyte,                            // total
        stat.ullAvailPhys / kKilobyte,                            // free
        (stat.ullTotalPageFile - stat.ullTotalPhys) / kKilobyte,  // swap total
        (stat.ullAvailPageFile - stat.ullAvailPhys) / kKilobyte,  // swap free
        stat.ullTotalPageFile / kKilobyte,                        // paged total
        stat.ullAvailPageFile / kKilobyte,                        // paged free
        stat.ullTotalVirtual / kKilobyte,   // virtual total
        stat.ullAvailVirtual / kKilobyte);  // virtual avail
>>>>>>> upstream/master

    return string;
}

<<<<<<< HEAD
}  // namespace provider
};  // namespace cma
=======
};  // namespace cma::provider
>>>>>>> upstream/master
