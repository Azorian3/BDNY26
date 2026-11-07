#!/bin/bash
set -e
cd /home/ubuntu/bdny/film
M="/home/ubuntu/attachments/9f951003-ae3b-46e0-a67a-236e18c7695b/Disc_2_11_-_Outro.mp3"
ffmpeg -y -v error -framerate 30 -i frames/%05d.jpg -ss 130 -t 45 -i "$M" \
 -filter_complex "[1:a]afade=t=in:st=0:d=2.5,afade=t=out:st=41:d=4,loudnorm=I=-16:TP=-1.5:LRA=11[a]" \
 -map 0:v -map "[a]" -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -shortest \
 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact -movflags +faststart+use_metadata_tags \
 -metadata title="Azorian3. You make the piece. We make the numbers behave." -metadata artist="James F. Canfield IV" -metadata album_artist="Azorian3" -metadata comment="Azorian3 for BDNY 2026" -metadata copyright="Azorian 3, LLC" \
 Azorian3_BDNY_Commercial.mp4
ffprobe -v error -show_entries format=duration:format_tags -of default=nw=1 Azorian3_BDNY_Commercial.mp4
ls -la Azorian3_BDNY_Commercial.mp4
