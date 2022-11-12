Name:		texlive-beamer2thesis
Version:	27539
Release:	1
Summary:	Thesis presentations using beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamer2thesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer2thesis.r27539.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer2thesis.doc.r27539.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package specifies a beamer theme for presenting a thesis.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamer2thesis/beamer2thesis.jpg
%{_texmfdistdir}/tex/latex/beamer2thesis/beamercolorthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerfontthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerinnerthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerouterthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerthemeTorinoTh.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/logopolito.jpg
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/README
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis.pdf
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis.tex
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis_ita.pdf
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis_ita.tex
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/content_end.tex
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/content_end_ita.tex
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/content_initial.tex
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/content_initial_ita.tex
%doc %{_texmfdistdir}/doc/latex/beamer2thesis/license

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
