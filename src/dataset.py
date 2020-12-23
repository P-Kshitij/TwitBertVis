from torch.utils.data import Dataset

class BERTdataset(Dataset):
    def __init__(self, encoded_text_dict):
        self.encoded_text_dict = encoded_text_dict

    def __len__(self):
        return len(self.encoded_text_dict['input_ids'])

    def __getitem__(self, item):
        ids = self.encoded_text_dict['input_ids'][item]
        token_type_ids = self.encoded_text_dict['token_type_ids'][item]
        attention_mask = self.encoded_text_dict['attention_mask'][item]

        return{
            'input_ids':ids,
            'token_type_ids':token_type_ids,
            'attention_mask': attention_mask
        }