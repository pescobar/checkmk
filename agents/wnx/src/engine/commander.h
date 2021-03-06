<<<<<<< HEAD
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

// tools to control starting operations

#pragma once
#include <string>
#include <string_view>

namespace cma {

namespace commander {
constexpr std::string_view kMainPeer = "main_peer";
constexpr std::string_view kReload = "reload";
<<<<<<< HEAD

bool RunCommand(std::string_view peer, std::string_view cmd);
=======
constexpr std::string_view kPassTrue = "pass_true";  // test command
constexpr std::string_view kUninstallAlert = "uninstall_alert";

using RunCommandProcessor = bool (*)(std::string_view peer,
                                     std::string_view cmd);
RunCommandProcessor ObtainRunCommandProcessor();

bool RunCommand(std::string_view peer, std::string_view cmd);

// normally only for testing
void ChangeRunCommandProcessor(RunCommandProcessor rcp);
>>>>>>> upstream/master
}  // namespace commander
}  // namespace cma
