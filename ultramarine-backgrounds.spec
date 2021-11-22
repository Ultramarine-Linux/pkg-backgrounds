%undefine _disable_source_fetch

Name: ultramarine-backgrounds
Version: %{fedora}
Release: 2.1%{?dist}
BuildArch: noarch
# details for the artworks' licenses can be seen in the COPYING file
License: CC-BY-SA 4.0 and CC0
Summary: Ultramarine Linux backgrounds
Provides: desktop-backgrounds
# licensing information
Source0: https://gitlab.ultramarine-linux.org/design/backgrounds/-/archive/%{version}/backgrounds-%{version}.tar.gz

# CC0 artworks


%description
This package contains desktop backgrounds for the Ultramarine Linux default theme.

%package    basic
Summary:    Ultramarine Linux backgrounds
Provides:   ultramarine-backgrounds = %{version}-%{release}
Obsoletes:   ultramarine-backgrounds < %{version}-%{release}

%description    basic
The desktop-backgrounds-basic package contains artwork intended to be used as
desktop background image.



%package        gnome
Summary:        The default Fedora wallpaper from GNOME desktop
Requires:       ultramarine-backgrounds-basic
# starting with this release, gnome uses picture-uri instead of picture-filename
# see gnome bz #633983
Requires:       gsettings-desktop-schemas >= 2.91.92
Provides:       system-backgrounds-gnome = %{version}-%{release}
License:        CC0

%description    gnome
The desktop-backgrounds-gnome package sets default background in GNOME-based desktops

%prep
%autosetup -n backgrounds-%{version}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

#pushd %{buildroot}%{_datadir}/backgrounds

#mkdir -p %{buildroot}%{_datadir}/backgrounds/
#ln -s ultramarine-linux/default %{buildroot}%{_datadir}/backgrounds/
#ln -s default/default.jpg %{buildroot}%{_datadir}/backgrounds/default.png

%files
%license COPYING

%files basic
%{_datadir}/backgrounds/ultramarine-linux/
#%%{_datadir}/backgrounds/default
#%%{_datadir}/backgrounds/default.png

%files gnome
%{_datadir}/gnome-background-properties/ultramarine-wallpapers.xml