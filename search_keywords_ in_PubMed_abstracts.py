"""
This Python script searches for keywords in a series of PubMed abstracts

This example can be applied to perform very simple text mining and can be compared to the “find” tool in Microsoft Word.
It might stop on the first occurence.
"""


import urllib2
import re

# word to be searched
word_regexp = re.compile('schistosoma')

# list of PMIDs where we want to search the word
pmids = ['18235848', '22607149', '22405002', '21630672']
for pmid in pmids:
    url = 'http://www.ncbi.nlm.nih.gov/pubmed?term=' + pmid
    handler = urllib2.urlopen(url)
    html = handler.read()
    title_regexp = re.compile('<h1>.{5,400}</h1>')
    title = title_regexp.search(html)
    title = title.group() 
    abstract_regexp = re.compile('<AbstractText>.{20,3000}</AbstractText>')
    abstract = abstract_regexp.search(html)
    abstract = abstract.group()
    word = word_regexp.search(abstract, re.IGNORECASE)
    if word:
        # display title and where the keyword was found
        print title
        print word.group(), word.start(), word.end()
