#
# Conditional build:
%bcond_without	imlib2		# disable imlib2 (pixmap themes) support
#
Summary:	Fluxbox - a windowmanager that is based on Blackbox
Summary(de.UTF-8):	Fluxbox - ein weiterer Window Manager für X
Summary(pl.UTF-8):	Mały i szybki zarządca okien dla X Window oparty o Blackbox
Summary(pt_BR.UTF-8):	Fluxbox é um gerenciador de janelas baseado no Blackbox
Name:		fluxbox
Version:	1.3.1
Release:	1
Epoch:		1
License:	MIT-like
Group:		X11/Window Managers
Source0:	http://downloads.sourceforge.net/fluxbox/%{name}-%{version}.tar.bz2
# Source0-md5:	0eaa940a69c0a876a520bb85d67b8bec
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Source3:	%{name}-pld.style
Source4:	%{name}-pld.jpg
Source5:	%{name}.menu
URL:		http://fluxbox.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_imlib2:BuildRequires:	imlib2-devel >= 1.0.0}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
%{?with_imlib2:BuildRequires:	xorg-lib-libXpm-devel}
BuildRequires:	xorg-lib-libXrandr-devel
Requires(post):	vfmg >= 0.9.95
Requires:	WindowMaker
Requires:	gxmessage
Requires:	vfmg >= 0.9.16-3
Provides:	blackbox
Obsoletes:	blackbox
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sysconfdir     /etc/X11/%{name}
%define		_wmpropsdir	/usr/share/gnome/wm-properties

%description
Fluxbox is yet another windowmanager for X. It's based on the Blackbox
0.61.1 code. Fluxbox looks like blackbox and handles styles, colors,
window placement and similar thing exactly like blackbox (100%
theme/style compatibility). So what's the difference between fluxbox
and blackbox then? The answer is: LOTS! Have a look at the homepage
for more info ;)

%description -l pl.UTF-8
Fluxbox jest zarządcą okien dla X Window opartym na Blackboksie
0.61.1. Jego zaletą jest estetyczny i szybki interfejs z wieloma
pulpitami i prostym menu. Wbudowano weń także algorytm rysowania
dekoracji okien, które mogą być jednokolorowe, gradientowe lub
trójwymiarowe.

%description -l pt_BR.UTF-8
Fluxbox é um gerenciador de janelas para X. Ele é baseado no código do
Blackbox 0.61.1. Fluxbox tem a aparência do blackbox e pode utilizar
seus estilos, cores e temas. Então qual a diferença entre o fluxbox e
o blackbox?

%description -l de.UTF-8
Fluxbox ist ein weiterer Window Manager für X basierend auf dem
Quellcode von Blackbox 0.61.1. Fluxbox ähnelt Blackbox und behandelt
Styles, Farben, Fensterplatzierungen und ähnliche Dinge genauso wie
Blackbox. Es ist somit 100% kompatibel zu den Blackbox Themes und
Styles.

%prep
%setup -q

echo "session.screen0.antialias: true" >> data/init.in

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-slit \
	--enable-gnome \
	--enable-xinerama \
	--enable-nls \
	--enable-xft \
	--enable-randr \
	%{?with_imlib2:--enable-imlib2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/{xsessions,wallpapers,%{name}/styles},%{_wmpropsdir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/styles/PLD
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/wallpapers
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/fluxbox/menu
touch $RPM_BUILD_ROOT%{_sysconfdir}/menu2

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/fluxbox/nls/no*

%clean
rm -rf $RPM_BUILD_ROOT

%post
# generate initial menu
[ -f /etc/sysconfig/vfmg ] && . /etc/sysconfig/vfmg
[ "$FLUXBOX" = yes -o "$FLUXBOX" = 1 -o ! -f %{_sysconfdir}/menu2 ] && \
	vfmg fluxbox > %{_sysconfdir}/menu2 2>/dev/null ||:

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/fbrun
%attr(755,root,root) %{_bindir}/fbsetbg
%attr(755,root,root) %{_bindir}/fbsetroot
%attr(755,root,root) %{_bindir}/fluxbox
%attr(755,root,root) %{_bindir}/fluxbox-generate_menu
%attr(755,root,root) %{_bindir}/fluxbox-remote
%attr(755,root,root) %{_bindir}/fluxbox-update_configs
%attr(755,root,root) %{_bindir}/startfluxbox
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/menu2
%dir %{_datadir}/fluxbox
%{_datadir}/fluxbox/[!n]*
%dir %{_datadir}/fluxbox/nls
%{_datadir}/fluxbox/nls/C
%lang(be) %{_datadir}/fluxbox/nls/be*
%lang(bg) %{_datadir}/fluxbox/nls/bg*
%lang(cs) %{_datadir}/fluxbox/nls/cs*
%lang(da) %{_datadir}/fluxbox/nls/da*
%lang(de) %{_datadir}/fluxbox/nls/de*
%lang(el) %{_datadir}/fluxbox/nls/el*
%lang(en) %{_datadir}/fluxbox/nls/en*
%lang(es) %{_datadir}/fluxbox/nls/es*
%lang(et) %{_datadir}/fluxbox/nls/et*
%lang(fi) %{_datadir}/fluxbox/nls/fi*
%lang(fr) %{_datadir}/fluxbox/nls/fr*
%lang(it) %{_datadir}/fluxbox/nls/it*
%lang(ja) %{_datadir}/fluxbox/nls/ja*
%lang(ko) %{_datadir}/fluxbox/nls/ko*
%lang(lv) %{_datadir}/fluxbox/nls/lv*
%lang(mk) %{_datadir}/fluxbox/nls/mk_MK*
%lang(nb) %{_datadir}/fluxbox/nls/nb*
%lang(nl) %{_datadir}/fluxbox/nls/nl*
%lang(pl) %{_datadir}/fluxbox/nls/pl*
%lang(pt_BR) %{_datadir}/fluxbox/nls/pt_BR*
%lang(pt) %{_datadir}/fluxbox/nls/pt_PT*
%lang(ru) %{_datadir}/fluxbox/nls/ru*
%lang(sk) %{_datadir}/fluxbox/nls/sk*
%lang(sl) %{_datadir}/fluxbox/nls/sl*
%lang(sv) %{_datadir}/fluxbox/nls/sv*
%lang(tr) %{_datadir}/fluxbox/nls/tr*
%lang(uk) %{_datadir}/fluxbox/nls/uk*
%lang(vi) %{_datadir}/fluxbox/nls/vi*
%lang(zh_CN) %{_datadir}/fluxbox/nls/zh_CN*
%lang(zh_TW) %{_datadir}/fluxbox/nls/zh_TW*
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/fluxbox.desktop
%{_datadir}/wallpapers/*.jpg
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
