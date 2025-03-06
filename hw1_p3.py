import nltk
from nltk import bigrams
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from collections import defaultdict, Counter
nltk.download('punkt_tab')

def preprocess(corpus):
    tokenized_corpus = []
    for sentence in corpus:
        tokens = ['<s>'] + [word.lower() for word in sentence] + ['</s>']
        tokenized_corpus.append(tokens)
    return tokenized_corpus


def build_bigram_model(tokenized_corpus):
    bigram_freq = defaultdict(Counter)
    unigram_freq = Counter()

    for document in tokenized_corpus:
        unigram_freq.update(document)
        for word1, word2 in bigrams(document):
            bigram_freq[word1][word2] += 1

    return bigram_freq, unigram_freq


def bigram_probability(bigram_freq, unigram_freq, word1, word2, smoothing=False):
    V = len(unigram_freq)
    bigram_count = bigram_freq[word1][word2]
    unigram_count = unigram_freq[word1]

    if smoothing:
        return (bigram_count + 1) / (unigram_count + V)
    else:
        if unigram_count == 0 or bigram_count == 0:
            print(f"Unseen bigram: ({word1}, {word2})")  # Debug line
            return 0
        return bigram_count / unigram_count


def sentence_probability(bigram_freq, unigram_freq, sentence, smoothing=False):
    tokens = ['<s>'] + word_tokenize(sentence.lower()) + ['</s>']
    probability = 1.0

    for word1, word2 in bigrams(tokens):
        probability *= bigram_probability(bigram_freq, unigram_freq, word1, word2, smoothing)

    return probability


def predict_next_words(bigram_freq, unigram_freq, sentence_prefix, N, smoothing=False):
    tokens = word_tokenize(sentence_prefix.lower())
    current_word = tokens[-1]
    generated_words = []

    for _ in range(N):
        if current_word not in bigram_freq:
            break

        next_word = max(bigram_freq[current_word], key=bigram_freq[current_word].get, default='</s>')
        if next_word == '</s>':
            break

        generated_words.append(next_word)
        current_word = next_word

    return ' '.join(generated_words)


if __name__ == "__main__":
    corpus = brown.sents()
    tokenized_corpus = preprocess(corpus)
    bigram_freq, unigram_freq = build_bigram_model(tokenized_corpus)

    test_sentence = "The dog barked at the cat."
    probability_no_smoothing = sentence_probability(bigram_freq, unigram_freq, test_sentence, smoothing=False)
    print(f"Sentence probability without smoothing: {probability_no_smoothing}")

    probability_with_smoothing = sentence_probability(bigram_freq, unigram_freq, test_sentence, smoothing=True)
    print(f"Sentence probability with smoothing: {probability_with_smoothing}")

    sentence_prefix = "I won 200"
    N = 5
    predicted_words = predict_next_words(bigram_freq, unigram_freq, sentence_prefix, N, smoothing=True)
    print(f"Predicted next {N} words: {predicted_words}")
