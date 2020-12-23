
import transformers
import config
import torch
import torch.nn as nn

class BERTModel(nn.Module):
    def __init__(self):
        super(BERTModel, self).__init__()
        self.bert = transformers.BertModel.from_pretrained(config.BERT_PATH)

    def forward(self, input_ids, token_type_ids, attention_mask):
        o1, _  =  self.bert(
            input_ids = input_ids,
            token_type_ids = token_type_ids,
            attention_mask =  attention_mask
        )
        return o1