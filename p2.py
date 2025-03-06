import nltk
from nltk.corpus import brown
from collections import defaultdict, Counter
import math
import numpy as np

nltk.download('brown')

def preprocess(corpus):
    tokenized_corpus = []
    for sentence in corpus:
        processed_sentence = ['<s>'] + [word.lower() for word in sentence] + ['</s>']
        tokenized_corpus.append(processed_sentence)
    return tokenized_corpus

def compute_tf(corpus):
    tf = defaultdict(Counter)
    for i, document in enumerate(corpus):
        tf[i] = Counter(document)
    return tf

def compute_df(tf):
    df = Counter()
    for document in tf.values():
        unique_words = set(document.keys())
        df.update(unique_words)
    return df

def compute_tfidf(tf, df, num_docs):
    tfidf = defaultdict(dict)
    for doc_id, word_counts in tf.items():
        for word, count in word_counts.items():
            tfidf[doc_id][word] = count * math.log(num_docs / (1 + df[word]))
    return tfidf

def create_cooccurrence_matrix(corpus, window_size=5):
    vocab = set(word for sentence in corpus for word in sentence)
    word_to_id = {word: i for i, word in enumerate(vocab)}
    id_to_word = {i: word for word, i in word_to_id.items()}
    vocab_size = len(vocab)
    cooccurrence_matrix = np.zeros((vocab_size, vocab_size))

    for sentence in corpus:
        for i, word in enumerate(sentence):
            word_id = word_to_id[word]
            start = max(0, i - window_size)
            end = min(len(sentence), i + window_size + 1)
            for j in range(start, end):
                if i != j:
                    context_word_id = word_to_id[sentence[j]]
                    cooccurrence_matrix[word_id, context_word_id] += 1

    return cooccurrence_matrix, word_to_id, id_to_word

def compute_ppmi(cooccurrence_matrix):
    total_count = np.sum(cooccurrence_matrix)
    row_sums = np.sum(cooccurrence_matrix, axis=1)
    col_sums = np.sum(cooccurrence_matrix, axis=0)
    ppmi_matrix = np.zeros_like(cooccurrence_matrix)

    for i in range(cooccurrence_matrix.shape[0]):
        for j in range(cooccurrence_matrix.shape[1]):
            if cooccurrence_matrix[i, j] > 0:
                p_ij = cooccurrence_matrix[i, j] / total_count
                p_i = row_sums[i] / total_count
                p_j = col_sums[j] / total_count
                pmi = math.log2(p_ij / (p_i * p_j)) if p_i * p_j > 0 else 0
                ppmi_matrix[i, j] = max(pmi, 0)

    return ppmi_matrix

if __name__ == "__main__":
    corpus = brown.sents()[0:1000]

    processed_corpus = preprocess(corpus)

    num_docs = len(processed_corpus)

    tf = compute_tf(processed_corpus)
    df = compute_df(tf)
    tfidf = compute_tfidf(tf, df, num_docs)

    print("TF-IDF for word 'county' in the first document: ", tfidf[0].get('county', 0))
    print("TF-IDF for word 'investigation' in the first document: ", tfidf[0].get('investigation', 0))

    window_size = 5
    cooccurrence_matrix, word_to_id, id_to_word = create_cooccurrence_matrix(processed_corpus, window_size=window_size)
    ppmi_matrix = compute_ppmi(cooccurrence_matrix)

    print("\nPPMI for a few word pairs:")
    words = [['expected', 'approve'], ['mentally', 'in'], ['send', 'bed']]
    for word_pair in words:
        word1, word2 = word_pair
        word1_id = word_to_id.get(word1, None)
        word2_id = word_to_id.get(word2, None)
        if word1_id is not None and word2_id is not None:
            ppmi_value = ppmi_matrix[word1_id, word2_id]
            print(f"PPMI({word1}, {word2}) = {ppmi_value}")
        else:
            print(f"Words '{word1}' or '{word2}' not found in vocabulary.")
