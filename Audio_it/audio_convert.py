import pydub
import time
import timeit
import tqdm
from pydub import AudioSegment
from tqdm import tqdm
source=input("\nEnter the source path of the ->AuDiO<- please eg:/home/user/directory/filename.format\n\n")
destination=input("\nEnter the destination path of the ->AuDiO_file.FoRmAt<- eg:/home/user/directory/filename.format\n\n")
from_format=input("\nEnter the ->Original<- file ->FoRmaT<- please ->mp3,wav\n\n")
to_format=input("\nPlease enter the ->FoRmaT<- to which the file is to be  ->CoNvErTeD<-  ->wav,mp3\n\n")
mp3_audio=AudioSegment.from_file(source,format=from_format)
mp3_audio.export(destination,format=to_format)
print("\nCoNvErsIoN StArTeD it takes less than a minute.........\n")
print("\nAgalvaarai Thaangum Nilambola Thammai Igalvaar Poruthal ->THALAI...<-\n\n")
for i in tqdm(range(100)):
    time.sleep(0.1)
print("\nconversion ->successfull<- enjoy your AuDiO")
