Summary:	2D Quantum Monte Carlo simulator for semiconductor devices
Name:		archimedes
Version:	2.0.0
Release:	%mkrel 1
License:	GPLv3+
Group:		Sciences/Physics
URL:		http://www.gnu.org/software/archimedes/
Source0:	ftp://ftp.gnu.org/gnu/archimedes/%{name}-%{version}.tar.bz2

BuildRequires:	ghostscript-dvipdf
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

%build
%configure --enable-manual
%make

%install
rm -rf %{buildroot}

%makeinstall_std INSTALL="%{__install} -p"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc ChangeLog
%doc NEWS
%doc README
%doc THANKS
%doc doc/%{name}.dvi
%doc doc/%{name}.pdf
%doc doc/%{name}.ps
%{_bindir}/%{name}
