#!/bin/sh
# Requires ghostscript
gs -q \
   -dBATCH \
   -dNOPAUSE \
   -dPrinted=false \
   -sDEVICE=pdfwrite \
   -sOutputFile=scielo20gt6.pdf \
   pdf/metadata.pdf \
   pdf/slides.pdf \
   $(find pdf/ -type f | sort | head -n-2)
