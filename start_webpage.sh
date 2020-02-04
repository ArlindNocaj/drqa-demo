 source /anaconda3/etc/profile.d/conda.sh
 conda activate DrQA
 cd ~/DrQA-Demo/
 export CLASSPATH=$CLASSPATH:~/DrQA-Demo/data/corenlp/*
 #python -W ignore scripts/pipeline/interactive.py
 export PYTHONWARNINGS="ignore"

./scripts/pipeline/interactive.py --reader-model ./data/reader/single.mdl --retriever-model ./handson/webpage_data-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz  --doc-db ./handson/webpage_data.db
