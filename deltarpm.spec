Summary:	Tools to create and apply deltarpms
Name:		deltarpm
Version:	3.6.1
Release:	1
License:	BSD
Group:		System/Configuration/Packaging
URL:		https://github.com/rpm-software-management/deltarpm
Source0:	https://codeload.github.com/rpm-software-management/deltarpm/%{name}-%{version}.tar.gz
Patch0:		deltarpm-3.6.1-rpm5.patch
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
%apply_patches

%build
%setup_compile_flags
%make rpmdumpheader="%{_libdir}/rpm/rpmdumpheader" prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
mkdir -p %{buildroot}%{_libdir}/rpm
%makeinstall_std rpmdumpheader="%{_libdir}/rpm/rpmdumpheader" DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%files
%doc README NEWS
%{_bindir}/*
%{_mandir}/man8/*
%{_libdir}/rpm/rpmdumpheader
