%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:		check
Version:	0.9.8
Release:	4
License:	LGPLv2+
Summary:	A unit test framework for C
Group:		System/Libraries
URL:		http://check.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/check/%{name}-%{version}.tar.gz

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals.  The output from
unit tests can be used within source code editors and IDEs.

%package -n	%{libname}
Summary:	C testing framework
Group:		System/Libraries

%description -n	%{libname}
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals. The output from
unit tests can be used within source code editors and IDEs.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}
Obsoletes:	%mklibname -d %{name} 0

%description -n	%{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

# move documentation
mv %{buildroot}%{_datadir}/doc/%{name} \
    %{buildroot}%{_datadir}/doc/%{develname}-%{version}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_datadir}/doc/%{develname}-%{version}
%{_datadir}/aclocal/check.m4
%{_libdir}/libcheck.so
%{_libdir}/libcheck.a
%{_includedir}/check.h
%{_libdir}/pkgconfig/check.pc
%{_infodir}/check.info*




%changelog
* Thu Jun 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9.8-4
+ Revision: 805562
- Drop some legacy junk

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-3
+ Revision: 663367
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-2mdv2011.0
+ Revision: 603825
- rebuild

* Thu Jan 14 2010 Emmanuel Andry <eandry@mandriva.org> 0.9.8-1mdv2010.1
+ Revision: 491461
- New version 0.9.8

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-3mdv2010.0
+ Revision: 413231
- rebuild

* Tue Mar 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.6-2mdv2009.1
+ Revision: 353409
- fix devel provides

* Sat Mar 07 2009 Emmanuel Andry <eandry@mandriva.org> 0.9.6-1mdv2009.1
+ Revision: 351734
- New version 0.9.6
- fix licence
- apply libraries policy
- use configure2_5x
- protect major

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.9.5-4mdv2009.0
+ Revision: 220554
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.9.5-3mdv2008.1
+ Revision: 123104
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode bz2 extension


* Thu Feb 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.5-3mdv2007.0
+ Revision: 115812
- add conflict with old devel package

* Mon Jan 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-2mdv2007.1
+ Revision: 114908
- fix dependency

* Fri Jan 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.5-1mdv2007.1
+ Revision: 113846
- new version

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.3-2mdv2007.0
- patch to build dynamic libraries

* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.3-1mdk
- New release 0.9.3
- %%mkrel

* Thu Jul 14 2005 Herton Ronaldo Krzesinski <herton@mandriva.com> 0.9.2-1mdk
- Adopted package for Mandriva Linux.

* Thu Feb 03 2005 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2005-02-03 12:00:24 (75515)
- %%desc cleanup.

* Mon Dec 20 2004 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2004-12-20 17:19:58 (73041)
- Oops.. forgot to include the source.

* Mon Dec 20 2004 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2004-12-20 17:18:43 (73037)
- New upstream Version: 0.9.3
- The update was done to check if the new version included suite_free(),
  but it looks that this function was removed rather than recently added.
  Anyway, the update was done, so let's make it available.

* Mon Nov 08 2004 André Murbach Maidl <murbach@conectiva.com.br>
+ 2004-11-08 15:37:03 (70833)
- Added %%doc macro

* Mon Nov 08 2004 André Murbach Maidl <murbach@conectiva.com.br>
+ 2004-11-08 11:16:48 (70791)
- Created spec file (Closes #13149)
  Added the package source

* Mon Nov 08 2004 André Murbach Maidl <murbach@conectiva.com.br>
+ 2004-11-08 10:52:30 (70775)
- Created package structure for check.

