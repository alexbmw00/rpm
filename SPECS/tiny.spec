Summary: Tiny C HTTP Web Server
Name: tiny
Version: 0.1
Release: 2%{?dist}
Group: Applications/File
License: GPLv2+
Url: http://mama.indstate.edu/users/ice/tiny/
Source: ftp://mama.indstate.edu/linux/tiny/tiny-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Very simple HTTP server written in pure C

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS" "CPPFLAGS=$(getconf LFS_CFLAGS)" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/var/www/html
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system

make	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/tiny.1
cp index.html $RPM_BUILD_ROOT/var/www/html
cp sysconfig/tiny $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
cp system/tiny.service $RPM_BUILD_ROOT/lib/systemd/system

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/tiny
%{_mandir}/man1/tiny.1*
%{_sysconfdir}/sysconfig
/lib/systemd/system
/var/www/html
%doc README LICENSE

%changelog
* Wed Apr 22 2019 Hector Vio <hector.silva@4linux.com.br> 0.1
- Criado o RPM.
