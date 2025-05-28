#!/bin/bash
echo 'JQ TRAINER LOGFILE' > ./input.log
while true; do
    printf '$ '    # manual prompt, no -p option
    read -e input
    echo "$input" >> ./input.log
    eval "$input"
done
