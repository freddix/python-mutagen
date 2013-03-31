%define		module	mutagen

Summary:	Audio metadata reader/writer
Name:		python-%{module}
Version:	1.21
Release:	1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://mutagen.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	7491af5d04706b1f60fcab71aadfd27f
URL:		http://code.google.com/p/quodlibet/wiki/Mutagen
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutagen is an audio metadata tag reader and writer implemented in pure
Python. It supports reading ID3v1.1, ID3v2.2, ID3v2.3, ID3v2.4, APEv2,
and FLAC, and writing ID3v1.1, ID3v2.4, APEv2, and FLAC.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO TUTORIAL
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}
%{_mandir}/man1/*

