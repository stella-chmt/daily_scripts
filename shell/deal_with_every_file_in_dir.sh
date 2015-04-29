#!/bin/bash
set -o nounset                              # Treat unset variables as an error

if [ $# -lt 1 ]; then
        echo "This script removes specific lines for every file in some directory!"
        echo "Usage: $0 directory"
        exit 1
fi
echo "This script removes specific lines for every file in this directory!"

DIRECTORY=$(cd `dirname $0` && pwd)
cd $DIRECTORY

function process ()
{
    echo "processing $1 begins"
    sed -e '/KeywordExtendTips/d' -e '/KeywordExtendUrl/d' -e '/AdShops/d' -e '/QueryID/d' -e '/FavIcon/d' -e '/Lat/d' -e '/Lng/d' -e '/200\ OK/d' -e '/GET:\ http/d' $1  > $1.bak
    mv $1.bak $1
    echo "processing $1 done"
}

cd $1
for my_file in `ls`;
do
     process $my_file
done
