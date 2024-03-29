#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-geronimo-jcache_1.0_spec
Version  : jcache.1.0.spec.1.0.alpha.1
Release  : 4
URL      : https://github.com/apache/geronimo-specs/archive/geronimo-jcache_1.0_spec-1.0-alpha-1.tar.gz
Source0  : https://github.com/apache/geronimo-specs/archive/geronimo-jcache_1.0_spec-1.0-alpha-1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1/geronimo-jcache_1.0_spec-1.0-alpha-1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1/geronimo-jcache_1.0_spec-1.0-alpha-1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-geronimo-jcache_1.0_spec-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-geronimo-jcache_1.0_spec package.
Group: Data

%description data
data components for the mvn-geronimo-jcache_1.0_spec package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1/geronimo-jcache_1.0_spec-1.0-alpha-1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1/geronimo-jcache_1.0_spec-1.0-alpha-1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1/geronimo-jcache_1.0_spec-1.0-alpha-1.jar
/usr/share/java/.m2/repository/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1/geronimo-jcache_1.0_spec-1.0-alpha-1.pom
