import transformers

BERT_PATH = "../models/bert-base-uncased/"
TEST_BATCH_SIZE = 8

MAX_LEN = 512
# TOKENIZER = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
TOKENIZER = transformers.AutoTokenizer.from_pretrained("ssun32/bert_twitter_turkle")