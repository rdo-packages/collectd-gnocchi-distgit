%global pypi_name collectd-gnocchi
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Gnocchi storage plugin for collectd

License:        Apache-2.0
URL:            https://github.com/gnocchixyz/collectd-gnocchi
Source0:        https://github.com/gnocchixyz/collectd-gnocchi/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  git-core

%description
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%package -n     python3-%{pypi_name}
Summary:        Gnocchi storage plugin for collectd

%description -n python3-%{pypi_name}
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

sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/collectd_gnocchi
%{python3_sitelib}/collectd_gnocchi-*-py*.dist-info

%changelog
