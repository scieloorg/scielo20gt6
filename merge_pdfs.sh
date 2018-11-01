#!/bin/sh
# Requires ghostscript
gs -q \
   -dBATCH \
   -dNOPAUSE \
   -sDEVICE=pdfwrite \
   -sOutputFile=scielo20gt6.pdf \
   pdf/slides.pdf $(find pdf/ -type f | sort | head -n-1)
