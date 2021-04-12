Summary:	FUSE module to mount ISO filesystem images
Summary(pl.UTF-8):	Moduł FUSE pozwalający montować obrazy ISO
Name:		fuse-iso
Version:	20070708
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://ubiz.ru/dm/fuseiso-%{version}.tar.bz2
# Source0-md5:	4bb50412b6d01f337565e28afddca3a5
Patch0:		%{name}.patch
Patch1:		%{name}-getopt_loop.patch
URL:		http://fuse.sourceforge.net/wiki/index.php/FuseIso
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.2
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUSE module to mount ISO filesystem images.

%description -l pl.UTF-8
Moduł FUSE pozwalający montować obrazy ISO.

%prep
%setup -q -n fuseiso-%{version}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
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
%attr(755,root,root) %{_bindir}/fuseiso
