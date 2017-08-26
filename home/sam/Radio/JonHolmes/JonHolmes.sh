#Example: "/home/sam/NAS/Radio/IainLee/"
directory="/home/sam/Radio/JonHolmes/"
raw_directory="/home/sam/Radio/Raw/JonHolmes/"
#Example: "IainLeeTalkRadio"
filename="Jon_Holmes"

#Duaration in seconds
#30mins = "1800"
#1 hour = "3600"
#2 hours = "7200"
#3 hours = "10800"
#4 hours = "14400"

duration="10920"

#Has to work within VLC - Please test before running"
URL="http://radio.talkradio.co.uk/stream"




today=$(date +"%Y-%m-%d")

#Testing
#today=$(date +"%Y-%m-%d-Time-%H-%M-Duration-$duration")
echo $today

mkdir -p $directory


cvlc $URL --sout file/mp3:$raw_directory$today-$filename-raw.mp3 --run-time=$duration --stop-time=$duration vlc://quit
ffmpeg -i $raw_directory$today-$filename-raw.mp3 -ab 128k $directory$today-$filename.mp3
