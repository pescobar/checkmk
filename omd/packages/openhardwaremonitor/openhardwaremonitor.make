<<<<<<< HEAD
=======
# TODO: This is not really a OMD package. It does not have a build target that
# is called during OMD package build. Shouldn't we cleanup this to work like
# the other dist package artifacts?

>>>>>>> upstream/master
OPENHARDWAREMONITOR := openhardwaremonitor
OPENHARDWAREMONITOR_VERS := 0.8.0
OPENHARDWAREMONITOR_DIR := $(OPENHARDWAREMONITOR)-$(OPENHARDWAREMONITOR_VERS)

<<<<<<< HEAD
OPENHARDWAREMONITOR_INSTALL := $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)-install
OPENHARDWAREMONITOR_UNPACK := $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)-unpack
OPENHARDWAREMONITOR_DIST := $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)-dist

.PHONY: $(OPENHARDWAREMONITOR) $(OPENHARDWAREMONITOR)-setup $(OPENHARDWAREMONITOR)-clean-ohm $(OPENHARDWAREMONITOR)-dist $(OPENHARDWAREMONITOR)-build $(OPENHARDWAREMONITOR)-install $(OPENHARDWAREMONITOR)-skel $(OPENHARDWAREMONITOR)-clean
=======
OPENHARDWAREMONITOR_UNPACK := $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)-unpack
OPENHARDWAREMONITOR_DIST := $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)-dist
OPENHARDWAREMONITOR_BUILD := $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)-build
OPENHARDWAREMONITOR_INSTALL := $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)-install

#OPENHARDWAREMONITOR_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(OPENHARDWAREMONITOR_DIR)
OPENHARDWAREMONITOR_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(OPENHARDWAREMONITOR_DIR)
#OPENHARDWAREMONITOR_WORK_DIR := $(PACKAGE_WORK_DIR)/$(OPENHARDWAREMONITOR_DIR)

.PHONY: $(OPENHARDWAREMONITOR)-setup $(OPENHARDWAREMONITOR)-dist
>>>>>>> upstream/master

# This package can not, because it's a Mono project, and should not be built, because we compile
# a linux distro independent windows binary, during packaging procedure in the context of the
# single linux distributions. Instead we build the exe file during src/ packaging phase on our
# development server. This is equal to the precompiled windows agent and the agent updater.
<<<<<<< HEAD
$(OPENHARDWAREMONITOR):

$(OPENHARDWAREMONITOR)-install: $(OPENHARDWAREMONITOR_INSTALL)

$(OPENHARDWAREMONITOR)-dist: $(OPENHARDWAREMONITOR_DIST)

# OpenHardwareMonitorCLI.exe OpenHardwareMonitorLib.dll: $(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorCLI.exe $(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorLib.dll
#	cp -p $(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorCLI.exe  \
#	      $(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorLib.dll \
#	      .

