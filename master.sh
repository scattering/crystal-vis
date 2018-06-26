cat file.txt | awk '{print "savg-sphere | savg-scale 0.1 | savg-translate",  $4,$5,$6;}' | bash > model.savg
