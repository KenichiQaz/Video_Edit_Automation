'''This is the main file that will be executed by the user.'''
from sys import argv
from moviepy.editor import *

def Merge_Files(original_file, intro_file, outro_file):
    '''This function merges the intro and outro files with the original file.'''
    if original_file is not None:
        clip = VideoFileClip(original_file)
        final_clip = concatenate_videoclips([intro_file,clip,outro_file])
        final_clip.write_videofile("output_1.mp4", codec='libx264')
    else:
        print("No file")

if __name__ == "__main__":
    if argv[3] == "":
        Merge_Files(argv[1],argv[2],argv[1])
    elif argv[3] != "":
        Merge_Files(argv[1],argv[2],argv[3])
