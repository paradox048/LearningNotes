import os
import shutil

DESKTOP_PATH = "/Users/derekduong/Desktop"
SCREENSHOT_FOLDER = "/Users/derekduong/Desktop/Screenshots_folder"

#Create the organized folder if it doesn't already exist
if not os.path.exists(SCREENSHOT_FOLDER):
    os.makedirs(SCREENSHOT_FOLDER)
    
# Iterate through all the screenshot files on the desktop
for file in os.listdir(DESKTOP_PATH):
    #check if the current file is a screenshot
    if "screenshot" in file.lower():
        #get full path of file
        file_path = os.path.join(DESKTOP_PATH, file)

        #move the file to the folder
        shutil.move(file_path, SCREENSHOT_FOLDER)

print("DONE!")