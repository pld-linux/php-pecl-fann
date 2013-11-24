%define		php_name	php%{?php_suffix}
%define		modname	fann
%define		status		devel
Summary:	%{modname} - artificial neural networks
Summary(pl.UTF-8):	%{modname} - sztuczne sieci neuronowe
Name:		%{php_name}-pecl-%{modname}
Version:	0.1.1
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	5eb404da7dd1a9cec74a0ed8b5b82d47
URL:		http://pecl.php.net/package/fann/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	fann-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fann (fast artificial neural network library) implements multilayer
feedforward networks with support for both fully connected and sparse
connected networks.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Fann (biblioteka szybkich sztucznych sieci neuronowych - ang. fast
artificial neural network library) implementuje wielowarstwowe
dwustronne sieci ze wsparciem zarówno dla w pełni połączonych jak i
rzadko połączonych sieci.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc CREDITS EXPERIMENTAL
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
