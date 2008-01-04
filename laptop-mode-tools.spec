Summary:	Userland scripts to control "laptop mode"
Name:		laptop-mode-tools
Version:	1.35
Release:	%mkrel 1

Source0:	http://www.samwel.tk/laptop_mode/tools/downloads/%{name}_%{version}.tar.gz
Patch1:		laptop-mode-tools-1.11-lsb.patch
License:	GPL
Group:		System/Kernel and hardware
Url:		http://www.samwel.tk/laptop_mode/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	suspend-scripts < 1.9.2
Requires:	hdparm sdparm
Requires(post):	rpm-helper
Requires(preun):rpm-helper
BuildArch:	noarch

%description
Userland scripts to control "laptop mode" Laptop mode is a Linux
kernel feature that allows your laptop to save considerable power, by
allowing the hard drive to spin down for longer periods of time. This
package contains the userland scripts that are needed to enable laptop
mode.

%prep
%setup -q
%patch1 -p1 -b .lsb

%install
rm -rf $RPM_BUILD_ROOT
install -m755 usr/sbin/laptop_mode -D $RPM_BUILD_ROOT%{_sbindir}/laptop_mode
cp usr/sbin/lm* $RPM_BUILD_ROOT/%{_sbindir}
install -m755 etc/init.d/laptop-mode -D $RPM_BUILD_ROOT%{_initrddir}/laptop-mode
mkdir -p $RPM_BUILD_ROOT%{_mandir}
cp -r man $RPM_BUILD_ROOT%{_mandir}/man8
cp -r etc/laptop-mode $RPM_BUILD_ROOT%{_sysconfdir}
cp -r etc/acpi $RPM_BUILD_ROOT%{_sysconfdir}
cp -r etc/apm $RPM_BUILD_ROOT%{_sysconfdir}

%post
%_post_service laptop-mode

%preun
%_preun_service laptop-mode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/*
%dir %{_sysconfdir}/laptop-mode
%{_sysconfdir}/laptop-mode/*-start
%{_sysconfdir}/laptop-mode/*-stop
%dir %{_sysconfdir}/laptop-mode/*.d
%config(noreplace) %{_sysconfdir}/laptop-mode/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/laptop-mode/*.conf
%config(noreplace) %{_sysconfdir}/acpi/events/*
%{_sysconfdir}/acpi/actions/*
%{_sysconfdir}/apm
%{_initrddir}/*
%{_mandir}/man8/*


