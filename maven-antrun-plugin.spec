%{?scl:%scl_package maven-antrun-plugin}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-antrun-plugin
Version:        1.8
Release:        4.2%{?dist}
Summary:        Maven AntRun Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-antrun-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip 

BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.ant:ant)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)

%description
This plugin provides the ability to run Ant tasks from within Maven.
It is even possible to embed Ant scripts in the POM.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q 

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.8-4.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.8-4.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Michal Srb <msrb@redhat.com> - 1.8-1
- Update to upstream release 1.8

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-10
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-9
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.7-7
- Use Requires: java-headless rebuild (#1067528)

* Mon Sep 02 2013 Michal Srb <msrb@redhat.com> - 1.7-6
- Adapt to current guidelines

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
