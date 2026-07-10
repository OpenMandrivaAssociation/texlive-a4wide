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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package increases the width of the typeset area of an a4 page. This
sort of operation is capable of producing typographically poor results;
the operation itself is better provided by the geometry package. The
package uses the a4 package.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/a4wide
%dir %{_datadir}/texmf-dist/tex/latex/a4wide
%doc %{_datadir}/texmf-dist/doc/latex/a4wide/a4wide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/a4wide/a4wide.tex
%{_datadir}/texmf-dist/tex/latex/a4wide/a4wide.sty
