# Installations:
pip install transformers
pip install tweepy

# download BERT
mkdir models/bert-base-uncased/
wget "https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-config.json" -O models/bert-base-uncased/config.json
wget "https://cdn.huggingface.co/bert-base-uncased-pytorch_model.bin" -O models/bert-base-uncased/pytorch_model.bin
wget "https://cdn.huggingface.co/bert-base-uncased-vocab.txt" -O models/bert-base-uncased/vocab.txt