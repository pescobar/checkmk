<<<<<<< HEAD
SHELL = /bin/bash -e -o pipefail

BUILD_HELPER_DIR := build-helper
PACKAGE_DIR := $(shell pwd)/packages

include Makefile.omd
include $(BUILD_HELPER_DIR)/build-helper-files.make
include packages/packages.make
=======
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

include Makefile.omd
include $(BUILD_BASE_DIR)/build-helper-files.make
>>>>>>> upstream/master

# You can build singele packages by calling macke <PACKAGENAME>
# e.g.: make nagios rrdtool
#
# You can select a subset of the packages by overriding this
# variale, e.g. make PACKAGES='nagios rrdtool' pack
#
# If you just want to test package building, you can reduce the
# number of packages to just "omd" - to speed up your tests.
# PACKAGES="omd"
#
# You can also create a file named .config and override the
# PACKAGES variable there to customzie the list of packages.

PACKAGES := \
<<<<<<< HEAD
    libgsf \
    perl-modules \
    Python \
    Python3 \
    freetds \
    re2 \
    python-modules \
    python3-modules \
    boost \
=======
    openssl \
    libgsf \
    postgresql \
    perl-modules \
    Python3 \
    freetds \
    re2 \
    python3-modules \
>>>>>>> upstream/master
    rrdtool \
    msitools \
    net-snmp \
    apache-omd \
    mod_fcgid \
<<<<<<< HEAD
    mod_wsgi \
    check_mk \
    check_multi \
    check_mysql_health \
    check_oracle_health \
    Webinject \
    dokuwiki \
=======
    python3-mod_wsgi \
    check_mk \
    check_mysql_health \
    check_oracle_health \
    Webinject \
>>>>>>> upstream/master
    jmx4perl \
    mk-livestatus \
    stunnel \
    nagios \
    monitoring-plugins \
    nagvis \
    nrpe \
    nsca \
    omd \
    openhardwaremonitor \
    navicli \
    pnp4nagios \
    maintenance \
    patch \
    heirloom-mailx \
    snap7 \
    heirloom-pkgtools

ifeq ($(EDITION),enterprise)
PACKAGES += enterprise
endif
ifeq ($(EDITION),managed)
PACKAGES += enterprise
PACKAGES += managed
endif

<<<<<<< HEAD
default: build
=======
BUILD_TARGET_VARS := $(call package_target_prefix,$(PACKAGES))
INSTALL_TARGETS := $(foreach package,$(addsuffix _INSTALL,$(BUILD_TARGET_VARS)),$($(package)))

PRE_INSTALL := $(BUILD_HELPER_DIR)/pre-install
INSTALL := $(BUILD_HELPER_DIR)/install
INSTALL_GLOBAL := $(BUILD_HELPER_DIR)/install-global

include packages/packages.make
>>>>>>> upstream/master

# Workaround: Makefiles evaluate Variables the first time they are read. If a variable is not set the
# moment it is read, it is replaced with an empty string. Therefor our dependencies get lost, if the
# inlcuded Makefiles are not ordered correctly. For that reason, we parse the Makefiles for certain
# variable definitions and write them to an extra Makefile, which we include before the package Makefile.
<<<<<<< HEAD
$(BUILD_HELPER_DIR)/build-helper-files.make:
	mkdir -p $(BUILD_HELPER_DIR)
=======
$(BUILD_BASE_DIR)/build-helper-files.make:
	$(MKDIR) $(BUILD_BASE_DIR)
>>>>>>> upstream/master
	$(RM) $@
	for P in $(PACKAGES); do \
	  inc_path=$(PACKAGE_DIR)/$$P/$$P.make; \
	  if [[ $$P == 'enterprise' || $$P == 'managed' ]] ; then \
	    inc_path=$(REPO_PATH)/$$P/$$P.make; \
	  fi ; \
	  P_VAR=$$(echo $${P^^} | tr '-' '_' ); \
<<<<<<< HEAD
	  egrep -h "$$P_VAR\s:=\s" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_VERS\s:=\s" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_DIR\s:=\s" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_BUILD\s:=\s" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_INSTALL\s:=\s" $$inc_path >> $@ ; \
	done

