Name:           oolspci
Version:        0.1.0
Release:        1%{?dist}
Summary:        Lists all PCI devices, vendor identifiers, memory regions, and kernel drivers.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oolspci
Source0:        oolspci-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oolspci is a sovereign, capability-bounded PCI INSPECTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oolspci
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oolspci-uninstall

%files
/usr/bin/oolspci
/usr/bin/oolspci-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
