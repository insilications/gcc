#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gcc
Version  : 12.1.0
Release  : 2596
URL      : file:///insilications/apps/gcc-12.1.0.tar.gz
Source0  : file:///insilications/apps/gcc-12.1.0.tar.gz
Summary  : zlib compression library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0-with-GCC-exception GPL-3.0 GPL-3.0+ GPL-3.0-with-GCC-exception LGPL-2.0+ LGPL-2.1 bzip2-1.0.6
Requires: gcc-doc
Requires: gcc-libubsan
Provides: cpp
Provides: cpp-symlinks
Provides: g++
Provides: g++-symlinks
Provides: g77
Provides: g77-symlinks
Provides: gcc-symlinks
Provides: gcov
Provides: gfortran
Provides: gfortran-symlinks
BuildRequires : Sphinx
BuildRequires : autogen
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : buildreq-golang
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expect
BuildRequires : flex
BuildRequires : gdb-dev
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gmp-dev
BuildRequires : gmp-dev32
BuildRequires : gmp-staticdev
BuildRequires : gmp-staticdev32
BuildRequires : graphviz
BuildRequires : grep
BuildRequires : guile
BuildRequires : libc6
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libstdc++
BuildRequires : libunwind-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses-dev
BuildRequires : perl
BuildRequires : pkgconfig(zlib)
BuildRequires : procps-ng
BuildRequires : procps-ng-dev
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sed
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : valgrind-dev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-optimize.patch
Patch2: 0002-vectorize.patch
Patch3: 0003-gomp-relax.patch
Patch4: 0004-avx512-when-we-ask-for-it.patch
Patch5: 0005-arch-native-override.patch
Patch6: 0006-Ignore-Werror-if-GCC_IGNORE_WERROR-envvar-set.patch
Patch7: 0007-Always-use-z-now-when-linking-with-pie.patch
Patch8: 0008-tune-inline.patch

%description
This directory contains the GNU Compiler Collection (GCC).
The GNU Compiler Collection is free software.  See the files whose
names start with COPYING for copying permission.  The manuals, and
some of the runtime libraries, are under different terms; see the
individual source files for details.

%prep
%setup -q -n gcc-12.1.0
cd %{_builddir}/gcc-12.1.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1654522040
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1f content
## altflags1
unset ASFLAGS
export CFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export ASMFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export CXXFLAGS="-fvisibility-inlines-hidden -fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export FCFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export FFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export LDFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export CFLAGS_FOR_TARGET="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export CXXFLAGS_FOR_TARGET="-fvisibility-inlines-hidden -fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export FFLAGS_FOR_TARGET="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export CPATH=/usr/include
export LIBRARY_PATH=%{_libdir}
export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1f end
%define gccpath gcc-12.1.0
%define gcc_target x86_64-generic-linux

export CPATH=/usr/include
export LIBRARY_PATH=%{_libdir}

if [ ! -d "../gcc-build" ]; then
    mkdir ../gcc-build;
fi

pushd ../gcc-build
../%{gccpath}/configure \
    --build=x86_64-generic-linux \
    --target=x86_64-generic-linux \
    --disable-libmpx \
    --disable-libunwind-exceptions \
    --disable-multiarch \
    --disable-vtable-verify \
    --disable-werror \
    --disable-bootstrap \
    --disable-cet \
    --disable-default-ssp \
    --enable-clocale=gnu \
    --enable-__cxa_atexit \
    --disable-default-pie \
    --disable-gnu-indirect-function \
    --enable-host-shared \
    --enable-languages="c,c++,fortran,go,jit" \
    --enable-ld=default \
    --enable-libstdcxx-pch \
    --enable-linker-build-id \
    --enable-linux-futex \
    --enable-lto \
    --with-pic \
    --enable-multilib \
    --enable-plugin \
    --enable-shared \
    --enable-threads=posix \
    --exec-prefix=/usr \
    --includedir=/usr/include \
    --libdir=/usr/lib64 \
    --libexecdir=/usr/lib64 \
    --prefix=/usr \
    --with-gcc-major-version-only \
    --with-glibc-version=2.35 \
    --with-gnu-ld \
    --with-isl \
    --with-pkgversion='Clear Linux OS for Intel Architecture' \
    --with-ppl=yes \
    --with-system-zlib \
    --with-arch=native \
    --with-tune=native \
    --enable-cxx-flags="-fvisibility-inlines-hidden -fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline" \
    --with-zstd
## make_macro content
# make -j14 V=1 profiledbootstrap

make -O -j15 V=1

popd