-include .config

DESTDIR ?=$(shell pwd)/destdir
RPM_TOPDIR=$$(pwd)/rpm.topdir
BIN_TGZ=check-mk-$(EDITION)-bin-$(OMD_VERSION).tar.gz
NEW_SERIAL=$$(($(OMD_SERIAL) + 1))
SKEL := $(DESTDIR)$(OMD_ROOT)/skel
# NEW_VERSION should be set on the command line.
# Replace all '/' since sed tries to interpret them
# '/' might occur in custom branches
# filenames and sed arguments should not contain '/'
NEW_VERSION_STRING := $(subst /,-,$(NEW_VERSION))
=======
	  egrep -h "$$P_VAR\s+:=\s+" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_VERS\s+:=\s+" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_DIR\s+:=\s+" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_BUILD\s+:=\s+" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_INSTALL\s+:=\s+" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_INTERMEDIATE_INSTALL\s+:=\s+" $$inc_path >> $@ ; \
	  egrep -h "$${P_VAR}_CACHE_PKG_PROCESS\s+:=\s+" $$inc_path >> $@ ; \
	  if [ "$$P" == "rrdtool" ]; then \
	    egrep -h "$${P_VAR}_BUILD_LIBRARY\s+:=\s+" $$inc_path >> $@ ; \
	    egrep -h "$${P_VAR}_INSTALL_LIBRARY\s+:=\s+" $$inc_path >> $@ ; \
	    egrep -h "$${P_VAR}_BUILD_BINDINGS\s+:=\s+" $$inc_path >> $@ ; \
	    egrep -h "$${P_VAR}_INSTALL_BINDINGS\s+:=\s+" $$inc_path >> $@ ; \
	  fi \
	done


-include .config

# debian/rules and RPM specfile (omd.spec) set DESTDIR to install files to
# the package build directories
DESTDIR ?= $(BUILD_BASE_DIR)/dest

RPM_TOPDIR := $(BUILD_BASE_DIR)/rpm/topdir
RPM_BUILDROOT := $(BUILD_BASE_DIR)/rpm/buildroot

SKEL := $(DESTDIR)$(OMD_ROOT)/skel
SKEL_PERMISSIONS := $(DESTDIR)$(OMD_ROOT)/share/omd/skel.permissions
>>>>>>> upstream/master
CMA_PKG_VERSION_TXT := $(shell if [ "$(DISTRO_CODE)" = "stretch" ]; then echo "-2" ; fi )
ARCH := $(shell uname -m)
CMA_PACKAGE:= $(REPO_PATH)/check-mk-$(EDITION)-$(PKG_VERSION)$(CMA_PKG_VERSION_TXT)-$(ARCH).cma

<<<<<<< HEAD
PRE_INSTALL := $(BUILD_HELPER_DIR)/pre-install
PRE_SKEL := $(BUILD_HELPER_DIR)/pre-skel
INSTALL := $(BUILD_HELPER_DIR)/install
INSTALL_GLOBAL := $(BUILD_HELPER_DIR)/install-global

BUILD_TARGET_VARS := $(shell echo $(PACKAGES)  | tr 'a-z' 'A-Z' | tr '-' '_' )
BUILD_TARGETS := $(foreach package,$(addsuffix _BUILD,$(BUILD_TARGET_VARS)),$($(package)))
INSTALL_TARGETS := $(foreach package,$(addsuffix _INSTALL,$(BUILD_TARGET_VARS)),$($(package)))
SKEL_TARGETS :=  $(foreach package,$(addsuffix _SKEL,$(BUILD_TARGET_VARS)),$($(package)))

.PHONY: install-global build install pack skel

build: $(BUILD_TARGETS)

install: $(INSTALL)

install-global: $(INSTALL_GLOBAL)

pack: $(BIN_TGZ)

skel: $(DESTDIR)$(OMD_ROOT)/share/omd/skel.permissions $(FIX_SKEL)

cma: $(CMA_PACKAGE)

