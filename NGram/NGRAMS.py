#!/usr/bin/python
import sys
import re
import collections


def generate_ngrams(s, n):
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    tokens = [token for token in s.split(" ") if token != ""]
    n_grams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in n_grams]


def ngramCountCorpusWithoutSmoothing(ngramStatement, ngramCountDict):
    ngramCountDictStatement = {}
    for key in ngramStatement:
        count = ngramCountDict[key]
        ngramCountDictStatement[key] = count
    return ngramCountDictStatement


def ngramProbabilityMatrixWithoutSmoothing(ngramCounter, corpusCount):
    probabilityMatrix = {}
    for key in ngramCounter:
        count = ngramCounter[key]
        totalCount = corpusCount[key.split()[0]]
        probabilityMatrix[key] = count / totalCount
    return probabilityMatrix


def ngramCountCorpusWithSmoothing(ngramStatement, ngramCountDict):
    ngramCountDictStatement = {}
    vcount = len(ngramCountDict)
    for key in ngramStatement:
        count = ((ngramStatement[key] + 1) * ngramCountDict[key.split()[0]]) / (
                ngramCountDict[key.split()[0]] + vcount)
        ngramCountDictStatement[key] = count

    return ngramCountDictStatement


def ngramProbabilityMatrixWithSmoothing(ngramCounter, corpusCount):
    probabilityMatrix = {}
    vcount = len(corpusCount)
    for key in ngramCounter:
        count = ngramCounter[key]
        totalCount = corpusCount[key.split()[0]]
        probabilityMatrix[key] = (count + 1) / (totalCount + vcount)
    return probabilityMatrix


def probabilitySentence(probabilityDictionary):
    probability = 1
    for key, value in probabilityDictionary.items():
        probability = probability * value
    return probability


def bigramsAlgorithms(statement1, statement2):
    print("BIGRAM WITHOUT SMOOTHING\n")
    file = open("corpus.txt", "r", encoding="utf8")
    text = file.read()
    bigramCounts = collections.Counter(generate_ngrams(text, 2))
    corpusCounts = collections.Counter(text.split())

    bigramStatement1 = collections.Counter(generate_ngrams(statement1, 2))
    bigramStatement2 = collections.Counter(generate_ngrams(statement2, 2))

    bigramCountCorpusStatement1 = ngramCountCorpusWithoutSmoothing(bigramStatement1, bigramCounts)
    bigramCountCorpusStatement2 = ngramCountCorpusWithoutSmoothing(bigramStatement2, bigramCounts)
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement1)
    print("\n\n")
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement2)
    print("\n\n\n\n")

    probabilityMatrixStatement1 = ngramProbabilityMatrixWithoutSmoothing(bigramCountCorpusStatement1, corpusCounts)
    ProbabilityMatrixStatement2 = ngramProbabilityMatrixWithoutSmoothing(bigramCountCorpusStatement2, corpusCounts)
    print("Probability Matrix for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n")
    print("Probability Matrix for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n\n\n")

    probabilityStatement1 = probabilitySentence(probabilityMatrixStatement1)
    probabilityStatement2 = probabilitySentence(ProbabilityMatrixStatement2)
    print("Probabilty of Statement : ", statement1)
    print(probabilityStatement1)
    print("\n\n")
    print("Probabilty of Statement : ", statement2)
    print(probabilityStatement2)
    print("\n\n\n\n")


def trigramsAlgorithms(statement1, statement2):
    print("TRIGRAM WITHOUT SMOOTHING\n")
    file = open("corpus.txt", "r", encoding="utf8")
    text = file.read()
    bigramCounts = collections.Counter(generate_ngrams(text, 3))
    corpusCounts = collections.Counter(text.split())

    bigramStatement1 = collections.Counter(generate_ngrams(statement1, 3))
    bigramStatement2 = collections.Counter(generate_ngrams(statement2, 3))

    bigramCountCorpusStatement1 = ngramCountCorpusWithoutSmoothing(bigramStatement1, bigramCounts)
    bigramCountCorpusStatement2 = ngramCountCorpusWithoutSmoothing(bigramStatement2, bigramCounts)
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement1)
    print("\n\n")
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement2)
    print("\n\n\n\n")

    probabilityMatrixStatement1 = ngramProbabilityMatrixWithoutSmoothing(bigramCountCorpusStatement1, corpusCounts)
    ProbabilityMatrixStatement2 = ngramProbabilityMatrixWithoutSmoothing(bigramCountCorpusStatement2, corpusCounts)
    print("Probability Matrix for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n")
    print("Probability Matrix for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n\n\n")

    probabilityStatement1 = probabilitySentence(probabilityMatrixStatement1)
    probabilityStatement2 = probabilitySentence(ProbabilityMatrixStatement2)
    print("Probabilty of Statement : ", statement1)
    print(probabilityStatement1)
    print("\n\n")
    print("Probabilty of Statement : ", statement2)
    print(probabilityStatement2)
    print("\n\n\n\n")


