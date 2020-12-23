import transformers

BERT_PATH = "../models/bert-base-uncased/"
TEST_BATCH_SIZE = 8

MAX_LEN = 512
# TOKENIZER = transformers.BertTokenizer.from_pretrained(
#     BERT_PATH,
#     do_lower_case=True
# )
TOKENIZER = transformers.AutoTokenizer.from_pretrained("ssun32/bert_twitter_turkle")