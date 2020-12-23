import config
import transformers

def predict(sentences):
    encoded_inputs = config.TOKENIZER(sentences, 
                                    padding=True, 
                                    truncation=True, 
                                    max_length=config.MAX_LEN,
                                    return_tensors="pt")
    model = transformers.BertModel.from_pretrained(config.BERT_PATH)
    output = model(**encoded_inputs)
    last_hidden_states = output[0][:,0,:].detach().numpy()
    return last_hidden_states
