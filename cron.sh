#!/bin/bash

python3 campaign2markdown.py > README.md

git add README.md
git commit -m "[cron.sh] Update README.md" -m "beep boop"
git push