#Prepare clean install environment
$(PRE_INSTALL):
	rm -rf $(DESTDIR)
	rm -rf $(BUILD_HELPER_DIR)/*-install
	$(MKDIR) $(DESTDIR)$(OMD_PHYSICAL_BASE)
	A="$(OMD_PHYSICAL_BASE)" ; ln -s $${A:1} $(DESTDIR)/omd
=======
.PHONY: install cma rpm deb clean setversion install-clean

# Called while building the .rpm/.deb packages
install: $(INSTALL_GLOBAL)

# Called by our release system to build appliance packages
cma: $(CMA_PACKAGE)

install-clean:
	rm -rf $(DESTDIR)
	rm -rf $(BUILD_HELPER_DIR)/*-install

# Prepare clean install environment
$(PRE_INSTALL):
	$(MKDIR) $(BUILD_HELPER_DIR)
	$(MKDIR) $(DESTDIR)$(OMD_PHYSICAL_BASE)
# The default physical base for OMD is /opt/omd. This may be changed by
# the user locally, but the logical path for OMD is always /omd. We use
# /omd during installation to make all programs that persist the path
# somehow use the logical path.
	A="$(OMD_PHYSICAL_BASE)" ; ln -sfn $${A:1} $(DESTDIR)/omd
>>>>>>> upstream/master
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/bin
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/lib/omd/hooks
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/omd
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/diskspace
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/man/man1
<<<<<<< HEAD
	touch $@


$(INSTALL_TARGETS): $(PRE_INSTALL)
$(APPLIANCE_INSTALL_CMA): $(PRE_INSTALL)

$(SKEL_TARGETS): $(PRE_SKEL)

$(INSTALL): $(INSTALL_TARGETS)
	# Repair packages that install with silly modes (such as Nagios)
	chmod -R o+Xr $(DESTDIR)$(OMD_ROOT)
	$(TOUCH) $@

$(PRE_SKEL) : $(INSTALL_GLOBAL)
	# Install skeleton files (subdirs skel/ in packages' directories)
	mkdir -p $(DESTDIR)$(OMD_ROOT)/skel
	@set -e ; cd packages ; for p in $(PACKAGES) ; do \
            if [ -d "$$p/skel" ] ; then  \
              tar cf - -C $$p/skel --exclude="*~" --exclude=".gitignore" . | tar xvf - -C $(DESTDIR)$(OMD_ROOT)/skel ; \
            fi ;\
        done
	$(TOUCH) $@

$(DESTDIR)$(OMD_ROOT)/share/omd/skel.permissions: $(SKEL_TARGETS)
	# Create permissions file for skel
=======
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/skel
	touch $@

$(INSTALL_TARGETS): $(PRE_INSTALL)

$(INSTALL): $(INSTALL_TARGETS)
# Repair packages that install with silly modes (such as Nagios)
	chmod -R o+Xr $(DESTDIR)$(OMD_ROOT)
	$(TOUCH) $@

$(SKEL_PERMISSIONS): $(INSTALL)
# Create permissions file for skel
>>>>>>> upstream/master
	mkdir -p $(DESTDIR)$(OMD_ROOT)/share/omd
	set -e ; cd packages ; for p in $(PACKAGES) ; do \
	    if [ -d $$p ] && [ -e $$p/skel.permissions ] ; then \
	        echo "# $$p" ; \
	        cat $$p/skel.permissions ; \
	    fi ; \
<<<<<<< HEAD
	done > $(DESTDIR)$(OMD_ROOT)/share/omd/skel.permissions

$(FIX_SKEL): $(SKEL_TARGETS)
	# Make sure, all permissions in skel are set to 0755, 0644
	@failed=$$(find $(DESTDIR)$(OMD_ROOT)/skel -type d -not -perm 0755) ; \
	if [ -n "$$failed" ] ; then \
	    echo "Fixing invalid permissions for skeleton dirs. Must be 0755:" ; \
            chmod -c 755 $$failed ; \
            echo "$$failed" ; \
        fi
	@failed=$$(find $(DESTDIR)$(OMD_ROOT)/skel -type f -not -perm 0644) ; \
	if [ -n "$$failed" ] ; then \
	    echo "Fixing invalid permissions for skeleton files. Must be 0644:" ; \
            echo "$$failed" ; \
            chmod -c 644 $$failed ; \
        fi

	# Fix packages which did not add ###ROOT###
	find $(DESTDIR)$(OMD_ROOT)/skel -type f | xargs -n1 sed -i -e 's+$(OMD_ROOT)+###ROOT###+g'

	# Remove site-specific directories that went under /omd/version
	rm -rf $(DESTDIR)/{var,tmp}
	$(TOUCH) $@

# Create installations files that do not lie beyond /omd/versions/$(OMD_VERSION)
# and files not owned by a specific package.
$(INSTALL_GLOBAL): $(INSTALL)
=======
	done > $(SKEL_PERMISSIONS)

# Create installations files that do not lie beyond /omd/versions/$(OMD_VERSION)
# and files not owned by a specific package.
$(INSTALL_GLOBAL): $(SKEL_PERMISSIONS)
>>>>>>> upstream/master
	# Create link to default version
	ln -sf $(OMD_VERSION) $(DESTDIR)$(OMD_BASE)/versions/default

	# Create global symbolic links. Those links are share between
	# all installed versions and refer to the default version.
	mkdir -p $(DESTDIR)/usr/bin
	ln -sfn /omd/versions/default/bin/omd $(DESTDIR)/usr/bin/omd
	mkdir -p $(DESTDIR)/usr/share/man/man8
	ln -sfn /omd/versions/default/share/man/man8/omd.8.gz $(DESTDIR)/usr/share/man/man8/omd.8.gz
	mkdir -p $(DESTDIR)/etc/init.d
	ln -sfn /omd/versions/default/share/omd/omd.init $(DESTDIR)/etc/init.d/omd
	mkdir -p $(DESTDIR)$(APACHE_CONF_DIR)
	ln -sfn /omd/versions/default/share/omd/apache.conf $(DESTDIR)$(APACHE_CONF_DIR)/zzz_omd.conf

	# Base directories below /omd
	mkdir -p $(DESTDIR)$(OMD_BASE)/sites
	mkdir -p $(DESTDIR)$(OMD_BASE)/apache

	# Information about distribution and OMD
	mkdir -p $(DESTDIR)$(OMD_ROOT)/share/omd
	install -m 644 distros/$(DISTRO_NAME)_$(DISTRO_VERSION).mk $(DESTDIR)$(OMD_ROOT)/share/omd/distro.info
	echo -e "OMD_VERSION = $(OMD_VERSION)\nOMD_PHYSICAL_BASE = $(OMD_PHYSICAL_BASE)" > $(DESTDIR)$(OMD_ROOT)/share/omd/omd.info

	# Install ChangeLog created from all werks
	mkdir -p $(DESTDIR)$(OMD_ROOT)/share/doc
	ln -sfn check_mk/ChangeLog $(DESTDIR)$(OMD_ROOT)/share/doc/ChangeLog
	install -m 644 Licenses.csv $(DESTDIR)$(OMD_ROOT)/share/doc/Licenses.csv
	install -m 644 Licenses.README.txt $(DESTDIR)$(OMD_ROOT)/share/doc/Licenses.README.txt
	install -m 644 License_texts.pdf $(DESTDIR)$(OMD_ROOT)/share/doc/License_texts.pdf

	if [ -f COMMIT ]; then \
	    install -m 644 COMMIT $(DESTDIR)$(OMD_ROOT)/share/doc ; \
	fi
<<<<<<< HEAD
	$(TOUCH) $@

$(BIN_TGZ): $(DESTDIR)$(OMD_ROOT)/share/omd/skel.permissions $(FIX_SKEL)
	# Pack the whole stuff into a tarball
	tar czf $@ --owner=root --group=root -C $(DESTDIR) .

rpm:
=======

# Perform some validations
	for SKEL_DIR in tmp var etc; do \
	    if [ -d "$(DESTDIR)$(OMD_ROOT)/$$SKEL_DIR" ]; then \
	        echo "ERROR: The directory $$SKEL_DIR is only allowed to exist in skel/" ; \
	        find "$(DESTDIR)$(OMD_ROOT)/$$SKEL_DIR" ; \
	        exit 1 ; \
	    fi ; \
	done
	$(TOUCH) $@

omd.spec: omd.spec.in
>>>>>>> upstream/master
	sed -e 's/^Requires:.*/Requires:        $(OS_PACKAGES)/' \
	    -e 's/%{version}/$(OMD_VERSION)/g' \
	    -e "s/%{pkg_version}/$(PKG_VERSION)/g" \
	    -e 's/%{edition}/$(EDITION)/g' \
	    -e 's/^Version:.*/Version: $(DISTRO_CODE)/' \
	    -e 's/^Release:.*/Release: $(OMD_SERIAL)/' \
	    -e 's#@APACHE_CONFDIR@#$(APACHE_CONF_DIR)#g' \
	    -e 's#@APACHE_NAME@#$(APACHE_INIT_NAME)#g' \
	    omd.spec.in > omd.spec
	if [ "$(EDITION)" =  "raw" ]; then \
	    sed -i '/icmpsender/d;/icmpreceiver/d' omd.spec ; \
	fi
