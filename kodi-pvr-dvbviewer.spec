%global kodi_addon pvr.dvbviewer
%global kodi_version 20
%global kodi_codename Nexus

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        20.4.0
Release:        1%{?dist}
Summary:        DVBViewer PVR for Kodi

License:        GPL-2.0-or-later
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(tinyxml)
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64}

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
%cmake3
%cmake3_build


%install
%cmake3_install

# Install AppData file
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Sun Jan 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:20.4.0-1
- Update to 20.4.0
- Add AppStream metadata
- Switch to SPDX license identifiers

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:7.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:7.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:7.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.3.1-1
- Update to 7.3.1

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:7.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.2.0-1
- Update to 7.2.0

* Sat Dec 05 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.1.0-2
- Rebuild for Kodi 19.0 beta 1

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.1.0-1
- Update to 7.1.0

* Wed Aug 19 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:6.0.6-1
- Update to 6.0.6 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.7.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.7.11-1
- Update to 3.7.11

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.6.6-2
- Enable arm build

* Thu Aug 30 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.6.6-1
- Update to 3.6.6
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.3.8-1
- Update to latest stable release for Kodi 18

* Tue Feb 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.14-1
- Update to 2.4.14

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.13-1
- Update to 2.4.13

* Sat Apr 29 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.4.10-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.17-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.35-1
- Initial RPM release
