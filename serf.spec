#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC4A6C625CCC8E1DF (bert@vmoo.com)
#
Name     : serf
Version  : 1.3.9
Release  : 12
URL      : https://www.apache.org/dist/serf/serf-1.3.9.tar.bz2
Source0  : https://www.apache.org/dist/serf/serf-1.3.9.tar.bz2
Source1  : https://www.apache.org/dist/serf/serf-1.3.9.tar.bz2.asc
Summary  : HTTP client library
Group    : Development/Tools
License  : Apache-2.0
Requires: serf-lib = %{version}-%{release}
Requires: serf-license = %{version}-%{release}
BuildRequires : apr-dev
BuildRequires : apr-util-dev
BuildRequires : buildreq-scons
BuildRequires : expat-dev
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
BuildRequires : util-linux-dev
BuildRequires : zlib-dev
Patch1: sconscript-python3.patch

%description
Welcome to Apache Serf, a high-performance asynchronous HTTP client library.
The Apache Serf library is a C-based HTTP client library built upon the Apache
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%package dev
Summary: dev components for the serf package.
Group: Development
Requires: serf-lib = %{version}-%{release}
Provides: serf-devel = %{version}-%{release}
Requires: serf = %{version}-%{release}

%description dev
dev components for the serf package.


%package lib
Summary: lib components for the serf package.
Group: Libraries
Requires: serf-license = %{version}-%{release}

%description lib
lib components for the serf package.


%package license
Summary: license components for the serf package.
Group: Default

%description license
license components for the serf package.


%package staticdev
Summary: staticdev components for the serf package.
Group: Default
Requires: serf-dev = %{version}-%{release}

%description staticdev
staticdev components for the serf package.


%prep
%setup -q -n serf-1.3.9
cd %{_builddir}/serf-1.3.9
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
scons %{?_smp_mflags}  PREFIX=/usr LIBDIR=/usr/lib64

%install
scons install --install-sandbox=%{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/serf
cp %{_builddir}/serf-1.3.9/LICENSE %{buildroot}/usr/share/package-licenses/serf/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/serf-1.3.9/NOTICE %{buildroot}/usr/share/package-licenses/serf/17499e4ea127286a863710db5d60e1916f5fa651

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/serf-1/serf.h
/usr/include/serf-1/serf_bucket_types.h
/usr/include/serf-1/serf_bucket_util.h
/usr/lib64/libserf-1.so
/usr/lib64/pkgconfig/serf-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libserf-1.so.1
/usr/lib64/libserf-1.so.1.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/serf/17499e4ea127286a863710db5d60e1916f5fa651
/usr/share/package-licenses/serf/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libserf-1.a
