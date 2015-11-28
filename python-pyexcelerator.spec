%define 	module	pyexcelerator
Summary:	Excel 97+ files Python generator
Summary(pl.UTF-8):	Pythonowy generator plików Excela 97+
Name:		python-%{module}
Version:	0.6.4.1
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.bz2
# Source0-md5:	8750d7242c2b2c0d496f9a2aaa083097
URL:		http://sourceforge.net/projects/pyexcelerator/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs  >= 2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generating Excel 97+ files with Python 2.4+ (need decorators),
importing Excel 95+ files, support for UNICODE in Excel files, using
variety of formatting features and printing options, Excel files and
OLE2 compound files dumper.

%description -l pl.UTF-8
Generator plików Excel 97+ wymagajacy Python 2.4 (wymaga
dekoratorów). Importuje pliki Excel 95+, wsparcie dla Unicode w
plikach Excel, używa sporej ilości formatowań i opcji drukowania.
Zrzuty plików Excela oraz plików komponentów OLE2.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%dir %{py_sitescriptdir}/pyExcelerator
%{py_sitescriptdir}/pyExcelerator/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pyExcelerator-*.egg-info
%endif
