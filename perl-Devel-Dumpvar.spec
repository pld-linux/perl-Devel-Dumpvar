#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Dumpvar
Summary:	Devel::Dumpvar - a pure-OO reimplementation of dumpvar.pl
Summary(pl):	Devel::Dumpvar - czysto obiektowo zorientowana reimplementacja dumpvar.pl
Name:		perl-Devel-Dumpvar
Version:	0.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9e65d920b1f6414e38a0cf2613cce48
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

%description -l pl
Wiêkszo¶æ perlowych modu³ów wykonuj±cych zrzuty skupia siê na
serializacji struktur danych do formatu, z którego mo¿na zbudowaæ
oryginaln± strukturê danych. Robi± to skupiaj±c siê na wielu ró¿nych
zastosowaniach, takich jak czytelno¶æ dla cz³owieka, mo¿liwo¶æ
bezpo¶redniego wykonania wyprodukowanego kodu lub zminimalizowaniu
rozmiaru zrzuconych danych.

Jeden fragment kodu jest wyj±tkiem, zawarty jest w debuggerze, w pliku
dumpvar.pl. Daje ³atwo czyteln± dla cz³owieka postaæ danych, bardzo
przydatn± przy odpluskwianiu, zawieraj±c± wiele dodatkowych informacji
nie obci±¿onych potrzeb± ponownego sk³adania oryginalnych danych.

Devel::Dumpvar jest czysto obiektowo zorientowan± implementacj± tej
samej funkcjonalno¶ci wykonan± jako modu³ Perla. Czyni to go du¿o
bardziej u¿yteczn± wersj± do zrzucania informacji do debugowych plików
logów lub innych zastosowañ gdzie nie trzeba ponownie sk³adaæ danych.

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
