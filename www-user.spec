Name: www-user
Version: 1.0
Release: 1
Source0: www.sysusers
Summary: The www user account, shared by various web servers
URL: https://openmandriva.org/
License: GPL
Group: Servers
BuildRequires: systemd-rpm-macros

%description
The www user account, shared by various web servers

%prep

%build

%install
install -p -D -m 0644 %{S:0} %{buildroot}%{_sysusersdir}/www.conf
mkdir -p %{buildroot}/srv/www

%pre
%sysusers_create_package www %{S:0}

%files
%{_sysusersdir}/www.conf
/srv/www
