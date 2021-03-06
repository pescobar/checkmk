CHECK_MYSQL_HEALTH := check_mysql_health
CHECK_MYSQL_HEALTH_VERS := 2.2.2
CHECK_MYSQL_HEALTH_DIR := $(CHECK_MYSQL_HEALTH)-$(CHECK_MYSQL_HEALTH_VERS)

<<<<<<< HEAD
CHECK_MYSQL_HEALTH_BUILD := $(BUILD_HELPER_DIR)/$(CHECK_MYSQL_HEALTH_DIR)-build
CHECK_MYSQL_HEALTH_INSTALL := $(BUILD_HELPER_DIR)/$(CHECK_MYSQL_HEALTH_DIR)-install
CHECK_MYSQL_HEALTH_UNPACK := $(BUILD_HELPER_DIR)/$(CHECK_MYSQL_HEALTH_DIR)-unpack

.PHONY: $(CHECK_MYSQL_HEALTH) $(CHECK_MYSQL_HEALTH)-install $(CHECK_MYSQL_HEALTH)-skel $(CHECK_MYSQL_HEALTH)-clean

$(CHECK_MYSQL_HEALTH): $(CHECK_MYSQL_HEALTH_BUILD)

$(CHECK_MYSQL_HEALTH)-install: $(CHECK_MYSQL_HEALTH_INSTALL)
=======
CHECK_MYSQL_HEALTH_UNPACK := $(BUILD_HELPER_DIR)/$(CHECK_MYSQL_HEALTH_DIR)-unpack
CHECK_MYSQL_HEALTH_BUILD := $(BUILD_HELPER_DIR)/$(CHECK_MYSQL_HEALTH_DIR)-build
CHECK_MYSQL_HEALTH_INSTALL := $(BUILD_HELPER_DIR)/$(CHECK_MYSQL_HEALTH_DIR)-install

#CHECK_MYSQL_HEALTH_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(CHECK_MYSQL_HEALTH_DIR)
CHECK_MYSQL_HEALTH_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(CHECK_MYSQL_HEALTH_DIR)
#CHECK_MYSQL_HEALTH_WORK_DIR := $(PACKAGE_WORK_DIR)/$(CHECK_MYSQL_HEALTH_DIR)
>>>>>>> upstream/master

# Configure options for Nagios. Since we want to compile
# as non-root, we use our own user and group for compiling.
# All files will be packaged as user 'root' later anyway.
CHECK_MYSQL_HEALTH_CONFIGUREOPTS = ""

$(CHECK_MYSQL_HEALTH_BUILD): $(CHECK_MYSQL_HEALTH_UNPACK)
	for i in configure.ac aclocal.m4 configure Makefile.am Makefile.in ; do \
<<<<<<< HEAD
	  test -f $(CHECK_MYSQL_HEALTH_DIR)/$$i && touch $(CHECK_MYSQL_HEALTH_DIR)/$$i ; \
	done
	cd $(CHECK_MYSQL_HEALTH_DIR) ; ./configure $(CHECK_MYSQL_HEALTH_CONFIGUREOPTS)
	$(MAKE) -C $(CHECK_MYSQL_HEALTH_DIR)
	$(TOUCH) $@

$(CHECK_MYSQL_HEALTH_INSTALL): $(CHECK_MYSQL_HEALTH_BUILD)
	install -m 755 $(CHECK_MYSQL_HEALTH_DIR)/plugins-scripts/check_mysql_health $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	$(TOUCH) $@

$(CHECK_MYSQL_HEALTH)-skel:

$(CHECK_MYSQL_HEALTH)-clean:
	rm -rf $(CHECK_MYSQL_HEALTH_DIR) $(BUILD_HELPER_DIR)/$(CHECK_MYSQL_HEALTH_DIR)*
=======
	  test -f $(CHECK_MYSQL_HEALTH_BUILD_DIR)/$$i && touch $(CHECK_MYSQL_HEALTH_BUILD_DIR)/$$i ; \
	done
	cd $(CHECK_MYSQL_HEALTH_BUILD_DIR) ; ./configure $(CHECK_MYSQL_HEALTH_CONFIGUREOPTS)
	$(MAKE) -C $(CHECK_MYSQL_HEALTH_BUILD_DIR)
	$(TOUCH) $@

$(CHECK_MYSQL_HEALTH_INSTALL): $(CHECK_MYSQL_HEALTH_BUILD)
	install -m 755 $(CHECK_MYSQL_HEALTH_BUILD_DIR)/plugins-scripts/check_mysql_health $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	$(TOUCH) $@
>>>>>>> upstream/master
