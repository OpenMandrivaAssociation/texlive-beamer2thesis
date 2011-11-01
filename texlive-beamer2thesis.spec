Name:		texlive-beamer2thesis
Version:	2.1
Release:	1
Summary:	Thesis presentations using beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamer2thesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer2thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer2thesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package specifies a beamer theme for presenting a thesis.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
