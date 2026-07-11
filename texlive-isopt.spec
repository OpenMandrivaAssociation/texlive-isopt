%global tl_name isopt
%global tl_revision 45509

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Writing a TeX length with a space between number and unit
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isopt
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isopt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isopt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Writing a TeX length with \the writes the value and the unit without a
space. Package isopt provides a macro \ISO which inserts a user defined
space between number and unit.

