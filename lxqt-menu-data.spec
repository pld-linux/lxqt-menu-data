Summary:	Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt
Summary(pl.UTF-8):	Pliki menu dla Panelu LXQt, Centrum Konfiguracji i PCManFM-Qt/libfm-qt
Name:		lxqt-menu-data
Version:	2.3.0
Release:	1
License:	LGPL-2.1-or-later
URL:		https://lxqt-project.org/
Source0:	https://github.com/lxqt/lxqt-menu-data/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	4f0181b7ce8db0682687a3686710fcdc
BuildRequires:	cmake >= 3.18.0
BuildRequires:	lxqt-build-tools
BuildRequires:	perl-base
BuildArch:	noarch

%description
Freedesktop.org compliant menu files for LXQt Panel, Configuration
Center and PCManFM-Qt/libfm-qt.

%description -l pl.UTF-8
Pliki menu zgodne ze standardem Freedesktop.org dla Panelu LXQt,
Centrum Konfiguracji i PCManFM-Qt/libfm-qt.

%prep
%setup -q

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%{_datadir}/cmake/lxqt-menu-data/
%{_datadir}/desktop-directories/lxqt-*.directory
%{_sysconfdir}/xdg/menus/lxqt-*.menu


%clean
rm -rf $RPM_BUILD_ROOT