<<<<<<< HEAD
	mkdir -p $(RPM_TOPDIR)/{SOURCES,BUILD,RPMS,SRPMS,SPECS}
	cp ../check-mk-$(EDITION)-$(OMD_VERSION).tar.gz $(RPM_TOPDIR)/SOURCES
=======

# Called by our release system to build RPM packages
# To make incremental builds possible, e.g. for testing, remove the install-clean target
rpm: install-clean omd.spec
	$(MKDIR) $(RPM_TOPDIR)/{SOURCES,BUILD,RPMS,SRPMS,SPECS}
>>>>>>> upstream/master
	# NO_BRP_STALE_LINK_ERROR ignores errors when symlinking from skel to
	# share,lib,bin because the link has a invalid target until the site is created
	# NO_BRP_CHECK_RPATH ignores errors with the compiled python2.7 binary which
	# has a rpath hard coded to the OMD shipped libpython2.7.
	NO_BRP_CHECK_RPATH="yes" \
	NO_BRP_STALE_LINK_ERROR="yes" \
<<<<<<< HEAD
	rpmbuild -bb --define "_topdir $(RPM_TOPDIR)" \
	     --buildroot=$$(pwd)/rpm.buildroot omd.spec
	mv -v $(RPM_TOPDIR)/RPMS/*/*.rpm $(REPO_PATH)
	rm -rf $(RPM_TOPDIR) rpm.buildroot

# create a debian/changelog to build the package
debian/changelog:
	# Build DEB from prebuild binary. This currently needs 'make dist' and thus only
	# works within a GIT repository.
	@if test -z "$(DEBFULLNAME)" || test -z "$(DEBEMAIL)"; then \
	  echo "please read 'man dch' and set DEBFULLNAME and DEBEMAIL" ;\
	  exit 1; \
	fi
	# this is a hack!
	rm -f debian/changelog
	dch --create --package check-mk-$(EDITION)-$(PKG_VERSION) \
	    --newversion 0.$(DISTRO_CODE) "`cat debian/changelog.tmpl`"
	dch --release "releasing ...."

deb: debian/changelog
	sed -e 's/###OMD_VERSION###/$(OMD_VERSION)/' \
	    -e "s/###PKG_VERSION###/$(PKG_VERSION)/" \
	    -e 's/###EDITION###/$(EDITION)/' \
	    -e 's/###OS_PACKAGES###/$(OS_PACKAGES)/' \
	    -e '/Depends:/s/\> /, /g' \
	    -e '/Depends:/s/@/ /g' \
	   `pwd`/debian/control.in > `pwd`/debian/control
	fakeroot bash -c "export EDITION=$(EDITION) ; debian/rules clean"
	debuild --set-envvar EDITION=$(EDITION) \
		--prepend-path=/usr/local/bin --no-lintian -i\.git -I\.git \
			-icheck-mk-$(EDITION)-bin-$(OMD_VERSION).tar.gz \
			-Icheck-mk-$(EDITION)-bin-$(OMD_VERSION).tar.gz \
			-i.gitignore -I.gitignore \
			-uc -us -rfakeroot
	# -- renaming deb package to DISTRO_CODE dependend name
	# arch=`dpkg-architecture -qDEB_HOST_ARCH` ; \
	# build=`sed -e '1s/.*(\(.*\)).*/\1/;q' debian/changelog` ; \
	# distro=`echo $$build | sed -e 's/build/$(DISTRO_CODE)/' ` ; \
	# echo "$$arch $$build $$distro"; \
	# mv "../omd-$(OMD_VERSION)_$${build}_$${arch}.deb" \
	#  "../omd-$(OMD_VERSION)_$${distro}_$${arch}.deb" ;

