import re

def clean_text(text):
    clean_text = re.sub('/', ' ', text)
    clean_text2 = re.sub('\w*\d\w*', ' ', clean_text)
    return clean_text2
    

def clean_word(word):
    word = re.sub('[)(]|\-$', ' ',word)
    word = re.sub('- $|^-|-$', '', word)
    return word



def clean_lemmatize_join_ent(doc):
    clean_t = [t.lemma_.strip().lower().replace(" ", "_") for t in doc]
    clean_t2 = " ".join(clean_t)
    
    return clean_t2


def clean_lemmatize_join_token(doc):
    clean_t = [t.lemma_.strip().lower() for t in doc.ents]
    clean_t2= []
    for i in clean_t:
        if len(re.split(" ", i)) == 1 and (len(str(i)) > 1):
            clean_t2.append(clean_word(i))
        else:
             for j in re.split(" ", i):
                if (len(str(j)) > 1):
                    clean_t2.append(clean_word(j))

    clean_t3 = " ".join(clean_t2)
    return clean_t3