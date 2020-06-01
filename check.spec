# check is used by pulseaudio, pulseaudio is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define __requires_exclude '.*/bin/awk|.*/bin/gawk'

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define lib32name %mklib32name %{name} %{major}
%define dev32name %mklib32name %{name} -d

%define _disable_rebuild_configure 1

Summary:	A unit test framework for C
Name:		check
Version:	0.14.0
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		https://libcheck.github.io/check/
Source0:	https://github.com/libcheck/check/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	texinfo
BuildRequires:	graphviz

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals.  The output from
unit tests can be used within source code editors and IDEs.

%package -n %{libname}
Summary:	C testing framework
Group:		System/Libraries

%description -n %{libname}
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals. The output from
unit tests can be used within source code editors and IDEs.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	C testing framework (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals. The output from
unit tests can be used within source code editors and IDEs.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}
Requires:	%{lib32name} = %{version}

%description -n %{dev32name}
This package contains development files for %{name}.
%endif

%prep
%setup -q
autoreconf -fiv
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libcheck.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libcheck.so
%{_prefix}/lib/pkgconfig/check.pc
%endif
