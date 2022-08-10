import seaborn as sns
import matplotlib.pyplot as plt



def df_append_result(df, doc_topic_matrix, name='NMF'):
    
    labels = [i.argsort()[:-1][0] for i in doc_topic_matrix]
    df2 = df.copy()
    df2[f"{name}"] = labels  
    
    return df2

def df_append_result_kMeans(df, doc_clusters, name='kMeans'):
    labels = list(doc_clusters)
    df2 = df.copy()
    df2[f"{name}"] = labels  
    
    return df2
    
def getCounts(df, top_word_each_topic, name):

    unique_topic_values = df[name].sort_values().unique()
    
  
  
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x = name, data=df.sort_values(by=name))
    
    ax.set_xticklabels(top_word_each_topic, rotation = 90, fontsize = 14)
    
    if name == 'NMF':
        plt.title("NMF topic modeling", fontsize = 14)
        plt.xlabel("Abstract Topic", fontsize = 14)
        plt.ylabel("Number of abstract", fontsize = 14)
        
        
    else:
        plt.title("kMeans abstract clustering", fontsize = 14)
        plt.xlabel("Abstract Topic", fontsize = 14)
        plt.ylabel("Number of abstract", fontsize = 14)

    fig.savefig(f'Image/{name}.jpg',  bbox_inches='tight')    
    plt.show()
    
    
def getCounts_2(df, top_word_each_topic, name):

    unique_topic_values = df[name].sort_values().unique()
    
  
  
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x = name, data=df.sort_values(by=name))
    
    ax.set_xticklabels(top_word_each_topic, rotation = 90, fontsize = 14)
    
    if name == 'NMF':
        plt.title("NMF topic modeling", fontsize = 14)
        plt.xlabel("Abstract Topic", fontsize = 14)
        plt.ylabel("Number of abstract", fontsize = 14)
        
        
    else:
        plt.title("kMeans abstract clustering", fontsize = 14)
        plt.xlabel("Abstract Topic", fontsize = 14)
        plt.ylabel("Number of abstract", fontsize = 14)

    fig.savefig(f'Image/{name}_2.jpg',  bbox_inches='tight')    
    plt.show() 