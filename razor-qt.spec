# TODO
# - merge something from razorqt.spec?
%define		qtver	4.6.0

Summary:	Razor a lightweight desktop toolbox
Summary(pl.UTF-8):	Razor jest lekkim zestawem narzędzi na biurko
Name:		razor-qt
Version:	0.4.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://razor-qt.org/downloads/razorqt-%{version}.tar.bz2
# Source0-md5:	724b5a43ba1e162d70203a32b2bd34ed
URL:		http://www.razor-qt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libmagic-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	QtCore >= %{qtver}
Requires:	QtDBus >= %{qtver}
Obsoletes:	razorqt < 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Razor-qt is an advanced, easy-to-use, and fast desktop environment
based on Qt technologies. Unlike desktop environments, Razor-qt also
works fine with weak machines.

%package devel
Summary:	RazorQt development package
Summary(pl.UTF-8):	Pakiet programistyczny RazorQt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}
Obsoletes:	razorqt-devel < 0.4

%description devel
RazorQt development package.

%description devel -l pl.UTF-8
Pakiet programistyczny RazorQt.

%prep
%setup -q -n razorqt-%{version}

%build
install -d build
cd build
%cmake .. \
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# not sure where kdm holds its sessions, so drop for now (it pulls kde otherwise)
rm -r $RPM_BUILD_ROOT%{_datadir}/apps/kdm/sessions

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
/etc/xdg/autostart/razor-ptbatterysystemtray-autostart.desktop
/etc/xdg/autostart/razor-qlipper-autostart.desktop
/etc/xdg/autostart/razor-qstardict-autostart.desktop
/etc/xdg/autostart/razor-qxkb-autostart.desktop
/etc/xdg/autostart/razor-xscreensaver-autostart.desktop
%{_sysconfdir}/xdg/menus/razor-applications.menu
%attr(755,root,root) %{_bindir}/razor-appswitcher
%attr(755,root,root) %{_bindir}/razor-autosuspend
%attr(755,root,root) %{_bindir}/razor-config
%attr(755,root,root) %{_bindir}/razor-config-appearance
%attr(755,root,root) %{_bindir}/razor-config-desktop
%attr(755,root,root) %{_bindir}/razor-config-mouse
%attr(755,root,root) %{_bindir}/razor-config-session
%attr(755,root,root) %{_bindir}/razor-desktop
%attr(755,root,root) %{_bindir}/razor-panel
%attr(755,root,root) %{_bindir}/razor-policykit-agent
%attr(755,root,root) %{_bindir}/razor-power
%attr(755,root,root) %{_bindir}/razor-runner
%attr(755,root,root) %{_bindir}/razor-session
%attr(755,root,root) %{_bindir}/razor-x11info
%attr(755,root,root) %{_bindir}/startrazor

%attr(755,root,root) %{_libdir}/libqtxdg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqtxdg.so.0
%attr(755,root,root) %{_libdir}/librazormount.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librazormount.so.0
%attr(755,root,root) %{_libdir}/librazorqt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librazorqt.so.0
%attr(755,root,root) %{_libdir}/librazorqxt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librazorqxt.so.0

%dir %{_libdir}/razor-desktop
%attr(755,root,root) %{_libdir}/razor-desktop/libanalogclock.so
%attr(755,root,root) %{_libdir}/razor-desktop/libdesktop-razor.so
%attr(755,root,root) %{_libdir}/razor-desktop/libdesktop-wm_native.so
%attr(755,root,root) %{_libdir}/razor-desktop/libhelloworld.so
%attr(755,root,root) %{_libdir}/razor-desktop/libiconview.so
%dir %{_libdir}/razor-panel
%attr(755,root,root) %{_libdir}/razor-panel/libclock.so
%attr(755,root,root) %{_libdir}/razor-panel/libdesktopswitch.so
%attr(755,root,root) %{_libdir}/razor-panel/libmainmenu.so
%attr(755,root,root) %{_libdir}/razor-panel/libmount.so
%attr(755,root,root) %{_libdir}/razor-panel/libquicklaunch.so
%attr(755,root,root) %{_libdir}/razor-panel/libscreensaver.so
%attr(755,root,root) %{_libdir}/razor-panel/libshowdesktop.so
%attr(755,root,root) %{_libdir}/razor-panel/libtaskbar.so
%attr(755,root,root) %{_libdir}/razor-panel/libtray.so

%{_iconsdir}/hicolor/scalable/apps/razor-autosuspend.svg

%{_datadir}/razor
%{_datadir}/desktop-directories/razor*.directory
%{_datadir}/xsessions/razor*.desktop
%{_desktopdir}/razor*.desktop

%dir %{_datadir}/librazorqt
%lang(cs) %{_datadir}/librazorqt/librazorqt_cs_CZ.qm
%lang(da) %{_datadir}/librazorqt/librazorqt_da_DK.qm
%lang(de) %{_datadir}/librazorqt/librazorqt_de_DE.qm
%lang(el) %{_datadir}/librazorqt/librazorqt_el_GR.qm
%lang(it) %{_datadir}/librazorqt/librazorqt_it_IT.qm
%lang(pl) %{_datadir}/librazorqt/librazorqt_pl_PL.qm
%lang(ru) %{_datadir}/librazorqt/librazorqt_ru_RU.qm
%lang(sk) %{_datadir}/librazorqt/librazorqt_sk_SK.qm
%lang(zh_CN) %{_datadir}/librazorqt/librazorqt_zh_CN.qm

%dir %{_datadir}/qtxdg
%lang(cs) %{_datadir}/qtxdg/qtxdg_cs_CZ.qm
%lang(da) %{_datadir}/qtxdg/qtxdg_da_DK.qm
%lang(de) %{_datadir}/qtxdg/qtxdg_de_DE.qm
%lang(el) %{_datadir}/qtxdg/qtxdg_el_GR.qm
%lang(it) %{_datadir}/qtxdg/qtxdg_it_IT.qm
%lang(pl) %{_datadir}/qtxdg/qtxdg_pl_PL.qm
%lang(ru) %{_datadir}/qtxdg/qtxdg_ru_RU.qm
%lang(sk) %{_datadir}/qtxdg/qtxdg_sk_SK.qm
%lang(zh_CN) %{_datadir}/qtxdg/qtxdg_zh_CN.qm

# temp files - it will be removed when it becomes part of upstream
%dir %{_libdir}/razor-xdg-tools
%attr(755,root,root) %{_libdir}/razor-xdg-tools/xdg-mime
%attr(755,root,root) %{_libdir}/razor-xdg-tools/xdg-open

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtxdg.so
%attr(755,root,root) %{_libdir}/librazormount.so
%attr(755,root,root) %{_libdir}/librazorqt.so
%attr(755,root,root) %{_libdir}/librazorqxt.so
%{_includedir}/qtxdg
%{_includedir}/razormount
%{_includedir}/razorqt
%{_includedir}/razorqxt
%{_pkgconfigdir}/qtxdg.pc
%{_pkgconfigdir}/razormount.pc
%{_pkgconfigdir}/razorqt.pc
%{_pkgconfigdir}/razorqxt.pc
