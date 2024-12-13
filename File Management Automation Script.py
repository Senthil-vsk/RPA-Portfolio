import os
import shutil

def organize_files(src_folder):
    for filename in os.listdir(src_folder):
        if filename.endswith('.txt'):
            shutil.move(os.path.join(src_folder, filename), 'Text_Files')
        elif filename.endswith('.jpg'):
            shutil.move(os.path.join(src_folder, filename), 'Images')
        elif filename.endswith('.pdf'):
            shutil.move(os.path.join(src_folder, filename), 'PDFs')

# Usage example
organize_files('path_to_your_folder')
