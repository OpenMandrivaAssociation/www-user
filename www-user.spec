Name: www-user
Version: 2.0
Release: 1
Source0: www.sysusers
Summary: The www user account, shared by various web servers
URL: https://openmandriva.org/
License: GPL
Group: Servers
BuildRequires: rpm-build >= 4.19.0

%description
The www user account, shared by various web servers

%prep

%build

%install
install -p -D -m 0644 %{S:0} %{buildroot}%{_sysusersdir}/www.conf
mkdir -p %{buildroot}/srv/www

%files
%{_sysusersdir}/www.conf
/srv/www
