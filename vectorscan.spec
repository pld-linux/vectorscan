Summary:	High-performance regular expression matching library
Summary(pl.UTF-8):	Biblioteka szybkiego dopasowywania wyrażeń regularnych
Name:		vectorscan
Version:	5.4.12
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/VectorCamp/vectorscan/archive/vectorscan/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	384eab5b23831993df96e5fa55f9951e
Patch0:		%{name}-pkgconfig.patch
URL:		https://github.com/VectorCamp/vectorscan
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.0
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	pcre-devel
BuildRequires:	ragel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vectorscan is a portable fork of Intel's Hyperscan, a high-performance
multiple regex matching library. It follows the same API as Hyperscan
and provides binary compatible drop-in replacement.

%description -l pl.UTF-8
Vectorscan to przenośne odgałęzienie biblioteki Intel Hyperscan,
służącej do szybkiego dopasowywania wielu wyrażeń regularnych
jednocześnie. Zachowuje to samo API co Hyperscan i stanowi zamiennik
binarnie kompatybilny.

%package devel
Summary:	Header files for Vectorscan library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Vectorscan
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	hyperscan-devel = %{version}

%description devel
Header files for Vectorscan library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Vectorscan.

%package static
Summary:	Static Vectorscan library
Summary(pl.UTF-8):	Statyczna biblioteka Vectorscan
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Vectorscan library.

%description static -l pl.UTF-8
Statyczna biblioteka Vectorscan.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -P0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_SHARED_LIBS=ON \
	-DBUILD_STATIC_LIBS=ON \
	-DBUILD_BENCHMARKS=OFF \
	-DBUILD_DOC=OFF \
	-DBUILD_EXAMPLES=OFF \
	-DBUILD_UNIT=OFF \
	..

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
%doc README.md LICENSE COPYING CHANGELOG.md CHANGELOG-vectorscan.md
%{_libdir}/libhs.so.*.*.*
%ghost %{_libdir}/libhs.so.5
%{_libdir}/libhs_runtime.so.*.*.*
%ghost %{_libdir}/libhs_runtime.so.5

%files devel
%defattr(644,root,root,755)
%{_libdir}/libhs.so
%{_libdir}/libhs_runtime.so
%dir %{_includedir}/hs
%{_includedir}/hs/*.h
%{_pkgconfigdir}/libhs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhs.a
%{_libdir}/libhs_runtime.a
