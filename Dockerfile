# Start with an ancient OS, so our builds are very
# permissive in terms of their glibc requirements
# when deployed elsewhere.

FROM centos:6

# Make GCC 6.3.1 the default compiler, as per VFXPlatform 2018

RUN yum install -y centos-release-scl
RUN yum install -y devtoolset-6
RUN scl enable devtoolset-6 bash

# So we can build stuff

RUN yum install -y epel-release
RUN yum install -y cmake3
RUN ln -s /usr/bin/cmake3 /usr/bin/cmake

RUN yum install -y scons

# Needed by boost::iostreams

RUN yum install -y bzip2-devel

# Needed to build libjpeg

RUN yum install -y nasm

# Needed for png

RUN yum install -y zlib-devel

# Needed for GLEW

RUN yum install -y libX11-devel
RUN yum install -y mesa-libGL-devel
RUN yum install -y mesa-libGLU-devel
RUN yum install -y libXmu-devel
RUN yum install -y libXi-devel

# Needed for OCIO

RUN yum install -y patch

# Needed by various things probably

RUN yum install -y doxygen

# Needed by OSL

RUN yum install -y flex
RUN yum install -y bison

# Needed by Qt

RUN yum install -y xkeyboard-config.noarch
RUN yum install -y fontconfig-devel.x86_64

COPY . /gafferDependenciesSource

ENV ARNOLD_ROOT /gafferDependenciesSource/3rdParty/arnold
ENV RMAN_ROOT /gafferDependenciesSource/3rdParty/3delight
ENV BUILD_DIR /gafferDependenciesBuild

ENV PATH /opt/rh/devtoolset-6/root/usr/bin:$PATH

RUN ls
RUN ls /gafferDependenciesSource
RUN ls /gafferDependenciesSource/build

WORKDIR /gafferDependenciesSource

RUN ./build/buildAll.sh
