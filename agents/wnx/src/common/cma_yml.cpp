#include "stdafx.h"

#include "cma_yml.h"

<<<<<<< HEAD
#include <string>
#include <string_view>

#include "fmt/format.h"
=======
#include <fmt/format.h>

#include <string>
#include <string_view>

>>>>>>> upstream/master
#include "logger.h"

namespace cma::yml {
void LogException(const std::string& format, std::string_view group,
                  std::string_view name, const std::exception& e) noexcept {
    try {
        XLOG::l(format, group, name, e.what());
    } catch (const std::exception& e) {
        try {
            XLOG::l.crit("Cannot print '{}' exception '{}'", format, e.what());
        } catch (const std::exception& e) {
            XLOG::l.crit("Cannot print, exception '{}'", e.what());
        }
    }
}

void LogException(const std::string& format, std::string_view name,
                  const std::exception& e) noexcept {
    try {
        XLOG::l(format, name, e.what());
    } catch (const std::exception& e) {
        try {
            XLOG::l.crit("Cannot print '{}' exception '{}'", format, e.what());
        } catch (const std::exception& e) {
            XLOG::l.crit("Cannot print, exception '{}'", e.what());
        }
    }
}

}  // namespace cma::yml
