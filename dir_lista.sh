!#/bin/bash

pat="/home/santosg/Desktop/Libros_feb1123/"
pref="BBB"

ls -1 ${pat}${pref}"_libros" > "dir_"${pref}".txt"

dd=`cat "dir_"${pref}".txt"`

echo $dd

for file in $dd
do 
 echo $file
 ./com.sh $file $pat
done



