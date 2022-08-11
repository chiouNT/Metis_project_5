# Recommender of the GEO datasets based on NLP analysis of their associated abstracts 

## Abstract

The gene expression or DNA profiling results of the research paper are usually stored at the GEO datasets. The reuse or comparison of the genomic data will greatly save the research resources to get hints about the potential drug targets or biomarkers. The project is to recommend the datasets for reanalysis based on the abstract of the literatures associated with the datasets.

## Data

The data is the abstracts scraped from the GEO database API (https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gds&id=200209437&version=2.0). There are around 3000 abstracts.

## Preprocessing and model building

During pre-processing the data, there are 2 steps. The first step is to remove all digit, backslash, parenthesis and hyphen in the abstract. The second step is to tokenize the abstract into the named entities, followed by lemmatization, string stripping, lowercasing, and adding hyphen between words in named entities. I then build the matrix of documents and words using TfidfVectorizer.

## Topic Model building

* Startegy I: kMeans clustering
* Startegy II: NMF topic modeling followed by kMeans clustering

## Algorithms

* Text preprocessing: Scispacy
* Text vectorization with TfidfVectorizer
*	kMeans clustering
*	NMF modeling
*	Word embedding via tSNE
*	Visualization via Matplotlib and Seaborn

## Communication

* The abstracts are clustered into 15 topics with the strategy II. One cluster, which is related to stem cells and chromatin, contains half amounts of the abstracts has the lowerest similairty of the abstracts within the cluster. All other clusters contain ~50-200 abstracts have higher similarity of the abstracts within the clusters. 

![alt text](https://github.com/chiouNT/NLP/blob/master/Image/tSNE_kMeans2.jpg)
![alt text](https://github.com/chiouNT/NLP/blob/master/Image/kMeans_2_distances.jpg)
![alt text](https://github.com/chiouNT/NLP/blob/master/Image/kMeans_2.jpg)

* The abstracts in the same clusters will be further filtered based on their associated datasets. The datasets with the similar topics and experimental designs, such as whole blood sequencing from different covid patient cohorts, will be useful for identifying the new biomarkers or drug taragets.

