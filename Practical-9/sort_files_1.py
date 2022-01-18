"""
CP1404/CP5632 Practical
Sort files Version 1
"""
import os
import shutil

def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort") #Folder
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        # Get extensions from the respective files

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        print("{}/{}".format(extension, filename))

        os.rename(filename, "{}/{}".format(extension, filename))

        shutil.move(filename, extension)
        # move files into new directories



main()