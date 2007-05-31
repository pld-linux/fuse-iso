%define		_name	fuseiso
Summary:	FUSE module to mount ISO filesystem images
Summary(pl.UTF-8):	Moduł FUSE pozwalający montować obrazy ISO
Name:		fuse-iso
Version:	20070507
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ubiz.ru/dm/%{_name}-%{version}.tar.bz2
# Source0-md5:	3de8d1f763a92b4eb03e641e820489e0
Patch0:		%{name}.patch
URL:		http://fuse.sourceforge.net/wiki/index.php/FuseIso
BuildRequires:	glib2-devel >= 1:2.2
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUSE module to mount ISO filesystem images.

%description -l pl.UTF-8
Moduł FUSE pozwalający montować obrazy ISO.

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
