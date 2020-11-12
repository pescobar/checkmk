
#include "stdafx.h"

#include "eventlogbase.h"
<<<<<<< HEAD
#include "eventlogstd.h"
#include "eventlogvista.h"

namespace cma::evl {
std::unique_ptr<cma::evl::EventLogBase> OpenEvl(const std::wstring &Name,
                                                bool VistaApi) {
    if (VistaApi && g_evt.close)
        return std::unique_ptr<EventLogBase>(new EventLogVista(Name));

    return std::unique_ptr<EventLogBase>(new EventLog(Name));
}

std::pair<uint64_t, cma::cfg::EventLevels> ScanEventLog(
    EventLogBase &log, uint64_t previouslyReadId, cma::cfg::EventLevels level) {
    // we must seek past the previously read event - if there was one
    const uint64_t seekPosition =
        previouslyReadId + (cma::cfg::kInitialPos == previouslyReadId ? 0 : 1);

    cma::cfg::EventLevels worstState = cma::cfg::EventLevels::kAll;
    uint64_t lastRecordId = previouslyReadId;

    // WARNING:
    // seek implementations for pre-Vista and post-Vista are completely
    // different.
    // seek *must not* return any value as it is different between pre/post
    // Vista.
    log.seek(seekPosition);
=======

#include "eventlogstd.h"
#include "eventlogvista.h"
#include "logger.h"

namespace cma::evl {
std::unique_ptr<cma::evl::EventLogBase> OpenEvl(const std::wstring &name,
                                                bool vista_api) {
    if (vista_api && g_evt.close)
        return std::unique_ptr<EventLogBase>(new EventLogVista(name));

    return std::unique_ptr<EventLogBase>(new EventLog(name));
}

std::pair<uint64_t, cma::cfg::EventLevels> ScanEventLog(
    EventLogBase &log, uint64_t pos, cma::cfg::EventLevels level) {
    // we must seek past the previously read event - if there was one
    const auto seek_pos = choosePos(pos);

    auto worst_state = cma::cfg::EventLevels::kAll;
    auto last_pos = pos;

    log.seek(seek_pos);
>>>>>>> upstream/master
    while (1) {
        auto record = log.readRecord();
        if (record == nullptr) break;
        ON_OUT_OF_SCOPE(delete record);

<<<<<<< HEAD
        lastRecordId = record->recordId();
        auto calculated = record->calcEventLevel(level);
        worstState = std::max(worstState, calculated);
    }

    return {lastRecordId, worstState};
}

std::pair<uint64_t, std::string> PrintEventLog(EventLogBase &log,
                                               uint64_t previouslyReadId,
                                               cma::cfg::EventLevels level,
                                               bool HideContext) {
    // we must seek past the previously read event - if there was one
    const uint64_t seekPosition =
        previouslyReadId + (cma::cfg::kInitialPos == previouslyReadId ? 0 : 1);

    uint64_t lastRecordId = previouslyReadId;

    // WARNING:
    // seek implementations for pre-Vista and post-Vista are completely
    // different.
    // seek *must not* return any value as it is different between pre/post
    // Vista.
    log.seek(seekPosition);
    std::string out;
=======
        last_pos = record->recordId();
        auto calculated = record->calcEventLevel(level);
        worst_state = std::max(worst_state, calculated);
    }

    return {last_pos, worst_state};
}

// return any(!) positive number or 0.
// usually this is positive, because Windows keeps numbers very long
// and do not drop first entry id to 0 even after reset
uint64_t PrintEventLog(EventLogBase &log, uint64_t from_pos,
                       cma::cfg::EventLevels level, bool hide_context,
                       EvlProcessor processor) {
    // we must seek past the previously read event - if there was one
    const auto seek_pos = choosePos(from_pos);

    auto last_pos = from_pos;

    log.seek(seek_pos);

>>>>>>> upstream/master
    while (1) {
        auto record = log.readRecord();

        if (record == nullptr) break;
        ON_OUT_OF_SCOPE(delete record);

<<<<<<< HEAD
        lastRecordId = record->recordId();
        auto str = record->stringize(level, HideContext);
        if (!str.empty()) out += str;
    }

    return {lastRecordId, out};
}  // namespace cma::evl
=======
        last_pos = record->recordId();
        auto str = record->stringize(level, hide_context);
        if (!str.empty())
            if (!processor(str)) break;
    }

    return last_pos;
}
>>>>>>> upstream/master

}  // namespace cma::evl
