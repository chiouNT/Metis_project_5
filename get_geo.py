import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import sys




def get_id(start, num):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=humans[MeSH Terms]+OR+Homo+sapiens[Organism]+OR+human[All Fields]&retstart={}&retmax={}".format(start, num)
    response_esearch = requests.get(url)
    page_html_esearch = response_esearch.text
    soup_esearch = BeautifulSoup(page_html_esearch, 'xml')
    
    id_list = [i.text for i in soup_esearch.find_all('Id')]
    print(id_list)
    return id_list

def get_title(soup):
    try:
        title = soup.find("title").text
        return title
    except:
        return None
    
def get_pmid(soup):
    try:
        pmid = soup.find("PubMedIds").text
        return pmid
    except:
        return None
    
def get_abstract(PMID):
    url ="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract&retmode=xml&id={}".format(PMID)

    response = requests.get(url)
    page_html = response.text
    soup = BeautifulSoup(page_html, 'xml')

    try:
        text = soup.find('Abstract').text
        return text  
    except:
        return None

    
def get_dict(id_list):

    id_list2 = []
    title_list = []
    pmid_list = []
    abstract_list = []


    for n, i in enumerate(id_list):
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gds&id={}&version=2.0".format(i)
        response = requests.get(url)
        page_html = response.text
        soup = BeautifulSoup(page_html, 'xml')
        
        title = get_title(soup)
        pmid = get_pmid(soup)
        abstract = get_abstract(pmid)
        


        m = len(abstract_list)
        if abstract != None:
            if (m==0) or (m!=0 and (abstract != abstract_list[-1])):
                id_list2.append(i)
                title_list.append(title)
                pmid_list.append(pmid)
                abstract_list.append(abstract)

            
        if n%100 == 0:
            print(n)
            
            
    Dict = {"Id": id_list2,
            "PMID": pmid_list,
            "Title": title_list,
            "Abstract": abstract_list
           }
        
    return Dict

def load_dict(Dict):
    
    df = pd.DataFrame(Dict)
    df.to_sql(f"geo_{start}_{num}", con, if_exists='append', index=False)


if __name__ == '__main__':

    start = int(sys.argv[1])
    length = 100
    num = int(sys.argv[2])  # input
    
    start_list = [(i*length+start) for i in range(int(num/length))] 
    
    for i in start_list:
        id_list = get_id(i, length)
        Dict = get_dict(id_list)
        con = sqlite3.connect("geo.db")
        load_dict(Dict)
        
    con.close()

    print("\nAll done!\n")