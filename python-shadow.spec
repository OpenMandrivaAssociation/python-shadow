%define oname pyshadow
%define name python-shadow
%define version 0.2
%define release 7

Summary: Python wrapper for shadow password file
Name: %{name}
Version: %{version}
Release: %{release}
Source: %oname-%{version}.tar.gz
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: https://www.twistedmatrix.com/users/z3p/files/
BuildRequires: python-devel
Obsoletes: %{oname}
Provides: %{oname}

%description
This is a module to allow access to the shadow password file.  It also includes
md5_crypt, which implements the md5_crypt function used to encrypt passwords
in the shadow password file.
				
%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %{oname}-%{version}

%build
%_bindir/python setup.py build

%install
%_bindir/python setup.py install --root=$RPM_BUILD_ROOT --record %name.files
chmod 0644 LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.files
%defattr(-,root,root)
%doc LICENSE README


%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.2-6mdv2011.0
+ Revision: 590090
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2010.0
+ Revision: 442483
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2009.0
+ Revision: 259778
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2009.0
+ Revision: 247633
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2-1mdv2008.1
+ Revision: 136460
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Pascal Terjan <pterjan@mandriva.org>
    - Fix a typo in the description

* Thu Jul 26 2007 Pascal Terjan <pterjan@mandriva.org> 0.2-1mdv2008.0
+ Revision: 55937
- follow python naming policy
- follow python naming policy
- 0.2
- mkrel
- follow python naming policy
- fix summary ended with dot
- Import pyshadow

