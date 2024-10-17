Name:		gmameui
Version:	0.2.12
Release:	4

Summary:	A sdlmame front-end
License:	GPLv3+
Group:		Emulators
URL:		https://gmameui.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		gmamaui-0.2.12_glibc.patch
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(expat)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	desktop-file-utils
BuildRequires:	scrollkeeper

%description
GMAMEUI is a fork of the defunct GXMame project.

It contains a number of enhancements over GXMame:
 - support for SDLMame,
 - support for more recent versions of MAME,
 - support for the recent features introduced to MAME (the last version 
    supported by GXMame was 0.95),
 - migration to Glade for UI, allowing easier maintenance,
 - a substantial number of bug fixes and UI improvements over GXMame.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="ArcadeGame" \
  --add-category="Emulator" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*

