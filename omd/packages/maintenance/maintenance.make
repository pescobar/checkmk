MAINTENANCE := maintenance
MAINTENANCE_VERS := $(OMD_VERSION)

<<<<<<< HEAD
MAINTENANCE_INSTALL := $(BUILD_HELPER_DIR)/$(MAINTENANCE)-install

.PHONY: $(MAINTENANCE) $(MAINTENANCE)-skel $(MAINTENANCE)-clean build-helper/maintenance

$(MAINTENANCE)-install: $(MAINTENANCE_INSTALL)

$(MAINTENANCE):
=======
MAINTENANCE_BUILD := $(BUILD_HELPER_DIR)/$(MAINTENANCE)-build
MAINTENANCE_INSTALL := $(BUILD_HELPER_DIR)/$(MAINTENANCE)-install

$(MAINTENANCE_BUILD):
	$(TOUCH) $@
>>>>>>> upstream/master

$(MAINTENANCE_INSTALL):
	install -v -m 755 $(PACKAGE_DIR)/$(MAINTENANCE)/merge-crontabs $(DESTDIR)$(OMD_ROOT)/bin
	install -v -m 755 $(PACKAGE_DIR)/$(MAINTENANCE)/diskspace $(DESTDIR)$(OMD_ROOT)/bin
	install -v -m 755 $(PACKAGE_DIR)/$(MAINTENANCE)/logrotate $(DESTDIR)$(OMD_ROOT)/bin
	$(TOUCH) $@
<<<<<<< HEAD

maintenance-skel:

maintenance-clean:
=======
>>>>>>> upstream/master
