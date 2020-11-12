<<<<<<< HEAD

// Perfect Mail Slot Transport
// by SK
// Usage example - see GreatExampleReceiverBegin, GreatExampleReceiverEnd and
// GreatExampleSender.
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

// Simple Mail Slot Transport
// Windows only
// by SK
// CODE STYLE is a bit old-fashioned, this is mix of MSN example with
// very old implementation

// Thread Safe
>>>>>>> upstream/master

// Sender is using postman
// Receiver is using mailbox (with thread/callback)

#pragma once
#include <windows.h>

#include <atomic>
#include <cstdint>
<<<<<<< HEAD
=======
#include <filesystem>
>>>>>>> upstream/master
#include <mutex>
#include <string>
#include <strstream>
#include <thread>

#include "tools/_process.h"  // folders
<<<<<<< HEAD
=======
#include "tools/_win.h"      // trace and log
>>>>>>> upstream/master
#include "tools/_xlog.h"     // trace and log

// to be moved outside
namespace wtools {
// we are using custom allocator because of Windows taking care about memory
// allocated
<<<<<<< HEAD
inline void* ProcessHeapAlloc(size_t Size) {
    return HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, Size);
}

inline void ProcessHeapFree(void* Data) {
    if (Data) HeapFree(GetProcessHeap(), 0, Data);
=======
inline void* ProcessHeapAlloc(size_t size) {
    return HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, size);
}

inline void ProcessHeapFree(void* data) {
    if (data) HeapFree(GetProcessHeap(), 0, data);
>>>>>>> upstream/master
}

// legacy from the past
inline ACL* BuildSDAcl() {
    SID_IDENTIFIER_AUTHORITY siaWorld = SECURITY_WORLD_SID_AUTHORITY;
    SID_IDENTIFIER_AUTHORITY siaCreator = SECURITY_CREATOR_SID_AUTHORITY;

    char buf_everyone_sid[32];
    char buf_creator_sid[32];

    auto everyone_sid = reinterpret_cast<SID*>(buf_everyone_sid);
    auto owner_sid = reinterpret_cast<SID*>(buf_creator_sid);

    // initialize well known SID's
    if (!InitializeSid(everyone_sid, &siaWorld, 1) ||
        !InitializeSid(owner_sid, &siaCreator, 1))
        return nullptr;

    *GetSidSubAuthority(everyone_sid, 0) = SECURITY_WORLD_RID;
    *GetSidSubAuthority(owner_sid, 0) = SECURITY_CREATOR_OWNER_RID;

    // compute size of acl
    auto acl_size = sizeof(ACL) +
                    2 * (sizeof(ACCESS_ALLOWED_ACE) - sizeof(DWORD)) +
                    GetSidLengthRequired(1) +  // well-known Everyone Sid
                    GetSidLengthRequired(1);   // well-known Creator Owner Sid

    // create ACL
    auto acl = static_cast<ACL*>(ProcessHeapAlloc(acl_size));

    // init ACL
    if (acl && InitializeAcl(acl, (int32_t)acl_size, ACL_REVISION) &&
        AddAccessAllowedAce(acl, ACL_REVISION, FILE_ALL_ACCESS, everyone_sid) &&
        AddAccessAllowedAce(acl, ACL_REVISION, FILE_ALL_ACCESS, owner_sid))
        return acl;

    // FAILURE is HERE
    ProcessHeapFree(acl);
    return nullptr;
}

// RAII class to keep MS Windows Security Descriptor temporary
class SecurityAttributeKeeper {
public:
    SecurityAttributeKeeper() {
        if (!allocAll()) cleanupAll();  // failed here
    }
    ~SecurityAttributeKeeper() { cleanupAll(); }

