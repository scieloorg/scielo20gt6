#!/bin/sh
fname=$(mktemp --suffix .tex)
pandoc -D latex \
  | sed '/\\begin.document./a \\\\pagenumbering\{gobble\}' \
  > "$fname"
pandoc -o pdf/metadata.pdf \
       --template "$fname" \
       --variable fontsize=12pt \
       --variable geometry='margin=2.2cm,top=3.5cm' \
       --variable papersize=a4 \
       --variable linestretch=1.5 \
       metadata.md
rm "$fname"
