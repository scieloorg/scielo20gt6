#!/bin/sh -e
for f in *.ipynb ; do
  number=$(jq -r .metadata.notebook_number "$f" | xargs printf '%02d')
  jupyter nbconvert --to html "$f"
  mv "${f%.*}.html" "html/${number}_${f%.*}.html"
done
