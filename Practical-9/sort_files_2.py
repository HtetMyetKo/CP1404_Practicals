"""
CP1404/CP5632 Practical
Sort files Version 1
"""
import os

def main():
    """Move files into where user wants to store them based on extension."""
    # The following dictionary will allow us to map extensions to the destination folder names
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

