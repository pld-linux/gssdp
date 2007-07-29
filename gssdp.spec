Summary:	SSDP library
Name:		gssdp
Version:	0.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.gupnp.org/sources/%{name}-%{version}.tar.gz
# Source0-md5:	fe7d83ecb4f67ea1db87b1e1d48d7622
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gtk-doc
BuildRequires:	libglade2-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSSDP implements resource discovery and announcement over SSDP.

%package devel
Summary:	Header files for gssdp
Summary(pl.UTF-8):	Pliki nagłówkowe gssdp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for gssdp.

%package static
Summary:	Static gssdp libraries
Summary(pl.UTF-8):	Statyczne biblioteki gssdp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gssdp libraries.

%description static -l pl.UTF-8
Statyczne biblioteki gssdp.

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
%attr(755,root,root)    %{_libdir}/libgssdp-1.0.so.0.0.0
%dir %{_datadir}/gssdp
%{_datadir}/gssdp/gssdp-device-sniffer.glade


%files devel
%defattr(644,root,root,755)
%{_includedir}/gssdp-1.0
%{_libdir}/libgssdp-1.0.la
%{_libdir}/libgssdp-1.0.so
%{_pkgconfigdir}/gssdp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssdp-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gssdp
