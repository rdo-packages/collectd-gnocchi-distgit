# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%global pypi_name collectd-gnocchi
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        1.7.1
Release:        1%{?dist}
Summary:        Gnocchi storage plugin for collectd

License:        ASL 2.0
URL:            https://github.com/gnocchixyz/collectd-gnocchi
Source0:        https://github.com/gnocchixyz/collectd-gnocchi/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr >= 2.0.0
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  git
Requires:       collectd-python

%description
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%package -n     python%{pyver}-%{pypi_name}
Summary:        Gnocchi storage plugin for collectd
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}
%if %{pyver} == 3
Obsoletes: python2-%{pypi_name} < %{version}-%{release}
%endif

Requires:       python%{pyver}-gnocchiclient >= 4.0.0
Requires:       python%{pyver}-keystoneauth1 >= 3.3.0
%description -n python%{pyver}-%{pypi_name}
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{pyver_build}

%install
%{pyver_install}


%files -n python%{pyver}-%{pypi_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/collectd_gnocchi
%{pyver_sitelib}/collectd_gnocchi-*-py*.egg-info

%changelog
* Fri Sep 14 2018 RDO <dev@lists.rdoproject.org> 1.7.1-1
- Update to 1.7.1