# On debian based systems register the alternative switches
alt:
	@if which update-alternatives >/dev/null 2>&1; then \
	    update-alternatives --install /omd/versions/default \
		omd /omd/versions/$(OMD_VERSION) $(OMD_SERIAL) \
		--slave /usr/bin/omd omd.bin /omd/versions/$(OMD_VERSION)/bin/omd \
		--slave /usr/share/man/man8/omd.8.gz omd.man8 \
               /omd/versions/$(OMD_VERSION)/share/man/man8/omd.8.gz ; \
	fi ;

setversion:
	NEW_OMD_VERSION=$(NEW_VERSION_STRING).$(EDITION_SHORT)$(DEMO_SUFFIX) ; \
	if [ -n "$$NEW_OMD_VERSION" ] && [ "$$NEW_OMD_VERSION" != "$(OMD_VERSION)" ]; then \
	    sed -ri 's/^(OMD_SERIAL[[:space:]]*= *).*/\1'"$(NEW_SERIAL)/" Makefile.omd ; \
	fi ; \
	sed -ri 's/^(OMD_VERSION[[:space:]]*= *).*/\1"'"$$NEW_OMD_VERSION"'"/' packages/omd/omdlib/__init__.py

test:
	t/test_all.sh

$(CMA_INSTALL): $(INSTALL_TARGETS)

