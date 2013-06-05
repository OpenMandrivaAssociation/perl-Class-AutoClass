%define upstream_name    Class-AutoClass
%define upstream_version 1.54

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.55
Release:    1

Summary:    Yet another OO helper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/Class-AutoClass-1.55.tar.gz
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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.540.0-2mdv2011.0
+ Revision: 681042
- add br
- mass rebuild

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.540.0-1mdv2011.0
+ Revision: 572697
- update to 1.54

* Thu Jan 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1.530.0-1mdv2011.0
+ Revision: 487048
- update to 1.53

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.520.0-1mdv2010.1
+ Revision: 473717
- update to 1.52

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1.510.0-1mdv2010.1
+ Revision: 467876
- update to 1.51

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-1mdv2010.1
+ Revision: 466457
- update to 1.50

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.01-2mdv2010.0
+ Revision: 440539
- rebuild

* Fri Mar 06 2009 Stéphane Téletchéa <steletch@mandriva.org> 1.01-1mdv2009.1
+ Revision: 349785
- Disabling tests
- Update to 1.01 for bioperl

* Fri Mar 06 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.092-7mdv2009.1
+ Revision: 349725
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.092-6mdv2009.0
+ Revision: 255845
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.092-4mdv2008.1
+ Revision: 136682
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.092-4mdv2008.0
+ Revision: 86073
- rebuild


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.092-3mdv2007.0
- Rebuild

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.092-2mdk
- fix buildrequires

* Mon Jun 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.092-1mdk
- New release 0.092
- make test in %%check

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.091-1mdk
- new release
- spec cleanup
- better url

* Mon Jan 17 2005 Guillaume Rousse <guillomovitch@mandrake.org> 0.09-1mdk 
- first mdk release


