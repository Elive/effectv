Summary: effectv
Name: effectv
Version: 0.3.9
Release: 1
Group: User Interface/Desktops
License: GPL
Source0: http://prdownloads.sourceforge.net/effectv/%{name}-%{version}.tar.gz
Patch0: %{name}-%{version}.rpm-ps2.patch
NoSource: 0
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPreReq: SDL >= 1.2.3, SDL-devel >= 1.2.3, XFree86-devel >= 3.3.6, XFree86-libs >= 3.3.6

%description 
EffecTV is a real-time video effect processor. You can enjoy movies,
TV programs and any other video stream through the many amazing effects. 

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/ja/man1

install -s -c -m755 effectv %{buildroot}%{_prefix}/bin
install -s -c -m644 effectv.1 %{buildroot}%{_mandir}/man1
install -s -c -m644 docs.japanese/effectv.1 %{buildroot}%{_mandir}/ja/man1

%files
%defattr(-,root,root)
%attr(755,root,root) %{_prefix}/bin/effectv
%attr(644,root,root) %{_mandir}/man1/effectv.1*
%attr(644,root,root) %{_mandir}/ja/man1/effectv.1*
%doc README* COPYING ChangeLog Coding-HOWTO CREWS FAQ TODO NEWS
%doc docs.japanese/

%clean
rm -rf %{buildroot}

%changelog
* Mon Jan 12 2004 FUKUCHI Kentaro <fukuchi@users.sourceforge.net>
- version 0.3.9

* Sat Oct 5 2002 FUKUCHI Kentaro <fukuchi@users.sourceforge.net>
- version 0.3.8

* Sat Aug 10 2002 FUKUCHI Kentaro <fukuchi@users.sourceforge.net>
- version 0.3.7

* Wed May 7 2002 FUKUCHI Kentaro <fukuchi@users.sourceforge.net>
- version 0.3.6

* Wed Apr 3 2002 FUKUCHI Kentaro <fukuchi@users.sourceforge.net>
- version 0.3.5

* Fri Nov 9 2001 TABUCHI Takaaki <tab@kondara.org>
- (0.3.3-3k)
