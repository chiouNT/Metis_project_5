from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
from sklearn.cluster import KMeans


additional_stop_words = ['patient', 'human', 'dna', 'cell', 'cancer', 'tumor', 'cellular', 'copyright', 'line', 'mouse', 'tissue', 'sample', 'blood']

def vectorizeText(inputText):
    cv = CountVectorizer(stop_words = additional_stop_words)
    doc_word_matrix = cv.fit_transform(inputText)
    
    return cv, doc_word_matrix

def vectorizeTextIDF(inputText):
    cv_tfidf = TfidfVectorizer(stop_words = additional_stop_words, min_df = 0.001, max_df = 0.75)
    doc_word_tfidf_matrix = cv_tfidf.fit_transform(inputText)
    
    return cv_tfidf, doc_word_tfidf_matrix

def doNMF(numTopics, doc_word_matrix, vectorizer, no_top_words):
    nmf_model = NMF(numTopics)
    nmf_model.fit(doc_word_matrix)
    topic_word_matrix = nmf_model.components_.round(3)
    
    words = vectorizer.get_feature_names()

    doc_topic_matrix = nmf_model.fit_transform(doc_word_matrix)
    top_word_each_topic = []
    
    for n, topic in enumerate(topic_word_matrix):
        top_word = [words[i] for i in topic.argsort()[:-no_top_words - 1:-1]]
        top_word_each_topic.append(", ".join(top_word))
        print("\nTopic ", n + 1)
        print(", ".join(top_word))
    print("\n")

    return doc_topic_matrix, topic_word_matrix, top_word_each_topic



def doLSA(numTopics, doc_word_matrix, vectorizer, no_top_words):
    lsa_model = TruncatedSVD(numTopics)
    lsa_model.fit(doc_word_matrix)
    topic_word_matrix = lsa_model.components_.round(3)
    
    words = vectorizer.get_feature_names()

    doc_topic_matrix = lsa_model.fit_transform(doc_word_matrix)
    top_word_each_topic = []
    
    for n, topic in enumerate(topic_word_matrix):
        top_word = [words[i] for i in topic.argsort()[:-no_top_words - 1:-1]]
        top_word_each_topic.append(", ".join(top_word))
        print("\nTopic ", n + 1)
        print(", ".join(top_word))
    print("\n")
         

    return doc_topic_matrix, topic_word_matrix, top_word_each_topic


    
def dokMeans(numClusters, doc_word_matrix, vectorizer, no_top_words):
    
    km = KMeans(n_clusters=numClusters, random_state=425)
    doc_clusters = km.fit_predict(doc_word_matrix)

    ordered_cluster = km.cluster_centers_
    words = vectorizer.get_feature_names()
    
    top_word_kMeans = []
        
    for n, topic in enumerate(ordered_cluster):
        top_word = [words[i] for i in topic.argsort()[:-no_top_words - 1:-1]]
        top_word_kMeans.append(", ".join(top_word))
        print("\nTopic ", n + 1)
        print(", ".join(top_word))
    print("\n")
         
        
    return doc_clusters, ordered_cluster, top_word_kMeans



def dokMeans2(numClusters, doc_topic_matrix, top_word_each_topic, no_top_words):
    
    km = KMeans(n_clusters=numClusters, random_state=425)
    doc_clusters = km.fit_predict(doc_topic_matrix)

    ordered_cluster = km.cluster_centers_
    words = top_word_each_topic
    
    top_word_kMeans = []
        
    for n, topic in enumerate(ordered_cluster):
        top_word = [words[i] for i in topic.argsort()[:-no_top_words - 1:-1]]
        top_word_kMeans.append(", ".join(top_word))
        print("\nTopic ", n + 1)
        print(", ".join(top_word))
    print("\n")
         
        
    return doc_clusters, ordered_cluster, top_word_kMeans
