%define fontname liberation
%define common_desc \
The Liberation Fonts are intended to be replacements for the three most \
commonly used fonts on Microsoft systems: Times New Roman, Arial, and Courier \
New.

%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:             %{fontname}-fonts
Summary:          Fonts to replace commonly used Microsoft Windows fonts
Version:          1.06.0.20100721
Release:          1
# The license of the Liberation Fonts is a EULA that contains GPLv2 and two
# exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like the one in
# GPLv3. This license is Free, but GPLv2 and GPLv3 incompatible.
License:          Liberation
Group:            User Interface/X
URL:              https://fedorahosted.org/liberation-fonts/
Source0:          https://fedorahosted.org/releases/l/i/liberation-fonts/%{name}-ttf-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    fontpackages-devel >= 1.13, xorg-x11-font-utils

%description
%common_desc

Meta-package of Liberation fonts which installs Sans, Serif, and Monospace,
Narrow families.

%package -n %{fontname}-fonts-common
Summary:          Shared common files of Liberation font families
Group:            User Interface/X
Requires:         fontpackages-filesystem >= 1.13
Obsoletes:        liberation-fonts < 1.04.93-7
Obsoletes:        liberation-fonts-compat <= 1.05.1.20090630

%description -n %{fontname}-fonts-common
%common_desc

Shared common files of Liberation font families.

%files -n %{fontname}-fonts-common
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING License.txt README
%dir %{_fontdir}
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}

%package -n %{fontname}-sans-fonts
Summary:      Sans-serif fonts to replace commonly used Microsoft Arial
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This is Sans-serif TrueType fonts that replaced commonly used Microsoft Arial.

%_font_pkg -n sans LiberationSans-*.ttf

%package -n %{fontname}-serif-fonts
Summary:      Serif fonts to replace commonly used Microsoft Times New Roman
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

This is Serif TrueType fonts that replaced commonly used Microsoft Times New \
Roman.

%_font_pkg -n serif LiberationSerif-*.ttf

%package -n %{fontname}-mono-fonts
Summary:      Monospace fonts to replace commonly used Microsoft Courier New
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}

%description -n %{fontname}-mono-fonts
%common_desc

This is Monospace TrueType fonts that replaced commonly used Microsoft Courier \
New.

%_font_pkg -n mono LiberationMono-*.ttf

%package -n %{fontname}-narrow-fonts
Summary:      Sans-serif Narrow fonts to replace commonly used Microsoft Arial Narrow
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}

%description -n %{fontname}-narrow-fonts
%common_desc

This is Sans-Serif Narrow TrueType fonts that replaced commonly used Microsoft \
Arial Narrow.

%_font_pkg -n narrow LiberationSansNarrow-*.ttf

%prep
%setup -q -n %{name}-ttf-%{version}

%build
%{nil}

%install
rm -rf %{buildroot}
# fonts .ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -sf %{_fontdir} %{buildroot}%{catalogue}/%{name}
# fonts.{dir,scale}
mkfontdir %{buildroot}%{_fontdir}
mkfontscale %{buildroot}%{_fontdir}

%clean
rm -rf %{buildroot}

