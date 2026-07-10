%global tl_name a4wide
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Wide a4 layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/a4wide
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a4wide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a4wide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package increases the width of the typeset area of an a4 page. This
sort of operation is capable of producing typographically poor results;
the operation itself is better provided by the geometry package. The
package uses the a4 package.

