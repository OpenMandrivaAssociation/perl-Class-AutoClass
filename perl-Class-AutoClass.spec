%define module  Class-AutoClass
%define name    perl-%{module}
%define version 1.01
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Yet another OO helper
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildrequires:  perl(IO::Stringy)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This perl module brings the following advantages:
- get and set methods for simple attributes can be automatically
  generated
- argument lists are handled as described below
- the protocol for object creation and initialization is close to
  the 'textbook' approach generally suggested for object-oriented Perl
  (see below)
- object initialization is handled correctly in the presence of multiple
  inheritance

%prep
%setup -n AutoClass

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
# %make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes INSTALL
%{perl_vendorlib}/Class
%{_mandir}/*/*
