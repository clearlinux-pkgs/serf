#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : serf
Version  : 1.3.9
Release  : 3
URL      : https://www.apache.org/dist/serf/serf-1.3.9.tar.bz2
Source0  : https://www.apache.org/dist/serf/serf-1.3.9.tar.bz2
Summary  : HTTP client library
Group    : Development/Tools
License  : Apache-2.0
Requires: serf-lib
BuildRequires : apr-dev
BuildRequires : apr-util-dev
BuildRequires : expat-dev
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)

BuildRequires : scons
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
Requires: serf-lib
Provides: serf-devel

%description dev
dev components for the serf package.


%package lib
Summary: lib components for the serf package.
Group: Libraries

%description lib
lib components for the serf package.


%prep
%setup -q -n serf-1.3.9
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
scons %{?_smp_mflags}  PREFIX=/usr LIBDIR=/usr/lib64

%install
scons install --install-sandbox=%{buildroot}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/serf-1/serf.h
/usr/include/serf-1/serf_bucket_types.h
/usr/include/serf-1/serf_bucket_util.h
/usr/lib64/*.a
/usr/lib64/libserf-1.so
/usr/lib64/pkgconfig/serf-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libserf-1.so.1
/usr/lib64/libserf-1.so.1.3.0
