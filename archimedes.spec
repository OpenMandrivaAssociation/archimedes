Summary:	2D Quantum Monte Carlo simulator for semiconductor devices
Name:		archimedes
Version:	2.0.0
Release:	%mkrel 1
License:	GPLv3+
Group:		Sciences/Physics
URL:		http://www.gnu.org/software/archimedes/
Source0:	ftp://ftp.gnu.org/gnu/archimedes/%{name}-%{version}.tar.bz2
BuildRequires:	dos2unix
BuildRequires:	ghostscript
BuildRequires:	tetex-latex

%description
Archimedes is a package for the design and simulation of submicron
semiconductor devices. It is a 2D Fast Monte Carlo simulator which can take
into account all the relevant quantum effects, thank to the implementation of
the Bohm effective potential method.

The physics and geometry of a general device is introduced by typing a simple
script, which makes, in this sense, Archimedes a powerful tool for the
simulation of quite general semiconductor devices.

%prep
%setup -q

# Suppress rpmlint error.
dos2unix COPYING

%build
%configure --enable-manual --bindir=%{_bindir} --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc NEWS
%doc README
%doc THANKS
%{_bindir}/%{name}


%changelog
* Thu Oct 27 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 707526
- imported package archimedes

  + Andrey Smirnov <asmirnov@mandriva.org>
    - import archimedes

