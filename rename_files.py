import os
import re

pdf_folder = r"C:\Users\syeda\Desktop\Specs"

code_dict = {}

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith('.pdf'):
        match = re.search(r'(SUFL\s*\d+)', filename, re.IGNORECASE)
        if match:
            code = match.group(1).replace(" ", "").upper()
            if code in code_dict:
                code_dict[code].append(filename)
            else:
                code_dict[code] = [filename]

print("=== EXECUTING CLEANUP (Deleting Extra Files) ===")
deleted_count = 0

for code, file_list in code_dict.items():
    file_list.sort()
    keep_file = file_list[0]
    print(f"\nCode: {code}")
    print(f"  -> KEEPING: {keep_file}")
    
    for extra_file in file_list[1:]:
        file_path = os.path.join(pdf_folder, extra_file)
        try:
            os.remove(file_path)
            deleted_count += 1
            print(f"  -> DELETED: {extra_file}")
        except Exception as e:
            print(f"  -> ERROR deleting {extra_file}: {e}")

print(f"\nTask Complete! Total duplicate files deleted: {deleted_count}")
print("Har SUFL code ki ab sirf aik original file mehfooz hai.")