    const SECURITY_ATTRIBUTES* get() const { return sa_; }
    SECURITY_ATTRIBUTES* get() { return sa_; }

private:
    bool allocAll() {
        acl_ = BuildSDAcl();  // this trash is referenced in the Security
                              // Descriptor, we should keepit safe
        sd_ = static_cast<SECURITY_DESCRIPTOR*>(
            ProcessHeapAlloc(sizeof(SECURITY_DESCRIPTOR)));
        sa_ = static_cast<SECURITY_ATTRIBUTES*>(
            ProcessHeapAlloc(sizeof(SECURITY_ATTRIBUTES)));

        if (acl_ && sd_ && sa_ &&  // <--- alloc check
            InitializeSecurityDescriptor(sd_, SECURITY_DESCRIPTOR_REVISION) &&
            SetSecurityDescriptorDacl(sd_, TRUE, acl_, FALSE)) {
            sa_->nLength = sizeof(SECURITY_ATTRIBUTES);
            sa_->lpSecurityDescriptor = sd_;
            sa_->bInheritHandle = FALSE;
            return true;
        }
        return false;
    }
    void cleanupAll() {
        if (acl_) ProcessHeapFree(acl_);
        if (sd_) ProcessHeapFree(sd_);
        if (sa_) ProcessHeapFree(sa_);
        acl_ = nullptr;
        sd_ = nullptr;
        sa_ = nullptr;
    }

    // below are allocated using ProcessHeapAlloc values
    SECURITY_DESCRIPTOR* sd_{nullptr};
    SECURITY_ATTRIBUTES* sa_{nullptr};
    ACL* acl_{nullptr};
};

}  // namespace wtools

