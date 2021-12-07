import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from numpy import spacing
import pandas as pd
import matplotlib.pyplot as plt
import collections, operator
import csv
from nltk.util import ngrams
import seaborn as sns

nltk.download('stopwords')
nltk.download('punkt')

# Question: "What do you like about the library's current website?" in row [13]

#import survey data and convert to nltk corpus

corpus = ''
corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    corpus = corpus + row[13] + ' '
    corpus_list.append(row[13])

           
file.close()

#tokenize words, convert to lowercase
tokens = nltk.word_tokenize(corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
filtered_tokens = []

for word in tokens:
    if not word in stop_words:
        filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)

#print(len(corpus_list), len(tokens), len(filtered_tokens))

# print list of all words
#print(tokens)

# print list of all words minus stopwords
#print(filtered_tokens)

# Transform word lists (tokens) into NLTK Text objects

text = nltk.Text(tokens)

filtered_text = nltk.Text(filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

freq_dist = FreqDist(tokens)

freq_dist_filtered = FreqDist(filtered_tokens)

#plot of top 25 tokens

#print(freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

filter_words = dict([(m, n) for m, n in freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also']])

#for key in sorted(filter_words):
 #   print("%s: %s" % (key, filter_words[key]))
 
data_analysis = nltk.FreqDist(filter_words)
#data_analysis.plot(25, cumulative=False)

## Creating FreqDist for filtered_words, keeping the 25 most common tokens
all_fdist = FreqDist(filter_words).most_common(25)

## Conversion to Pandas series via Python Dictionary for easier plotting
all_fdist = pd.Series(dict(all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "What do you like about the library website?"')
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=all_fdist.index, y=all_fdist.values, ax=ax)
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("sitelikes.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(text.collocations(n))

