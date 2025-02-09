%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:           mingw32-glib2
Version:        2.19.10
Release:        %mkrel 2
Summary:        MinGW Windows GLib2 library

License:        LGPLv2+
Group:          Development/Other
URL:            https://www.gtk.org
Source0:        http://download.gnome.org/sources/glib/2.19/glib-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch

Patch0:         glib-i386-atomic.patch

BuildRequires:  mingw32-filesystem >= 43-6
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-iconv
BuildRequires:  mingw32-gettext

BuildRequires:  pkgconfig
# Native version required for msgfmt use in build
BuildRequires:  gettext
# Native version required for glib-genmarshal
BuildRequires:  glib2-devel

# These are required for the glib-i386-atomic patch.
BuildRequires:  autoconf, automake, libtool, gettext-devel, gtk-doc

Requires:       pkgconfig


%description
MinGW Windows Glib2 library.


%prep
%setup -q -n glib-%{version}
%patch0 -p1 -b .i386-atomic

# Required for the glib-i386-atomic patch.
libtoolize --force --copy
autoreconf


%build
%{_mingw32_configure} --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT/%{_mingw32_libdir}/charset.alias

# Remove manpages which duplicate Fedora native.
rm -rf $RPM_BUILD_ROOT%{_mingw32_mandir}

%find_lang glib20


%clean
rm -rf $RPM_BUILD_ROOT


%files -f glib20.lang
%defattr(-,root,root)
%{_mingw32_bindir}/glib-genmarshal.exe
%{_mingw32_bindir}/glib-gettextize
%{_mingw32_bindir}/glib-mkenums
%{_mingw32_bindir}/gobject-query.exe
%{_mingw32_bindir}/gspawn-win32-helper-console.exe
%{_mingw32_bindir}/gspawn-win32-helper.exe
%{_mingw32_bindir}/libgio-2.0-0.dll
%{_mingw32_bindir}/libglib-2.0-0.dll
%{_mingw32_bindir}/libgmodule-2.0-0.dll
%{_mingw32_bindir}/libgobject-2.0-0.dll
%{_mingw32_bindir}/libgthread-2.0-0.dll
%{_mingw32_includedir}/glib-2.0/
%{_mingw32_libdir}/gio-2.0.def
%{_mingw32_libdir}/glib-2.0.def
%{_mingw32_libdir}/glib-2.0/
%{_mingw32_libdir}/gmodule-2.0.def
%{_mingw32_libdir}/gobject-2.0.def
%{_mingw32_libdir}/gthread-2.0.def
%{_mingw32_libdir}/libgio-2.0.dll.a
%{_mingw32_libdir}/libgio-2.0.la
%{_mingw32_libdir}/libglib-2.0.dll.a
%{_mingw32_libdir}/libglib-2.0.la
%{_mingw32_libdir}/libgmodule-2.0.dll.a
%{_mingw32_libdir}/libgmodule-2.0.la
%{_mingw32_libdir}/libgobject-2.0.dll.a
%{_mingw32_libdir}/libgobject-2.0.la
%{_mingw32_libdir}/libgthread-2.0.dll.a
%{_mingw32_libdir}/libgthread-2.0.la
%{_mingw32_libdir}/pkgconfig/gio-2.0.pc
%{_mingw32_libdir}/pkgconfig/gio-unix-2.0.pc
%{_mingw32_libdir}/pkgconfig/glib-2.0.pc
%{_mingw32_libdir}/pkgconfig/gmodule-2.0.pc
%{_mingw32_libdir}/pkgconfig/gmodule-export-2.0.pc
%{_mingw32_libdir}/pkgconfig/gmodule-no-export-2.0.pc
%{_mingw32_libdir}/pkgconfig/gobject-2.0.pc
%{_mingw32_libdir}/pkgconfig/gthread-2.0.pc
%{_mingw32_datadir}/aclocal/glib-2.0.m4
%{_mingw32_datadir}/aclocal/glib-gettext.m4
%{_mingw32_datadir}/glib-2.0/
%{_mingw32_datadir}/gtk-doc/html/gio/
%{_mingw32_datadir}/gtk-doc/html/glib/
%{_mingw32_datadir}/gtk-doc/html/gobject/
