%define	shortname	delightful
Summary:	A set of widgets for Awesome window manager
Summary(hu.UTF-8):	Widget-ek gyűjteménye Awesome ablakkezelőhöz
Name:		awesome-plugin-%{shortname}
Version:	20110123
Release:	0.1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.xz
# Source0-md5:	872b8860c74249114453da93ca234bd1
URL:		http://solitudo.net/software/awesome/delightful/
Source1:	imap.lua
Requires:	awesome >= 3.4
Requires:	awesome-plugin-freedesktop
Requires:	awesome-plugin-vicious
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Your average Awesome widget is quite dull. Some might consider that a
feature. In this case, Delightful is probably not for you. Delightful
try to add some “bling” to the widgets. Not un-needed “bling” but
something useful. Many Delightful widgets provide a dynamically
updated icon along with the widget text. The icon might indicate the
sound volume or battery level. Some of the widgets use Naughty based
pop-ups and notifications to provide useful, additional information
that doesn’t fit the Awesome wibox. Tooltips are used always when it
makes sense.

%package imap
Summary:	IMAP support
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description imap
IMAP support.

%package weather
Summary:	Weather support
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	lua-expat
Requires:	lua-metar
Requires:	lua-weather

%description weather
Weather support.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}
cp -r delightful/* $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}
install -d $RPM_BUILD_ROOT%{_datadir}/lua/5.1
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/lua/5.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt awesome-3.4.3-delightful-sample-configuration.diff
%dir %{_datadir}/awesome/lib/%{shortname}
%dir %{_datadir}/awesome/lib/%{shortname}/widgets
%{_datadir}/awesome/lib/%{shortname}/utils.lua
%{_datadir}/awesome/lib/%{shortname}/widgets/battery.lua
%{_datadir}/awesome/lib/%{shortname}/widgets/cpu.lua
%{_datadir}/awesome/lib/%{shortname}/widgets/datetime.lua
%{_datadir}/awesome/lib/%{shortname}/widgets/memory.lua
%{_datadir}/awesome/lib/%{shortname}/widgets/network.lua
%{_datadir}/awesome/lib/%{shortname}/widgets/pulseaudio.lua

%files imap
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/%{shortname}/widgets/imap.lua
%{_datadir}/lua/5.1/imap.lua

%files weather
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/%{shortname}/widgets/weather.lua
