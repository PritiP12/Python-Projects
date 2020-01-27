

from moviepy import video
from moviepy.editor import *
from multiprocessing import Process, Semaphore
import sys
import soundfile as sf
import pyloudnorm as pyln
import pandas as pd

def break_files():
     clip = VideoFileClip(r"C:\Users\Dell\Downloads\Match_Video.mp4")
     duration_clip=clip.duration
     print(duration_clip)
     df = pd.read_csv(r"C:\Users\Dell\Desktop\class\Book_1.csv")
     num = 0
     for ind in df.index:
          #print(df['start time'][ind], df['end time'][ind])
          clip = VideoFileClip(r"C:\Users\Dell\Downloads\Match_Video.mp4").subclip(df['start time'][ind], df['end time'][ind])
          #'{}_'.format(str(num).zfill(3))
          clip.write_videofile(r"C:\Users\Dell\Desktop\class\broken_files\output_%s.mp4" % num)
          clip.audio.write_audiofile(r"C:\Users\Dell\Desktop\class\broken_files\output_%s.wav" % num)
          num += 1

directory = r"C:\Users\Dell\Desktop\class\broken_files"
dict1 = {}
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
         path = os.path.join(directory,filename)
         data, rate = sf.read(path)  # load audio (with shape (samples, channels))
         meter = pyln.Meter(rate)  # create BS.1770 meter
         loudness = meter.integrated_loudness(data)  # measure loudness
         dict_key=filename.split(".")[0] + ".mp4"
         dict1[dict_key] = loudness
         #print(loudness)
#print(dict1)
list1 = sorted(dict1.items(), key=lambda kv: (kv[1], kv[0]),reverse=True)
list1=list1[:3]
print(list1)

list2=[]
for i in list1:
     list2.append(i[0])
list2=sorted(list2)
print(list2)

clip1=[]
from moviepy.editor import VideoFileClip, concatenate_videoclips

for i in list2:
     clip1.append(VideoFileClip(os.path.join(directory,i)))

final_clip = concatenate_videoclips(clip1)
final_clip.write_videofile(os.path.join(directory,"my_concatenation.mp4"))
