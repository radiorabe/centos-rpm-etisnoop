# centos-rpm-etisnoop
CentOS 7 RPM Specfile for [Opendigitalradio's ETISnoop](https://github.com/Opendigitalradio/etisnoop) which is part of [RaBe's DAB / DAB+ broadcasting package collection](https://build.opensuse.org/project/show/home:radiorabe:dab).

## Usage
There are pre-built binary packages for CentOS 7 available on [Radio RaBe's OBS DAB / DAB+ broadcasting package repository](https://build.opensuse.org/project/show/home:radiorabe:dab), which can be installed as follows:

```bash
curl -o /etc/yum.repos.d/home:radiorabe:dab.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/dab/CentOS_7/home:radiorabe:dab.repo
     
yum install etisnoop
```

## CentOS 7 Support

The 2.1.0 version of etisnoop requires a modern compiler to build. CentOS 7
does not provide such a GCC out of the box. You can work around this by
installing a modern version from SCL, but this is not supported on OBS hence
we do not currently provide binaries for CentOS 7.

```bash
# install modern toolchain on CentOS 7
yum install -y centos-release-scl
yum install -y devtoolset-9

# enter shell with modern toolkin on path
scl enable devtoolset-6 bash

# build RPM the usual way:
rpmbuild -ba etisnoop.spec
```

If you want to use a prebuilt version of etisnoop, there is a package available
for Fedora and we recommend you use that instead.
