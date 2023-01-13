#!/bin/bash
git rm push.sh
git add .
git commit -m $1
git push