namespace cma {
class MailSlot;

constexpr bool kUsePublicProfileLog = true;  // to Profile(not to Windows)

constexpr const char* const kMailSlotLogFilePrivate =
    "\\Logs\\cmk_mail_log.log";
constexpr const char* const kMailSlotLogFileName = "cmk_mail.log";

<<<<<<< HEAD
inline bool IsMailApiTraced() { return false; }

// #TODO gtest
inline const std::string GetMailApiLog() {
    static std::string folder_path = "";
    if (0 == folder_path[0]) {
        if (kUsePublicProfileLog) {
            std::string public_folder_path =
                cma::tools::win::GetSomeSystemFolderA(FOLDERID_Public);
            if (!public_folder_path.empty()) {
                folder_path = public_folder_path + kMailSlotLogFileName;
            }
        } else {
            char win_path[256];
            auto len = GetWindowsDirectoryA(win_path, 256);
            if (len) {
                folder_path = win_path;
                folder_path += "\\Logs";
                folder_path += kMailSlotLogFileName;
            }
        }
    }
    return folder_path;
=======
inline bool IsMailApiTraced() { return true; }

// #TODO gtest
inline const std::string GetMailApiLog() {
    using namespace cma::tools;
    namespace fs = std::filesystem;

    if (kUsePublicProfileLog) {
        fs::path path = win::GetSomeSystemFolder(FOLDERID_Public);
        if (!path.empty()) return (path / kMailSlotLogFileName).u8string();
    }

    fs::path win_path = win::GetSomeSystemFolder(FOLDERID_Windows);

    if (!win_path.empty())
        return (win_path / "Logs" / kMailSlotLogFileName).u8string();

    return {};
}

template <typename... Args>
void MailSlotLog(Args... args) {
    xlog::l(IsMailApiTraced(), args...).filelog(GetMailApiLog());
>>>>>>> upstream/master
}

// This is Thread Callback definition
// Slot is a your slot, just to have
// Data & Len is self explanatory
// Context is parameter supplied by YOU, my friend when you creates mailbox,
// it may be nullptr or something important like an address of an object of
// a class to which callback should deliver data
<<<<<<< HEAD
typedef bool (*MailBoxThreadFoo)(const MailSlot* Slot, const void* Data,
                                 int Len, void* Context);

// const char* const MAIL_SLOT_PREFIX     = "\\\\.\\mailslot\\";
const char* const MAIL_SLOT_VCAST_SERVER =
    "nc_vcast_server";  // created inside service
const char* const kVCastMailSlotPrefix =
    "nc_vcast_client";  // created inside app
const int DEFAULT_THREAD_SLEEP = 20;
const char* const kUseThisNamePrefix =
    "^^^:";  // send to the hosting app with answer channel
const char* const kInternalTestString =
    "*test*";  // send to the hosting app with answer channel
=======
using MailBoxThreadFoo = bool (*)(const MailSlot* slot, const void* data,
                                  int len, void* context);

constexpr int DEFAULT_THREAD_SLEEP = 20;
>>>>>>> upstream/master

class MailSlot {
public:
    enum ErrCodes {
        SUCCESS = 0,
        FAILED_READ = -1,
        TOO_SMALL = -2,
        FAILED_INFO = -3,
        FAILED_INIT = -4,
        FAILED_CREATE = -5
    };

<<<<<<< HEAD
private:
    MailSlot(const MailSlot&) {}
    MailSlot& operator=(const MailSlot&) {}

public:
    // convert slot name into fully qualified global object
    static std::string BuildMailSlotName(const char* Name, int Id,
                                         const char* PcName = ".") {
        std::string name = "\\\\";
        name += PcName;
        name += "\\mailslot\\Global\\";  // this work. ok. don't touch.
        name += Name;
        name += "_";
        name +=
            std::to_string(Id);  // session id or something unique you prefer
        return name;
    }

    MailSlot(const char* Name, int Id, const char* PcName = ".")
        : handle_(0)
        , owner_(false)
        , keep_running_(true)
        , main_thread_(nullptr) {
        name_ = BuildMailSlotName(Name, Id, PcName);
    }

    // with prepapred mail slot
    MailSlot(const char* Name)
        : handle_(0)
        , owner_(false)
        , keep_running_(true)
        , main_thread_(nullptr)
        , name_(Name)

    {}
=======
    MailSlot(const MailSlot&) = delete;
    MailSlot& operator=(const MailSlot&) = delete;

    MailSlot(MailSlot&&) = delete;
    MailSlot& operator=(MailSlot&&) = delete;

public:
    // convert slot name into fully qualified global object
    static std::string BuildMailSlotName(const char* slot_name, int id,
                                         const char* pc_name) {
        std::string name = "\\\\";
        name += pc_name;
        name += "\\mailslot\\Global\\";  // this work. ok. don't touch.
        name += slot_name;
        name += "_";
        name += std::to_string(id);  // session id or something unique
        return name;
    }
    MailSlot(const char* name, int id, const char* pc_name) {
        name_ = BuildMailSlotName(name, id, pc_name);
    }

    MailSlot(const char* name, int id) {
        name_ = BuildMailSlotName(name, id, ".");
    }

    // with prepared mail slot
    explicit MailSlot(const char* name) : name_(name) {}
>>>>>>> upstream/master

    ~MailSlot() { Close(); }

    // API below

    // Accessors
<<<<<<< HEAD
    bool IsOwner() const {
        return owner_;
    }  // true, wehn mailslot had been "created", false if "opened"
    bool IsPostman() const { return !owner_; }
    const char* GetName() const { return name_.c_str(); }
    HANDLE GetHandle() { return handle_; }

    // mailbox start here
    bool ConstructThread(cma::MailBoxThreadFoo Foo, int SleepValue,
                         void* Context, bool ForceOpen = false) {
        if (main_thread_) {
            xlog::l(IsMailApiTraced(), XLOG_FUNC + " Double call is forbidden")
                .filelog(GetMailApiLog());
            return false;
        }
        keep_running_ = true;
        if (ForceOpen) {
            // future use only or wil be removed
=======
    [[nodiscard]] bool IsOwner() const noexcept {
        return owner_;
    }  // true, if mailslot had been "created", false if "opened"
    [[nodiscard]] bool IsPostman() const noexcept { return !owner_; }
    [[nodiscard]] const char* GetName() const noexcept { return name_.c_str(); }
    [[nodiscard]] HANDLE GetHandle() const noexcept { return handle_; }

    bool ConstructThread(cma::MailBoxThreadFoo foo, int sleep_ms,
                         void* context) {
        return ConstructThread(foo, sleep_ms, context, false);
    }

    // mailbox start here
    bool ConstructThread(cma::MailBoxThreadFoo foo, int sleep_ms, void* context,
                         bool force_open) {
        if (main_thread_) {
            MailSlotLog(XLOG_FUNC + " Double call is forbidden");
            return false;
        }

        keep_running_ = true;
        if (force_open) {
            // future use only or will be removed
>>>>>>> upstream/master
            for (int i = 0; i < 10; i++) {
                auto ret = Create();
                if (ret) break;
                Close();
                using namespace std::chrono;
                std::this_thread::sleep_for(100ms);
            }
        } else
            while (!Create()) {
                name_ += "x";
            }

        main_thread_ = std::make_unique<std::thread>(
<<<<<<< HEAD
            &MailSlot::MailBoxThread, this, Foo, SleepValue, Context);
=======
            &MailSlot::MailBoxThread, this, foo, sleep_ms, context);
>>>>>>> upstream/master
        return true;
    }

    // mailbox dies here
    void DismantleThread() {
        keep_running_ = false;
        if (main_thread_) {
            if (main_thread_->joinable()) main_thread_->join();
            main_thread_.reset();
        }
        Close();
    }

    // postman the only operation
<<<<<<< HEAD
    bool ExecPost(const void* Data, uint64_t Length) {
        auto len = static_cast<int>(Length);
        if (!Data && len) {
            xlog::l(IsMailApiTraced(), "Bad data for \"%s\"posting %p %d",
                    name_.c_str(), Data, len)
                .filelog(GetMailApiLog());
=======
    bool ExecPost(const void* data, uint64_t length) {
        auto len = static_cast<int>(length);
        if (data == nullptr && len != 0) {
            MailSlotLog("Bad data for \"%s\"posting %p %d", name_.c_str(), data,
                        len);
>>>>>>> upstream/master
            return false;
        }

        if (Open()) {
<<<<<<< HEAD
            auto ret = Post(Data, len);
            Close();
            return ret;
        } else {
            xlog::l(IsMailApiTraced(), "Can't open mail slot \"%s\"",
                    name_.c_str())
                .filelog(GetMailApiLog());
            return false;
        }
    }
    // protected:
=======
            auto ret = Post(data, len);
            Close();
            return ret;
        }

        MailSlotLog("Can't open mail slot \"%s\"", name_.c_str());
        return false;
    }

    // returns false on duplicated name
>>>>>>> upstream/master
    bool Create() {
        std::lock_guard<std::mutex> lck(lock_);

        if (handle_) return true;  // bad(already exists) call

        handle_ = createMailSlot(name_.c_str());

<<<<<<< HEAD
        if (handle_ == INVALID_HANDLE_VALUE) handle_ = nullptr;

        if (!handle_ && GetLastError() == 183)  // duplicated file name
        {
            xlog::l(IsMailApiTraced(),
                    "Duplicated OWN mail slot \"%s\" Retry with OPEN",
                    name_.c_str())
                .filelog(GetMailApiLog());
            return false;
        }

        auto ret = handle_ != nullptr;

        if (ret) {
            owner_ = true;  // we create -> we own
            xlog::l(IsMailApiTraced(), "OWN Mail slot \"%s\" was opened",
                    name_.c_str())
                .filelog(GetMailApiLog());
        } else {
            xlog::l(IsMailApiTraced(), "Fail open OWN mail slot \"%s\" %d",
                    name_.c_str(), GetLastError())
                .filelog(GetMailApiLog());
=======
        if (handle_ == nullptr &&
            ::GetLastError() == 183)  // duplicated file name
        {
            MailSlotLog("Duplicated OWN mail slot \"%s\" Retry with OPEN",
                        name_.c_str());
            return false;
        }

        if (handle_ != nullptr) {
            owner_ = true;  // we create -> we own
            MailSlotLog("OWN Mail slot \"%s\" was opened", name_.c_str());
        } else {
            MailSlotLog("Fail open OWN mail slot \"%s\" %d", name_.c_str(),
                        ::GetLastError());
>>>>>>> upstream/master
        }

        return true;
    }

    bool Open() {
        std::lock_guard<std::mutex> lck(lock_);

        if (handle_) return true;  // bad(already exists) call
        handle_ = openMailSlotWrite(name_.c_str());

<<<<<<< HEAD
        if (handle_ == INVALID_HANDLE_VALUE) {
            auto error = GetLastError();
            handle_ = nullptr;
            // please do not use printf - chrome host app communicates with
            // chrome via stdin/stdout making printf breaks communication
            // printf("Error %d opening file %s\n", error, name_.c_str());
            xlog::l(IsMailApiTraced(), "Fail open mail slot \"%s\" %d",
                    name_.c_str(), error)
                .filelog(GetMailApiLog());
        } else
            xlog::l(IsMailApiTraced(), "Mail slot \"%s\" was opened",
                    name_.c_str())
                .filelog(GetMailApiLog());
=======
        if (wtools::IsInvalidHandle(handle_)) {
            auto error = ::GetLastError();
            handle_ = nullptr;
            MailSlotLog("Fail open mail slot \"%s\" %d", name_.c_str(), error);
        } else
            MailSlotLog("Mail slot \"%s\" was opened", name_.c_str());
>>>>>>> upstream/master

        return handle_ != nullptr;
    }

    bool Close() {
        std::lock_guard<std::mutex> lck(lock_);
<<<<<<< HEAD
        if (handle_) {
            auto ret = CloseHandle(handle_);
            if (!ret) {
                // if failed do not clean value
                auto error = GetLastError();
                xlog::l(IsMailApiTraced(), "Fail CLOSE mail slot \"%s\" %d",
                        name_.c_str(), error)
                    .filelog(GetMailApiLog());
            } else
                handle_ = nullptr;
        }
=======
        if (nullptr == handle_) return true;

        auto ret = ::CloseHandle(handle_);
        if (ret)
            handle_ = nullptr;
        else {
            // if failed do not clean value
            auto error = ::GetLastError();
            MailSlotLog("Fail CLOSE mail slot \"%s\" %d", name_.c_str(), error);
        }

>>>>>>> upstream/master
        return true;
    }

    bool Post(const void* Data, int Len) {
        std::lock_guard<std::mutex> lck(lock_);
        if (!handle_ || IsOwner()) {
<<<<<<< HEAD
            xlog::l(IsMailApiTraced(), "Bad situation %p %d", handle_,
                    (int)IsOwner())
                .filelog(GetMailApiLog());
            return false;
        }

        DWORD cbWritten = 0;
        auto fResult = WriteFile(handle_, Data, Len, &cbWritten, nullptr);

        if (0 == fResult) {
            xlog::l(IsMailApiTraced(), "Bad write %d", GetLastError())
                .filelog(GetMailApiLog());

            return false;
        }

        return true;
    }

    int Get(void* Data, unsigned int MaxLen) {
        std::lock_guard<std::mutex> lck(lock_);
        if (!handle_ || IsPostman()) return FAILED_INIT;
        auto hEvent = CreateEvent(nullptr, FALSE, FALSE, nullptr);
        if (nullptr == hEvent) {
            auto error = GetLastError();
            xlog::l(IsMailApiTraced(), "Failed Create Event with error %d",
                    error)
                .filelog(GetMailApiLog());

            return FAILED_CREATE;
        }
        ON_OUT_OF_SCOPE(CloseHandle(hEvent));
=======
            MailSlotLog("Bad situation %p %d", handle_, (int)IsOwner());
            return false;
        }

        DWORD written = 0;
        auto success = ::WriteFile(handle_, Data, Len, &written, nullptr);

        if (success) return true;

        MailSlotLog("Bad write %d", ::GetLastError());
        return false;
    }

    int Get(void* data, unsigned int max_len) {
        std::lock_guard<std::mutex> lck(lock_);
        if (!handle_ || IsPostman()) return ErrCodes::FAILED_INIT;
        auto event = ::CreateEvent(nullptr, FALSE, FALSE, nullptr);
        if (nullptr == event) {
            auto error = ::GetLastError();
            MailSlotLog("Failed Create Event with error %d", error);

            return ErrCodes::FAILED_CREATE;
        }
        ON_OUT_OF_SCOPE(::CloseHandle(event));
>>>>>>> upstream/master

        OVERLAPPED ov = {0};
        ov.Offset = 0;
        ov.OffsetHigh = 0;
<<<<<<< HEAD
        ov.hEvent = hEvent;
=======
        ov.hEvent = event;
>>>>>>> upstream/master

        DWORD message_size = 0;
        DWORD message_count = 0;

<<<<<<< HEAD
        auto fResult = GetMailslotInfo(handle_,  // mailslot handle
                                       nullptr,  // no maximum message size
                                       &message_size,   // size of next message
                                       &message_count,  // number of messages
                                       nullptr);        // no read time-out

        if (!fResult) return ErrCodes::FAILED_INFO;

        if (message_size == MAILSLOT_NO_MESSAGE) return ErrCodes::SUCCESS;

        if (Data == nullptr) {
            return message_size;
        }

        if (MaxLen < message_size) return ErrCodes::TOO_SMALL;

        DWORD message_read = 0;
        fResult = ReadFile(handle_, Data, message_size, &message_read, &ov);

        if (fResult) return message_read;

        auto error = GetLastError();
        xlog::l(IsMailApiTraced(), "Failed read mail slot with error %d", error)
            .filelog(GetMailApiLog());
=======
        auto success = ::GetMailslotInfo(handle_,  // mailslot handle
                                         nullptr,  // no maximum message size
                                         &message_size,  // size of next message
                                         &message_count,  // number of messages
                                         nullptr);        // no read time-out

        if (!success) return ErrCodes::FAILED_INFO;

        if (message_size == MAILSLOT_NO_MESSAGE) return ErrCodes::SUCCESS;

        if (data == nullptr) return message_size;

        if (max_len < message_size) return ErrCodes::TOO_SMALL;

        DWORD message_read = 0;
        success = ::ReadFile(handle_, data, message_size, &message_read, &ov);

        if (success) return message_read;

        auto error = ::GetLastError();
        MailSlotLog("Failed read mail slot with error %d", error);
>>>>>>> upstream/master

        return ErrCodes::FAILED_READ;
    }

<<<<<<< HEAD
    void MailBoxThread(cma::MailBoxThreadFoo Foo, int SleepValue,
                       void* Context) {
=======
    void MailBoxThread(cma::MailBoxThreadFoo foo, int sleep_value,
                       void* context) {
>>>>>>> upstream/master
        int buffer_size = 16000;
        char* buffer = new char[buffer_size];
        while (keep_running_) {
            auto required_size = Get(nullptr, buffer_size);
            if (required_size > buffer_size) {
                delete[] buffer;
                buffer = new char[required_size];
<<<<<<< HEAD
                if (buffer) {
                    buffer_size = required_size;
                }
=======
                buffer_size = required_size;
>>>>>>> upstream/master
            }

            auto read_size = Get(buffer, buffer_size);
            if (read_size > 0) {
<<<<<<< HEAD
                Foo(this, buffer, read_size, Context);
            } else if (read_size < 0) {
            }

            Sleep(SleepValue > 0
                      ? SleepValue
                      : cma::DEFAULT_THREAD_SLEEP);  // we need sleep to
                                                     // prevent polling
=======
                foo(this, buffer, read_size, context);
            } else if (read_size < 0) {
            }

            ::Sleep(sleep_value > 0
                        ? sleep_value
                        : cma::DEFAULT_THREAD_SLEEP);  // we need sleep to
                                                       // prevent polling
>>>>>>> upstream/master
        }
        delete[] buffer;
    }

    // typically called from the ::Open, to write data in
<<<<<<< HEAD
    static HANDLE openMailSlotWrite(const char* Name) {
        return CreateFileA(Name, GENERIC_WRITE, FILE_SHARE_READ, nullptr,
                           OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
    }

    static HANDLE createMailSlot(const char* Name) {
=======
    static HANDLE openMailSlotWrite(const char* name) {
        return ::CreateFileA(name, GENERIC_WRITE, FILE_SHARE_READ, nullptr,
                             OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
    }

    static HANDLE createMailSlot(const char* name) {
>>>>>>> upstream/master
        wtools::SecurityAttributeKeeper
            security_attribute_keeper;  // black magic behind, do not try to
                                        // understand, RAII auto-destroy
        auto sa = security_attribute_keeper.get();
        if (nullptr == sa) {
<<<<<<< HEAD
            xlog::l(IsMailApiTraced(), "Failed to create security descriptor")
                .filelog(GetMailApiLog());
            return INVALID_HANDLE_VALUE;
        }

        return CreateMailslotA(
            Name,                   // name
=======
            MailSlotLog("Failed to create security descriptor");
            return nullptr;
        }

        return CreateMailslotA(
            name,                   // name
>>>>>>> upstream/master
            0,                      // no maximum message size
            MAILSLOT_WAIT_FOREVER,  // no time-out for operations
            sa);                    // black magic resulted SECURITY_ATTRIBUTES
    }

private:
<<<<<<< HEAD
    std::mutex lock_;   // protect data
    std::string name_;  // fully qualified mailslot name
    HANDLE handle_;     // handle to the mailslot
    bool owner_;        // true - we receive data, false - we send data

    std::atomic<bool> keep_running_;  // thread flag
    std::unique_ptr<std::thread>
        main_thread_;  // thread itself, Controlled by Construct/Dismantle
=======
    std::mutex lock_;          // protect data
    std::string name_;         // fully qualified mailslot name
    HANDLE handle_ = nullptr;  // handle to the mailslot
    bool owner_ = false;       // true - we receive data, false - we send data

    std::atomic<bool> keep_running_ = true;  // thread flag
    std::unique_ptr<std::thread>
        main_thread_{};  // controlled by Construct/Dismantle
>>>>>>> upstream/master
};
};  // namespace cma
