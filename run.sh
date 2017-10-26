#!/bin/bash

python mutate.py
for i in output/*.csv;
do
    csvmidi $i > $i.mid
    timidity $i.mid -Ow -o - | ffmpeg -t 6 -i - -acodec libmp3lame -ab 128k $i.mp3
done
