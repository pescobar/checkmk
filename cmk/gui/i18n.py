<<<<<<< HEAD
#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2015             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

import gettext as gettext_module
from typing import (  # pylint: disable=unused-import
    Dict, NamedTuple, Optional, List, Tuple, Text,
)
from pathlib2 import Path  # pylint: disable=unused-import
import six
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import gettext as gettext_module
from typing import Dict, NamedTuple, Optional, List, Tuple
from pathlib import Path

from flask_babel.speaklater import LazyString  # type: ignore[import]
>>>>>>> upstream/master

import cmk.utils.paths

#.
#   .--Gettext i18n--------------------------------------------------------.
#   |           ____      _   _            _     _ _  ___                  |
#   |          / ___| ___| |_| |_ _____  _| |_  (_) |( _ ) _ __            |
#   |         | |  _ / _ \ __| __/ _ \ \/ / __| | | |/ _ \| '_ \           |
#   |         | |_| |  __/ |_| ||  __/>  <| |_  | | | (_) | | | |          |
#   |          \____|\___|\__|\__\___/_/\_\\__| |_|_|\___/|_| |_|          |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Handling of the regular localization of the GUI                      |
#   '----------------------------------------------------------------------'

# NullTranslations is the base class used by all translation classes in gettext
Translation = NamedTuple("Translation", [
    ("translation", gettext_module.NullTranslations),
    ("name", str),
])

# Current active translation object
<<<<<<< HEAD
_translation = None  # type: Optional[Translation]


def _(message):
    # type: (str) -> Text
    if not _translation:
        return six.text_type(message)
    return _translation.translation.ugettext(message)


def get_current_language():
    # type: () -> Optional[str]
=======
_translation: Optional[Translation] = None


def _(message: str) -> str:
    if _translation:
        return _translation.translation.gettext(message)
    return str(message)


def _l(string: str) -> str:
    """Like _() but the string returned is lazy which means it will be translated when it is used as
    an actual string."""
    return LazyString(_, string)


def ungettext(singular: str, plural: str, n: int) -> str:
    if _translation:
        return _translation.translation.ngettext(singular, plural, n)
    if n == 1:
        return str(singular)
    return str(plural)


def get_current_language() -> Optional[str]:
>>>>>>> upstream/master
    if _translation:
        return _translation.name
    return None


<<<<<<< HEAD
def _get_language_dirs():
    # type: () -> List[Path]
    return _get_base_language_dirs() + _get_package_language_dirs()


def _get_base_language_dirs():
    # type: () -> List[Path]
    return [cmk.utils.paths.locale_dir, cmk.utils.paths.local_locale_dir]


def _get_package_language_dirs():
    # type: () -> List[Path]
=======
def _get_language_dirs() -> List[Path]:
    return _get_base_language_dirs() + _get_package_language_dirs()


def _get_base_language_dirs() -> List[Path]:
    return [cmk.utils.paths.locale_dir, cmk.utils.paths.local_locale_dir]


def _get_package_language_dirs() -> List[Path]:
>>>>>>> upstream/master
    """Return a list of extension package specific localization directories

    It's possible for extension packages to provide custom localization files
    which are meant for localizing extension specific texts. These localizations
    are then used in addition to the builtin and local localization files.
    """
<<<<<<< HEAD
    package_locale_dir = cmk.utils.paths.local_locale_dir.joinpath("packages")
=======
    package_locale_dir = cmk.utils.paths.local_locale_dir / "packages"
>>>>>>> upstream/master
    if not package_locale_dir.exists():
        return []
    return list(package_locale_dir.iterdir())


<<<<<<< HEAD
def get_language_alias(lang):
    # type: (Optional[str]) -> Text
=======
def get_language_alias(lang: Optional[str]) -> str:
>>>>>>> upstream/master
    if lang is None:
        return _("English")

    alias = lang
    for lang_dir in _get_base_language_dirs():
        try:
<<<<<<< HEAD
            with lang_dir.joinpath(lang, "alias").open(encoding="utf-8") as f:
=======
            with (lang_dir / lang / "alias").open(encoding="utf-8") as f:
