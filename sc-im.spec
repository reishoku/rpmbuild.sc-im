%define pkg_name sc-im

Name: %{pkg_name}
Version: 0.8.4
Release: 2%{?dist}
Summary: Spreadsheet Calculator Improvised -- An ncurses spreadsheet program for terminal

License: BSD-4-Clause
URL:     https://github.com/andmarti1424/sc-im
Source0: https://github.com/andmarti1424/%{pkg_name}/archive/refs/tags/v%{version}.tar.gz

# FIXME: Optimize Build/Runtime dependencies
BuildRequires: gcc
BuildRequires: pkgconf pkgconf-pkg-config
BuildRequires: doxygen
BuildRequires: ncurses-libs
BuildRequires: ncurses-devel
BuildRequires: libxml2-devel
BuildRequires: libzip-devel
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: bzip2-devel
BuildRequires: openssl-devel
# BuildRequires: compat-openssl11
BuildRequires: libxls-devel
BuildRequires: libxlsxwriter-devel
BuildRequires: luajit-devel
# BuildRequires: ncurses-compat-libs
# BuildRequires: groff

Requires: glibc
Requires: bash
Requires: ncurses-libs
Requires: libxml2
Requires: libzip
Requires: compat-lua-libs
Requires: zlib
Requires: xz-libs
Requires: bzip2-libs
Requires: openssl-libs
Requires: libxls
Requires: libxlsxwriter

%define additional_cflags "-DMAXROWS=65536"

%description
Spreadsheet Calculator Improvised, aka sc-im, is an ncurses based, vim-like spreadsheet calculator.

sc-im is based on sc, whose original authors are James Gosling and Mark Weiser, and mods were later added by Chuck Martin.

%prep
%{__tar} zxf %{SOURCE0}

%build
cd sc-im-%{version}/src
export CFLAGS="%{optflags}"
export CFLAGS+=" %{?additional_cflags}"
%{make_build} -B \
  -f ./Makefile \
  sc-im \
  DESTDIR=%{buildroot} \
  VERBOSE=1 \
  prefix=%{_prefix}


%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}
cd %{_builddir}/sc-im-%{version}/src

install -p -d %{buildroot}%{_prefix}/bin
install -p -d %{buildroot}%{_datadir}/sc-im
install -p -d %{buildroot}%{_mandir}/man1

install -p --strip sc-im   %{buildroot}%{_prefix}/bin/sc-im
install -p         scopen  %{buildroot}%{_prefix}/bin/scopen
install -p -m 644  doc     %{buildroot}%{_datadir}/sc-im/sc-im_help
install -p -m 644  plot_*  %{buildroot}%{_datadir}/sc-im/
install -p -m 644  sc-im.1 %{buildroot}%{_mandir}/man1/sc-im.1
install -p         %{_builddir}/sc-im-%{version}/LICENSE %{buildroot}%{_datadir}/%{name}/LICENSE


%files
%{_bindir}/sc-im
%{_bindir}/scopen
%{_datadir}/%{name}/plot_bar
%{_datadir}/%{name}/plot_line
%{_datadir}/%{name}/plot_pie
%{_datadir}/%{name}/plot_scatter
%{_datadir}/%{name}/sc-im_help
%doc     %{_mandir}/man1/sc-im.1.gz
%license %{_datadir}/%{name}/LICENSE

%changelog
* Wed May 21 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me>
- Adjust RPM spec for EL10 platform
- Built for EL10 platform

* Sat May 10 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me>
- Initial RPM Package build (RPM spec is not completed, but builds successfully)
