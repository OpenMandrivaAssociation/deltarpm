Summary:	Tools to create and apply deltarpms
Name:		deltarpm
Version:	3.6.1
Release:	1
License:	BSD
Group:		System/Configuration/Packaging
URL:		https://github.com/rpm-software-management/deltarpm
Source0:	https://codeload.github.com/rpm-software-management/deltarpm/%{name}-%{version}.tar.gz
Patch0:		deltarpm-3.4-mandir.patch
Patch1:		deltarpm-3.4-rpm5.patch
BuildRequires:	rpm >= 1:5.3
BuildRequires:	rpm-devel
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel

%description
This package contains tools to create and apply deltarpms. A deltarpm
contains the difference between an old and a new version of a rpm,
which makes it possible to recreate the new rpm from the deltarpm and
the old one. You don't have to have a copy of the old rpm, deltarpms
can also work with installed rpms.

Starting from version 2.2, there are also tools to handle ISO diffs.

%prep
%setup -q
%patch0 -p1 -b .mandir~
%patch1 -p1 -b .rpm5~

%build
# parallel build broken due to 'make' being called within Makefile, so build separately
%make -C zlib* CFLAGS="%{optflags} -O3" LDFLAGS="%{ldflags}" libz.a
%make prefix="%{_prefix}" rpmdumpheader="%{_usrlibrpm}/rpmdumpheader" CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}%{_usrlibrpm}
%makeinstall_std prefix="%{_prefix}" rpmdumpheader="%{_usrlibrpm}/rpmdumpheader"


%files
%doc README NEWS
%{_bindir}/makedelta*
%{_bindir}/applydelta*
%{_bindir}/drpmsync
%{_bindir}/fragiso
%{_bindir}/combinedeltarpm
%{_mandir}/man8/makedelta*.8*
%{_mandir}/man8/applydelta*.8*
%{_mandir}/man8/drpmsync.8*
%{_mandir}/man8/combinedeltarpm.8*
%{_usrlibrpm}/rpmdumpheader
