#!/bin/sh -e
for f in *.ipynb ; do
  number=$(jq -r .metadata.notebook_number "$f" | xargs printf '%02d')
  jupyter nbconvert --to pdf \
                    --config nbconvert_config.py \
                    --template custom_latex_template_jupyter.tplx \
                    "$f"
  mv "${f%.*}.pdf" "pdf/${number}_${f%.*}.pdf"
done
