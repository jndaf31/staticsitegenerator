from textnode import *
from htmlnode import *
from generate import regen_dir, generate_page

def main():
    regen_dir('static','public')
    generate_page('content/index.md','template.html','public/index.html')
main()