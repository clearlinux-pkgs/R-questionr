#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-questionr
Version  : 0.6.3
Release  : 12
URL      : https://cran.r-project.org/src/contrib/questionr_0.6.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/questionr_0.6.3.tar.gz
Summary  : Functions to Make Surveys Processing Easier
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : R-Hmisc
BuildRequires : R-classInt
BuildRequires : R-htmltools
BuildRequires : R-janitor
BuildRequires : R-labelled
BuildRequires : R-miniUI
BuildRequires : R-rstudioapi
BuildRequires : R-shiny
BuildRequires : R-tidyr
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n questionr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532216489

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532216489
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library questionr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library questionr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library questionr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library questionr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/questionr/data/rp99.RData
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
