Summary:	Fluxbox is a windowmanager that is based on Blackbox
Summary(pl):	Ma³y i szybki zarz±dca okien dla X Window oparty o Blackbox
Summary(pt_BR):	Fluxbox é um gerenciador de janelas baseado no Blackbox
Name:		fluxbox
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/fluxbox/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://fluxbox.sourceforge.net/
Patch0:		%{name}-XFT.patch
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-xft-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Obsoletes:	blackbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
rm -rf $RPM_BUILD_ROOT
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-kde

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_wmpropsdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/fluxbox
%{_datadir}/fluxbox/*
%{_wmpropsdir}/fluxbox.desktop
%{_mandir}/man1/*
