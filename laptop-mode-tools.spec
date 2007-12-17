Summary:	Userland scripts to control "laptop mode"
Name:		laptop-mode-tools
Version:	1.32
Release:	%mkrel 2

Source0:	http://www.samwel.tk/laptop_mode/tools/downloads/%{name}-%{version}.tar.bz2
#Patch0:		laptop-mode-tools-1.27-subsys.patch
Patch1:		laptop-mode-tools-1.11-lsb.patch
# (fc) 1.32-2mdv don't use unexisting echo lsb function (use 1.31 initscript)
Patch2:		laptop-mode-tools-1.32-nolsbecho.patch
License:	GPL
Group:		System/Kernel and hardware
Url:		http://www.samwel.tk/laptop_mode/index.html
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
#%patch0 -p1 -b .subsys
%patch1 -p1 -b .lsb
%patch2 -p1 -b .noecholsb
perl -pi -e 's|LM_AC_HD_IDLE_TIMEOUT_SECONDS=5|LM_AC_HD_IDLE_TIMEOUT_SECONDS=120||g' etc/laptop-mode/laptop-mode.conf
perl -pi -e 's|LM_BATT_HD_IDLE_TIMEOUT_SECONDS=5|LM_BATT_HD_IDLE_TIMEOUT_SECONDS=120||g' etc/laptop-mode/laptop-mode.conf

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
%dir %{_sysconfdir}/laptop-mode/*/
%config(noreplace) %{_sysconfdir}/laptop-mode/*.conf
%config(noreplace) %{_sysconfdir}/acpi/events/*
%{_sysconfdir}/acpi/actions/*
%{_sysconfdir}/apm
%{_initrddir}/*
%{_mandir}/man8/*


