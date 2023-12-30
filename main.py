from moviepy.editor import *

input_clip = VideoFileClip("Input Video/BG VIDEO.mp4")
txt_clip = TextClip("Something must be here", fontsize=70, color="white")
txt_clip = txt_clip.set_position("centre").set_duration(10)

out_clip = CompositeVideoClip([input_clip, txt_clip])
out_clip.write_videofile("hello.mp4")