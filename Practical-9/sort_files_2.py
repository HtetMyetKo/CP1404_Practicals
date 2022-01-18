"""
CP1404/CP5632 Practical
Sort files Version 1
"""
import os

def main():
    """Move files into where user wants to store them based on extension."""

    extension_to_category = {}
    # Create dictionary so it will pair extensions to the directory names

    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            # Get input and pair extensions to the directory names
            extension_to_category[extension] = category


main()