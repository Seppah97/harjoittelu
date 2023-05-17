#!/bin/bash




printf "\nThis is a test, please wait.\n"

start=`date +%s`



echo Hello World

curl http://example.com

end=`date +%s`

runtime=$((end-start))

printf "\nAll completed!\n\nTime elapsed: %d\n" "${runtime}"