import os
import sys
import shutil

path1 = r"C:\Users\uqeboitt\PycharmProjects\VASP\Data\Matthew"
folders = os.listdir(path1)
print(folders)
for folder in folders:
    subfolders = os.listdir(os.path.join(path1, folder))
    print(subfolders)
    for subfolder in subfolders:
        file_in = open(os.path.join(path1, folder, subfolder, "POSCAR"), "r").readlines()
        file_out = open(os.path.join(path1, folder, subfolder, "POSCAR"), "w")
        file_in_copy = open(os.path.join(path1, folder, subfolder, "_POSCAR_"), "w")

        file_in_copy.writelines(file_in)

        file_out_lines = []

        for x in file_in[:8]:
            file_out_lines.append(x)
        file_out_lines.append("S\n")
        for x in file_in[8:80]:
            file_out_lines.append(x[:-1] + " F F F\n")
        file_out_lines.append(file_in[80][:-1] + " F F T\n" )

        file_out.writelines(file_out_lines)