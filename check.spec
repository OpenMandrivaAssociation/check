%define name	check
%define version	0.9.5
%define release	%mkrel 4
%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	libname2007 %mklibname %{name} 0.9.3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Summary:	A unit test framework for C
Group:		System/Libraries
URL:		http://check.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/check/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%package -n	%{libname}-devel 
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires(post): info-install
Requires(preun):info-install
Obsoletes:	%{name}
Conflicts: %libname2007-devel

%description -n	%{libname}-devel
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

# move documentation
mv %{buildroot}%{_datadir}/doc/%{name} \
    %{buildroot}%{_datadir}/doc/%{libname}-devel-%{version}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{libname}-devel
%_install_info %{name}.info

%postun -n %{libname}-devel
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_datadir}/doc/%{libname}-devel-%{version}
%{_datadir}/aclocal/check.m4
%{_libdir}/libcheck.la
%{_libdir}/libcheck.so
%{_libdir}/libcheck.a
%{_includedir}/check.h
%{_libdir}/pkgconfig/check.pc
%{_infodir}/check.info*


