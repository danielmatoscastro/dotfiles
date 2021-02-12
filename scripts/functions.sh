#!/usr/bin/env bash

compress_video_with_h265() {
    ffmpeg -i $1 -vcodec libx265 -crf 28 $2
}
