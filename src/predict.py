import config
import transformers
import dataset
import torch
from tqdm import tqdm
import numpy as np

def get_dataloader(encoded_inputs):
    test_dataset = dataset.BERTdataset(encoded_inputs)
    test_dataloader = torch.utils.data.DataLoader(
        dataset = test_dataset,
        batch_size = config.TEST_BATCH_SIZE
    )
    return test_dataloader

def predict(sentences):
    encoded_inputs = config.TOKENIZER(sentences, 
                                    padding=True, 
                                    truncation=True, 
                                    max_length=config.MAX_LEN,
                                    return_tensors="pt")
    #model = transformers.BertModel.from_pretrained(config.BERT_PATH)
    model = transformers.AutoModel.from_pretrained("ssun32/bert_twitter_turkle")
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    test_dataloader = get_dataloader(encoded_inputs)

    last_hidden_states = []
    with torch.no_grad():
        for data in tqdm(test_dataloader, total=len(test_dataloader)):
            for k,v in data.items():
                data[k] = v.to(device)
            output = model(**data)
            output = output[0][:,0,:].detach().numpy()
            for arr in output:
                last_hidden_states.append(arr)
    
    # output = model(**encoded_inputs)
    # last_hidden_states = output[0][:,0,:].detach().numpy()
    last_hidden_states =  np.array(last_hidden_states)
    print(last_hidden_states.shape)
    return last_hidden_states
