#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 08:58:45 2021

@author: santosg
"""

file1 = open("lib.html","a")


#file1.writelines(L)

t1 = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>A simple HTML document</title>
</head>
<body>
'''

t2 = '<a href="/Users/santosg/Desktop/Libros_may1221/Wang2016_Book_AbsoluteBeginnersGuideToComput.pdf">ok</a>'

t3 = '''
    <p>Hello World!<p>
</body>
</html>
'''

file1.writelines(t1)
file1.writelines(t2)
file1.writelines(t3)


file1.close()