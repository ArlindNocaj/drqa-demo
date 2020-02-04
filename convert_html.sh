#!/usr/bin/env bash

source /anaconda3/etc/profile.d/conda.sh
conda activate DrQA
cd ~/DrQA-Demo/handson
./convert_html_to_json.py $1 --output ./webpage_data.json
rm webpage_data.db
# convert json to compact version
jq -c . webpage_data.json > webpage_data_compact.json
../scripts/retriever/build_db.py webpage_data_compact.json webpage_data.db
../scripts/retriever/build_tfidf.py webpage_data.db ./
