Summary:	2D Quantum Monte Carlo simulator for semiconductor devices
Name:		archimedes
Version:	2.0.1
Release:	3
License:	GPLv3+
Group:		Sciences/Physics
URL:		http://www.gnu.org/software/archimedes/
Source0:	ftp://ftp.gnu.org:21/gnu/archimedes/%{name}-%{version}.tar.bz2
BuildRequires:	dos2unix
BuildRequires:	ghostscript
BuildRequires:	tetex-latex
BuildRequires:	gcc-c++, gcc, gcc-cpp

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
export CC=gcc
export CXX=g++

%configure --enable-manual --bindir=%{_bindir} --libdir=%{_libdir}
%make

%install
make install INSTALL="%{__install} -p" DESTDIR=%{buildroot}


%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_bindir}/%{name}
