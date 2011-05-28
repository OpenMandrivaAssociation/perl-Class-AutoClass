%define upstream_name    Class-AutoClass
%define upstream_version 1.54

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Yet another OO helper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
Buildrequires:  perl(IO::Stringy)
BuildRequires:	perl(Module::Build)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc Changes
%{perl_vendorlib}/Class
%{_mandir}/*/*
