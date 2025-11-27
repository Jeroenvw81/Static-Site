import os
import shutil
import sys
from config import dir_path_static, dir_path_content, dir_path_public, template_path, default_basepath

from gencontent import generate_page_recursive
from copy_static import copy_files_recursive

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying source files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath,
    )

main()
