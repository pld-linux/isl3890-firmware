# TODO
# - check license
Summary:	Firmware for the ISL3880 and ISL3890 Driver
Name:		isl3890-firmware
Version:	1.0.4.3
Release:	1
License:	distributable
Group:		System Environment/Kernel
Source0:	http://prism54.org/firmware/1.0.4.3.arm
# Source0-md5:	8bd4310971772a486b9784c77f8a6df9
URL:		http://www.prism54.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the ISL3880 and ISL3890 drivers.

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
