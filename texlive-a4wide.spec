Name:		texlive-a4wide
Version:	20943
Release:	2
Summary:	"Wide" a4 layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/a4wide
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a4wide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a4wide.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package increases the width of the typeset area of an a4
page. This sort of operation is capable of producing
typographically poor results; the operation itself is better
provided by the geometry package. The package uses the a4
package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/a4wide/a4wide.sty
%doc %{_texmfdistdir}/doc/latex/a4wide/a4wide.pdf
%doc %{_texmfdistdir}/doc/latex/a4wide/a4wide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
