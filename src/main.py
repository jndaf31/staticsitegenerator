from textnode import *
from htmlnode import *
from generate import regen_dir, generate_pages_recursive

def main():
    regen_dir('static','public')
    generate_pages_recursive('content','template.html','public')
main()