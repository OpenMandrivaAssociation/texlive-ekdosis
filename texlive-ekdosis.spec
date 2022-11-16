Name:		texlive-ekdosis
Version:	61113
Release:	1
Summary:	Typesetting TEI-xml compliant Critical Editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ekdosis
License:	gpl3+ fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ekdosis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ekdosis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ekdosis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ekdosis is a LuaLaTeX package designed for multilingual
critical editions. It can be used to typeset texts and
different layers of critical notes in any direction accepted by
LuaTeX. Texts can be arranged in running paragraphs or on
facing pages, in any number of columns which in turn can be
synchronized or not. In addition to printed texts, ekdosis can
convert .tex source files so as to produce TEI xml-compliant
critical editions. Database-driven encoding under LaTeX then
allows extraction of texts entered segment by segment according
to various criteria: main edited text, variant readings,
translations or annotated borrowings between texts.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/ekdosis
%{_texmfdistdir}/tex/lualatex/ekdosis
%doc %{_texmfdistdir}/doc/lualatex/ekdosis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
