import sys
sys.path.append('..')

import time
import corpus as cp
import distributed_representation as dr

corpus = cp.Corpus(data = '../data/ptb/ptb.train.txt', mode = "l", 
                max_vocabulary_size = 5000, max_line = 0, 
                minimum_freq = 5)

#setting
window_size = 1
embedding_dims = 100
batch_size = 128

#skipgram
start = time.time()
dr_sgns = dr.DistributedRepresentation(corpus, embedding_dims, window_size, batch_size, mode_type = 1, 
                                sgns = 0, trace = True)
dr_sgns.train(num_epochs = 1, learning_rate = 0.01)

process_time = time.time() - start
print(process_time)

#negative sampling
start = time.time()
dr_sgns = dr.DistributedRepresentation(corpus, embedding_dims, window_size, batch_size, mode_type = 1, 
                                sgns = 1, negative_samples = 5, trace = True)
dr_sgns.train(num_epochs = 1, learning_rate = 0.01)

process_time = time.time() - start
print(process_time)