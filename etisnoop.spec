#
# spec file for package etisnoop
#
# Copyright (c) 2016 - 2018 Radio Bern RaBe
#                           http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-etisnoop
#

Name:           etisnoop
Version:        2.1.0
Release:        1%{?dist}
Summary:        ETISnoop analyser

License:        GPLv3+
URL:            https://github.com/Opendigitalradio/%{name}
Source0:        https://github.com/Opendigitalradio/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  faad2-devel
BuildRequires:  gcc-c++


%description
The ETSnoop analyser decodes and prints out a RAW ETI file in a form that makes
analysis easier. It can show information about the signalling, details about
the FIGs, and extract a DAB+ subchannel into a fil

%prep
%setup -q


%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*


%changelog
* Sun Jan 16 2022 Lucas BIckel <hairmare@rabe.ch> - 2.1.0-1
- Bump to latest upstream version
- Remove outdated libfec-odr dependency

* Fri Jun 08 2018 Lucas Bickel <hairmare@rabe.ch> - 2.0.0-1
- Bump to latest upstream version

* Tue Oct 04 2016 Christian Affolter <c.affolter@purplehaze.ch> - 1.1.0-1
- Switched from Git master to official release, upstream is using autotools now

* Sat Aug 27 2016 Christian Affolter <c.affolter@purplehaze.ch> - master-1
- Initial release
