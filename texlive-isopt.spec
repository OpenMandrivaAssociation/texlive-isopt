Name:		texlive-isopt
Version:	45509
Release:	2
Summary:	Writing a TeX length with a space between number and unit
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isopt
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isopt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isopt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Writing a TeX length with \the writes the value and the unit
without a space. Package isopt provides a macro \ISO which
inserts a user defined space between number and unit.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/isopt
%doc %{_texmfdistdir}/doc/latex/isopt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