def bigramsAlgorithmsWithSmoothing(statement1, statement2):
    print("BIGRAM WITH SMOOTHING\n")
    file = open("corpus.txt", "r", encoding="utf8")
    text = file.read()
    bigramCounts = collections.Counter(generate_ngrams(text, 2))
    corpusCounts = collections.Counter(text.split())

    bigramStatement1 = collections.Counter(generate_ngrams(statement1, 2))
    bigramStatement2 = collections.Counter(generate_ngrams(statement2, 2))

    bigramCountCorpusStatement1 = ngramCountCorpusWithSmoothing(bigramStatement1, bigramCounts)
    bigramCountCorpusStatement2 = ngramCountCorpusWithSmoothing(bigramStatement2, bigramCounts)
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement1)
    print("\n\n")
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement2)
    print("\n\n\n\n")

    probabilityMatrixStatement1 = ngramProbabilityMatrixWithSmoothing(bigramCountCorpusStatement1, corpusCounts)
    ProbabilityMatrixStatement2 = ngramProbabilityMatrixWithSmoothing(bigramCountCorpusStatement2, corpusCounts)
    print("Probability Matrix for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n")
    print("Probability Matrix for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n\n\n")

    probabilityStatement1 = probabilitySentence(probabilityMatrixStatement1)
    probabilityStatement2 = probabilitySentence(ProbabilityMatrixStatement2)
    print("Probabilty of Statement : ", statement1)
    print(probabilityStatement1)
    print("\n\n")
    print("Probabilty of Statement : ", statement2)
    print(probabilityStatement2)
    print("\n\n\n\n")


def trigramsAlgorithmsWithSmoothing(statement1, statement2):
    print("TRIGRAM WITH SMOOTHING\n")
    file = open("corpus.txt", "r", encoding="utf8")
    text = file.read()
    bigramCounts = collections.Counter(generate_ngrams(text, 3))
    corpusCounts = collections.Counter(text.split())

    bigramStatement1 = collections.Counter(generate_ngrams(statement1, 3))
    bigramStatement2 = collections.Counter(generate_ngrams(statement2, 3))

    bigramCountCorpusStatement1 = ngramCountCorpusWithSmoothing(bigramStatement1, bigramCounts)
    bigramCountCorpusStatement2 = ngramCountCorpusWithSmoothing(bigramStatement2, bigramCounts)
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement1)
    print("\n\n")
    print("Bigram Count for Statement : ", statement1)
    print(bigramCountCorpusStatement2)
    print("\n\n\n\n")

    probabilityMatrixStatement1 = ngramProbabilityMatrixWithSmoothing(bigramCountCorpusStatement1, corpusCounts)
    ProbabilityMatrixStatement2 = ngramProbabilityMatrixWithSmoothing(bigramCountCorpusStatement2, corpusCounts)
    print("Probability Matrix for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n")
    print("Probability Matrix for Statement for Statement : ", statement1)
    print(probabilityMatrixStatement1)
    print("\n\n\n\n")

    probabilityStatement1 = probabilitySentence(probabilityMatrixStatement1)
    probabilityStatement2 = probabilitySentence(ProbabilityMatrixStatement2)
    print("Probabilty of Statement : ", statement1)
    print(probabilityStatement1)
    print("\n\n")
    print("Probabilty of Statement : ", statement2)
    print(probabilityStatement2)
    print("\n\n\n\n")


if __name__ == "__main__":
    n = int(sys.argv[2])
    b = int(sys.argv[4])
    statement1 = "Milstein is a gifted violinist who creates all sorts of sounds and arrangements ."
    statement2 = "It was a strange and emotional thing to be at the opera on a Friday night ."
    if n == 2:
        if b == 0:
            bigramsAlgorithms(statement1, statement2)
        elif b == 1:
            bigramsAlgorithmsWithSmoothing(statement1, statement2)
        else:
            print("b Should Be 0 OR 1")
    elif n == 3:
        if b == 0:
            trigramsAlgorithms(statement1, statement2)
        elif b == 1:
            trigramsAlgorithmsWithSmoothing(statement1, statement2)
        else:
            print("b Should Be 0 OR 1")
    else:
        print("N Should Be 2 OR 3")
