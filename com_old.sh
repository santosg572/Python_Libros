#!/bin/bash

#pat="/Users/santosg/Desktop/"

#pat="/Volumes/FLOR/Libros_TODOS/"

pat="/home/santosg/Desktop/Libros_feb1123/HHH_libros/"

folder="HTML_libros"

python3 com.py ${pat} ${folder} > ${folder}.txt

python3 creaHTML.py ${folder}






