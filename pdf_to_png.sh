files="./*.pdf"
for filepath in $files; do
    FILENAME=${filepath%.pdf}
    pdftoppm -png -x 0 -y 275 -W 800 -H 750 $filepath ${FILENAME}
    mv ${FILENAME}-1.png ${FILENAME}.png
done
