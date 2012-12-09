Name:		xwd
Version:	1.0.5
Release:	1
Summary:	Dump an image of an X window
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xwd is an X Window System window dumping utility. Xwd allows X users to store
window images in a specially formatted dump file. This file can then be read by
various other X utilities for redisplay, printing, editing, formatting,
archiving, image processing, etc.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xwd
%{_mandir}/man1/xwd.*


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.5-1
+ Revision: 781016
- version update 1.0.5

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2
+ Revision: 671376
- mass rebuild

* Mon Nov 08 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 594890
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464751
- New version: 1.0.3

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-2mdv2009.1
+ Revision: 350743
- rebuild

* Mon Jun 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 230103
- New version

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2008.1
+ Revision: 179445
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.
    - Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 80801
- rebuild for 2008
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension

