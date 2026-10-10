import os
import shutil

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
