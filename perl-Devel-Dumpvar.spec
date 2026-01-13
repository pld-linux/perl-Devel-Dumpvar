#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Devel
%define		pnam	Dumpvar
Summary:	Devel::Dumpvar - a pure-OO reimplementation of dumpvar.pl
Summary(pl.UTF-8):	Devel::Dumpvar - czysto obiektowo zorientowana reimplementacja dumpvar.pl
Name:		perl-Devel-Dumpvar
Version:	1.06
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4a7e4d4fb9150e43c354fe674631ce1c
URL:		http://search.cpan.org/dist/Devel-Dumpvar/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most Perl dumping modules are focused on serializing data structures
into a format that can be rebuilt into the original data structure.
They do this with a variety of different focuses, such as human
readability, the ability to execute the dumped code directly, or to
minimize the size of the dumped data.

Expect for the one contained in the debugger, in the file dumpvar.pl.
This is a readily human-readable form, highly useful for debugging,
containing a lot of extra information without the burden of needing to
be re-assembled into the original data.

Devel::Dumpvar is a pure object-orientated implementation of the same
functionality made as a module. This makes it much more usable version
to use for dumping information to debug log files or other uses where
you don't need to reassemble the data.

%description -l pl.UTF-8
Większość perlowych modułów wykonujących zrzuty skupia się na
serializacji struktur danych do formatu, z którego można zbudować
oryginalną strukturę danych. Robią to skupiając się na wielu różnych
zastosowaniach, takich jak czytelność dla człowieka, możliwość
bezpośredniego wykonania wyprodukowanego kodu lub zminimalizowaniu
rozmiaru zrzuconych danych.

Jeden fragment kodu jest wyjątkiem, zawarty jest w debuggerze, w pliku
dumpvar.pl. Daje łatwo czytelną dla człowieka postać danych, bardzo
przydatną przy odpluskwianiu, zawierającą wiele dodatkowych informacji
nie obciążonych potrzebą ponownego składania oryginalnych danych.

Devel::Dumpvar jest czysto obiektowo zorientowaną implementacją tej
samej funkcjonalności wykonaną jako moduł Perla. Czyni to go dużo
bardziej użyteczną wersją do zrzucania informacji do debugowych plików
logów lub innych zastosowań gdzie nie trzeba ponownie składać danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Devel/Dumpvar.pm
%{_mandir}/man3/*
