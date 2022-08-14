#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : pypi-sphinxcontrib_applehelp
Version  : 1.0.2
Release  : 33
URL      : https://files.pythonhosted.org/packages/9f/01/ad9d4ebbceddbed9979ab4a89ddb78c9760e74e6757b1880f1b2760e8295/sphinxcontrib-applehelp-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/01/ad9d4ebbceddbed9979ab4a89ddb78c9760e74e6757b1880f1b2760e8295/sphinxcontrib-applehelp-1.0.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/9f/01/ad9d4ebbceddbed9979ab4a89ddb78c9760e74e6757b1880f1b2760e8295/sphinxcontrib-applehelp-1.0.2.tar.gz.asc
Summary  : sphinxcontrib-applehelp is a sphinx extension which outputs Apple help books
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_applehelp-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_applehelp-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_applehelp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
sphinxcontrib-applehelp is a sphinx extension which outputs Apple help books

%package license
Summary: license components for the pypi-sphinxcontrib_applehelp package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_applehelp package.


%package python
Summary: python components for the pypi-sphinxcontrib_applehelp package.
Group: Default
Requires: pypi-sphinxcontrib_applehelp-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_applehelp package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_applehelp package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_applehelp)

%description python3
python3 components for the pypi-sphinxcontrib_applehelp package.


%prep
%setup -q -n sphinxcontrib-applehelp-1.0.2
cd %{_builddir}/sphinxcontrib-applehelp-1.0.2
pushd ..
cp -a sphinxcontrib-applehelp-1.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408940
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_applehelp
cp %{_builddir}/sphinxcontrib-applehelp-1.0.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_applehelp/50d2292390ae54694468ea4c35b53bb06a646e77
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_applehelp/50d2292390ae54694468ea4c35b53bb06a646e77

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
