%define name	deltarpm
%define version	3.4
%define release	%mkrel 6
%define rpmdir	%{_prefix}/lib/rpm

Summary:	Tools to create and apply deltarpms
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.suse.com/pub/projects/deltarpm/%{name}-%{version}.tar.bz2
Patch0:		deltarpm-3.4-mandir.patch
Patch1:		deltarpm-3.4-rpm5.patch
URL: http://www.novell.com/products/linuxpackages/suselinux/deltarpm.html
License:	BSD
Group:		System/Configuration/Packaging
BuildRequires:	rpm-devel, popt-devel, zlib-devel, bzip2-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains tools to create and apply deltarpms. A deltarpm
contains the difference between an old and a new version of a rpm,
which makes it possible to recreate the new rpm from the deltarpm and
the old one. You don't have to have a copy of the old rpm, deltarpms
can also work with installed rpms.

Starting from version 2.2, there are also tools to handle ISO diffs.

%prep
%setup -q
%patch0 -p1 -b .mandir
%patch1 -p1 -b .rpm5

%build
%make prefix="%{_prefix}" rpmdumpheader="%{rpmdir}/rpmdumpheader" CFLAGS="%optflags -I%_includedir/rpm"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{rpmdir}
%makeinstall_std prefix="%{_prefix}" rpmdumpheader="%{rpmdir}/rpmdumpheader"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
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
%{rpmdir}/rpmdumpheader
