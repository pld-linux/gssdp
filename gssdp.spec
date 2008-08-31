Summary:	SSDP library
Summary(pl.UTF-8):	Biblioteka SSDP
Name:		gssdp
Version:	0.6.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.gupnp.org/sources/gssdp/%{name}-%{version}.tar.gz
# Source0-md5:	aac3f73343a82db7a9acd5233ab32719
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.9.1
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSSDP implements resource discovery and announcement over SSDP.

%description -l pl.UTF-8
GSSDP implementuje wykrywanie i rozgłaszanie zasobów przy użyciu SSDP.

%package devel
Summary:	Header files for gssdp
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gssdp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.9.1
Requires:	libsoup-devel >= 2.2.97

%description devel
This package contains header files for gssdp.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki gssdp.

%package static
Summary:	Static gssdp libraries
Summary(pl.UTF-8):	Statyczna biblioteka gssdp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gssdp libraries.

%description static -l pl.UTF-8
Statyczna biblioteka gssdp.

%package apidocs
Summary:	gssdp API documentation
Summary(pl.UTF-8):	Dokumentacja API gssdp
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gssdp API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gssdp.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gssdp-device-sniffer
%attr(755,root,root) %{_libdir}/libgssdp-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgssdp-1.0.so.1
%dir %{_datadir}/gssdp
%{_datadir}/gssdp/gssdp-device-sniffer.glade

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssdp-1.0.so
%{_libdir}/libgssdp-1.0.la
%{_includedir}/gssdp-1.0
%{_pkgconfigdir}/gssdp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssdp-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gssdp
