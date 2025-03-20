#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-questionr
Version  : 0.8.0
Release  : 64
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/questionr_0.8.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/questionr_0.8.0.tar.gz
Summary  : Functions to Make Surveys Processing Easier
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-classInt
Requires: R-highr
Requires: R-htmltools
Requires: R-labelled
Requires: R-miniUI
Requires: R-rlang
Requires: R-rstudioapi
Requires: R-shiny
Requires: R-styler
BuildRequires : R-classInt
BuildRequires : R-highr
BuildRequires : R-htmltools
BuildRequires : R-janitor
BuildRequires : R-labelled
BuildRequires : R-miniUI
BuildRequires : R-rlang
BuildRequires : R-rstudioapi
BuildRequires : R-shiny
BuildRequires : R-styler
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n questionr
pushd ..
cp -a questionr buildavx2
popd
pushd ..
cp -a questionr buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742515018

%install
export SOURCE_DATE_EPOCH=1742515018
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/questionr/DESCRIPTION
/usr/lib64/R/library/questionr/INDEX
/usr/lib64/R/library/questionr/Meta/Rd.rds
/usr/lib64/R/library/questionr/Meta/data.rds
/usr/lib64/R/library/questionr/Meta/features.rds
/usr/lib64/R/library/questionr/Meta/hsearch.rds
/usr/lib64/R/library/questionr/Meta/links.rds
/usr/lib64/R/library/questionr/Meta/nsInfo.rds
/usr/lib64/R/library/questionr/Meta/package.rds
/usr/lib64/R/library/questionr/Meta/vignette.rds
/usr/lib64/R/library/questionr/NAMESPACE
/usr/lib64/R/library/questionr/NEWS.md
/usr/lib64/R/library/questionr/R/questionr
/usr/lib64/R/library/questionr/R/questionr.rdb
/usr/lib64/R/library/questionr/R/questionr.rdx
/usr/lib64/R/library/questionr/data/datalist
/usr/lib64/R/library/questionr/data/fecondite.RData
/usr/lib64/R/library/questionr/data/fertility.RData
/usr/lib64/R/library/questionr/data/happy.RData
/usr/lib64/R/library/questionr/data/hdv2003.RData
/usr/lib64/R/library/questionr/data/rp2012.RData
/usr/lib64/R/library/questionr/data/rp2018.RData
/usr/lib64/R/library/questionr/doc/index.html
/usr/lib64/R/library/questionr/doc/recoding_addins.Rmd
/usr/lib64/R/library/questionr/doc/recoding_addins.html
/usr/lib64/R/library/questionr/help/AnIndex
/usr/lib64/R/library/questionr/help/aliases.rds
/usr/lib64/R/library/questionr/help/paths.rds
/usr/lib64/R/library/questionr/help/questionr.rdb
/usr/lib64/R/library/questionr/help/questionr.rdx
/usr/lib64/R/library/questionr/html/00Index.html
/usr/lib64/R/library/questionr/html/R.css
/usr/lib64/R/library/questionr/po/en/LC_MESSAGES/R-questionr.mo
/usr/lib64/R/library/questionr/po/en@quot/LC_MESSAGES/R-questionr.mo
/usr/lib64/R/library/questionr/po/fr/LC_MESSAGES/R-questionr.mo
/usr/lib64/R/library/questionr/rstudio/addins.dcf
/usr/lib64/R/library/questionr/shiny/css/ifuncs.css
/usr/lib64/R/library/questionr/shiny/js/iorder.js
/usr/lib64/R/library/questionr/shiny/js/jquery-ui.js
/usr/lib64/R/library/questionr/tests/testthat.R
/usr/lib64/R/library/questionr/tests/testthat/test_describe.R
/usr/lib64/R/library/questionr/tests/testthat/test_ggsurvey.R
/usr/lib64/R/library/questionr/tests/testthat/test_multi.R
/usr/lib64/R/library/questionr/tests/testthat/test_tables.R
/usr/lib64/R/library/questionr/tests/testthat/test_weighting.R
