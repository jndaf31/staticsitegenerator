from textnode import *
from htmlnode import *
from generate import regen_dir, generate_pages_recursive
import sys
import os

def main():
    basepath = '/'
    if sys.argv[0]:
        basepath = sys.argv[0]

    
    regen_dir('static','docs')
    generate_pages_recursive('content','template.html','docs', basepath)
main()