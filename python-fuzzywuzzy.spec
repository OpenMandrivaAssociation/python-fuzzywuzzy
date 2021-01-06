# Created by pyp2rpm-3.3.5
%global pypi_name fuzzywuzzy

Name:           python-%{pypi_name}
Version:        0.18.0
Release:        1
Summary:        Fuzzy string matching in python
Group:          Development/Python
License:        GPLv2
URL:            https://github.com/seatgeek/fuzzywuzzy
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(python-levenshtein) >= 0.12
BuildRequires:  python3dist(setuptools)

%description
FuzzyWuzzy Fuzzy string matching like a boss. It uses Levenshtein Distance < to
calculate the differences between sequences in a simple-to-use
package.Requirements - Python 2.7 or higher - difflib - python-Levenshtein <
(optional, provides a 4-10x speedup in String Matching, though may result in
differing results for certain cases <

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
