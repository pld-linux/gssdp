Summary:	GObject-based SSDP (Simple Service Discovery Protocol) library
Summary(pl.UTF-8):	Biblioteka SSDP (Simple Service Discovery Protocol) oparta na GObject
Name:		gssdp
# note: 0.12.x is stable, 0.13.x unstable
Version:	0.12.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	b7942485e82a181eb4f08ef172576d80
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libsoup-devel >= 2.26.1
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.22
Requires:	gtk+2 >= 2:2.12.0
Requires:	libsoup >= 2.26.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSSDP is a GObject-based API that implements resource discovery and
announcement over SSDP (Simple Service Discovery Protocol).

%description -l pl.UTF-8
GSSDP to oparte na bibliotece GObject API implementujące wykrywanie i
rozgłaszanie zasobów przy użyciu protokołu SSDP (Simple Service
Discovery Protocol).

%package devel
Summary:	Header files for GSSDP
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GSSDP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.22
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
Requires:	gtk-doc-common

%description apidocs
GSSDP API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GSSDP.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gssdp-device-sniffer
%attr(755,root,root) %{_libdir}/libgssdp-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgssdp-1.0.so.3
%{_libdir}/girepository-1.0/GSSDP-1.0.typelib
%{_datadir}/gssdp

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssdp-1.0.so
%{_datadir}/gir-1.0/GSSDP-1.0.gir
%{_includedir}/gssdp-1.0
%{_pkgconfigdir}/gssdp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssdp-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gssdp
