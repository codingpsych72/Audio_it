#!/bin/sh

python3 script_start.py

echo "    e Y8b                    888 ,e,               ,e,   d8  " 
echo "   d8b Y8b    8888 8888  e88 888  I   '88 88'       I   d88  "
echo "  d888b Y8b   8888 8888 d888 888 888 d888 888b 888 888 d88888" 
echo " d888888888b  Y888 888P Y888 888 888 Y888 888P     888  888  " 
echo "d8888888b Y8b   88 88     88 888 888   88 88       888  888  " 
echo " "
echo "The Linux Audio converter:(mp3,mp4,wav)+Youtube Downloader"
echo " "
echo " "

while [ $choice!=4 ] 
do
echo " "
echo "WhAt Do YoU WaNt Me To Do FoR YoU ? "
echo " "
echo " "
echo " Type  1 to Download youtube video"
echo "       2 to Extract the Audio     "
echo "       3 to Convert the Audio     "
echo "       4 to quit.....             "
echo " "
echo "and hit Enter                     "
echo " "
read choice
case $choice in
  1)
  echo " "
  echo "You have choosen to download a youtube video " 
  python3 youtube_dwn_start.py
  echo " "
  echo " "
  python3 youtube_dwn.py	
  echo "**************************************************************************************************************************************************************"
  ;;
  2)
  echo " "
  echo "You have choosen to Extract the audio from a video " 
  python3 video_convert_start.py
  echo " "
  echo " "
  python3 video_convert.py
  echo "**************************************************************************************************************************************************************"
  ;;
  3)
  echo " "
  echo "You have choosen to convert the audio format " 
  python3 audio_convert_start.py
  echo " "
  echo " "
  python3 audio_convert.py
  echo " "
  echo "**************************************************************************************************************************************************************"
  ;;
  4)
  echo " "
  echo "Nandri Meendum Santhippom(ThAnK YoU....)"
  exit 0
  echo "**************************************************************************************************************************************************************"
  
esac
done




 

