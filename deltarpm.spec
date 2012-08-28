Summary: Create deltas between rpms
Name: deltarpm
Version: 3.6
Release: 0.1.20110223git
License: BSD
Group: System/Configuration/Packaging
URL: http://gitorious.org/deltarpm/deltarpm
# Generate source by doing:
# git clone git://gitorious.org/deltarpm/deltarpm
# cd deltarpm
# git archive --format=tar --prefix="deltarpm-git-20110223/" 7ed5208166 | \
#   bzip2 > deltarpm-git-20110223.tar.bz2
Source: %{name}-git-20110223.tar.bz2
Patch0: deltarpm-rpm5.patch
BuildRequires: bzip2-devel, lzma-devel, rpm-devel, popt-devel
BuildRequires: zlib-devel
%py_requires -d

%description
A deltarpm contains the difference between an old
and a new version of a rpm, which makes it possible
to recreate the new rpm from the deltarpm and the old
one. You don't have to have a copy of the old rpm,
deltarpms can also work with installed rpms.

%package -n drpmsync
Summary: Sync a file tree with deltarpms
Group: System/Configuration/Packaging
Requires: deltarpm = %{version}-%{release}

%description -n drpmsync
This package contains a tool to sync a file tree with
deltarpms.

%package -n deltaiso
Summary: Create deltas between isos containing rpms
Group: System/Configuration/Packaging
Requires: deltarpm = %{version}-%{release}

%description -n deltaiso
This package contains tools for creating and using deltasisos,
a difference between an old and a new iso containing rpms.

%package -n python-deltarpm
Summary: Python bindings for deltarpm
Group: System/Configuration/Packaging
Requires: deltarpm = %{version}-%{release}

%description -n python-deltarpm
This package contains python bindings for deltarpm.


%prep
%setup -q -n %{name}-git-20110223
%patch0 -p1

%build
%make -C zlib* CFLAGS="%{optflags} -O3" LDFLAGS="%{ldflags}" libz.a
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" \
    bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir} prefix=%{_prefix} \
    zlibbundled='' zlibldflags='-lz' zlibcppflags=''
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" \
    bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir} prefix=%{_prefix} \
    zlibbundled='' zlibldflags='-lz' zlibcppflags='' \
    python

%install
%{__rm} -rf %{buildroot}
%makeinstall pylibprefix=%{buildroot}

rm -rf %{buildroot}%{_libdir}/python3*

%files
%doc LICENSE.BSD README
%doc %{_mandir}/man8/applydeltarpm*
%doc %{_mandir}/man8/makedeltarpm*
%doc %{_mandir}/man8/combinedeltarpm*
%{_bindir}/applydeltarpm
%{_bindir}/combinedeltarpm
%{_bindir}/makedeltarpm
%{_bindir}/rpmdumpheader

%files -n deltaiso
%doc LICENSE.BSD README
%doc %{_mandir}/man8/applydeltaiso*
%doc %{_mandir}/man8/makedeltaiso*
%{_bindir}/applydeltaiso
%{_bindir}/fragiso
%{_bindir}/makedeltaiso

%files -n drpmsync
%doc LICENSE.BSD README
%doc %{_mandir}/man8/drpmsync*
%{_bindir}/drpmsync

%files -n python-deltarpm
%doc LICENSE.BSD
%{python_sitearch}/*
