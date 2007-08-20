Name: xwd
Version: 1.0.1
Release: %mkrel 3
Summary: dump an image of an X window
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xwd
%{_mandir}/man1/xwd.*


