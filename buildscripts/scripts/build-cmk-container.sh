#!/bin/bash
<<<<<<< HEAD
set -e
=======
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

set -ex
>>>>>>> upstream/master
unset LANG

log() { echo "[$(date '+%F %T')] ==============================" "$@"; }
die() { log "$@"; exit 1; }

<<<<<<< HEAD
if [ "$1" = "-h" ] || [ "$1" = "--help" ] || [ "$1" = "" ] || [ "$2" = "" ] || [ "$3" = "" ] || [ "$4" = "" ]; then
    echo "Aufrufen: bw-docker-bauen [BRANCH] [EDITION] [VERSION] [SET_LATEST_TAG]"
    echo "          bw-docker-bauen 1.5.0 enterprise 1.5.0p4 no"
=======
if [ "$1" = "-h" ] || [ "$1" = "--help" ] || [ "$1" = "" ] || [ "$2" = "" ] || [ "$3" = "" ] || [ "$4" = "" ] || [ "$5" = "" ]; then
    echo "Aufrufen: bw-docker-bauen [BRANCH] [EDITION] [VERSION] [SET_LATEST_TAG] [DEMO]"
    echo "          bw-docker-bauen 1.5.0 enterprise 1.5.0p4 no no"
>>>>>>> upstream/master
    echo
    exit 1
fi

BRANCH=$1
EDITION=$2
VERSION=$3
SET_LATEST_TAG=$4
<<<<<<< HEAD
=======
DEMO=''
if [ $5 == yes ]; then
    DEMO='.demo'
fi
>>>>>>> upstream/master

if [ $EDITION = raw ]; then
    SUFFIX=.cre
elif [ $EDITION = enterprise ]; then
    SUFFIX=.cee
elif [ $EDITION = managed ]; then
    SUFFIX=.cme
else
    die "FEHLER: Unbekannte Edition '$EDITION'"
fi

mkdir -p /bauwelt/tmp
TMP_PATH=$(mktemp --directory -p /bauwelt/tmp --suffix=.cmk-docker)
<<<<<<< HEAD
DOCKER_PATH="$TMP_PATH/check-mk-${EDITION}-${VERSION}${SUFFIX}/docker"
DOCKER_IMAGE_ARCHIVE="check-mk-${EDITION}-docker-${VERSION}.tar.gz"
PKG_NAME="check-mk-${EDITION}-${VERSION}"
=======
DOCKER_PATH="$TMP_PATH/check-mk-${EDITION}-${VERSION}${SUFFIX}${DEMO}/docker"
DOCKER_IMAGE_ARCHIVE="check-mk-${EDITION}-docker-${VERSION}${DEMO}.tar.gz"
PKG_NAME="check-mk-${EDITION}-${VERSION}${DEMO}"
>>>>>>> upstream/master
PKG_FILE="${PKG_NAME}_0.stretch_$(dpkg --print-architecture).deb"

trap "rm -rf \"$TMP_PATH\"" SIGTERM SIGHUP SIGINT

log "Unpack source tar to $TMP_PATH"
<<<<<<< HEAD
tar -xz -C "$TMP_PATH" -f "/bauwelt/download/${VERSION}/check-mk-${EDITION}-${VERSION}${SUFFIX}.tar.gz"
=======
tar -xz -C "$TMP_PATH" -f "/bauwelt/download/${VERSION}/check-mk-${EDITION}-${VERSION}${SUFFIX}${DEMO}.tar.gz"
>>>>>>> upstream/master

log "Copy debian package..."
cp "/bauwelt/download/${VERSION}/${PKG_FILE}" "$DOCKER_PATH/"

log "Building container image"
make -C "$DOCKER_PATH" "$DOCKER_IMAGE_ARCHIVE"

log "Verschiebe Image-Tarball..."
mv -v "$DOCKER_PATH/$DOCKER_IMAGE_ARCHIVE" "/bauwelt/download/${VERSION}/"

if [ $EDITION = raw ]; then
    log "Erstelle \"{$BRANCH}-latest\" tag..."
<<<<<<< HEAD
    docker tag "checkmk/check-mk-${EDITION}:${VERSION}" "checkmk/check-mk-${EDITION}:${BRANCH}-latest"

    log "Erstelle \"latest\" tag..."
    docker tag "checkmk/check-mk-${EDITION}:${VERSION}" "checkmk/check-mk-${EDITION}:latest"

    log "Lade zu Docker-Hub hoch..."
    docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSPHRASE}
    DOCKERCLOUD_NAMESPACE=checkmk docker push "checkmk/check-mk-${EDITION}:${VERSION}"
    DOCKERCLOUD_NAMESPACE=checkmk docker push "checkmk/check-mk-${EDITION}:${BRANCH}-latest"
    if [ "$SET_LATEST_TAG" = "yes" ]; then
        DOCKERCLOUD_NAMESPACE=checkmk docker push "checkmk/check-mk-${EDITION}:latest"
=======
    docker tag "checkmk/check-mk-${EDITION}${DEMO}:${VERSION}" "checkmk/check-mk-${EDITION}${DEMO}:${BRANCH}-latest"

    log "Erstelle \"latest\" tag..."
    docker tag "checkmk/check-mk-${EDITION}${DEMO}:${VERSION}" "checkmk/check-mk-${EDITION}${DEMO}:latest"

    log "Lade zu Docker-Hub hoch..."
    docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSPHRASE}
    DOCKERCLOUD_NAMESPACE=checkmk docker push "checkmk/check-mk-${EDITION}${DEMO}:${VERSION}"
    DOCKERCLOUD_NAMESPACE=checkmk docker push "checkmk/check-mk-${EDITION}${DEMO}:${BRANCH}-latest"
    if [ "$SET_LATEST_TAG" = "yes" ]; then
        DOCKERCLOUD_NAMESPACE=checkmk docker push "checkmk/check-mk-${EDITION}${DEMO}:latest"
>>>>>>> upstream/master
    fi
fi

log "Räume temporäres Verzeichnis $TMP_PATH weg"
rm -rf "$TMP_PATH"
