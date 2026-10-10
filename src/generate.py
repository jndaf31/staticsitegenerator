import os
import shutil
from splitblocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath = '/'):
    for index in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, index)):
            generate_page(os.path.join(dir_path_content, index),template_path,os.path.join(dest_dir_path,index), basepath)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, index),template_path,os.path.join(dest_dir_path,index))

def generate_page(from_path: str, template_path: str, dest_path: str, basepath = '/'):
    print(f'Generating page from {from_path} to {dest_path.replace('.md','.html')} using {template_path}...')

    markdown_f = open(from_path,'r')
    markdown = markdown_f.read()
    markdown_f.close()

    template_f = open(template_path,'r')
    template = template_f.read()
    template_f.close()

    html_content = markdown_to_html_node(markdown).to_html()



    page_title = extract_title(markdown)

    page = template.replace('{{ Title }}', page_title).replace('{{ Content }}',html_content)
    page.replace('href="/',f'href="{basepath}').replace('src="/',f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    page_f = open(dest_path.replace('.md','.html'),'w')
    page_f.write(page)
    page_f.close()
    

    

def extract_title(markdown: str) -> str:
    lines = markdown.split('\n')
    title = ''

    for l in lines:
        if l.startswith('# '):
            title = l[2:].strip()
            return title
    raise Exception('No h1 header.')

def regen_dir(src: str, dst: str):
        if os.path.exists(dst):
            print(f"{dst} folder exists, deleting...")
            shutil.rmtree(dst)
        cpy_recursive(src,dst)

def cpy_recursive(src: str, dst: str):

    if not os.path.exists(dst):
        print(f'Creating blank {dst} folder')
        os.mkdir(dst)
    
    for i in os.listdir(src):
        if os.path.isfile(os.path.join(src, i)):
            print(f'copying {os.path.join(src, i)} -> {os.path.join(dst, i)}')
            shutil.copy(os.path.join(src, i),os.path.join(dst,i))
        else:
            cpy_recursive(os.path.join(src, i),os.path.join(dst,i))
