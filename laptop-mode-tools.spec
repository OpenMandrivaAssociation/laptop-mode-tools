Summary:	Userland scripts to control "laptop mode"
Name:		laptop-mode-tools
Version:	1.60
Release:	%mkrel 1
Source0:	http://www.samwel.tk/laptop_mode/tools/downloads/%{name}_%{version}.tar.gz
Patch1:		laptop-mode-tools-1.11-lsb.patch
Patch3:		brcmsmac-has-no-power-management-support.patch
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.samwel.tk/laptop_mode/laptop_mode
Conflicts:	suspend-scripts < 1.9.2
Requires:	hdparm
Requires:	sdparm
Requires(post):	rpm-helper
Requires(preun):rpm-helper
BuildArch:	noarch

%description
Userland scripts to control "laptop mode". Laptop mode is a Linux
kernel feature that allows your laptop to save considerable power, by
allowing the hard drive to spin down for longer periods of time. This
package contains the userland scripts that are needed to enable laptop
mode.

%prep
%setup -q -n %{name}_%{version}
%patch1 -p1 -b .lsb
%patch3 -p1

%install
#not created during install
mkdir -p %{buildroot}%{_sysconfdir}/pm/sleep.d

DESTDIR=%{buildroot} \
INIT_D=%{buildroot}%{_initrddir} \
MAN_D=%{_mandir} \
INSTALL="install" \
  ./install.sh

%post
%_post_service laptop-mode

%preun
%_preun_service laptop-mode

%files
%doc README
%{_sbindir}/*
%{_prefix}/lib/pm-utils/sleep.d/01laptop-mode
%dir %{_sysconfdir}/laptop-mode
%{_sysconfdir}/laptop-mode/*-start
%{_sysconfdir}/laptop-mode/*-stop
%dir %{_sysconfdir}/laptop-mode/*.d
%config(noreplace) %{_sysconfdir}/laptop-mode/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/laptop-mode/*.conf
%config(noreplace) %{_sysconfdir}/acpi/events/*
%attr(755,root,root) %{_sysconfdir}/acpi/actions/*
%{_sysconfdir}/udev/rules.d/99-laptop-mode.rules
%{_sysconfdir}/power/event.d/laptop-mode
%{_sysconfdir}/power/scripts.d/laptop-mode
%{_sysconfdir}/apm
%{_sysconfdir}/pm
%{_initrddir}/*
/lib/udev/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/module-helpers
%{_datadir}/%{name}/modules/*
%{_datadir}/%{name}/module-helpers/*
%{_mandir}/man8/*
