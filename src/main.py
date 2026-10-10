from textnode import *
from htmlnode import *
from generate import regen_dir, generate_pages_recursive
import sys
import os

def main():
    basepath = '/'
    if len(sys.argv)>0 and sys.argv[1]:
        basepath = sys.argv[1]

    
    regen_dir('static','docs')
    generate_pages_recursive('content','template.html','docs', basepath)
main()