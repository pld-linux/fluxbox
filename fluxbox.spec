Summary:	Fluxbox is a windowmanager that is based on Blackbox
Summary(pl):	Ma³y i szybki zarz±dca okien dla X Window oparty o Blackbox
Summary(pt_BR):	Fluxbox é um gerenciador de janelas baseado no Blackbox
Name:		fluxbox
Version:	0.9.8
Release:	1
Epoch:         	0
License:	BSD-like
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/fluxbox/%{name}-%{version}.tar.bz2
# Source0-md5:	1f8192b768355b010ff8ae7a694bcf0c
Source1:	%{name}.desktop
Source2:        %{name}-xsession.desktop
Patch0:		%{name}-XFT.patch
Patch1:		%{name}-nls-codesets.patch
URL:		http://fluxbox.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xft-devel
Provides:	blackbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	blackbox

%define         _sysconfdir     /etc/X11/%{name}
%define		_wmpropsdir	/usr/share/wm-properties

%description
Fluxbox is yet another windowmanager for X. It's based on the Blackbox
0.61.1 code. Fluxbox looks like blackbox and handles styles, colors,
window placement and similar thing exactly like blackbox (100%
theme/style compatibility). So what's the difference between fluxbox
and blackbox then? The answer is: LOTS! Have a look at the homepage
for more info ;)

%description -l pl
Fluxbox jest zarz±dc± okien dla X Window opartym na Blackboksie
0.61.1. Jego zalet± jest estetyczny i szybki interfejs z wieloma
pulpitami i prostym menu. Wbudowano weñ tak¿e algorytm rysowania
dekoracji okien, które mog± byæ jednokolorowe, gradientowe lub
trójwymiarowe.

%description -l pt_BR
Fluxbox é um gerenciador de janelas para X. Ele é baseado no código do
Blackbox 0.61.1. Fluxbox tem a aparência do blackbox e pode utilizar
seus estilos, cores e temas. Então qual a diferença entre o fluxbox e
o blackbox?

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-slit \
	--enable-kde \
	--enable-gnome

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/fluxbox
%{_datadir}/fluxbox/[!n]*
%dir %{_datadir}/fluxbox/nls
%{_datadir}/fluxbox/nls/C
%{_datadir}/fluxbox/nls/POSIX
%{_datadir}/fluxbox/nls/US_ASCII
%{_datadir}/fluxbox/nls/en*
%lang(bg) %{_datadir}/fluxbox/nls/bg*
%lang(da) %{_datadir}/fluxbox/nls/da*
%lang(de) %{_datadir}/fluxbox/nls/de*
%lang(es) %{_datadir}/fluxbox/nls/es*
%lang(et) %{_datadir}/fluxbox/nls/et*
%lang(fr) %{_datadir}/fluxbox/nls/fr*
%lang(it) %{_datadir}/fluxbox/nls/it*
%lang(ja) %{_datadir}/fluxbox/nls/ja*
%lang(lv) %{_datadir}/fluxbox/nls/lv*
%lang(nl) %{_datadir}/fluxbox/nls/nl*
%lang(pt) %{_datadir}/fluxbox/nls/pt_PT
%lang(pt_BR) %{_datadir}/fluxbox/nls/pt_BR
%lang(ru) %{_datadir}/fluxbox/nls/ru*
%lang(sv) %{_datadir}/fluxbox/nls/sv*
%lang(tr) %{_datadir}/fluxbox/nls/tr*
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/fluxbox.desktop
%{_mandir}/man1/*
