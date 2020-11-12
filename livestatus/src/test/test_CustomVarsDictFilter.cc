<<<<<<< HEAD
#include <cstddef>
#include <iomanip>
#include <sstream>
#include <string>
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include <iomanip>
#include <sstream>
#include <string>

#include "Column.h"
>>>>>>> upstream/master
#include "CustomVarsDictColumn.h"
#include "CustomVarsDictFilter.h"
#include "Filter.h"
#include "MonitoringCore.h"
#include "NagiosCore.h"
#include "Row.h"
#include "data_encoding.h"
#include "gtest/gtest.h"
#include "nagios.h"
#include "opids.h"
#include "test_utilities.h"

namespace {
std::string b16encode(const std::string& str) {
    std::ostringstream os;
    os << std::hex << std::uppercase << std::setfill('0');
    for (auto ch : str) {
        os << std::setw(2)
           << static_cast<unsigned>(static_cast<unsigned char>(ch));
    }
    return os.str();
}

struct CustomVarsDictFilterTest : public ::testing::Test {
    bool accepts(AttributeKind kind, const std::string& value) {
        CustomVarsDictColumn cvdc{
<<<<<<< HEAD
            "name", "description", -1, -1, -1, offsetof(host, custom_variables),
            &core,  kind};
=======
            "name", "description", ColumnOffsets{}.add([](Row r) {
                return &r.rawData<host>()->custom_variables;
            }),
            &core, kind};
>>>>>>> upstream/master
        CustomVarsDictFilter filter{Filter::Kind::row, cvdc,
                                    RelationalOperator::equal, value};
        return filter.accepts(Row{&test_host}, {}, {});
    }

    NagiosCore core{NagiosPaths{}, NagiosLimits{}, NagiosAuthorization{},
                    Encoding::utf8};

    TestHost test_host{
        {{"ERNIE", "Bert"},
         {"GUT", "Mies"},
         {"_TAG_" + b16encode("Rock'n"), b16encode("Rock'n Roll")},
         {"_TAG_" + b16encode("Rollin"), b16encode("Rock'n Rollin'")},
         {"_TAG_" + b16encode("GUT"), b16encode("Guten Tag!")},
         {"_LABEL_" + b16encode("GÓÐ"), b16encode("Góðan dag!")},
         {"_LABEL_" + b16encode("GUT"), b16encode("foo")},
         {"_LABELSOURCE_" + b16encode("GUT"), b16encode("bar")}}};
};
}  // namespace

TEST_F(CustomVarsDictFilterTest, empty) {
    EXPECT_TRUE(accepts(AttributeKind::tags, ""));
    EXPECT_TRUE(accepts(AttributeKind::tags, " "));
    EXPECT_FALSE(accepts(AttributeKind::tags, "GUT"));
    EXPECT_FALSE(accepts(AttributeKind::tags, "GUT '' "));
}

<<<<<<< HEAD
TEST_F(CustomVarsDictFilterTest, unquoted_kinds) {
=======
TEST_F(CustomVarsDictFilterTest, UnquotedKinds) {
>>>>>>> upstream/master
    EXPECT_TRUE(accepts(AttributeKind::custom_variables, "GUT Mies"));
    EXPECT_TRUE(accepts(AttributeKind::tags, "GUT Guten Tag!"));
    EXPECT_TRUE(accepts(AttributeKind::labels, "GUT foo"));
    EXPECT_TRUE(accepts(AttributeKind::label_sources, "GUT bar"));
    EXPECT_FALSE(accepts(AttributeKind::label_sources, "GUT bart"));
}

<<<<<<< HEAD
TEST_F(CustomVarsDictFilterTest, unquoted_splitting) {
=======
TEST_F(CustomVarsDictFilterTest, UnquotedSplitting) {
>>>>>>> upstream/master
    EXPECT_TRUE(accepts(AttributeKind::tags, "     GUT Guten Tag!"));
    EXPECT_TRUE(accepts(AttributeKind::tags, "     GUT    Guten Tag!"));
    EXPECT_FALSE(accepts(AttributeKind::tags, "    GUT    Guten Tag!    "));
}

<<<<<<< HEAD
TEST_F(CustomVarsDictFilterTest, unquoted_utf8) {
=======
TEST_F(CustomVarsDictFilterTest, UnquotedUTF8) {
>>>>>>> upstream/master
    EXPECT_TRUE(accepts(AttributeKind::labels, "GÓÐ Góðan dag!"));
    EXPECT_TRUE(accepts(AttributeKind::labels, "     GÓÐ Góðan dag!"));
    EXPECT_TRUE(accepts(AttributeKind::labels, "     GÓÐ    Góðan dag!"));
    EXPECT_FALSE(accepts(AttributeKind::labels, "    GÓÐ    Góðan dag!   "));
}

<<<<<<< HEAD
TEST_F(CustomVarsDictFilterTest, quoted_splitting) {
=======
TEST_F(CustomVarsDictFilterTest, QuotedSplitting) {
>>>>>>> upstream/master
    EXPECT_TRUE(accepts(AttributeKind::tags, "'GUT' 'Guten Tag!'"));
    EXPECT_TRUE(accepts(AttributeKind::tags, "     'GUT' 'Guten Tag!'"));
    EXPECT_TRUE(accepts(AttributeKind::tags, "     'GUT'    'Guten Tag!'"));
    EXPECT_TRUE(accepts(AttributeKind::tags, "    'GUT'    'Guten Tag!'    "));
}

<<<<<<< HEAD
TEST_F(CustomVarsDictFilterTest, quoted_escape) {
=======
TEST_F(CustomVarsDictFilterTest, QuotedEscape) {
>>>>>>> upstream/master
    EXPECT_TRUE(accepts(AttributeKind::tags, "'Rock''n' 'Rock''n Roll'"));
    EXPECT_TRUE(accepts(AttributeKind::tags, "'Rock''n' 'Rock''n Roll"));
    EXPECT_TRUE(accepts(AttributeKind::tags, "'Rollin' 'Rock''n Rollin'''"));
    EXPECT_TRUE(accepts(AttributeKind::labels, "'GUT'foo"));
}
