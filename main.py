from moviepy.editor import *

INTRO=""
OUTRO=""

def Merge_Files(original_file):
    if file is not None:
        clip = VideoFileClip(original_file)
        final_clip=moviepy.editor.concatenate_videoclips([INTRO,clip1,OUTRO])
        final_clip.write_videofile("output_1.mp4", codec='libx264')
    else:
        print("No file")
        
if __name__ == "__main__":
    Merge_Files("input.mp4")
