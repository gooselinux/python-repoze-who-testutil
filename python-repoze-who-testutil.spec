%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global rcver rc1

Name:		python-repoze-who-testutil
Version:	1.0
Release:	0.4.%{rcver}%{?dist}
Summary:	Test utilities for repoze.who-powered applications
Group:		Development/Languages
License:	BSD
URL:		http://code.gustavonarea.net/repoze.who-testutil/
Source0:	http://pypi.python.org/packages/source/r/repoze.who-testutil/repoze.who-testutil-%{version}%{rcver}.tar.gz
Source1:    http://repoze.org/LICENSE.txt

Patch0:     %{name}-setuptools.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	python-devel, python-setuptools-devel
# Test suite requirements
# BuildRequires:	python-paste-deploy, python-repoze-who, python-nose, python-coverage
Requires:	python-repoze-who
Requires:	python-zope-interface
Requires:	python-paste-deploy

%description
repoze.who-testutil is a repoze.who plugin which modifies repoze.who‘s 
original middleware to make it easier to forge authentication, without 
bypassing identification (this is, running the metadata providers).
It’s been created in order to ease testing of repoze.who-powered 
applications, in a way independent of the identifiers, authenticators 
and challengers used originally by your application, so that you won’t have 
to update your test suite as your application grows and the authentication 
method changes.

%prep
%setup -q -n repoze.who-testutil-%{version}%{rcver}
cp %{SOURCE1} .
%patch0 -p0 -b .setuptools

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
# Tests are pretty broken. Oh, the irony.
# PYTHONPATH=$(pwd) nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 05 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.3.rc1
- Patch the setup.py to use our own setuptools package

* Wed May 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-0.2.rc1
- include license copy

* Wed May  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-0.1.rc1
- Initial package for Fedora
