%if 0%{?fedora} > 1
%global with_python3 1
%else
%global with_python3 0
%endif

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

BuildRequires:  python2-devel
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-setuptools
BuildRequires:  git
Requires:       collectd-python

%description
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%package -n     python2-%{pypi_name}
Summary:        Gnocchi storage plugin for collectd
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-gnocchiclient >= 4.0.0
Requires:       python2-keystoneauth1 >= 3.3.0
%description -n python2-%{pypi_name}
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%if 0%{?with_python3} > 0
%package -n     python3-%{pypi_name}
Summary:        Gnocchi storage plugin for collectd
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:       python3-gnocchiclient >= 4.0.0
Requires:       python3-keystoneauth1 >= 3.3.0
%description -n python3-%{pypi_name}
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if 0%{?with_python3} > 0
%py3_build
%endif

%install
%if 0%{?with_python3} > 0
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
%endif

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/collectd_gnocchi
%{python2_sitelib}/collectd_gnocchi-*-py*.egg-info

%if 0%{?with_python3} > 0
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/collectd_gnocchi
%{python3_sitelib}/collectd_gnocchi-*-py*.egg-info
%endif

%changelog
* Fri Sep 14 2018 RDO <dev@lists.rdoproject.org> 1.7.1-1
- Update to 1.7.1

