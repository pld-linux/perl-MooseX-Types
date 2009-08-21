#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	Types
Summary:	MooseX::Types - Organise your Moose types in libraries
Summary(pl.UTF-8):	MooseX::Types - porządkuje typy Moose w biblioteki
Name:		perl-MooseX-Types
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b153e2da41a3177b43a4b47211231805
URL:		http://search.cpan.org/dist/MooseX-Types/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Clan >= 6.00
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Moose >= 0.61
BuildRequires:	perl-Sub-Install >= 0.924
BuildRequires:	perl-Sub-Name
BuildRequires:	perl-Test-Simple >= 0.80
BuildRequires:	perl-namespace-clean >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The types provided with Moose are by design global. This package helps
you to organise and selectively import your own and the built-in types
in libraries. As a nice side effect, it catches typos at compile-time
too.

However, the main reason for this module is to provide an easy way to
not have conflicts with your type names, since the internal fully
qualified names of the types will be prefixed with the library's name.

This module will also provide you with some helper functions to make
it easier to use Moose types in your code.

String type names will produce a warning, unless it's for a class_type
or role_type declared within the library, or a fully qualified name
like 'MyTypeLibrary::Foo'.



%description -l pl.UTF-8
Typy Moose dostarczona są zgodne z projektem globalnym. Pakiet ten
pomaga zorganizować i selektywnie importować własne oraz wbudowane
typy z bibliotek. Jako miły skutek uboczny, wychwytuje również
literówki w czasie kompilacji.

Jednakże głównym celem tego modułu jest dostarczenie łatwego sposobu,
aby uniknąć konfliktów ze swoimi nazwami typów, ponieważ wbudowane
nazwy typów będzą opatrzone prefiksem z nazwą biblioteki.

Moduł ten będzie również dostarczać niektóre funkcje pomocnicze, aby
ułatwić użycie typów Moose w kodzie.

Napis typu nazwy dadzą ostrzeżenie, chyba że jest to dla class_type
lub role_type zadeklarowanych w bibliotece lub w wbudowana nazwa jak
'MyTypeLibrary::Foo'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/*.pm
%{perl_vendorlib}/MooseX/Types
%{_mandir}/man3/*
