%undefine _debugsource_packages

Summary:	Tools to create and apply deltarpms
Name:		deltarpm
Version:	3.6.3
Release:	4
License:	BSD
Group:		System/Configuration/Packaging
URL:		https://github.com/rpm-software-management/deltarpm
Source0:	https://github.com/rpm-software-management/deltarpm/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	rpm >= 4.14.0
BuildRequires:	pkgconfig(rpm) >= 4.14.0
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libzstd)

%description
This package contains tools to create and apply deltarpms. A deltarpm
contains the difference between an old and a new version of a rpm,
which makes it possible to recreate the new rpm from the deltarpm and
the old one. You don't have to have a copy of the old rpm, deltarpms
can also work with installed rpms.

Starting from version 2.2, there are also tools to handle ISO diffs.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build CC=%{__cc} rpmdumpheader="%{_libdir}/rpm/rpmdumpheader" prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
mkdir -p %{buildroot}%{_libdir}/rpm
%make_install rpmdumpheader="%{_libdir}/rpm/rpmdumpheader" DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

# Drop drpmsync as we can't use it (missing perl deps)
find %{buildroot} -name "drpmsync*" -delete

%files
%doc README NEWS
%{_bindir}/*
%doc %{_mandir}/man8/*
%{_libdir}/rpm/rpmdumpheader
