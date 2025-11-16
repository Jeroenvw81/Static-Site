import os
import shutil
from config import source_dir_path, dest_dir_path

from copy_static import copy_static


def main():
    print("Deleting public directory...")
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
    
    print("Copying source files to public directory...")
    copy_static(source_dir_path, dest_dir_path)

main()