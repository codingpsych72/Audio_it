import pydub
import time
import timeit
import tqdm
from pydub import AudioSegment
from tqdm import tqdm
source=input("\nEnter the source path of ->ViDeO<- please eg:/home/user/directory/filename.format\n\n")
destination=input("\nEnter the destination path with file name eg:/home/user/directory/filename.format\n\n")
from_format=input("\nEnter the original ->ViDeO<- file format please ->mp4\n\n")
to_format=input("\nPlease enter the  ->AuDiO<- format to which the file is to be converted ->mp3,wav\n\n")
mp3_audio=AudioSegment.from_file(source,format=from_format)
mp3_audio.export(destination,format=to_format)
print("\nCoNvErsIoN StArTeD it takes less than a minute.........\n")
print("\nAgalvaarai Thaangum Nilambola Thammai Igalvaar Poruthal ->THALAI...<-\n\n")
for i in tqdm(range(100)):
    time.sleep(0.1)
print("\n->ViDeo -2- AuDiO<- conversion successfull enjoy your audio")
