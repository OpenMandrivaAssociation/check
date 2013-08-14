%define __noautoreq '.*/bin/awk|.*/bin/gawk'

%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	A unit test framework for C
Name:		check
Version:	0.9.10
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://check.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/check/%{name}-%{version}.tar.gz

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

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall

# move documentation
mv %{buildroot}%{_datadir}/doc/%{name} \
    %{buildroot}%{_datadir}/doc/%{devname}-%{version}

%files -n %{libname}
%{_libdir}/libcheck.so.%{major}*

%files -n %{devname}
%{_bindir}/checkmk
%{_datadir}/doc/%{devname}-%{version}
%{_datadir}/aclocal/check.m4
%{_libdir}/libcheck.so
%{_includedir}/check.h
%{_includedir}/check_stdint.h
%{_libdir}/pkgconfig/check.pc
%{_infodir}/check.info*
%{_mandir}/man1/checkmk.1*
