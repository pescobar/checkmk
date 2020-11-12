// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef RendererPython_h
#define RendererPython_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <iosfwd>
#include <string>
#include <vector>
=======

#include <iosfwd>
#include <string>
#include <vector>

>>>>>>> upstream/master
#include "Renderer.h"
#include "data_encoding.h"
class Logger;

class RendererPython : public Renderer {
public:
    RendererPython(std::ostream &os, Logger *logger, Encoding data_encoding);

    void outputNull() override;
    void outputBlob(const std::vector<char> &value) override;
    void outputString(const std::string &value) override;

    void beginQuery() override;
    void separateQueryElements() override;
    void endQuery() override;

    void beginRow() override;
    void beginRowElement() override;
    void endRowElement() override;
    void separateRowElements() override;
    void endRow() override;

    void beginList() override;
    void separateListElements() override;
    void endList() override;

    void beginSublist() override;
    void separateSublistElements() override;
    void endSublist() override;

    void beginDict() override;
    void separateDictElements() override;
    void separateDictKeyValue() override;
    void endDict() override;
};

#endif  // RendererPython_h
