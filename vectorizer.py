from glob import glob
from tqdm import tqdm
import numpy as np
import re
word = re.compile("e(v|u)enl(y|ie)|kingl(y|ie)|onel(y|ie)|a(v|u)owe|godl(ie|y)|l(y|i)(f|v)el(y|ie)|cro(vv|w)ne?")
vocab = set()
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

for ii in tqdm(glob("*/*.txt")):
    with open(ii,'r') as infile:
        lines = infile.readlines()
        if len(lines)>4:
            for line in lines[4:]:
                for token in line.replace("\xad",'').replace(".",' ').replace(",",' ').split(' '):
                    #get the word that matches the regex above.
                    morpheme = word.search(token)
                    if morpheme and morpheme[0] not in stopwords:
                        vocab.add(morpheme[0]) #significant speedup over using a list.
vocab = list(vocab)
print(len(vocab))
#store the list of words that the regex matched.
with open("list of words.ending","w+") as outfile:
    outfile.write(str(vocab))
for ii in tqdm(glob("*/*.txt")):
    vec = np.zeros(len(vocab))
    with open(ii,'r') as infile:
        lines = infile.readlines()
        if len(lines)>4:
            for line in lines[4:]:
                for token in line.replace("\xad",'').replace(".",' ').replace(",",' ').split():
                    morpheme = word.search(token)
                    if morpheme and morpheme[0] not in stopwords:
                        vec[vocab.index(morpheme[0])] += 1
    #made up this file extension, so that I can easily glob it later.
    np.savetxt(ii[:-4]+".nsv",vec)
