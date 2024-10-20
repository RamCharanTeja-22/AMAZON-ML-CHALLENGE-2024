import os
import shutil
def move_file_with_duplicate_check(src_path, dest_dir):
    filename= os.path.basename(src_path)
    dest_path = os.path.join(dest_dir, filename)
    if os.path.exists(dest_path):
        base, ext = os.path.splitext(filename) 
        counter = 1
        while os.path.exists(dest_path): 
            global duplicate_found
            duplicate_found=True
            new_filename=f"(base)_(counter)(ext)"
            dest_path=os.path.join(dest_dir, new_filename) 
            counter + 1

    shutil.move(src_path, dest_path) 
    print("Moved: (src_path) -> (dest_path)")
source_dir = r'C:\Users\NL Swathi\Desktop\INFOSYS_PROJECT\downloads'
csv_dir=r'C:\Users\NL Swathi\Desktop\INFOSYS_PROJECT\downloads\csv_files'
dat_dir=r'C:\Users\NL Swathi\Desktop\INFOSYS_PROJECT\downloads\dat_files'
os.makedirs(csv_dir, exist_ok=True)
os.makedirs(dat_dir, exist_ok=True)
duplicate_found=False
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        extension=filename.lower().strip()

        if extension.endswith('.csv'):
            move_file_with_duplicate_check(file_path, csv_dir)
        elif extension.endswith('.dat'):
            move_file_with_duplicate_check(file_path,dat_dir)
            
if duplicate_found:
    print("Duplicate files were found and renamed.")
else:
    print("Nef-duplicate files were found.")

