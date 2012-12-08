Summary:	Userland scripts to control "laptop mode"
Name:		laptop-mode-tools
Version:	1.57
%define subrel 1
Release:	%mkrel 5
Source0:	http://www.samwel.tk/laptop_mode/tools/downloads/%{name}_%{version}.tar.gz
Patch1:		laptop-mode-tools-1.11-lsb.patch
Patch2:		fix-kernel-release-detection.patch
Patch3:		brcmsmac-has-no-power-management-support.patch
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.samwel.tk/laptop_mode/laptop_mode
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%patch2 -p1
%patch3 -p1

%install
rm -rf %{buildroot}

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/modules
%{_datadir}/%{name}/modules/*
%{_datadir}/%{name}/module-helpers/*
%{_mandir}/man8/*


%changelog
* Wed Oct 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.57-3.1
- built for updates

* Fri Sep 09 2011 Franck Bui <franck.bui@mandriva.com> 1.57-3mdv2011.0
+ Revision: 699152
- brcmsmac has no power management support
- Don't be fooled by 3.x kernel releases
- Update to 1.57

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.55-2
+ Revision: 666059
- mass rebuild

  + Shlomi Fish <shlomif@mandriva.org>
    - Type: add a missing dot.

* Sun Jul 11 2010 Emmanuel Andry <eandry@mandriva.org> 1.55-1mdv2011.0
+ Revision: 550746
- New version 1.55

* Mon Mar 22 2010 Emmanuel Andry <eandry@mandriva.org> 1.54-1mdv2010.1
+ Revision: 526613
- New version 1.54

* Sun Jan 03 2010 Frederik Himpe <fhimpe@mandriva.org> 1.53-1mdv2010.1
+ Revision: 485866
- update to new version 1.53

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.52-1mdv2010.1
+ Revision: 462190
- update to new version 1.52

* Tue Sep 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.51-1mdv2010.0
+ Revision: 423712
- update to new version 1.51

* Mon Jul 27 2009 Frederik Himpe <fhimpe@mandriva.org> 1.50-1mdv2010.0
+ Revision: 400835
- Update to new version 1.50

* Wed Jun 10 2009 Frederik Himpe <fhimpe@mandriva.org> 1.49-1mdv2010.0
+ Revision: 384903
- update to new version 1.49

* Thu Feb 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.47-1mdv2009.1
+ Revision: 339857
- Update to new version 1.47

* Mon Jan 26 2009 Emmanuel Andry <eandry@mandriva.org> 1.46-1mdv2009.1
+ Revision: 333805
- New version 1.46
- update files list

* Fri Aug 29 2008 Olivier Blin <blino@mandriva.org> 1.45-2mdv2009.0
+ Revision: 277278
- package modules so that laptop-mode-tools work again (broken as of 1.40 release, #43286)
- package pmu scripts
- use upstream install script

* Tue Jul 15 2008 Frederik Himpe <fhimpe@mandriva.org> 1.45-1mdv2009.0
+ Revision: 236162
- update to new version 1.45

* Mon Jun 23 2008 Frederik Himpe <fhimpe@mandriva.org> 1.43-1mdv2009.0
+ Revision: 228393
- New version 1.43

* Mon May 12 2008 Frederik Himpe <fhimpe@mandriva.org> 1.42-1mdv2009.0
+ Revision: 206234
- New version

* Wed Apr 23 2008 Frederik Himpe <fhimpe@mandriva.org> 1.41-1mdv2009.0
+ Revision: 196987
- New version
- Fix license

* Tue Mar 25 2008 Olivier Blin <blino@mandriva.org> 1.36-3mdv2008.1
+ Revision: 189843
- make sure acpid action scripts are executable

* Mon Mar 03 2008 Olivier Blin <blino@mandriva.org> 1.36-2mdv2008.1
+ Revision: 177933
- rebuild to fix changelog

* Mon Mar 03 2008 Olivier Blin <blino@mandriva.org> 1.36-1mdv2008.1
+ Revision: 177873
- 1.36 (defaults to ondemand on AC power)

* Tue Feb 12 2008 Olivier Blin <blino@mandriva.org> 1.35-2mdv2008.1
+ Revision: 166315
- do not require obsolete acpi service in initscript
- update URL

* Fri Jan 04 2008 Olivier Blin <blino@mandriva.org> 1.35-1mdv2008.1
+ Revision: 144950
- remove unapplied HD_IDLE_TIMEOUT settings from spec
- 1.35
- remove LSB echo patch (fixed upstream)
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.32-2mdv2008.1
+ Revision: 128328
- kill re-definition of %%buildroot on Pixel's request


* Wed Feb 21 2007 Frederic Crozat <fcrozat@mandriva.com> 1.32-2mdv2007.0
+ Revision: 123991
- Patch2: revert initscript to 1.31 (don't use unexisting lsb function)
- Fix url

* Sun Dec 03 2006 Emmanuel Andry <eandry@mandriva.org> 1.32-1mdv2007.1
+ Revision: 90182
- New version 1.2
  bunzipped patches
  drop patch0
- Import laptop-mode-tools

* Fri Jun 23 2006 Austin Acton <austin@mandriva.org> 1.31-2mdv2007.0
- bump default spindown to 2 min

* Thu Apr 20 2006 Austin Acton <austin@mandriva.org> 1.31-1mdk
- New release 1.31

* Thu Mar 23 2006 Austin Acton <austin@mandriva.org> 1.30-3mdk
- requires hdparm and sdparm

* Thu Mar 02 2006 Austin Acton <austin@mandriva.org> 1.30-2mdk
- add some missing files

* Thu Mar 02 2006 Austin Acton <austin@mandriva.org> 1.30-1mdk
- New release 1.30

* Wed Feb 22 2006 Austin Acton <austin@mandriva.org> 1.27-1mdk
- New release 1.27
- rediff patch0

* Sat Feb 11 2006 Austin Acton <austin@mandriva.org> 1.23-1mdk
- New release 1.23

* Thu Feb 02 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.22-2mdk
- add lm-profiler
- add apm events
- add man pages
- hrm, directories should probably rather be owned by suspend-scripts in stead..

* Thu Feb 02 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.22-1mdk
- 1.22
- %%mkrel
- regenerated P0
- own acpi dirs
- cosmetics

* Mon Jan 09 2006 Olivier Blin <oblin@mandriva.com> 1.11-2mdk
- Patch1: LSB support in init script (from Andrey Borzenkov, #20526)

* Sun Dec 04 2005 Austin Acton <austin@mandriva.org> 1.11-1mdk
- New release 1.11
- remove patch, added upstream

* Mon Aug 29 2005 Austin Acton <austin@mandriva.org> 1.10-2mdk
- add scaling_governor support

* Wed Aug 17 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.10-1mdk
- New release 1.10

* Sat Aug 13 2005 Frederic Lepied <flepied@mandriva.com> 1.09-2mdk
- provides acpi files
- call laptop_mode auto in reload|restart (bug #17454)

* Thu Aug 11 2005 Frederic Lepied <flepied@mandriva.com> 1.09-1mdk
- New release 1.09

* Fri Aug 05 2005 Frederic Lepied <flepied@mandriva.com> 1.08-1mdk
- initial packaging

