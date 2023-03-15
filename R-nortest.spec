#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-nortest
Version  : 1.0.4
Release  : 42
URL      : https://cran.r-project.org/src/contrib/nortest_1.0-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nortest_1.0-4.tar.gz
Summary  : Tests for Normality
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
normality.

%prep
%setup -q -c -n nortest
cd %{_builddir}/nortest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641067097

%install
export SOURCE_DATE_EPOCH=1641067097
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nortest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nortest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nortest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc nortest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nortest/DESCRIPTION
/usr/lib64/R/library/nortest/INDEX
/usr/lib64/R/library/nortest/Meta/Rd.rds
/usr/lib64/R/library/nortest/Meta/features.rds
/usr/lib64/R/library/nortest/Meta/hsearch.rds
/usr/lib64/R/library/nortest/Meta/links.rds
/usr/lib64/R/library/nortest/Meta/nsInfo.rds
/usr/lib64/R/library/nortest/Meta/package.rds
/usr/lib64/R/library/nortest/NAMESPACE
/usr/lib64/R/library/nortest/R/nortest
/usr/lib64/R/library/nortest/R/nortest.rdb
/usr/lib64/R/library/nortest/R/nortest.rdx
/usr/lib64/R/library/nortest/help/AnIndex
/usr/lib64/R/library/nortest/help/aliases.rds
/usr/lib64/R/library/nortest/help/nortest.rdb
/usr/lib64/R/library/nortest/help/nortest.rdx
/usr/lib64/R/library/nortest/help/paths.rds
/usr/lib64/R/library/nortest/html/00Index.html
/usr/lib64/R/library/nortest/html/R.css
