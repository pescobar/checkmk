MSITOOLS := msitools
MSITOOLS_VERS := 0.94
MSITOOLS_DIR := msitools-$(MSITOOLS_VERS)

<<<<<<< HEAD
LCAB_VERSION := 1.0b12
LCAB_DIR     := lcab-$(LCAB_VERSION)

MSITOOLS_BUILD := $(BUILD_HELPER_DIR)/$(MSITOOLS_DIR)-build
MSITOOLS_INSTALL := $(BUILD_HELPER_DIR)/$(MSITOOLS_DIR)-install
MSITOOLS_PATCHING := $(BUILD_HELPER_DIR)/$(MSITOOLS_DIR)-patching
.PHONY: skel

# Problem here is: msitools is not compilable on older distros
# like Debian 5 or RedHat 5.X. So here we rather ignore
# compile problems and msi{build,info} will be missing. Check_MK
# then knows this and the agent bakery cannot create MSI
# packages. People need to upgrade to a more modern platform
# for that.

ifneq ($(filter $(DISTRO_CODE),sles15),)
=======
# TODO: Extract LCAB to dedicated package
LCAB_VERSION := 1.0b12
LCAB_DIR     := lcab-$(LCAB_VERSION)

#LCAB_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(LCAB_DIR)
LCAB_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(LCAB_DIR)
#LCAB_WORK_DIR := $(PACKAGE_WORK_DIR)/$(LCAB_DIR)

MSITOOLS_PATCHING := $(BUILD_HELPER_DIR)/$(MSITOOLS_DIR)-patching
MSITOOLS_BUILD := $(BUILD_HELPER_DIR)/$(MSITOOLS_DIR)-build
MSITOOLS_INSTALL := $(BUILD_HELPER_DIR)/$(MSITOOLS_DIR)-install

#MSITOOLS_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(MSITOOLS_DIR)
MSITOOLS_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(MSITOOLS_DIR)
#MSITOOLS_WORK_DIR := $(PACKAGE_WORK_DIR)/$(MSITOOLS_DIR)

ifneq ($(filter $(DISTRO_CODE),sles15 sles15sp1),)
>>>>>>> upstream/master
GSF_CONFIGURE_VARS := GSF_LIBS="$(PACKAGE_LIBGSF_LDFLAGS)" GSF_CFLAGS="$(PACKAGE_LIBGSF_CFLAGS)"
else
GSF_CONFIGURE_VARS :=
endif

<<<<<<< HEAD
$(MSITOOLS): $(MSITOOLS_BUILD)

$(MSITOOLS)-install: $(MSITOOLS_INSTALL)

$(MSITOOLS_BUILD): $(LIBGSF_BUILD) $(MSITOOLS_PATCHING) $(BUILD_HELPER_DIR)/$(LCAB_DIR)-unpack
	# Do not try to compile on lenny. Compiler is too old
	if [ "$$($(GCC_SYSTEM) --version | $(SED) -n '1s/.* //p' )" != 4.3.2 ] && cd $(MSITOOLS_DIR) && $(GSF_CONFIGURE_VARS) ./configure --prefix=$(OMD_ROOT) ; then \
	  $(MAKE) -C libmsi ; \
	  $(MAKE) msibuild ; \
	  $(MAKE) msiinfo ; \
	fi
	cd $(LCAB_DIR) && ./configure && $(MAKE)
=======
$(MSITOOLS_BUILD): $(LIBGSF_INTERMEDIATE_INSTALL) $(MSITOOLS_PATCHING) $(BUILD_HELPER_DIR)/$(LCAB_DIR)-unpack
	cd $(MSITOOLS_BUILD_DIR) && \
          $(GSF_CONFIGURE_VARS) ./configure --prefix=$(OMD_ROOT) ; \
	  $(MAKE) -C libmsi ; \
	  $(MAKE) msibuild ; \
	  $(MAKE) msiinfo ; \
	cd $(LCAB_BUILD_DIR) && ./configure && $(MAKE)
>>>>>>> upstream/master
	$(TOUCH) $@

$(MSITOOLS_INSTALL): $(MSITOOLS_BUILD)
	echo $(DESTDIR)
<<<<<<< HEAD
	if [ -f $(MSITOOLS_DIR)/.libs/msiinfo ] ; then \
	    install -m 755 $(MSITOOLS_DIR)/.libs/msiinfo $(DESTDIR)$(OMD_ROOT)/bin ; \
	    install -m 755 $(MSITOOLS_DIR)/.libs/msibuild $(DESTDIR)$(OMD_ROOT)/bin ; \
	    install -m 755 $(LCAB_DIR)/lcab $(DESTDIR)$(OMD_ROOT)/bin ; \
	    install -m 755 $(MSITOOLS_DIR)/libmsi/.libs/libmsi.so* $(DESTDIR)$(OMD_ROOT)/lib ; \
	    $(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/check_mk/agents/windows ; \
	    install -m 644 $(PACKAGE_DIR)/$(MSITOOLS)/*.msi $(DESTDIR)$(OMD_ROOT)/share/check_mk/agents/windows ; \
	fi
	$(TOUCH) $@

$(MSITOOLS)-skel:

$(MSITOOLS)-clean:
	$(RM) -r $(MSITOOLS_DIR) $(LCAB_DIR) $(BUILD_HELPER_DIR)/$(MSITOOLS)* $(BUILD_HELPER_DIR)/$(LCAB_DIR)*
=======
	install -m 755 $(MSITOOLS_BUILD_DIR)/.libs/msiinfo $(DESTDIR)$(OMD_ROOT)/bin ; \
	install -m 755 $(MSITOOLS_BUILD_DIR)/.libs/msibuild $(DESTDIR)$(OMD_ROOT)/bin ; \
	install -m 755 $(LCAB_BUILD_DIR)/lcab $(DESTDIR)$(OMD_ROOT)/bin ; \
	install -m 755 $(MSITOOLS_BUILD_DIR)/libmsi/.libs/libmsi.so* $(DESTDIR)$(OMD_ROOT)/lib ; \
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/check_mk/agents/windows ; \
	install -m 644 $(PACKAGE_DIR)/$(MSITOOLS)/*.msi $(DESTDIR)$(OMD_ROOT)/share/check_mk/agents/windows ; \
	$(TOUCH) $@
>>>>>>> upstream/master
