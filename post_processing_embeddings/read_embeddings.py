import numpy as np

with open("processed_embeddings.npz","rb") as read:
    new_embeddings = np.load(read)
    words = new_embeddings["words"]
    embeddings = new_embeddings["embeddings"]

print(words.shape)
print(embeddings.shape)