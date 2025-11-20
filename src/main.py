import os
import shutil
from config import dir_path_static, dir_path_content, dir_path_public, template_path

from gencontent import generate_page
from copy_static import copy_static

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying source files to public directory...")
    copy_static(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

main()
