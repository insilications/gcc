#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gcc
Version  : 12.1.0
Release  : 2581
URL      : file:///insilications/apps/gcc-12.1.0.tar.gz
Source0  : file:///insilications/apps/gcc-12.1.0.tar.gz
Summary  : Library supporting Foreign Function Interfaces
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
Patch1: gcc-stable-branch.patch
Patch2: optimize.patch
Patch3: vectorize.patch
Patch4: gomp-relax.patch
Patch5: avx512-when-we-ask-for-it.patch
Patch6: arch-native-override.patch
Patch7: 0001-Ignore-Werror-if-GCC_IGNORE_WERROR-environment-varia.patch
Patch8: 0001-Always-use-z-now-when-linking-with-pie.patch
Patch9: tune-inline.patch

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
%patch9 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653976025
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1f content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export CFLAGS_FOR_TARGET="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS_FOR_TARGET="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS_FOR_TARGET="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/include:/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1f end
%define gcc_target x86_64-generic-linux
%define gccpath gcc-12.1.0

if [ ! -d "../gcc-build" ]; then
    mkdir ../gcc-build;
fi

pushd ../gcc-build
../%{gccpath}/configure \
    --build=%{gcc_target} \
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
    --enable-gnu-indirect-function \
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
    --target=%{gcc_target}\
    --with-arch=native \
    --with-gcc-major-version-only \
    --with-glibc-version=2.35 \
    --with-gnu-ld \
    --with-isl \
    --with-pkgversion='Clear Linux OS for Intel Architecture'\
    --with-ppl=yes \
    --with-system-zlib \
    --with-tune=native \
    --with-zstd \
    --enable-cxx-flags="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
## make_macro content
make -j16 V=1 VERBOSE=1

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
        make -O %{?_smp_mflags} CPPFLAGS="-D_GLIBCXX_GTHREAD_USE_WEAK=0" \
             LIBGCC2_DEBUG_CFLAGS="-g -DGTHREAD_USE_WEAK=0"

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
export SOURCE_DATE_EPOCH=1653976025
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1f content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export CFLAGS_FOR_TARGET="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS_FOR_TARGET="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS_FOR_TARGET="-DNDEBUG -ggdb3 -ggnu-pubnames -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -fno-lto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -fexceptions -pthread -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/include:/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1f end
## install_macro start
pushd ../gcc-build
%make_install
cd -

mkdir -p %{buildroot}-v3/usr/libexec/gccgo/bin
rm -f %{buildroot}-v3/usr/bin/go
rm -f %{buildroot}-v3/usr/bin/gofmt
mkdir -p %{buildroot}-v4/usr/libexec/gccgo/bin
rm -f %{buildroot}-v4/usr/bin/go
rm -f %{buildroot}-v4/usr/bin/gofmt


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

%find_lang cpplib cpp.lang
%find_lang gcc tmp.lang
%find_lang libstdc++ cxx.lang
cat *.lang > gcc.lang
## install_macro end

%files
%defattr(-,root,root,-)
