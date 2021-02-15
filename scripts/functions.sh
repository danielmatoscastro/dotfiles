#!/usr/bin/env bash

compress_video_with_h265() {
    ffmpeg -i $1 -vcodec libx265 -crf 28 $2
}

md2pdf(){
    pdf=${@[-1]}
    md=${@:1:${#}-1}

    pandoc -V geometry:a4paper -s -o $pdf "$md"
}
