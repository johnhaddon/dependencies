# Docker builds
# =============
#
# The purpose of the GafferHQ/dependencies project is to provide
# a consistent, repeatable, build recipe for all of Gaffer's
# dependencies. To ensure repeatability we use Docker to perform
# all release builds, so that the exact same build environment is
# used each time.
#
# Usage
# -----
#
# Make sure the 3rd party dependencies are available to the build :
#
# - Copy your Arnold installation to 3rdParty/arnold
# - Copy your 3Delight installation to 3rdParty/3delight
#
# > Note : It is _not_ sufficient to use symlinks, as these will
# > not be followed when copying files into the docker container.
#
# Run the build :
#
# `docker build -t gaffer-dependencies .`
#
# Extract the result :
#
# ```
# container=`docker create gaffer-dependencies`
# docker cp $container:/gafferDependencies-0.44.0.0-linux.tar.gz ./
# docker rm $container
# ```

# We start with an ancient OS, so our builds are very
# permissive in terms of their glibc requirements
# when deployed elsewhere.

FROM centos:6

# Make GCC 6.3.1 the default compiler, as per VFXPlatform 2018

RUN yum install -y centos-release-scl
RUN yum install -y devtoolset-6

# Install CMake, SCons, and other miscellaneous build tools.

RUN yum install -y epel-release
RUN yum install -y cmake3
RUN ln -s /usr/bin/cmake3 /usr/bin/cmake

RUN yum install -y scons
RUN yum install -y patch
RUN yum install -y doxygen

# Install boost dependencies (needed by boost::iostreams)

RUN yum install -y bzip2-devel

# Install JPEG dependencies

RUN yum install -y nasm

# Install PNG dependencies

RUN yum install -y zlib-devel

# Install GLEW dependencies

RUN yum install -y libX11-devel
RUN yum install -y mesa-libGL-devel
RUN yum install -y mesa-libGLU-devel
RUN yum install -y libXmu-devel
RUN yum install -y libXi-devel

# Install OSL dependencies

RUN yum install -y flex
RUN yum install -y bison

# Install Qt dependencies

RUN yum install -y xkeyboard-config.noarch
RUN yum install -y fontconfig-devel.x86_64

# Install packages needed to generate the
# Gaffer documentation. Note that we are
# limited to Sphinx 1.4 because recommonmark
# is incompatible with later versions.

RUN yum install -y python27-python-pip.noarch
RUN scl enable python27 -- bash -c 'pip install sphinx==1.4 sphinx_rtd_theme recommonmark'

#COPY . /gafferDependenciesSource

# Build!

#ENV ARNOLD_ROOT /gafferDependenciesSource/3rdParty/arnold
#ENV RMAN_ROOT /gafferDependenciesSource/3rdParty/3delight
#ENV BUILD_DIR /gafferDependenciesBuild

#WORKDIR /gafferDependenciesSource

#RUN ./build/buildAll.sh
#ENV PATH /opt/rh/devtoolset-6/root/usr/bin:$PATH
