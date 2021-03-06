LIBGSF := libgsf
LIBGSF_VERS := 1.14.44
LIBGSF_DIR := $(LIBGSF)-$(LIBGSF_VERS)

<<<<<<< HEAD
LIBGSF_BUILD := $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)-build
LIBGSF_INSTALL := $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)-install
LIBGSF_UNPACK := $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)-unpack

.PHONY: $(LIBGSF)-build $(LIBGSF)-install $(LIBGSF)-skel $(LIBGSF)-clean

$(LIBGSF): $(LIBGSF_BUILD)

$(LIBGSF)-install: $(LIBGSF_INSTALL)


ifneq ($(filter $(DISTRO_CODE),sles15),)
$(LIBGSF_BUILD): $(LIBGSF_UNPACK)
	cd $(LIBGSF_DIR) && ./configure --prefix=$(OMD_ROOT)
	$(MAKE) -C $(LIBGSF_DIR)
# Package msitools needs some stuff during the build.
	$(MAKE) -C $(LIBGSF_DIR) prefix=$(PACKAGE_LIBGSF_DESTDIR) install
=======
LIBGSF_UNPACK := $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)-unpack
LIBGSF_BUILD := $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)-build
LIBGSF_INTERMEDIATE_INSTALL := $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)-install-intermediate
LIBGSF_INSTALL := $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)-install

LIBGSF_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(LIBGSF_DIR)
LIBGSF_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(LIBGSF_DIR)
#LIBGSF_WORK_DIR := $(PACKAGE_WORK_DIR)/$(LIBGSF_DIR)

# Used by msitools
PACKAGE_LIBGSF_DESTDIR := $(LIBGSF_INSTALL_DIR)
PACKAGE_LIBGSF_LDFLAGS := -L$(PACKAGE_LIBGSF_DESTDIR)/lib -lgsf-1
PACKAGE_LIBGSF_CFLAGS := -I$(PACKAGE_LIBGSF_DESTDIR)/include/libgsf-1

ifneq ($(filter $(DISTRO_CODE),sles15 sles15sp1),)
$(LIBGSF_BUILD): $(LIBGSF_UNPACK)
	cd $(LIBGSF_BUILD_DIR) && ./configure --prefix=""
	$(MAKE) -C $(LIBGSF_BUILD_DIR)
>>>>>>> upstream/master
	$(TOUCH) $@
else
$(LIBGSF_BUILD):
	$(MKDIR) $(BUILD_HELPER_DIR)
	$(TOUCH) $@
endif

<<<<<<< HEAD
$(LIBGSF_INSTALL): $(LIBGSF_BUILD)
ifneq ($(filter $(DISTRO_CODE),sles15),)
	$(MAKE) DESTDIR=$(DESTDIR) -C $(LIBGSF_DIR) install
endif
	$(TOUCH) $@

$(LIBGSF)-skel:

$(LIBGSF)-clean:
	rm -rf $(LIBGSF_DIR) $(BUILD_HELPER_DIR)/$(LIBGSF_DIR)*
=======
$(LIBGSF_INTERMEDIATE_INSTALL): $(LIBGSF_BUILD)
ifneq ($(filter $(DISTRO_CODE),sles15 sles15sp1),)
	$(MAKE) DESTDIR=$(LIBGSF_INSTALL_DIR) -C $(LIBGSF_BUILD_DIR) install
endif
	$(TOUCH) $@

$(LIBGSF_INSTALL): $(LIBGSF_INTERMEDIATE_INSTALL)
ifneq ($(filter $(DISTRO_CODE),sles15 sles15sp1),)
	$(RSYNC) $(LIBGSF_INSTALL_DIR)/ $(DESTDIR)$(OMD_ROOT)/
endif
	$(TOUCH) $@
>>>>>>> upstream/master
