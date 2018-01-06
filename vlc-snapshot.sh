#!/bin/sh
git clone -v https://git.videolan.org/git/vlc/vlc-3.0.git vlc

cd vlc

VERSION=$(grep AC_INIT configure.ac | sed -e 's/AC_INIT(vlc, //g' -e 's/\(-git\|-rc[0-9]\+\)\?)//g')
COMMIT=$(git rev-list HEAD -n1)
SHORTCOMMIT=$(echo ${COMMIT:0:7})
DATE=$(git log -1 --format=%cd --date=short | tr -d \-)
#rm -fr .git
cd ..

printf "Creating tarball... "
tar -cJf vlc-$VERSION-$SHORTCOMMIT.tar.xz vlc
rm -fr vlc
printf "done.\n"

echo %global commit0 $COMMIT
echo %global date $DATE
echo Version: $VERSION
