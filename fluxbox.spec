Summary:	Fluxbox is a windowmanager that is based on Blackbox
Summary(pl):    Ma³y i szybki menad¿er okien dla X Window oparty o Blackbox
Name:		fluxbox
Version:	0.1.7
Release:	1
Group:		X11/Window Managers
License:	GPL
URL:		http://fluxbox.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/fluxbox/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
BuildRequires:	XFree86-devel
Obsoletes:	blackbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man
%define         _sysconfdir     /etc/X11/%{name}

%define         _gcc_ver        %(%{__cc} --version | cut -b 1)
%if %{_gcc_ver} == 2
%define         __cxx           "%{__cc}"
%endif

%description

Fluxbox is yet another windowmanager for X. It's based on the Blackbox
0.61.1 code. Fluxbox looks like blackbox and handles styles, colors,
window placement and similar thing exactly like blackbox (100%
theme/style compatibility). So what's the difference between fluxbox
and blackbox then? The answer is: LOTS!
Have a look at the homepage for more info ;)

%description -l pl
Fluxbox jest mened¿erem okien dla X Window opartym na Blackbox 0.61.1
Jego zalet± jest estetyczny i szybki interfejs z wieloma pulpitami 
i prostym menu. Wbudowano weñ tak¿e algorytm rysowania dekoracji okien, 
które mog± byæ jednokolorowe, gradientowe lub trójwymiarowe. 

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
#aclocal
#autoconf
#automake -a -c
./configure  --enable-kde \
             --prefix=/usr/X11R6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/wm-properties

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wm-properties/

gzip -9nf AUTHORS COPYING ChangeLog INSTALL NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/fluxbox
%{_datadir}/fluxbox/*
%{_datadir}/wm-properties/fluxbox.desktop
%{_mandir}/man1/*
