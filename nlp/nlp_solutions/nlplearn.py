###################################################################
########           NLP Learn - Bot NLP tool kit       #############
###################################################################

""" 

    nlplearn.py - This file contains the codes to perform Natural language processing. 
    
"""    

from nltk.tokenize import word_tokenize
import re
import nltk
# from nltk.corpus import stopwords
# from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import os,sys
import joblib
sys.path.append(os.path.normpath(os.getcwd()))

from config import onetime_file

try:
    cosine_sim,indices, tfidf_fit1, tfidf_matrix1 = joblib.load(onetime_file)
except:
    cosine_sim, indices, tfidf_fit1, tfidf_matrix1 = ['','','','']

metadata = pd.read_csv('data/metadata_prep.csv')

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
# STOPWORDS = set(stopwords.words('english'))
STOPWORDS = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}

def text_prepare(doc):

    doc = doc.lower()
    doc = REPLACE_BY_SPACE_RE.sub(' ',doc)
    doc = BAD_SYMBOLS_RE.sub('',doc)
    doc = " ".join([w for w in word_tokenize(doc) if not w in STOPWORDS])
    return doc


def tfidf_fit(docs):

    docs = [text_prepare(text) for text in docs]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_fit = tfidf_vectorizer.fit(docs)
    tfidf_matrix = tfidf_fit.transform(docs)

    return tfidf_fit, tfidf_matrix


def similarity_search(doc, list_index, tfidf_fit=tfidf_fit1,tfidf_matrix=tfidf_matrix1):

    out = cosine_similarity(tfidf_fit.transform([text_prepare(doc)]), tfidf_matrix.tocsr()[list_index,:])
    a = list(out[0])
    b = sorted(range(len(a)), key=lambda i: a[i], reverse=True)[:5]
    return b


def metadata_filtering(docs):

    tfidf = TfidfVectorizer(stop_words='english')
    docs = docs.fillna('')
    tfidf_matrix = tfidf.fit_transform(docs)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    return cosine_sim


def get_recommendations(title, metadata=metadata,indices=indices, cosine_sim=cosine_sim):

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]

    return metadata['title'].iloc[movie_indices]

