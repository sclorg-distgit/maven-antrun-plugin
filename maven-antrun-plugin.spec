%global pkg_name maven-antrun-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.7
Release:        8.12%{?dist}
Summary:        Maven AntRun Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-antrun-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip 
Patch0:         fix-deps.patch

BuildArch: noarch

BuildRequires: maven30-plexus-utils
BuildRequires: %{?scl_prefix_java_common}ant
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: maven30-maven-install-plugin
BuildRequires: maven30-maven-compiler-plugin
BuildRequires: maven30-maven-plugin-plugin
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-surefire-plugin
BuildRequires: maven30-maven-surefire-provider-junit
BuildRequires: maven30-maven-jar-plugin
BuildRequires: maven30-maven-javadoc-plugin


%description
Runs Ant scripts embedded in the POM

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%patch0
#%patch1
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.7-8.12
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.11
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.7-8.10
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.7-8.9
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.7-8.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.7-8
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 1.7-7
- Migrate away from mvn-rpmbuild (Resolves: #997495)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.7-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 1 2011 Alexander Kurtakov <akurtako@redhat.com> 1.7-1
- Update to 1.7 upstream release.

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 1.6-4
- Build with maven 3.x.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Alexander Kurtakov <akurtako@redhat.com> 1.6-2
- Make it work with ant 1.8.2.

* Thu Oct 14 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6-1
- Update to 1.6.

* Mon Sep 20 2010 Alexander Kurtakov <akurtako@redhat.com> 1.5-1
- Update to 1.5.
- Use upstream tarball.
- Add License and readme as doc.

* Tue Aug 31 2010 Alexander Kurtakov <akurtako@redhat.com> 1.4-4
- Fix runtime issue of not finding ant-launcher.

* Tue Aug 31 2010 Alexander Kurtakov <akurtako@redhat.com> 1.4-3
- Add patch to fix build.

* Fri May 28 2010 Alexander Kurtakov <akurtako@redhat.com> 1.4-2
- Add provides/obsoletes.

* Thu May 27 2010 Alexander Kurtakov <akurtako@redhat.com> 1.4-1
- Initial package.
