%global         commit          8c8293ba8969a46947606a93ff0cb5a083aab47a
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           tinyxml2
Version:        6.0.0
Release:        5
Summary:        C++ XML parser
License:        zlib
URL:            https://github.com/leethomason/%{name}
Source0:        https://github.com/leethomason/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
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
%autosetup -n %{name}-%{commit}
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
%{_libdir}/lib%{name}.so.6.0.0
%{_libdir}/lib%{name}.so.6

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%changelog
* Thu Nov 21 2019 zhujunhao <zhujunhao5@huawei.com> - 6.0.0-5
- Initial package.
