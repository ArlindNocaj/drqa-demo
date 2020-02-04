#!/usr/bin/env bash
wget \
    --mirror \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --domains openai.com \
     --adjust-extension \
     -v -np\
     -e robots=off \
         https://openai.com/
