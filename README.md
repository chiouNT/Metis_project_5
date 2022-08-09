# NLP project: Genetic Variant Classification

## Abstract

The DNA sequencing results of the * paper are usually stored at the GEO datasets. The reuse or compare of the DNA sequencing data will greatly save the research resources. The project is to recommend the datasets for reanalysis based on the abstract of the literatures associated with the datasets.

## Data

The data is the abstracts scraped from the GEO database API. There are around 3000 abstracts

## Preprocessing and model building

In pre-processing the data, there are 2 steps. The first step is to remove all digit, backslash, parenthesis and hyphen in the abstract. The second step is to tokenize the abstract into the named entities, followed by lemmatization, string stripping, lowercasing, and adding hyphen between words in named entities. I then build a model using TfidfVectorizer and NMP topic modeler with a topic components (n=5)  

## Algorithms

* Text preprocessing: Scispacy
* Text vectorization with TfidfVectorizer
*	kMeans clustering
*	NMF modeling
*	Word embedding via tSNE
*	Visualization via Matplotlib and Seaborn




## Communication
* The analysis showed that most abstracts in the GEO database have the low similarity. Only 10% of them are clustered well with kMeans clustering strategy.

![alt text](https://github.com/chiouNT/NLP/blob/master/Image/tSNE_kMeans.jpg)
