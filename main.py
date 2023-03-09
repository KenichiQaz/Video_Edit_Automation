from moviepy.editor import *
import sys

class Video:
    def __init__(self, intro, video, outro):
        self.intro = intro
        self.video = video
        self.outro = outro
        
    def Merge_Files(original_file):
        if file is not None:
            clip = VideoFileClip(original_file)
            final_clip=moviepy.editor.concatenate_videoclips([INTRO,clip1,OUTRO])
            final_clip.write_videofile("output_1.mp4", codec='libx264')
        else:
            print("No file")

if __name__ == "__main__":
    if sys.argv[3] == "":
        video.Merge_Files(sys.argv[1],sys.argv[2],sys.argv[1])
    elif sys.argv[3] != "":
        video.Merge_Files(sys.argv[1],sys.argv[2],sys.argv[3])
