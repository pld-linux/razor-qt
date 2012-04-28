# TODO
# - merge with razorqt.spec
%define		qtver	4.6.0

Summary:	Razor-qt desktop environment
Name:		razor-qt
Version:	0.4.0
Release:	0.5
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://razor-qt.org/downloads/razorqt-%{version}.tar.bz2
# Source0-md5:	3a38bfa08edb7d5d8abc3898dc0bb050
URL:		http://http://razor-qt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	libmagic-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	udev-devel
Requires:	QtCore >= %{qtver}
Requires:	QtDBus >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Razor-qt is an advanced, easy-to-use, and fast desktop environment
based on Qt technologies. Unlike desktop environments, 
Razor-qt also works fine with weak machines.

%package devel
Summary:	Development files for razor-qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}

%description devel
Development files for razor-qt.

%prep
%setup -q -n razorqt-%{version}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt4

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc README
%attr(755,root,root) %{_bindir}/razor*
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
%attr(755,root,root) %{_libdir}/razor-desktop/lib*.so
%dir %{_libdir}/razor-panel
%attr(755,root,root) %{_libdir}/razor-panel/lib*.so
%dir %{_libdir}/razor-xdg-tools
%attr(755,root,root) %{_libdir}/razor-xdg-tools/xdg-mime
%attr(755,root,root) %{_libdir}/razor-xdg-tools/xdg-open
%{_datadir}/razor
%{_datadir}/desktop-directories/razor*.directory
%{_datadir}/xsessions/razor*.desktop
%{_datadir}/applications/razor*.desktop
%{_datadir}/apps/kdm/sessions/razor*.desktop
%{_sysconfdir}/xdg/menus/razor-applications.menu
%dir %{_datadir}/librazorqt
%lang(pl) %{_datadir}/librazorqt/librazorqt_pl_PL.qm
%lang(ru) %{_datadir}/librazorqt/librazorqt_ru_RU.qm
%dir %{_datadir}/qtxdg
%lang(pl) %{_datadir}/qtxdg/qtxdg_pl_PL.qm
%lang(ru) %{_datadir}/qtxdg/qtxdg_ru_RU.qm

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
