%define		_modname	fann
%define		_status		devel

Summary:	%{_modname} - artificial neural networks
Summary(pl):	%{_modname} - sztuczne sieci neuronowe
Name:		php-pecl-%{_modname}
Version:	0.1.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	5eb404da7dd1a9cec74a0ed8b5b82d47
URL:		http://pecl.php.net/package/fann/
BuildRequires:	fann-devel
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Fann (fast artificial neural network library) implements multilayer
feedforward networks with support for both fully connected and sparse
connected networks.

In PECL status of this extension is: %{_status}.

%description -l pl
Fann (biblioteka szybkich sztucznych sieci neuronowych - ang. fast
artificial neural network library) implementuje wielowartswowe
dwustronne sieci ze wsparciem zar�wno dla w pe�ni po��czonych jak i
rzadko po��czonych sieci.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
