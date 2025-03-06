import numpy as np

def load_glove_vectors(file_path):
    glove_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.strip().split()
            word = values[0]
            vector = np.array(values[1:], dtype=np.float32)
            glove_dict[word] = vector
    return glove_dict

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def most_similar_words(word, glove_dict, top_n=5):
    if word not in glove_dict:
        return []
    word_vector = glove_dict[word]
    similarities = {}
    for other_word, other_vector in glove_dict.items():
        if other_word != word:
            similarities[other_word] = cosine_similarity(word_vector, other_vector)
    return sorted(similarities, key=similarities.get, reverse=True)[:top_n]

glove_file = "glove.6B.50d.txt"
glove_dict = load_glove_vectors(glove_file)

pairs = [("cat", "dog"), ("car", "bus"), ("apple", "banana")]
for w1, w2 in pairs:
    print(f"Cosine similarity between '{w1}' and '{w2}': {cosine_similarity(glove_dict[w1], glove_dict[w2]):.4f}")

words_to_check = ["king", "computer", "university"]
for word in words_to_check:
    print(f"Top-5 words similar to '{word}': {most_similar_words(word, glove_dict)}")
