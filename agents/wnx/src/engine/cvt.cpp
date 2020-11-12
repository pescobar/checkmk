// Windows Tools
#include "stdafx.h"

#include "cvt.h"

<<<<<<< HEAD
#include <cstdint>
#include <filesystem>
#include <string>

#include "SimpleIni.h"
#include "logger.h"
#include "tools/_raii.h"
#include "tools/_xlog.h"

namespace cma::cfg::cvt {

// this function is deprecated
YAML::Node LoadIni(const std::filesystem::path& IniFile) {
    namespace fs = std::filesystem;
    if (IniFile.empty()) {
        XLOG::l("Empty file name to load");
        return {};
    }

    std::error_code ec;
    if (!fs::exists(IniFile, ec)) {
        XLOG::l("File '{}' doesn't exist");
        return {};
    }

    return {};
}
}  // namespace cma::cfg::cvt
=======
#include <filesystem>

#include "logger.h"

namespace cma::cfg::cvt {}  // namespace cma::cfg::cvt
>>>>>>> upstream/master
