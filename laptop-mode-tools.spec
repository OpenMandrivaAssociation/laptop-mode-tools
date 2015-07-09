Summary:	Userland scripts to control "laptop mode"
Name:		laptop-mode-tools
Version:	1.67
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.samwel.tk/laptop_mode/laptop_mode
Source0:	http://samwel.tk/laptop_mode/tools/downloads/%{name}_%{version}.tar.gz
Patch3:		brcmsmac-has-no-power-management-support.patch
BuildArch:	noarch
Requires:	hdparm
Requires:	sdparm
Requires(post,postun):	rpm-helper

%description
Userland scripts to control "laptop mode". Laptop mode is a Linux
kernel feature that allows your laptop to save considerable power, by
allowing the hard drive to spin down for longer periods of time. This
package contains the userland scripts that are needed to enable laptop
mode.

%prep
%setup -qn %{name}_%{version}
%apply_patches

%install
#not created during install
mkdir -p %{buildroot}%{_sysconfdir}/pm/sleep.d

DESTDIR=%{buildroot} \
ULIB_D=%{_libdir} \
MAN_D=%{_mandir} \
INSTALL="install" \
  ./install.sh

# (tpg) not needed
rm -rf %{_initdir}/laptop-mode

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-laptop-mode.preset << EOF
enable laptop-mode.service
EOF

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
%{_presetdir}/86-laptop-mode.preset
%{_unitdir}/laptop-mode.service
%{_libdir}/pm-utils/sleep.d/01laptop-mode
%{_tmpfilesdir}/laptop-mode.conf
/lib/udev/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/module-helpers
%{_datadir}/%{name}/modules/*
%{_datadir}/%{name}/module-helpers/*
%{_mandir}/man8/*

