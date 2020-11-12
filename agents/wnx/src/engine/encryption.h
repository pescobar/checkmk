<<<<<<< HEAD
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.

>>>>>>> upstream/master
#ifndef encryption_h__
#define encryption_h__

#include <wincrypt.h>

<<<<<<< HEAD
=======
#include <optional>
>>>>>>> upstream/master
#include <string>
#include <string_view>
#include <vector>

<<<<<<< HEAD
#include "common/wtools.h"
#include "tools/_misc.h"

#include "cfg.h"
#include "logger.h"

=======
#include "tools/_misc.h"

>>>>>>> upstream/master
namespace cma::encrypt {
// algorithm can't currently be changed
enum Algorithm {
    kDefault = CALG_AES_256,
    kHash = CALG_MD5

};

enum class Length {
    kDefault = 0,
    k128 = 128,
    k192 = 192,
    k256 = 256,
    k512 = 512,
    k1024 = 1024,
    k2048 = 2048
};

class Commander {
public:
    explicit Commander();

<<<<<<< HEAD
    Commander(const std::string &Password, Length KeyLength = Length::kDefault);

    Commander(const BYTE *Key, DWORD KeyLength);
=======
    Commander(const std::string &key, Length length = Length::kDefault);

    Commander(const BYTE *key, DWORD length);
>>>>>>> upstream/master

    ~Commander();

    // in-place encrypt buffer
<<<<<<< HEAD
    std::tuple<bool, size_t> encode(void *InOut, size_t InputSize,
                                    size_t BufferSize,
                                    bool LastBlock = true) const;
    std::tuple<bool, size_t> decode(void *InOut, size_t input_size,
                                    bool LastBlock = true);

    std::optional<cma::ByteVector> getKey() const;

    bool randomizeBuffer(void *Buffer, size_t BufferSize) const;
=======
    std::tuple<bool, size_t> encode(void *in_out, size_t size,
                                    size_t buffer_size,
                                    bool last_block = true) const;
    std::tuple<bool, size_t> decode(void *in_out, size_t size,
                                    bool last_block = true);

    std::optional<cma::ByteVector> getKey() const;

    bool randomizeBuffer(void *buffer, size_t buffer_size) const;
>>>>>>> upstream/master

    const bool available() const { return key_ != 0; }

    std::optional<uint32_t> blockSize() const;

<<<<<<< HEAD
    std::optional<size_t> CalcBufferOverhead(size_t DataSize) const noexcept;
=======
    std::optional<size_t> CalcBufferOverhead(size_t data_size) const noexcept;
>>>>>>> upstream/master

private:
    void cleanup();
    HCRYPTPROV obtainContext();
    void releaseContext();

    void checkAndConfigure();

    static size_t keySize(ALG_ID algorithm);

<<<<<<< HEAD
    HCRYPTKEY generateKey(Length KeyLength) const;
    HCRYPTKEY importKey(const BYTE *key, DWORD key_size) const;
    // derive key and iv from the password in the same manner as openssl does
    HCRYPTKEY deriveOpenSSLKey(const std::string &Password, Length KeyLength,
                               int Iterations);
=======
    HCRYPTKEY generateKey(Length key_length) const;
    HCRYPTKEY importKey(const BYTE *key, DWORD key_size) const;
    // derive key and iv from the password in the same manner as openssl does
    HCRYPTKEY deriveOpenSSLKey(const std::string &password, Length key_length,
                               int iterations);
>>>>>>> upstream/master
    void releaseKey();

    HCRYPTPROV crypt_provider_;
    HCRYPTKEY key_;
    Algorithm algorithm_;
};

std::unique_ptr<Commander> MakeCrypt();

<<<<<<< HEAD
std::tuple<HCRYPTHASH, size_t> GetHash(HCRYPTPROV Provider);
=======
std::tuple<HCRYPTHASH, size_t> GetHash(HCRYPTPROV crypt_provider);
>>>>>>> upstream/master
}  // namespace cma::encrypt
#endif  // encryption_h__
