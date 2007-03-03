%define		_name	fuseiso

Summary:	FUSE module to mount ISO filesystem images
Summary(pl):	Modu³ FUSE pozwalaj±cy montowaæ obrazy ISO
Name:		fuse-iso
Version:	20061017
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ubiz.ru/dm/%{_name}-%{version}.tar.bz2
# Source0-md5:	eed65f7f73f1d7b4291e1d49ee237bb0
URL:		http://fuse.sourceforge.net/wiki/index.php/FuseIso
BuildRequires:	glib2-devel >= 2.2
BuildRequires:	libfuse-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Patch0:		%{name}.patch

%description
FUSE module to mount ISO filesystem images

%description -l pl
Modu³ FUSE pozwalaj±cy montowaæ obrazy ISO

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{_name}
