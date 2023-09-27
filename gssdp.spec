#
# Conditional build:
%bcond_without	apidocs	# gi-docgen based API documentation
%bcond_without	vala	# Vala bindings
%bcond_with	sniffer	# sniffer package (GUI)

Summary:	GObject-based SSDP (Simple Service Discovery Protocol) library
Summary(pl.UTF-8):	Biblioteka SSDP (Simple Service Discovery Protocol) oparta na GObject
Name:		gssdp
# note: 1.4.x is stable libsoup 2.x based version; for libsoup3 based 1.6+ see gssdp1.6.spec
Version:	1.4.1
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gssdp/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	468514c096b6768a040e382de51fe85d
URL:		https://wiki.gnome.org/Projects/GUPnP
BuildRequires:	docbook-dtd412-xml
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	glib2-devel >= 1:2.54
BuildRequires:	gobject-introspection-devel >= 1.36.0
%{?with_sniffer:BuildRequires:	gtk4-devel >= 4}
BuildRequires:	libsoup-devel >= 2.26.1
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.029
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.20}
BuildRequires:	xz
Requires:	glib2 >= 1:2.54
Requires:	libsoup >= 2.26.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSSDP is a GObject-based API that implements resource discovery and
announcement over SSDP (Simple Service Discovery Protocol).

%description -l pl.UTF-8
GSSDP to oparte na bibliotece GObject API implementujące wykrywanie i
rozgłaszanie zasobów przy użyciu protokołu SSDP (Simple Service
Discovery Protocol).

%package sniffer
Summary:	Graphical SSDP sniffer
Summary(pl.UTF-8):	Graficzny sniffer SSDP
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	gtk4 >= 4

%description sniffer
Graphical SSDP sniffer.

%description sniffer -l pl.UTF-8
Graficzny sniffer SSDP.

%package devel
Summary:	Header files for GSSDP
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GSSDP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.54
Requires:	libsoup-devel >= 2.26.1

%description devel
This package contains header files for GSSDP library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki GSSDP.

%package static
Summary:	Static GSSDP library
Summary(pl.UTF-8):	Statyczna biblioteka GSSDP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GSSDP library.

%description static -l pl.UTF-8
Statyczna biblioteka GSSDP.

%package apidocs
Summary:	GSSDP API documentation
Summary(pl.UTF-8):	Dokumentacja API GSSDP
Group:		Documentation
BuildArch:	noarch

%description apidocs
GSSDP API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GSSDP.

%package -n vala-gssdp
Summary:	Vala binding for GSSDP library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GSSDP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.20
BuildArch:	noarch

%description -n vala-gssdp
Vala binding for GSSDP library.

%description -n vala-gssdp -l pl.UTF-8
Wiązanie języka Vala do biblioteki GSSDP.

%prep
%setup -q

%build
%meson build \
	%{?with_apidocs:-Dgtk_doc=true} \
	%{!?with_sniffer:-Dsniffer=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/gssdp-1.2 $RPM_BUILD_ROOT%{_gidocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/libgssdp-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgssdp-1.2.so.0
%{_libdir}/girepository-1.0/GSSDP-1.2.typelib

%if %{with sniffer}
%files sniffer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gssdp-device-sniffer
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssdp-1.2.so
%{_datadir}/gir-1.0/GSSDP-1.2.gir
%{_includedir}/gssdp-1.2
%{_pkgconfigdir}/gssdp-1.2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssdp-1.2.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/gssdp-1.2
%endif

%if %{with vala}
%files -n vala-gssdp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gssdp-1.2.deps
%{_datadir}/vala/vapi/gssdp-1.2.vapi
%endif
