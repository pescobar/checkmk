NET_SNMP := net-snmp
<<<<<<< HEAD
NET_SNMP_VERS  := 0b32548
NET_SNMP_DIR := $(NET_SNMP)-$(NET_SNMP_VERS)

=======
NET_SNMP_VERS := 0b32548
NET_SNMP_DIR := $(NET_SNMP)-$(NET_SNMP_VERS)

NET_SNMP_PATCHING := $(BUILD_HELPER_DIR)/$(NET_SNMP_DIR)-patching
>>>>>>> upstream/master
NET_SNMP_BUILD := $(BUILD_HELPER_DIR)/$(NET_SNMP_DIR)-build
NET_SNMP_INSTALL := $(BUILD_HELPER_DIR)/$(NET_SNMP_DIR)-install
NET_SNMP_INSTALL_BASE := $(BUILD_HELPER_DIR)/$(NET_SNMP_DIR)-install-base
NET_SNMP_INSTALL_PYTHON := $(BUILD_HELPER_DIR)/$(NET_SNMP_DIR)-install-python
NET_SNMP_INSTALL_PERL := $(BUILD_HELPER_DIR)/$(NET_SNMP_DIR)-install-perl
<<<<<<< HEAD
NET_SNMP_PATCHING := $(BUILD_HELPER_DIR)/$(NET_SNMP_DIR)-patching

.PHONY: $(NET_SNMP) $(NET_SNMP)-install $(NET_SNMP)-install-base $(NET_SNMP)-install-python $(NET_SNMP)-install-perl $(NET_SNMP)-skel $(NET_SNMP)-clean

$(NET_SNMP): $(NET_SNMP_BUILD)

$(NET_SNMP)-install: $(NET_SNMP_INSTALL)

$(NET_SNMP_BUILD): $(NET_SNMP_PATCHING) $(PYTHON_BUILD) $(PERL_MODULES_BUILD)
# Skip Perl-Modules because of build errors when MIB loading is disabled.
# Skip Python binding because we need to use our own python, see install target.
	cd $(NET_SNMP_DIR) \
=======

#NET_SNMP_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(NET_SNMP_DIR)
NET_SNMP_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(NET_SNMP_DIR)
#NET_SNMP_WORK_DIR := $(PACKAGE_WORK_DIR)/$(NET_SNMP_DIR)

$(NET_SNMP_BUILD): $(NET_SNMP_PATCHING) $(PYTHON3_CACHE_PKG_PROCESS) $(PERL_MODULES_BUILD)
# Skip Perl-Modules because of build errors when MIB loading is disabled.
# Skip Python binding because we need to use our own python, see install target.
	cd $(NET_SNMP_BUILD_DIR) \
>>>>>>> upstream/master
        && if [ "$(DISTRO_CODE)" == "el8" ]; then export CFLAGS='-Wformat -I../../include -D_REENTRANT -D_GNU_SOURCE -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fwrapv -fno-strict-aliasing -I/usr/local/include -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'; fi \
        && ./configure \
	    --enable-ipv6 \
	    --disable-agent \
	    --disable-snmptrapd-subagent \
	    --with-mibdirs="\$$HOME/local/share/snmp/mibs:$(OMD_ROOT)/share/snmp/mibs:/usr/share/snmp/mibs" \
	    --with-defaults \
	    --disable-scripts \
<<<<<<< HEAD
	    --prefix=$(OMD_ROOT) && make
=======
	    --prefix=$(OMD_ROOT) && $(MAKE)
>>>>>>> upstream/master
	$(TOUCH) $@

$(NET_SNMP_INSTALL): $(NET_SNMP_INSTALL_BASE) $(NET_SNMP_INSTALL_PYTHON) $(NET_SNMP_INSTALL_PERL)
	$(TOUCH) $@

$(NET_SNMP_INSTALL_BASE): $(NET_SNMP_BUILD)
<<<<<<< HEAD
	cd $(NET_SNMP_DIR)/snmplib && make DESTDIR=$(DESTDIR) installlibs
	cd $(NET_SNMP_DIR)/apps && make DESTDIR=$(DESTDIR) installbin
	cd $(NET_SNMP_DIR)/man && make DESTDIR=$(DESTDIR) install
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/snmp/mibs
	cd $(NET_SNMP_DIR)/mibs && make DESTDIR=$(DESTDIR) mibsinstall
