import os
import shutil

def copy_static(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    entries = os.listdir(src)
    for entry in entries:
        source_path = os.path.join(src, entry)
        dest_path = os.path.join(dest, entry)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        elif os.path.isdir(source_path):
            copy_static(source_path, dest_path)
