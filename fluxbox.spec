Summary:	Fluxbox is a windowmanager that is based on Blackbox
Summary(pl):	Ma³y i szybki zarz±dca okien dla X Window oparty o Blackbox
Name:		fluxbox
Version:	0.1.14
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/fluxbox/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://fluxbox.sourceforge.net/
Patch0:		%{name}-XFT.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
Obsoletes:	blackbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sysconfdir     /etc/X11/%{name}

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

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-kde \
	--enable-gnome

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/wm-properties

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wm-properties/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/fluxbox
%{_datadir}/fluxbox/*
%{_datadir}/wm-properties/fluxbox.desktop
%{_mandir}/man1/*