$(CMA_PACKAGE): $(CMA_INSTALL) $(APPLIANCE_INSTALL_CMA) $(APPLIANCE_SKEL_CMA) $(DESTDIR)$(OMD_ROOT)/share/omd/skel.permissions $(FIX_SKEL)
=======
	REPO_PATH=$(REPO_PATH) \
	rpmbuild -bb --define "_topdir $(RPM_TOPDIR)" \
	     --buildroot=$(RPM_BUILDROOT) omd.spec
	mv -v $(RPM_TOPDIR)/RPMS/*/*.rpm $(REPO_PATH)
	rm -rf $(RPM_TOPDIR) $(RPM_BUILDROOT)

debian/changelog:
	sed -e 's/###DISTRO_CODE###/$(DISTRO_CODE)/g' \
	    -e "s/###PKG_VERSION###/$(PKG_VERSION)/g" \
	    -e "s/###NOW###/$(shell date -R)/g" \
	    -e 's/###EDITION###/$(EDITION)/g' \
	    debian/changelog.in > debian/changelog

debian/control: debian/control.in
	sed -e 's/###OMD_VERSION###/$(OMD_VERSION)/g' \
	    -e "s/###PKG_VERSION###/$(PKG_VERSION)/g" \
	    -e 's/###EDITION###/$(EDITION)/g' \
	    -e 's/###OS_PACKAGES###/$(OS_PACKAGES)/g' \
	    -e '/Depends:/s/\> /, /g' \
	    -e '/Depends:/s/@/ /g' \
	   debian/control.in > debian/control

# Called by our release system to build DEB packages
#
# Check out "man debuild" and "man dpkg-buildpackage" to get a description of
# the build mechanism.
# Please keep in bind that we are building for multiple Ubuntu/Debian version
# and need to be compatible to all of the tool chains shipped with them.
#
# In case we want to have fast package creation without need to rebuild
# everything, we'd have to
# a) add -nc fo jessie/trusty/xenial
# b) drop the "clean" argument for newer distros
# c) remove the dh_prep from debian/rules
deb: debian/changelog debian/control
	if [ "$(DISTRO_CODE)" = "jessie" ] || [ "$(DISTRO_CODE)" = "trusty" ] || [ "$(DISTRO_CODE)" = "xenial" ]; then \
	    TARGET="-us -uc -B" ; \
	else \
	    TARGET="--no-sign -- clean build-arch binary-arch" ; \
	fi && \
	    debuild \
	    --preserve-envvar="NEXUS_*" \
	    --preserve-envvar="PYTHON_ENABLE_OPTIMIZATIONS" \
	    --prepend-path=/usr/local/bin \
	    --set-envvar EDITION=$(EDITION) \
	    --no-lintian \
	    -i\.git -I\.git \
	    -i.gitignore -I.gitignore \
	    -rfakeroot \
	    $$TARGET

setversion:
# NEW_VERSION should be set on the command line.  Replace all '/' since sed
# tries to interpret them '/' might occur in custom branches filenames and sed
# arguments should not contain '/'
	NEW_OMD_VERSION=$(subst /,-,$(NEW_VERSION)).$(EDITION_SHORT)$(DEMO_SUFFIX) ; \

# Please note: APPLIANCE_*_CMA are defined in omd/packages/appliance/appliance.make
$(APPLIANCE_INSTALL_CMA): $(PRE_INSTALL)

# Please note: APPLIANCE_*_CMA are defined in omd/packages/appliance/appliance.make
$(CMA_PACKAGE): $(APPLIANCE_INSTALL_CMA) install
>>>>>>> upstream/master
	# Create info file to mark minimal cma firmware version requirement
	@if [ "$(DISTRO_CODE)" = "stretch" ]; then \
	    MIN_VERSION=1.4.0 ; \
	else \
	    MIN_VERSION=1.1.2 ; \
	fi ; \
	echo -e "MIN_VERSION=$${MIN_VERSION}\n" > $(DESTDIR)/opt/omd/versions/$(OMD_VERSION)/cma.info

	# Mark demo builds in cma.info file
	@if [ -n "$(DEMO_SUFFIX)" ]; then \
	    echo -e "DEMO=1\n" >> $(DESTDIR)/opt/omd/versions/$(OMD_VERSION)/cma.info ; \
	fi

	tar czf $@ \
	    --owner=root \
	    --group=root \
	    -C $(DESTDIR)/opt/omd/versions/ \
	    $(OMD_VERSION)

<<<<<<< HEAD
clean: $(addsuffix -clean,$(PACKAGES))
	rm -rf $(DESTDIR)
	@for p in packages/* ; do \
	    if [ -d $$p ] && [ -f $$p/Makefile ]; then \
		$(MAKE) -C $$p clean ; \
	    fi ; \
	done
	$(RM) -r $(BUILD_HELPER_DIR)

# Only for development: install tarball below /
xzf:
	tar xzf $(BIN_TGZ) -C / # HACK: Add missing suid bits if compiled as non-root
	chmod 750 $(OMD_ROOT)/lib/nagios/plugins/check_dhcp
	setcap 'cap_net_raw,cap_net_bind_service=+ep' $(OMD_ROOT)/lib/nagios/plugins/check_dhcp
	chmod 750 $(OMD_ROOT)/lib/nagios/plugins/check_icmp
	setcap "cap_net_raw+ep" $(OMD_ROOT)/lib/nagios/plugins/check_icmp
	chmod 750 $(OMD_ROOT)/bin/mkeventd_open514
	setcap "cap_net_bind_service+ep" $(OMD_ROOT)/bin/mkeventd_open514
	$(APACHE_CTL) -k graceful
=======
clean: install-clean
	$(RM) -r $(BUILD_HELPER_DIR)
	$(RM) -r $(BUILD_BASE_DIR)
	$(RM) -r $(PACKAGE_BUILD_DIR)
>>>>>>> upstream/master

setup:
	@echo "Please run the build in a docker container."
	@echo "Dockerfiles for all Distros can be found under 'buildscripts/infrastructure/build-nodes/'."
