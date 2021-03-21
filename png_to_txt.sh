files="./*.png"
for filepath in $files; do
    FILENAME=${filepath%.png}
    #echo ${FILENAME}
    END_CHAR=${FILENAME: -1}
    if [ "1" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} -l jpn
    fi
    if [ "2" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} 
    fi
    if [ "3" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} -l jpn
    fi
    if [ "4" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} 
    fi
    if [ "5" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} -l jpn
    fi
    if [ "6" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} 
    fi
    if [ "7" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} -l jpn
    fi
    if [ "8" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} 
    fi
    if [ "9" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} -l jpn
    fi
    if [ "0" = $END_CHAR ];then
        tesseract $filepath  ${FILENAME} 
    fi

done
