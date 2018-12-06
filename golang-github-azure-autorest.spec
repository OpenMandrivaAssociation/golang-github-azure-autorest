# Run tests in check section
%bcond_without check

# https://github.com/Azure/go-autorest
%global goipath         github.com/Azure/go-autorest
Version:                10.11.4

%global common_description %{expand:
This package implements an HTTP request pipeline suitable for use across 
multiple go-routines and provides the shared routines relied on by AutoRest 
generated Go code.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        HTTP request client for use with Autorest-generated API client packages
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/dgrijalva/jwt-go)
BuildRequires: golang(github.com/dimchansky/utfbom)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(golang.org/x/crypto/pkcs12)

%if %{with check}
BuildRequires: golang(github.com/stretchr/testify)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks -d "autorest/azure/auth"
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 10.11.4-1
- Bump to 10.11.4

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 10.3.0-1
- First package for Fedora

