%define upstream_name    Config-JFDI
%define upstream_version 0.065

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Just * Do it: A Catalyst::Plugin::ConfigLoader-style layer over Config::Any
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp::Clan::Share)
BuildRequires: perl(Clone)
BuildRequires: perl(Config::Any)
BuildRequires: perl(Data::Visitor)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Hash::Merge::Simple)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Most)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


