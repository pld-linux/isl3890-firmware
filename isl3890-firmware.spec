# TODO
# - check license
Summary:	Firmware for the ISL3880 and ISL3890 drivers
Summary(pl.UTF-8):	Firmware dla sterowników ISL3880 i ISL3890
Name:		isl3890-firmware
Version:	1.0.4.3
Release:	2
License:	distributable
Group:		Base/Kernel
Source0:	http://prism54.org/firmware/1.0.4.3.arm
# Source0-md5:	8bd4310971772a486b9784c77f8a6df9
URL:		http://www.prism54.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the ISL3880 and ISL3890
drivers.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla sterowników ISL3880 i ISL3890.

%prep
%setup -qcT
cp %{SOURCE0} isl3890

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a isl3890 $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/isl3890