#$(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorCLI.exe $(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorLib.dll:  $(OPENHARDWAREMONITOR_UNPACK) $(OPENHARDWAREMONITOR_DIR)/OpenHardwareMonitorCLI $(OPENHARDWAREMONITOR_DIR)/OpenHardwareMonitor.sln
$(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe:  $(OPENHARDWAREMONITOR_UNPACK) $(OPENHARDWAREMONITOR_DIR)/OpenHardwareMonitorCLI $(OPENHARDWAREMONITOR_DIR)/OpenHardwareMonitor.sln
=======

# TODO: Can this be removed?
$(OPENHARDWAREMONITOR)-dist: $(OPENHARDWAREMONITOR_DIST)

$(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe: $(OPENHARDWAREMONITOR_UNPACK) $(OPENHARDWAREMONITOR_BUILD_DIR)/OpenHardwareMonitorCLI $(OPENHARDWAREMONITOR_BUILD_DIR)/OpenHardwareMonitor.sln
>>>>>>> upstream/master
# The strange "cat" below is necessary because the extremely ancient Mono
# versions coming with even the latest Ubuntus still contain the rather severe
# bug https://github.com/mono/mono/issues/6752. ("...System.Exception: Magic
# number is wrong: 542") :-P
<<<<<<< HEAD
	xbuild /p:Configuration=Release \
	       /p:TargetFrameworkVersion="v4.5" \
	       $(OPENHARDWAREMONITOR_DIR)/OpenHardwareMonitor.sln \
	       /target:OpenHardwareMonitorCLI | cat
	cp $(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorCLI.exe $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)
	cp $(OPENHARDWAREMONITOR_DIR)/Bin/Release/OpenHardwareMonitorLib.dll $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)

$(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorLib.dll: $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe

$(OPENHARDWAREMONITOR_DIR)/OpenHardwareMonitorCLI: $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI
	cp -r $< $(OPENHARDWAREMONITOR_DIR)/

$(OPENHARDWAREMONITOR_DIR)/OpenHardwareMonitor.sln: $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitor.sln
	cp $<  $(OPENHARDWAREMONITOR_DIR)/
=======
	cd $(OPENHARDWAREMONITOR_BUILD_DIR) ; \
	    xbuild /p:Configuration=Release \
	       /p:TargetFrameworkVersion="v4.5" \
	       OpenHardwareMonitor.sln \
	       /target:OpenHardwareMonitorCLI | cat
	cp $(OPENHARDWAREMONITOR_BUILD_DIR)/Bin/Release/OpenHardwareMonitorCLI.exe $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)
	cp $(OPENHARDWAREMONITOR_BUILD_DIR)/Bin/Release/OpenHardwareMonitorLib.dll $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)

$(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorLib.dll: $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe

$(OPENHARDWAREMONITOR_BUILD_DIR)/OpenHardwareMonitorCLI: $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI
	$(MKDIR) $(OPENHARDWAREMONITOR_BUILD_DIR)
	cp -r $< $(OPENHARDWAREMONITOR_BUILD_DIR)/

$(OPENHARDWAREMONITOR_BUILD_DIR)/OpenHardwareMonitor.sln: $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitor.sln
	$(MKDIR) $(OPENHARDWAREMONITOR_BUILD_DIR)
	cp $<  $(OPENHARDWAREMONITOR_BUILD_DIR)/
>>>>>>> upstream/master

# Remove dependencies for now, to avoid triggering rebuild in chroots:
# $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorLib.dll
$(OPENHARDWAREMONITOR_INSTALL):
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/check_mk/agents/windows/ohm
	install -m 755 $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe $(DESTDIR)$(OMD_ROOT)/share/check_mk/agents/windows/ohm
	install -m 755 $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorLib.dll $(DESTDIR)$(OMD_ROOT)/share/check_mk/agents/windows/ohm
	$(TOUCH) $@

<<<<<<< HEAD
$(OPENHARDWAREMONITOR)-skel:

=======
>>>>>>> upstream/master
# ToDo: Remove this from build scrtip.
$(OPENHARDWAREMONITOR)-setup:
	sudo apt-get install \
	    mono-complete \
	    mono-xbuild

<<<<<<< HEAD
$(OPENHARDWAREMONITOR_DIST): $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe
	$(TOUCH) $@

$(OPENHARDWAREMONITOR)-clean-ohm: clean
	rm -f OpenHardwareMonitorCLI.exe OpenHardwareMonitorLib.dll

$(OPENHARDWAREMONITOR)-clean:
	rm -rf $(OPENHARDWAREMONITOR_DIR) $(BUILD_HELPER_DIR)/$(OPENHARDWAREMONITOR_DIR)*
=======
$(OPENHARDWAREMONITOR_BUILD):
	$(TOUCH) $@

$(OPENHARDWAREMONITOR_DIST): $(PACKAGE_DIR)/$(OPENHARDWAREMONITOR)/OpenHardwareMonitorCLI.exe
	$(TOUCH) $@
>>>>>>> upstream/master
