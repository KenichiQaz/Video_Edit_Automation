from moviepy.editor import *
from sys import argv

class Video:
    def __init__(self, intro, video, outro):
        self.intro = intro
        self.video = video
        self.outro = outro
        
    def Merge_Files(original_file):
        if file is not None:
            clip = VideoFileClip(original_file)
            final_clip=moviepy.editor.concatenate_videoclips([INTRO,clip,OUTRO])
            final_clip.write_videofile("output_1.mp4", codec='libx264')
        else:
            print("No file")

if __name__ == "__main__":
    if argv[3] == "":
        video.Merge_Files(argv[1],argv[2],argv[1])
    elif argv[3] != "":
        video.Merge_Files(argv[1],argv[2],argv[3])
