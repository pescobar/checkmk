
// provides basic api to start and stop service

#include "stdafx.h"

#include "async_answer.h"

#include <chrono>
#include <cstdint>
#include <mutex>
#include <string>
#include <vector>

#include "common/cfg_info.h"
#include "logger.h"
<<<<<<< HEAD
=======
#include "section_header.h"       // names
>>>>>>> upstream/master
#include "windows_service_api.h"  // global situation

namespace cma::srv {

<<<<<<< HEAD
bool AsyncAnswer::isAnswerOlder(std::chrono::milliseconds Milli) const {
=======
bool AsyncAnswer::isAnswerOlder(std::chrono::milliseconds period) const {
>>>>>>> upstream/master
    using namespace std::chrono;
    auto tp = steady_clock::now();

    std::lock_guard lk(lock_);
<<<<<<< HEAD
    return duration_cast<milliseconds>(tp - tp_id_) > Milli;
=======
    return duration_cast<milliseconds>(tp - tp_id_) > period;
>>>>>>> upstream/master
}

void AsyncAnswer::dropAnswer() {
    std::lock_guard lk(lock_);
    dropDataNoLock();
    sw_.stop();
    sw_.reset();
}

// returns true when answer is ready, false when timeout expires but not ready
<<<<<<< HEAD
bool AsyncAnswer::waitAnswer(std::chrono::milliseconds WaitInterval) {
=======
bool AsyncAnswer::waitAnswer(std::chrono::milliseconds to_wait) {
>>>>>>> upstream/master
    using namespace std::chrono;

    std::unique_lock lk(lock_);
    ON_OUT_OF_SCOPE(sw_.stop());
    return cv_ready_.wait_until(
<<<<<<< HEAD
        lk, steady_clock::now() + WaitInterval, [this]() -> bool {
=======
        lk, steady_clock::now() + to_wait, [this]() -> bool {
>>>>>>> upstream/master
            // check for global exit
            if (cma::srv::IsGlobalStopSignaled()) {
                XLOG::l.i("Breaking Answer on stop");
                return true;
            }
            return awaited_segments_ <= received_segments_;
        });
}

// combines two vectors together
// in case of exception returns false
// Caller MUST Fix section size!
static bool AddVectorGracefully(std::vector<uint8_t>& Out,
<<<<<<< HEAD
                                const std::vector<uint8_t>& In) noexcept {
    auto old_size = Out.size();
    // we have theoretical possibility of exception here
=======
                                const std::vector<uint8_t>& In) {
    auto old_size = Out.size();
    // we have theoretical possibility of exception here

>>>>>>> upstream/master
    try {
        // a bit of optimization
        Out.reserve(Out.size() + In.size());
        Out.insert(Out.end(), In.begin(), In.end());

        // divider after every section with data
        Out.push_back(static_cast<uint8_t>('\n'));
<<<<<<< HEAD
=======
        return true;
>>>>>>> upstream/master
    } catch (const std::exception& e) {
        // return to invariant...
        XLOG::l(XLOG_FLINE + "- disaster '{}'", e.what());
        Out.resize(old_size);
<<<<<<< HEAD
        return false;
    }
    return true;
=======
    }

    return false;
>>>>>>> upstream/master
}

// kills data in any case
// return gathered data back
AsyncAnswer::DataBlock AsyncAnswer::getDataAndClear() {
    std::lock_guard lk(lock_);
    try {
        if (order_ == Order::plugins_last) {
            if (!plugins_.empty()) AddVectorGracefully(data_, plugins_);
            if (!local_.empty()) AddVectorGracefully(data_, local_);
            plugins_.clear();
            local_.clear();
        }

        auto v = std::move(data_);
        dropDataNoLock();
        return v;
    } catch (const std::exception& e) {
        XLOG::l(XLOG_FLINE + " - no-no-no '{}'", e.what());
        dropDataNoLock();
        return {};
    }
}

<<<<<<< HEAD
bool AsyncAnswer::prepareAnswer(std::string_view Ip) noexcept {
=======
bool AsyncAnswer::prepareAnswer(std::string_view Ip) {
>>>>>>> upstream/master
    std::lock_guard lk(lock_);

    if (!external_ip_.empty() || awaited_segments_ != 0 ||
        received_segments_ != 0)
        return false;

    dropDataNoLock();
    external_ip_ = Ip;
    awaited_segments_ = 0;
    received_segments_ = 0;
    plugins_.clear();
    local_.clear();
    sw_.start();
    return true;
}

// sorted list of all received sections
std::vector<std::string> AsyncAnswer::segmentNameList() {
    std::unique_lock lk(lock_);
    std::vector<std::string> list;
    for (const auto& s : segments_) list.emplace_back(s.name_);
    lk.unlock();
    std::sort(list.begin(), list.end());
    return list;
}

// Reporting Function, which called by the section plugins and providers
// Thread safe!
bool AsyncAnswer::addSegment(
<<<<<<< HEAD
    const std::string SectionName,   // name
    const AnswerId Id,               // "password"
    const std::vector<uint8_t> Data  // data for section
) {
    std::lock_guard lk(lock_);
    if (Id != tp_id_) {
        XLOG::d("Invalid attempt to add data '{}'", SectionName);
=======
    const std::string& section_name,  // name
    const AnswerId answer_id,         // "password"
    const std::vector<uint8_t>& data  // data for section
) {
    std::lock_guard lk(lock_);
    if (answer_id != tp_id_) {
        XLOG::d("Invalid attempt to add data '{}'", section_name);
>>>>>>> upstream/master
        return false;
    }

    for (const auto& s : segments_) {
<<<<<<< HEAD
        if (s.name_ == SectionName) {
            XLOG::l("Section '{}' tries to store data twice. F-f", SectionName);
=======
        if (s.name_ == section_name) {
            XLOG::l("Section '{}' tries to store data twice. F-f",
                    section_name);
>>>>>>> upstream/master
            return false;  // duplicated section run
        }
    }

    try {
<<<<<<< HEAD
        segments_.push_back({SectionName, Data.size()});

        // reserve + array math
        if (order_ == Order::plugins_last && SectionName == "plugins") {
            plugins_ = Data;
        } else if (order_ == Order::plugins_last && SectionName == "local") {
            local_ = Data;
        } else if (!Data.empty()) {
            if (!AddVectorGracefully(data_, Data)) segments_.back().length_ = 0;
=======
        segments_.push_back({section_name, data.size()});

        // reserve + array math
        if (order_ == Order::plugins_last &&
            section_name == cma::section::kPlugins) {
            plugins_ = data;
        } else if (order_ == Order::plugins_last &&
                   section_name == cma::section::kLocal) {
            local_ = data;
        } else if (!data.empty()) {
            if (!AddVectorGracefully(data_, data)) segments_.back().length_ = 0;
>>>>>>> upstream/master
        }
    } catch (const std::exception& e) {
        // not possible, but we have to check
        XLOG::l(XLOG_FLINE + "-exception '{}'", e.what());
    }

    received_segments_++;

    if (awaited_segments_ <= received_segments_) {
        // theoretically on answer may wait many threads
        // so notify all.
        cv_ready_.notify_all();
    }

    return true;
}

// used to kick answer and check status
bool AsyncAnswer::tryBreakWait() {
    std::lock_guard lk(lock_);
    cv_ready_.notify_all();

    return true;
}

// resets data, internal use only
void AsyncAnswer::dropDataNoLock() {
    tp_id_ = GenerateAnswerId();
    awaited_segments_ = 0;
    received_segments_ = 0;
    data_.resize(0);
    segments_.resize(0);
    external_ip_ = "";
}
}  // namespace cma::srv
