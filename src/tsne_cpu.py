from sklearn import manifold
from time import time 

def tsne_cpu(X):
    t0 = time()
    tsne = manifold.TSNE(n_components=2, perplexity=20.0,init='random')
    Y = tsne.fit_transform(X)
    t1 = time()
    print('input shape:', X.shape, ' time taken: ',t1-t0)
    return Y