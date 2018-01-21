#
# spec file for package naviserver nsdbilite module
#

Summary:        NaviServer nsdbilite module
Name:           naviserver-mod_nsdbilite
Version:        0.2
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsdbilite
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
BuildRequires:  naviserver-mod_nsdbi
BuildRequires:  naviserver-mod_nsdbi-devel
BuildRequires:  sqlite3-devel
Requires:       naviserver-mod_nsdbi
Requires:       naviserver
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the nsdbilite database driver. It connects a SQLite database
to a NaviServer web server using the nsdbi interface.

%prep
%setup -q %{name}-%{version}

%build
make NAVISERVER=/var/lib/naviserver

%install
mkdir -p %buildroot/var/lib/naviserver/bin
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%post -n naviserver-mod_nsdbilite
/sbin/ldconfig

%postun -n naviserver-mod_nsdbilite
/sbin/ldconfig

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/bin/nsdbilite.so

%changelog

