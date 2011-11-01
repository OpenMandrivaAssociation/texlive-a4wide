Name:		texlive-a4wide
Version:	20110105
Release:	1
Summary:	"Wide" a4 layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/a4wide
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a4wide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a4wide.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package increases the width of the typeset area of an a4
page. This sort of operation is capable of producing
typographically poor results; the operation itself is better
provided by the geometry package. The package uses the a4
package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/a4wide/a4wide.sty
%doc %{_texmfdistdir}/doc/latex/a4wide/a4wide.pdf
%doc %{_texmfdistdir}/doc/latex/a4wide/a4wide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
