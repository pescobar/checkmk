<<<<<<< HEAD
FROM 10.9.1.101:4000/sles-15-base

SHELL ["/bin/bash", "-c"]

RUN zypper addrepo -G http://10.9.1.101:8081/repository/sles15 sles15 \
=======
FROM registry.suse.com/suse/sle15:15.0

SHELL ["/bin/bash", "-c"]
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 PATH="/opt/bin:${PATH}"

ARG ARTIFACT_STORAGE
RUN zypper addrepo -G ${ARTIFACT_STORAGE}/repository/sles15 sles15 \
>>>>>>> upstream/master
    && zypper ref -s \
    && zypper -n in -y --force-resolution \
    apache2-devel \
    bind-utils \
<<<<<<< HEAD
    boost-devel \
=======
>>>>>>> upstream/master
    curl \
    flex \
    freeradius-client-devel \
    freetype2-devel \
    gcc \
    gcc-c++ \
    gd-devel \
    git \
    glib2-devel \
    groff \
    intltool \
    krb5-devel \
    libXpm-devel \
    libbz2-devel \
    libcurl-devel \
    libevent-devel \
    libexpat-devel \
    libffi-devel \
    libgnutls-devel \
    libjpeg62-devel \
    libltdl7 \
    libmysqlclient-devel \
    libopenssl-devel \
    libpcap-devel \
    libpng16-devel \
    libtiff-devel \
    libtool \
    libuuid-devel \
    libvpx-devel \
    libxml2-devel \
    make \
    mysql \
    openldap2-devel \
    openssh \
    pango-devel \
    patch \
    postgresql-devel \
    readline-devel \
    rpcbind \
    rpm-build \
    rpm-devel \
<<<<<<< HEAD
    rrdtool-devel \
=======
>>>>>>> upstream/master
    samba-client \
    sqlite3-devel \
    tar \
    texinfo \
    tk-devel \
    unzip \
    wget \
<<<<<<< HEAD
    && zypper clean -a

COPY bw-build-gnu-toolchain.sh /usr/sbin
RUN bw-build-gnu-toolchain.sh -b
RUN rm /usr/bin/gcc /usr/bin/g++
=======
    chrpath \
    joe \
    iputils \
    vim \
    && zypper clean -a

# Install our standard tool chain for building
# - gnu-toolchain is needed for compiling all the C++ stuff
# - cmake is needed for e.g. building re2
# - openssl is needed by Python 3.7+
# - python is needed by our build / test chain
ARG NEXUS_ARCHIVES_URL
ARG NEXUS_USERNAME
ARG NEXUS_PASSWORD
ARG DISTRO
ARG BRANCH_VERSION
ENV NEXUS_ARCHIVES_URL="$NEXUS_ARCHIVES_URL" NEXUS_USERNAME="$NEXUS_USERNAME" NEXUS_PASSWORD="$NEXUS_PASSWORD" DISTRO="$DISTRO" BRANCH_VERSION="$BRANCH_VERSION"

COPY scripts/* /opt/
RUN /opt/install-gnu-toolchain.sh
RUN /opt/install-cmake.sh
RUN /opt/install-openssl.sh
RUN /opt/install-python2.sh
RUN /opt/install-python.sh
RUN /opt/install-pipenv.sh
RUN /opt/install-nodejs.sh
RUN /opt/install-freetds.sh

# Ensure all our build containers have the jenkins user (with same uid/gid). The non privileged
# jobs will be executed as this user in the container
RUN groupadd -g 1000 jenkins \
    && useradd -m -u 1001 -g 1000 -s /bin/bash jenkins

ARG VERS_TAG
RUN echo $VERS_TAG > /version.txt
>>>>>>> upstream/master
