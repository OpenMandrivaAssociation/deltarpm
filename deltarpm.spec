Summary:	Tools to create and apply deltarpms
Name:		deltarpm
Version:	3.4
Release:	%mkrel 13
Source0:	ftp://ftp.suse.com/pub/projects/deltarpm/%{name}-%{version}.tar.bz2
Patch0:		deltarpm-3.4-mandir.patch
Patch1:		deltarpm-3.4-rpm5.patch
URL:		http://www.novell.com/products/linuxpackages/suselinux/deltarpm.html
License:	BSD
Group:		System/Configuration/Packaging
BuildRequires:	rpm >= 1:5.3
BuildRequires:	rpm-devel popt-devel zlib-devel bzip2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_usrlibrpm}
%makeinstall_std prefix="%{_prefix}" rpmdumpheader="%{_usrlibrpm}/rpmdumpheader"

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
%{_usrlibrpm}/rpmdumpheader


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.4-10mdv2011.0
+ Revision: 663762
- mass rebuild

* Sun Jan 09 2011 Funda Wang <fwang@mandriva.org> 3.4-9mdv2011.0
+ Revision: 630748
- %{_usrlibrpm} only exists in rpm > 5.3
- finally fix linkage
- fix link order

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - rpm5 rebuild for main/release

* Sun Dec 05 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.4-8mdv2011.0
+ Revision: 610658
- update rpm5 support & apply some misc build fixes/improvements..

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4-7mdv2011.0
+ Revision: 604783
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4-6mdv2010.1
+ Revision: 522450
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3.4-5mdv2010.0
+ Revision: 413346
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.4-4mdv2009.1
+ Revision: 348002
- rebuild for latest rpm
- rediff fuzzy patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new rpm

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 3.4-2mdv2009.0
+ Revision: 220579
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - add support for rpm5.org (P1)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 03 2007 Funda Wang <fwang@mandriva.org> 3.4-1mdv2008.1
+ Revision: 114565
- New version 3.4

* Sun Jun 10 2007 Olivier Thauvin <nanardon@mandriva.org> 3.3-4mdv2008.0
+ Revision: 37866
- add rpm includedir path to cflags, use it


* Thu Nov 30 2006 Thierry Vignaud <tvignaud@mandriva.com> 3.3-3mdv2007.0
+ Revision: 88831
- Import deltarpm

* Wed Nov 29 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.3-3mdv2007.1
- fix URL

* Wed Mar 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.3-2mdk
- Rebuild for rpm 4.4.5

* Thu Oct 13 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.3-1mdk
- 3.3

* Fri Aug 05 2005 Thierry Vignaud <tvignaud@mandriva.com> 2.3-2mdk
- fix description

* Fri Aug 05 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.3-1mdk
- 2.3

* Thu May 12 2005 Olivier Thauvin <nanardon@mandriva.org> 2.2-3mdk
- rebuild for rpm4.4

* Fri Apr 22 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.2-2mdk
- fix rdevs tag encoding (thanks michael)

* Fri Mar 18 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.2-1mdk
- 2.2
- add makdeltaiso tools
- mkdeltarpm is obsoleted by makedeltarpm

* Sun Jan 23 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-3mdk
- make mkdeltarpm generate .seq files so that we can simply check with
  applydeltarpm -c -s for a possible rpm reconstruction

* Mon Jan 10 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-2mdk
- add support for gzip'ed rpm
- add mkdeltarpm helper script

* Thu Jan 06 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-1mdk
- First Mandrakelinux package

