import time
from tqdm import tqdm
import pytube
from pytube import YouTube
link=input("\nPlease copy and paste or EnTeR the ->URL<-\n\n")
path=input("\nPlease enter the ->DeStInAtIoN<- path of the video to be saved eg:/home/user/directory\n\n")
print("\nPlease wait while i fetch the Data\n\n")
for i in tqdm(range(100)):
    time.sleep(0.01)
print("\nDoWnLoAd StArTeD.......It takes less than a minute......\n\n")
print("\nAgalvaarai Thaangum Nilambola Thammai Igalvaar Poruthal ->THALAI...<-\n\n")
yt=pytube.YouTube(link)
downy=yt.streams.first()
downy.download(path)
for i in tqdm(range(100)):
    time.sleep(0.1)
print("\nDoWnLoAd CoMpLeTeD....Enjoy the Video....\n\n")


