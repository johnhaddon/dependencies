# Start with an ancient OS, so our builds are very
# permissive in terms of their glibc requirements
# when deployed elsewhere.

FROM centos:6

# Make GCC 6.3.1 the default compiler, as per VFXPlatform 2018

RUN yum install centos-release-scl -y
RUN yum install devtoolset-6 -y
RUN scl enable devtoolset-6 bash

# So we can build stuff

RUN yum install epel-release -y
RUN yum install cmake3 -y
RUN ln -s /usr/bin/cmake3 /usr/bin/cmake

RUN yum install scons -y

# Needed by boost::iostreams

RUN yum install bzip2-devel -y

# Needed to build libjpeg

RUN yum install nasm -y

# Needed for png

RUN yum install zlib-devel -y

# Needed for GLEW

RUN yum install libX11-devel -y
RUN yum install mesa-libGL-devel -y
RUN yum install mesa-libGLU-devel -y
RUN yum install libXmu-devel -y
RUN yum install libXi-devel -y

# Needed for OCIO

RUN yum install patch -y

# Needed by various things probably

RUN yum install doxygen -y

# Needed by OSL

RUN yum install flex -y
RUN yum install bison -y

COPY . /gafferDependenciesSource

ENV ARNOLD_ROOT /gafferDependenciesSource/3rdParty/arnold
ENV RMAN_ROOT /gafferDependenciesSource/3rdParty/3delight
ENV BUILD_DIR /gafferDependenciesBuild

ENV PATH /opt/rh/devtoolset-6/root/usr/bin:$PATH

RUN ls
RUN ls /gafferDependenciesSource
RUN ls /gafferDependenciesSource/build

WORKDIR /gafferDependenciesSource

#RUN ./build/buildAll.sh
