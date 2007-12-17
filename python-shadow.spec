%define oname pyshadow
%define name python-shadow
%define version 0.2
%define release %mkrel 1

Summary: Python wrapper for shadow password file
Name: %{name}
Version: %{version}
Release: %{release}
Source: %oname-%{version}.tar.gz
License: GPL
Group: Development/Python
Url: http://www.twistedmatrix.com/users/z3p/files/
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
