#!/usr/bin/env bash

compress_video_with_h265() {
    ffmpeg -i $1 -vcodec libx265 -crf 28 $2
}

md2pdf(){
    pdf=${@[-1]}
    md=${@:1:${#}-1}

    pandoc -V geometry:a4paper -s -o $pdf "$md"
}

md2html(){
    html=${@[-1]}                                                                                                                                                                                                                                                                      
    md=${@:1:${#}-1}

    html_title=$(echo $html | awk -F '.' '{print $1}')

    pandoc -s -o $html "$md" --metadata pagetitle=$html_title
}

md2html_convert_all(){
    for file in *.md
    do
        echo "$file"
        file_html=$(echo "$file" | awk -F '.' '{print $1}')
        pandoc -s -o "$file_html.html" "$file" --metadata pagetitle="$file_html"
  done
}
