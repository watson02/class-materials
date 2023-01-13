#!/bin/bash
git rm push.py
git add .
git commit -m $1
git push