>>>>>>> upstream/master
                alias = f.read().strip()
        except (OSError, IOError):
            pass
    return alias


<<<<<<< HEAD
def get_languages():
    # type: () -> List[Tuple[str, Text]]
=======
def get_languages() -> List[Tuple[str, str]]:
>>>>>>> upstream/master
    # Add the hard coded english language to the language list
    # It must be choosable even if the administrator changed the default
    # language to a custom value
    languages = {('', _('English'))}

    for lang_dir in _get_language_dirs():
        try:
            languages.update([(val.name, _("%s") % get_language_alias(val.name))
                              for val in lang_dir.iterdir()
                              if val.name != "packages" and val.is_dir()])
        except OSError:
            # Catch "OSError: [Errno 2] No such file or
            # directory:" when directory not exists
            pass

    return sorted(list(languages), key=lambda x: x[1])


<<<<<<< HEAD
def unlocalize():
    # type: () -> None
=======
def unlocalize() -> None:
>>>>>>> upstream/master
    global _translation
    _translation = None


<<<<<<< HEAD
def localize(lang):
    # type: (str) -> None
=======
def localize(lang: Optional[str]) -> None:
>>>>>>> upstream/master
    global _translation
    if lang is None:
        unlocalize()
        return

    gettext_translation = _init_language(lang)
    if not gettext_translation:
        unlocalize()
        return

    _translation = Translation(translation=gettext_translation, name=lang)


<<<<<<< HEAD
def _init_language(lang):
    # type: (str) -> Optional[gettext_module.NullTranslations]
=======
def _init_language(lang: str) -> Optional[gettext_module.NullTranslations]:
>>>>>>> upstream/master
    """Load all available "multisite" translation files. All are loaded first.
    The builtin ones are used as "fallback" for the local files which means that
    the texts in the local files have precedence.
    """
<<<<<<< HEAD
    translations = []  # type: List[gettext_module.NullTranslations]
=======
    translations: List[gettext_module.NullTranslations] = []
>>>>>>> upstream/master
    for locale_base_dir in _get_language_dirs():
        try:
            translation = gettext_module.translation("multisite",
                                                     str(locale_base_dir),
                                                     languages=[lang],
                                                     codeset='UTF-8')

        except IOError:
            continue

        # Create a chain of fallback translations
        if translations:
            translation.add_fallback(translations[-1])
        translations.append(translation)

    if not translations:
        return None

    return translations[-1]


<<<<<<< HEAD
def initialize():
    # type: () -> None
=======
def initialize() -> None:
>>>>>>> upstream/master
    unlocalize()


#.
#   .--User i18n-----------------------------------------------------------.
#   |                _   _                 _ _  ___                        |
#   |               | | | |___  ___ _ __  (_) |( _ ) _ __                  |
#   |               | | | / __|/ _ \ '__| | | |/ _ \| '_ \                 |
#   |               | |_| \__ \  __/ |    | | | (_) | | | |                |
#   |                \___/|___/\___|_|    |_|_|\___/|_| |_|                |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Users can localize custom strings using the global configuration     |
#   '----------------------------------------------------------------------'

<<<<<<< HEAD
_user_localizations = {}  # type: Dict[Text, Dict[Optional[str], Text]]


# Localization of user supplied texts
def _u(text):
    # type: (Text) -> Text
    ldict = _user_localizations.get(text)
    if ldict:
        return ldict.get(get_current_language(), text)
    return text


def set_user_localizations(localizations):
    # type: (Dict[Text, Dict[Optional[str], Text]]) -> None
=======
_user_localizations: Dict[str, Dict[str, str]] = {}


# Localization of user supplied texts
def _u(text: str) -> str:
    ldict = _user_localizations.get(text)
    if ldict:
        current_language = get_current_language()
        if current_language is None:
            return text
        return ldict.get(current_language, text)
    return text


def set_user_localizations(localizations: Dict[str, Dict[str, str]]) -> None:
>>>>>>> upstream/master
    _user_localizations.clear()
    _user_localizations.update(localizations)


initialize()
