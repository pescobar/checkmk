# Paths to necessary Tools
ECHO := $(shell which echo)
FIND := $(shell which find)
GCC_SYSTEM := $(shell which gcc)
LN := $(shell which ln)
LS := $(shell which ls)
MKDIR := $(shell which mkdir) -p
MV := $(shell which mv)
PATCH := $(shell which patch)
PERL := $(shell which perl)
RSYNC := $(shell which rsync) -a
SED := $(shell which sed)
TAR_BZ2 := $(shell which tar) xjf
TAR_XZ := $(shell which tar) xJf
TAR_GZ := $(shell which tar) xzf
TEST := $(shell which test)
TOUCH := $(shell which touch)
UNZIP := $(shell which unzip) -o

<<<<<<< HEAD
# Rules for patching
$(BUILD_HELPER_DIR)/%-patching: $(BUILD_HELPER_DIR)/%-unpack 
	set -e ; DIR=$$($(ECHO) $* | $(SED) 's/-[0-9.]\+.*//'); \
	for P in $$($(LS) $(PACKAGE_DIR)/$$DIR/patches/*.dif); do \
	    $(ECHO) "applying $$P..." ; \
	    $(PATCH) -p1 -b -d $* < $$P ; \
	done
	$(TOUCH) $@

# Rules for unpacking 
$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tar.xz
	$(RM) -r $* 
	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TAR_XZ) $<
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tar.gz
	$(RM) -r $* 
	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TAR_GZ) $<
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tgz
	$(RM) -r $* 
	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TAR_GZ) $<
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tar.bz2
	$(RM) -r $* 
	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TAR_BZ2) $<
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.zip
	$(RM) -r $* 
	$(MKDIR) $(BUILD_HELPER_DIR)
	$(UNZIP) $<
=======
HUMAN_INSTALL_TARGETS := $(foreach package,$(PACKAGES),$(addsuffix -install,$(package)))
HUMAN_BUILD_TARGETS := $(foreach package,$(PACKAGES),$(addsuffix -build,$(package)))

.PHONY: $(HUMAN_INSTALL_TARGETS) $(HUMAN_BUILD_TARGETS)

# Provide some targets for convenience: [pkg] instead of /abs/path/to/[pkg]/[pkg]-[version]-install
$(HUMAN_INSTALL_TARGETS): %-install:
# TODO: Can we make this work as real dependency without submake?
	$(MAKE) $($(addsuffix _INSTALL, $(call package_target_prefix,$*)))

$(HUMAN_BUILD_TARGETS): %-build:
# TODO: Can we make this work as real dependency without submake?
	$(MAKE) $($(addsuffix _BUILD, $(call package_target_prefix,$*)))

# Each package may have a packages/[pkg]/skel directory which contents will be
# packed into destdir/skel. These files will be installed, e.g. [site]/etc/...
# and may contain macros that are replaced during site creation/update.
#
# These files here need to be installed into skel/ before the install target is
# executed, because the install target is allowed to do modifications to the
# files.
$(INSTALL_TARGETS): $(BUILD_HELPER_DIR)/%-install: $(BUILD_HELPER_DIR)/%-skel-dir
$(BUILD_HELPER_DIR)/%-skel-dir: $(PRE_INSTALL)
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/skel
	set -e ; \
	    PACKAGE_NAME="$$(echo "$*" | sed 's/-[0-9.]\+.*//')"; \
	    if [ "$$PACKAGE_NAME" = "Python" ]; then \
		PACKAGE_NAME="Python3" ; \
	    fi ; \
	    PACKAGE_PATH="$(PACKAGE_DIR)/$$PACKAGE_NAME"; \
	    if [ ! -d "$$PACKAGE_PATH" ]; then \
		echo "ERROR: Package directory does not exist" ; \
		exit 1; \
	    fi ; \
	    if [ -d "$$PACKAGE_PATH/skel" ]; then \
		tar cf - -C "$$PACKAGE_PATH/skel" \
		    --exclude="*~" \
		    --exclude=".gitignore" \
		    . | tar xvf - -C $(DESTDIR)$(OMD_ROOT)/skel ; \
            fi

# Rules for patching
$(BUILD_HELPER_DIR)/%-patching: $(BUILD_HELPER_DIR)/%-unpack
	set -e ; DIR=$$($(ECHO) $* | $(SED) 's/-[0-9.]\+.*//'); \
	if [ "$$DIR" = "Python" ]; then \
	    DIR="Python3" ; \
	fi ; \
	if [ ! -d "$(PACKAGE_DIR)/$$DIR" ]; then \
	    echo "ERROR: Package directory does not exist" ; \
	    exit 1; \
	fi ; \
	for P in $$($(LS) $(PACKAGE_DIR)/$$DIR/patches/*.dif); do \
	    $(ECHO) "applying $$P..." ; \
	    $(PATCH) -p1 -b -d $(PACKAGE_BUILD_DIR)/$* < $$P ; \
	done
	$(TOUCH) $@

# Rules for unpacking
$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tar.xz
	$(RM) -r $(PACKAGE_BUILD_DIR)/$*
	$(MKDIR) $(PACKAGE_BUILD_DIR)
	$(TAR_XZ) $< -C $(PACKAGE_BUILD_DIR)

	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tar.gz
	$(RM) -r $(PACKAGE_BUILD_DIR)/$*
	$(MKDIR) $(PACKAGE_BUILD_DIR)
	$(TAR_GZ) $< -C $(PACKAGE_BUILD_DIR)

	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tgz
	$(RM) -r $(PACKAGE_BUILD_DIR)/$*
	$(MKDIR) $(PACKAGE_BUILD_DIR)
	$(TAR_GZ) $< -C $(PACKAGE_BUILD_DIR)

	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.tar.bz2
	$(RM) -r $(PACKAGE_BUILD_DIR)/$*
	$(MKDIR) $(PACKAGE_BUILD_DIR)
	$(TAR_BZ2) $< -C $(PACKAGE_BUILD_DIR)

	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TOUCH) $@

$(BUILD_HELPER_DIR)/%-unpack: $(PACKAGE_DIR)/*/%.zip
	$(RM) -r $(PACKAGE_BUILD_DIR)/$*
	$(MKDIR) $(PACKAGE_BUILD_DIR)
	$(UNZIP) $< -d $(PACKAGE_BUILD_DIR)

	$(MKDIR) $(BUILD_HELPER_DIR)
>>>>>>> upstream/master
	$(TOUCH) $@

debug:
	echo $(PACKAGE_DIR)

# Include rules to make packages
<<<<<<< HEAD
include     packages/apache-omd/apache-omd.make \
    packages/boost/boost.make \
    packages/stunnel/stunnel.make \
    packages/check_mk/check_mk.make \
    packages/check_multi/check_multi.make \
    packages/check_mysql_health/check_mysql_health.make \
    packages/check_oracle_health/check_oracle_health.make \
    packages/dokuwiki/dokuwiki.make \
    packages/freetds/freetds.make \
    packages/heirloom-pkgtools/heirloom-pkgtools.make \
    packages/jmx4perl/jmx4perl.make \
    packages/libgsf/libgsf.make \
    packages/maintenance/maintenance.make \
    packages/mk-livestatus/mk-livestatus.make \
    packages/mod_fcgid/mod_fcgid.make \
    packages/mod_wsgi/mod_wsgi.make \
=======
include \
    packages/openssl/openssl.make \
    packages/apache-omd/apache-omd.make \
    packages/stunnel/stunnel.make \
    packages/check_mk/check_mk.make \
    packages/check_mysql_health/check_mysql_health.make \
    packages/check_oracle_health/check_oracle_health.make \
    packages/freetds/freetds.make \
    packages/heirloom-pkgtools/heirloom-pkgtools.make \
    packages/perl-modules/perl-modules.make \
    packages/jmx4perl/jmx4perl.make \
    packages/libgsf/libgsf.make \
    packages/postgresql/postgresql.make \
    packages/maintenance/maintenance.make \
    packages/mod_fcgid/mod_fcgid.make \
>>>>>>> upstream/master
    packages/monitoring-plugins/monitoring-plugins.make \
    packages/msitools/msitools.make \
    packages/nagios/nagios.make \
    packages/nagvis/nagvis.make \
    packages/heirloom-mailx/heirloom-mailx.make \
    packages/navicli/navicli.make \
<<<<<<< HEAD
    packages/net-snmp/net-snmp.make \
    packages/nrpe/nrpe.make \
    packages/nsca/nsca.make \
    packages/omd/omd.make \
    packages/openhardwaremonitor/openhardwaremonitor.make \
    packages/patch/patch.make \
    packages/perl-modules/perl-modules.make \
    packages/pnp4nagios/pnp4nagios.make \
    packages/Python/Python.make \
    packages/Python3/Python3.make \
    packages/python-modules/python-modules.make \
    packages/python3-modules/python3-modules.make \
    packages/re2/re2.make \
    packages/rrdtool/rrdtool.make \
=======
    packages/nrpe/nrpe.make \
    packages/nsca/nsca.make \
    packages/openhardwaremonitor/openhardwaremonitor.make \
    packages/patch/patch.make \
    packages/pnp4nagios/pnp4nagios.make \
    packages/Python3/Python3.make \
    packages/python3-modules/python3-modules.make \
    packages/omd/omd.make \
    packages/net-snmp/net-snmp.make \
    packages/python3-mod_wsgi/python3-mod_wsgi.make \
    packages/re2/re2.make \
    packages/rrdtool/rrdtool.make \
    packages/mk-livestatus/mk-livestatus.make \
>>>>>>> upstream/master
    packages/snap7/snap7.make \
    packages/Webinject/Webinject.make \
    packages/appliance/appliance.make

ifeq ($(EDITION),enterprise)
include $(REPO_PATH)/enterprise/enterprise.make
endif
ifeq ($(EDITION),managed)
include $(REPO_PATH)/enterprise/enterprise.make \
    $(REPO_PATH)/managed/managed.make
endif
<<<<<<< HEAD


=======
>>>>>>> upstream/master
