import math
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def show_doc_in_cluster(doc_word_matrix, docs, doc_clusters, ordered_cluster, topic_no):
    
    cluster_center = ordered_cluster[topic_no]
    labels = list(doc_clusters)
    label_of_interest = [label == topic_no for label in labels]
###    doc_in_cluster = doc_topic_matrix[label_of_interest]
    
    n_list =[]
    dists = []
    dists2 = []
    for n, i in enumerate(doc_word_matrix):
        if label_of_interest[n]:
            dist = (np.dot(i, cluster_center)/np.linalg.norm(i)/np.linalg.norm(cluster_center), n)
            dists.append(dist)
            dist2 = (np.dot(i, cluster_center)/np.linalg.norm(i)/np.linalg.norm(cluster_center))
            if math.isnan(dist2):
                dists2.append(0)
            else:
                dists2.append(dist2)
            
        
    index_min_dist = [i[1] for i in sorted(dists)][:3]

    
    ##return index_min_dist, [docs[i] for i in index_min_dist]
    return dists2



def show_doc_in_cluster_NMF(doc_topic_matrix, docs, topic_no):
    
    labels = [i.argsort()[:-1][0] for i in doc_topic_matrix]

    label_of_interest = [label == topic_no for label in labels]
###    doc_in_cluster = doc_topic_matrix[label_of_interest]
    doc_topic_matrix_topic = doc_topic_matrix[label_of_interest]
    
    
    
    dists = []
    dists2 = []
    for n, i in enumerate(doc_topic_matrix_topic):
        for m, j in enumerate(doc_topic_matrix_topic):
            if n != m:
                dist = (np.dot(i, j)/np.linalg.norm(i)/np.linalg.norm(j), (i, j))
                dists.append(dist)
                dist2 = (np.dot(i, j)/np.linalg.norm(i)/np.linalg.norm(j))
                if math.isnan(dist2):
                    dists2.append(0)
                else:
                    dists2.append(dist2)

            
        
    #index_min_dist = [i[1:3] for i in sorted(dists)][:3]

    
    ##return index_min_dist, [docs[i] for i in index_min_dist], dist2
    return dists2

def distance_plot(doc_word, docs, doc_clusters, ordered_cluster, name):
    df_box_plot = pd.DataFrame()
    for i in range(15):
        a = show_doc_in_cluster(doc_word, docs, doc_clusters, ordered_cluster, i)
        b =[f'{i}']*len(a)
        df = pd.DataFrame([b, a]).T
        df_box_plot = pd.concat([df_box_plot, df], axis = 0)
        
    df2 = df_box_plot.copy()
    df2.columns = ['cluster', 'distances']
    df2['distances'] = df2['distances'].astype(float)
    sns.set(font_scale =1.5)
    p = sns.boxplot(x='cluster', y="distances", data =df2)
    p.set_title("Distance to the centroids")
    plt.savefig(f'Image/{name}_distances.jpg',  bbox_inches='tight')
    plt.show()
    
    
def distance_plot2(doc_topic_matrix, docs, name):
    df_box_plot = pd.DataFrame()
    for i in range(15):
        a = show_doc_in_cluster_NMF(doc_topic_matrix, docs, i)
        b =[f'{i}']*len(a)
        df = pd.DataFrame([b, a]).T
        df_box_plot = pd.concat([df_box_plot, df], axis = 0)
        
    df2 = df_box_plot.copy()
    df2.columns = ['cluster', 'distances']
    df2['distances'] = df2['distances'].astype(float)
    sns.set(font_scale =1.5)
    p = sns.boxplot(x='cluster', y="distances", data =df2)
    p.set_title("Distance to the centroids")
    plt.savefig(f'Image/{name}_distances.jpg',  bbox_inches='tight')
    plt.show()