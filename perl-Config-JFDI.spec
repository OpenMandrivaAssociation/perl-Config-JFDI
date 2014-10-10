%define upstream_name    Config-JFDI
%define upstream_version 0.065

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Just * Do it: A Catalyst::Plugin::ConfigLoader-style layer over Config::Any
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Carp::Clan::Share)
BuildRequires:	perl(Clone)
BuildRequires:	perl(Config::Any)
BuildRequires:	perl(Data::Visitor)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Hash::Merge::Simple)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::AttributeHelpers)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildArch:	noarch

%description
Config::JFDI is an implementation of the Catalyst::Plugin::ConfigLoader
manpage that exists outside of the Catalyst manpage.

Essentially, Config::JFDI will scan a directory for files matching a
certain name. If such a file is found which also matches an extension that
Config::Any can read, then the configuration from that file will be loaded.

Config::JFDI will also look for special files that end with a "_local"
suffix. Files with this special suffix will take precedence over any other
existing configuration file, if any. The precedence takes place by merging
the local configuration with the "standard" configuration via the
Hash::Merge::Simple manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.65.0-2mdv2011.0
+ Revision: 654283
- rebuild for updated spec-helper

* Sun Jan 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.65.0-1mdv2011.0
+ Revision: 627632
- update to new version 0.065

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.64.0-1mdv2011.0
+ Revision: 471075
- import perl-Config-JFDI


* Sun Nov 29 2009 cpan2dist 0.064-1mdv
- initial mdv release, generated with cpan2dist