=======
	cd $(NET_SNMP_BUILD_DIR)/snmplib && $(MAKE) DESTDIR=$(DESTDIR) installlibs
	cd $(NET_SNMP_BUILD_DIR)/apps && $(MAKE) DESTDIR=$(DESTDIR) installbin
	cd $(NET_SNMP_BUILD_DIR)/man && $(MAKE) DESTDIR=$(DESTDIR) install
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/snmp/mibs
	cd $(NET_SNMP_BUILD_DIR)/mibs && $(MAKE) DESTDIR=$(DESTDIR) mibsinstall
>>>>>>> upstream/master
	$(TOUCH) $@

$(NET_SNMP_INSTALL_PYTHON): $(NET_SNMP_BUILD)
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/lib/python
<<<<<<< HEAD
	cd $(NET_SNMP_DIR)/python && \
		export PYTHONPATH="$$PYTHONPATH:$(PACKAGE_PYTHON_PYTHONPATH):$(DESTDIR)$(OMD_ROOT)/lib/python" ; \
	    export LDFLAGS="$(PACKAGE_PYTHON_LDFLAGS)" ; \
	    export LD_LIBRARY_PATH="$(PACKAGE_PYTHON_LD_LIBRARY_PATH)" ; \
	    $(PACKAGE_PYTHON_EXECUTABLE) setup.py install --basedir=.. --home=$(DESTDIR)$(OMD_ROOT) \
		--prefix='' \
		--install-platlib=$(DESTDIR)$(OMD_ROOT)/lib/python \
		--install-purelib=$(DESTDIR)$(OMD_ROOT)/lib/python \
=======
	cd $(NET_SNMP_BUILD_DIR)/python && \
		export PYTHONPATH="$$PYTHONPATH:$(PACKAGE_PYTHON3_PYTHONPATH):$(DESTDIR)$(OMD_ROOT)/lib/python" ; \
	    export LDFLAGS="$(PACKAGE_PYTHON3_LDFLAGS)" ; \
	    export LD_LIBRARY_PATH="$(PACKAGE_PYTHON3_LD_LIBRARY_PATH)" ; \
	    $(PACKAGE_PYTHON3_EXECUTABLE) setup.py install --basedir=.. --home=$(DESTDIR)$(OMD_ROOT) \
		--prefix='' \
		--install-platlib=$(DESTDIR)$(OMD_ROOT)/lib/python3 \
		--install-purelib=$(DESTDIR)$(OMD_ROOT)/lib/python3 \
>>>>>>> upstream/master
		--root=/ \
		--single-version-externally-managed
	$(TOUCH) $@
# For some obscure reason beyond the mental capacities of mere humans, the
# easy_install mechanism triggered by the setup call above results in the
# creation of a lib/python/site.py, a copy of site-patch.py from setuptools.
# Having this in the PYTHONPATH makes it impossible to run python3-based SW as a
# site user, including gdb! So let's simply nuke it here...
# TODO(sp): Disabled for now, otherwise the netsnmp module is not found. Figure
# out what's really going on here!
#	$(RM) $(DESTDIR)$(OMD_ROOT)/lib/python/site.py*

<<<<<<< HEAD
$(NET_SNMP_INSTALL_PERL): $(NET_SNMP_BUILD)
	cd $(NET_SNMP_DIR)/perl && \
	    make \
=======
# TODO: Use perl standard path variables
$(NET_SNMP_INSTALL_PERL): $(NET_SNMP_BUILD)
	cd $(NET_SNMP_BUILD_DIR)/perl && \
	    $(MAKE) \
>>>>>>> upstream/master
		DESTDIR=$(DESTDIR)$(OMD_ROOT) \
		INSTALLSITEARCH=/lib/perl5/lib/perl5 \
		INSTALLSITEMAN3DIR=/share/man/man3 \
		INSTALLARCHLIB=/lib/perl5/lib/perl5/x86_64-linux-gnu-thread-multi \
		install
<<<<<<< HEAD
	$(TOUCH) $@


$(NET_SNMP)-skel:

$(NET_SNMP)-clean:
	$(RM) -r $(NET_SNMP_DIR) $(BUILD_HELPER_DIR)/$(NET_SNMP)*
=======
# Fixup some library permissions. They need to be owner writable to make
# dh_strip command of deb packaging procedure work
	find $(DESTDIR)$(OMD_ROOT)/lib/perl5/lib/perl5/auto/*SNMP -type f -name \*.so -exec chmod u+w {} \;
	$(TOUCH) $@
>>>>>>> upstream/master