# Work around libstdc++'s use of weak symbols to libpthread in static
# mode: libpthread doesn't get pulled in and therefore we get crashes
# due to the calls being resolved to address 0x0.
# We rebuild the .a without weak symbols.
# See:
#  https://sourceware.org/bugzilla/show_bug.cgi?id=5784
#  https://gcc.gnu.org/bugzilla/show_bug.cgi?id=78017
#  (and more)
for dir in ../gcc-build/x86_64-generic-linux/{,32}; do
    for lib in libstdc++-v3/libsupc++ libstdc++-v3/src; do
        pushd $dir/$lib
        # Save any shared libraries
        mv .libs saved.libs || :
        rename lib savedlib lib*.so.* || :

        make clean
        make -O -j14 CPPFLAGS="-D_GLIBCXX_GTHREAD_USE_WEAK=0" \
             LIBGCC2_DEBUG_CFLAGS="-g3 -DGTHREAD_USE_WEAK=0 -fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"

        # Restore the saved shared libraries (if any)
        rename savedlib lib savedlib* || :
        if [ -d saved.libs ]; then
            mv saved.libs/*.so.* .libs || :
        fi

        # Update timestamps so make install won't recreate
        find -name '*.so*' | xargs -rt touch -r `find -name '*.a' | head -1`
        popd
    done
done
## make_macro end


%install
export SOURCE_DATE_EPOCH=1654522040
rm -rf %{buildroot}
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1f content
## altflags1
unset ASFLAGS
export CFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export ASMFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export CXXFLAGS="-fvisibility-inlines-hidden -fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export FCFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export FFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export LDFLAGS="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export CFLAGS_FOR_TARGET="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export CXXFLAGS_FOR_TARGET="-fvisibility-inlines-hidden -fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export FFLAGS_FOR_TARGET="-fno-lto -g3 -fPIC -O3 -mno-vzeroupper -march=native -mtune=native -mavx -mavx2 -msse2avx -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -floop-nest-optimize -floop-block -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-plt -fno-stack-protector -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -flive-range-shrinkage -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -fno-reorder-blocks-and-partition -Wl,--emit-relocs -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export CPATH=/usr/include
export LIBRARY_PATH=%{_libdir}
export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1f end
## install_macro start
%define gccpath gcc-12.1.0
%define gcc_target x86_64-generic-linux

pushd ../gcc-build
%make_install

if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
    pushd %{buildroot}/usr/share/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi

cd -

cd %{buildroot}/usr/bin
if [ -e %{gcc_target}-g77 ]; then
    ln -sf %{gcc_target}-g77 g77 || true
    ln -sf g77 f77 || true
fi
if [ -e x86_64-generic-linux-gfortran ]; then
    ln -sf %{gcc_target}-gfortran gfortran || true
    ln -sf gfortran f95 || true
fi
ln -sf %{gcc_target}-g++ g++
ln -sf %{gcc_target}-gcc gcc
#ln -sf %{gcc_target}-cpp cpp
install -d %{buildroot}/usr/lib
ln -sf ../bin/cpp %{buildroot}/usr/lib/cpp
ln -sf g++ c++
ln -sf gcc cc
cd -

# This conflicts with golang, stash away
# We use gccgo to build golang
mkdir -p %{buildroot}/usr/libexec/gccgo/bin
mv %{buildroot}/usr/bin/go %{buildroot}/usr/libexec/gccgo/bin
mv %{buildroot}/usr/bin/gofmt %{buildroot}/usr/libexec/gccgo/bin

find %{buildroot}/usr/ -name libiberty.a | xargs rm -f
find %{buildroot}/usr/ -name libiberty.h | xargs rm -f
chmod 0755 %{buildroot}*/usr/lib64/libgcc_s.so.1
chmod 0755 %{buildroot}*/usr/lib32/libgcc_s.so.1

chmod a+x %{buildroot}*/usr/bin
chmod a+x %{buildroot}*/usr/lib64
find %{buildroot}*/usr/lib64 %{buildroot}/usr/lib*/gcc -name '*.so*' -print0 | xargs -r0 chmod -f 755
find %{buildroot}*/usr/lib64 %{buildroot}/usr/lib*/gcc -name '*.o' -print0 | xargs -r0 chmod -f 644


# This is only for gdb
mkdir -p %{buildroot}//usr/share/gdb/auto-load//usr/lib64
mkdir -p %{buildroot}//usr/share/gdb/auto-load//usr/lib32
mv %{buildroot}//usr/lib64/libstdc++.so.*-gdb.py %{buildroot}//usr/share/gdb/auto-load//usr/lib64/.
mv %{buildroot}//usr/lib32/libstdc++.so.*-gdb.py %{buildroot}//usr/share/gdb/auto-load//usr/lib32/.

# merge the two C++ include trees (needed for Clang)
pushd %{buildroot}/usr/include/c++/*/x86_64-generic-linux
find -type f \! -path ./32/\* | while read f; do
    cmp -s $f 32/$f && continue
    (
        echo '#ifdef __LP64__'
        cat $f
        echo '#else'
        cat 32/$f
        echo '#endif'
    ) > rpm-tmp-hdr
    mv rpm-tmp-hdr $f
done
for f in ./32/*; do
  rm -rf $f
  ln -s ../$(basename $f) $f
done
popd

# Also clang compat
(cd %{buildroot}/usr/lib64 && ln -s -t . gcc/x86_64-generic-linux/*/*.[ao])
(cd %{buildroot}/usr/lib32 && ln -s -t . ../lib64/gcc/x86_64-generic-linux/*/32/*.[ao])
## install_macro end
## custom find_lang start
%find_lang cpplib cpp.lang
%find_lang gcc tmp.lang
%find_lang libstdc++ cxx.lang
cat *.lang > gcc.lang
## custom find_lang end

%files
%defattr(-,root,root,-)
