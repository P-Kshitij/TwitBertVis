
import transformers
import config
import torch
import torch.nn as nn

class BERTModel(nn.Module):
    def __init__(self):
        super(BERTModel, self).__init__()
        self.bert = transformers.BertModel.from_pretrained(config.BERT_PATH)

    def forward(self, ids, mask, token_type_ids, target_tags):
        o1, _  =  self.bert(
            ids,
            attention_mask = mask,
            token_type_ids = token_type_ids
        )
        return o1