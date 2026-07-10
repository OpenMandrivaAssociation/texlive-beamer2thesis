%global tl_name beamer2thesis
%global tl_revision 72949

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Thesis presentations using beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamer2thesis
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer2thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer2thesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package specifies a beamer theme for presenting a thesis.

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
%dir %{_datadir}/texmf-dist/doc/latex/beamer2thesis
%dir %{_datadir}/texmf-dist/tex/latex/beamer2thesis
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/README
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/beamer2thesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/beamer2thesis.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/beamer2thesis_ita.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/beamer2thesis_ita.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/content_end.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/content_end_ita.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/content_initial.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/content_initial_ita.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer2thesis/license
%{_datadir}/texmf-dist/tex/latex/beamer2thesis/beamer2thesis.jpg
%{_datadir}/texmf-dist/tex/latex/beamer2thesis/beamercolorthemetorinoth.sty
%{_datadir}/texmf-dist/tex/latex/beamer2thesis/beamerfontthemetorinoth.sty
%{_datadir}/texmf-dist/tex/latex/beamer2thesis/beamerinnerthemetorinoth.sty
%{_datadir}/texmf-dist/tex/latex/beamer2thesis/beamerouterthemetorinoth.sty
%{_datadir}/texmf-dist/tex/latex/beamer2thesis/beamerthemeTorinoTh.sty
%{_datadir}/texmf-dist/tex/latex/beamer2thesis/logopolito.jpg
