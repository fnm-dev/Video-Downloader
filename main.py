import pytube
import moviepy.editor as mp
import re
import os

link = input("Enter the link of the video you want to download: ")
option = input("Audio or video? (a/v) ")
path = r"D:\Users\FelipePC\Downloads"
yt = pytube.YouTube(link)

print("Downloading...")
yt.streams.get_highest_resolution().download(path)
print("Download completed.")

if option == 'a':
    print("Converting...")
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
else:
    print("Successful!")
