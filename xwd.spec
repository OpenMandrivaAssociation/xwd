Name:		xwd
Version:	1.0.1
Release:	%mkrel 5
Summary:	Dump an image of an X window
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros	>= 1.1.5
BuildRequires:	libx11-devel	>= 1.1.3
BuildRequires:	libxmu-devel	>= 1.0.3

%description
Xwd is an X Window System window dumping utility. Xwd allows X users to store
window images in a specially formatted dump file. This file can then be read by
various other X utilities for redisplay, printing, editing, formatting,
archiving, image processing, etc.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xwd
%{_mandir}/man1/xwd.*
