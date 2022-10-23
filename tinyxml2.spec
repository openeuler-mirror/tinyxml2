Name:           tinyxml2
Version:        9.0.0
Release:        1
Summary:        C++ XML parser
License:        zlib
URL:            https://github.com/leethomason/%{name}
Source0:        https://github.com/leethomason/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  gcc-c++ cmake

%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrated into other programs.  TinyXML-2 parses an XML document, and builds 
from that a Document Object Model (DOM) that can be read, modified, and saved.

%package        devel
Summary:        Development files for tinyxml2
Requires:       %{name} = %{version}-%{release}
%description    devel
The devel package contains development files for tinyxml2.It provides
header files and libraries for tinyxml2.

%prep
%autosetup -n %{name}-%{version}
chmod -c -x *.cpp *.h
sed -i -e 's,lib/,${CMAKE_INSTALL_LIBDIR}/,g' CMakeLists.txt

%build
mkdir objdir
cd objdir
%cmake .. -DBUILD_STATIC_LIBS=OFF
%make_build

%check
cd objdir
make test

%install
cd objdir
%make_install

%post
/sbin/ldconfig

%files
%doc readme.md
%{_libdir}/lib%{name}.so.9.0.0
%{_libdir}/lib%{name}.so.9

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%changelog
* Mon Oct 24 2022 YukariChiba <i@0x7f.cc> - 9.0.0-1
- Upgrade version to 9.0.0
- Switch to use stable version source url

* Thu Nov 21 2019 zhujunhao <zhujunhao5@huawei.com> - 6.0.0-5
- Initial package.
