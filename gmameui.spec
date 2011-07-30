Name:			gmameui
Version:		0.2.12
Release:		%mkrel 2

Summary:	A sdlmame front-end
License:	GPLv3+
Group:		Emulators
URL:		http://gmameui.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	libgnome2-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	libglade2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	vte-devel
BuildRequires:	libarchive-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="ArcadeGame" \
  --add-category="Emulator" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}
%{_datadir}/omf/%{name}/%{name}-C.omf
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*

%clean
rm -rf %{buildroot}

