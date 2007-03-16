Summary:	Themeable window decorator and compositing manager for beryl
Summary(pl.UTF-8):	Dekorator okien dla beryla używający motywów
Name:		heliodor
Version:	0.2.0
Release:	1
License:	LGPL v2+
Group:		Themes
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ccbcdab0a90e4d5250cc2d58faeadd17
URL:		http://beryl-project.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	control-center-devel >= 2.0
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libwnck-devel >= 2.0
BuildRequires:	metacity-devel >= 2.15.21
BuildRequires:	pango-devel >= 1.10.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	beryl-core >= 1:%{version}
Requires:	control-center >= 2.0
Requires:	gtk+2 >= 2:2.8.0
Requires:	metacity >= 2.15.21
Obsoletes:	compiz-quinnstorm-gnome-decorator
Obsoletes:	compiz-quinnstorm-gnome-settings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heliodor is themeable window decorator and compositing manager for
beryl. Heliodor is intended for use with GNOME.

%description -l pl.UTF-8
Heliodor jest dekoratorem okien dla beryla używającym motywów. Jest
przeznaczony do używania wraz z GNOME.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopfilesdir=%{_datadir}/wm-properties

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/heliodor
%attr(755,root,root) %{_libdir}/window-manager-settings/libberyl.so
