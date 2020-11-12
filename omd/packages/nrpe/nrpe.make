NRPE := nrpe
NRPE_VERS := 3.2.1
NRPE_DIR := $(NRPE)-$(NRPE_VERS)

<<<<<<< HEAD
NRPE_BUILD := $(BUILD_HELPER_DIR)/$(NRPE_DIR)-build
NRPE_INSTALL := $(BUILD_HELPER_DIR)/$(NRPE_DIR)-install
NRPE_UNPACK := $(BUILD_HELPER_DIR)/$(NRPE_DIR)-unpack

.PHONY: $(NRPE) $(NRPE)-install $(NRPE)-skel $(NRPE)-build

$(NRPE): $(NRPE_BUILD)

$(NRPE)-install: $(NRPE_INSTALL)

# Configure options for Nagios. Since we want to compile
# as non-root, we use our own user and group for compiling.
# All files will be packaged as user 'root' later anyway.
NRPE_CONFIGUREOPTS = ""

$(NRPE_BUILD): $(NRPE_UNPACK)
	cd $(NRPE_DIR) ; ./configure $(NRPE_CONFIGUREOPTS)
	$(MAKE) -C $(NRPE_DIR)/src check_nrpe
	$(TOUCH) $@

$(NRPE_INSTALL): $(NRPE_BUILD)
	install -m 755 $(NRPE_DIR)/src/check_nrpe $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/doc/nrpe
	install -m 644 $(NRPE_DIR)/*.md $(DESTDIR)$(OMD_ROOT)/share/doc/nrpe
	install -m 644 $(NRPE_DIR)/LEGAL $(DESTDIR)$(OMD_ROOT)/share/doc/nrpe
	$(TOUCH) $@

$(NRPE)-skel:

$(NRPE)-clean:
	$(RM) -r $(NRPE_DIR) $(BUILD_HELPER_DIR)/$(NRPE)*
=======
NRPE_UNPACK := $(BUILD_HELPER_DIR)/$(NRPE_DIR)-unpack
NRPE_BUILD := $(BUILD_HELPER_DIR)/$(NRPE_DIR)-build
NRPE_INSTALL := $(BUILD_HELPER_DIR)/$(NRPE_DIR)-install

#NRPE_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(NRPE_DIR)
NRPE_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(NRPE_DIR)
#NRPE_WORK_DIR := $(PACKAGE_WORK_DIR)/$(NRPE_DIR)

$(NRPE_BUILD): $(NRPE_UNPACK)
	cd $(NRPE_BUILD_DIR) ; ./configure
	$(MAKE) -C $(NRPE_BUILD_DIR)/src check_nrpe
	$(TOUCH) $@

$(NRPE_INSTALL): $(NRPE_BUILD)
	install -m 755 $(NRPE_BUILD_DIR)/src/check_nrpe $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/doc/nrpe
	install -m 644 $(NRPE_BUILD_DIR)/*.md $(DESTDIR)$(OMD_ROOT)/share/doc/nrpe
	install -m 644 $(NRPE_BUILD_DIR)/LEGAL $(DESTDIR)$(OMD_ROOT)/share/doc/nrpe
	$(TOUCH) $@
>>>>>>> upstream/master
