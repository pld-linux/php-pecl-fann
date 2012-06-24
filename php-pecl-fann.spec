%define		_modname	fann
%define		_status		devel
Summary:	%{_modname} - artificial neural networks
Summary(pl.UTF-8):	%{_modname} - sztuczne sieci neuronowe
Name:		php-pecl-%{_modname}
Version:	0.1.1
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	5eb404da7dd1a9cec74a0ed8b5b82d47
URL:		http://pecl.php.net/package/fann/
BuildRequires:	fann-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fann (fast artificial neural network library) implements multilayer
feedforward networks with support for both fully connected and sparse
connected networks.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Fann (biblioteka szybkich sztucznych sieci neuronowych - ang. fast
artificial neural network library) implementuje wielowarstwowe
dwustronne sieci ze wsparciem zarówno dla w pełni połączonych jak i
rzadko połączonych sieci.

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
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
