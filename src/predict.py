import config
import transformers
from tsne_cpu import tsne_cpu
from visualise import visualise
#from model import BERTModel

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

if __name__ == "__main__":
    inputs = ['Hey this is a good time to be in AI', 'Not sure where this field is headed though', 'AI is the way to go', 'Artifical Intelligence is the future', 'AI robots will kill us']
    outputs = predict(inputs)
    outputs_2d = tsne_cpu(outputs)
    print(outputs_2d)
    visualise(outputs_2d)