#!/bin/sh
git clone -v https://git.videolan.org/git/vlc.git vlc

cd vlc

VERSION=$(grep AC_INIT configure.ac | sed -e 's/AC_INIT(vlc, //g' -e 's/-git)//g')
COMMIT=$(git rev-list HEAD -n1)
SHORTCOMMIT=$(echo ${COMMIT:0:7})
#rm -fr .git
cd ..

printf "Creating tarball... "
tar -cJf vlc-$VERSION-$SHORTCOMMIT.tar.xz vlc
rm -fr vlc
printf "done.\n"

echo $VERSION - $COMMIT
