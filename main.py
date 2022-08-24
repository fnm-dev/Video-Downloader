import pytube
import moviepy.editor as mp
import re
import os
from time import sleep


while True:
    link = input("Enter the link of the video you want to download: ")
    option = input("Audio or video (a/v)? ")
    path = os.getcwd()
    yt = pytube.YouTube(link)

    print("\nTitle:", yt.title)
    print("Author:", yt.author)
    print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
    print("Number of views:", yt.views)
    print("Length of video:", yt.length, "seconds")

    print("\nDownloading...")
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
        print("\nSuccessful!")

    sleep(1)
    os.system('cls')
