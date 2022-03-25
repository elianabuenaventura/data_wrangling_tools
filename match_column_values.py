"""
This Python script compares column values in different Excel files against one another to search for matches
"""


# LOAD YOUR .cvs FILES
## To begin the search for matches, you will import the pandas module and read your files as csv files. 
## The files are saved as comma separated value files (csv files) and you will use the read_csv() function to parse them. 
## You could alternatively leave your Excel files with the native .xlsx extension and use the pandas.read_excel() function.
## The sampled sequences DataFrame were assigned the variable A and the reference sequences DataFrame were assigned the variable B. 
## To validate things are working, the code parses the DataFrames checking specifically for their columns.


import pandas as pd

A = pd.read_csv(r'path/to/sampled_seqs.csv')
B = pd.read_csv(r'path/to/ref_seqs.csv')

print(A.columns)
print(B.columns)


### Output:
  
### Index(['Unknown_sample_no', 'Unknown_sample_seq'], dtype='object')
### Index(['Reference_sequences_ID', 'Reference_sequences'], dtype='object')



# CONVERT DATAFRAMES INTO PYTHON LISTS
## Next, you convert both columns in both DataFrames into python lists. 
## To do this the code uses the .tolist() method on a specified column of a particular DataFrame. 
## For example, the column ‘Unknown_sample_no’ in DataFrame A is converted to a list. 
## This step is applied to the two columns in the two files, as shown in the code snippet below.


My_unknown_id = A['Unknown_sample_no'].values.tolist()
My_unknown_seq = A['Unknown_sample_seq'].values.tolist()

Reference_species = B['Reference_sequences_ID'].values.tolist()
Reference_sequences = B['Reference_sequences'].values.tolist()



# JOIN YOUR LISTS TO KEEP DATA STRUCTURE
## You should keep the association between the unique identifier ‘Unknown_sample_no’ and its corresponding sequence ‘Unknown_sample_seq’. 
## Similarly, you should also keep the association between the the unique identifier ‘Reference_sequences_ID’ and their corresponding reference sequence ‘Reference_sequences’. 
## You can maintain this association by converting the two lists into two dictionaries.
## You can use the zip function to join the lists and then use the dict function to convert them in appropriately assigned dictionaries.


Ref_dict = dict(zip(Reference_species, Reference_sequences))
Unknown_dict = dict(zip(my_unknown_id, my_unknown_seq))


## To confirm the dictionaries have been made correctly, you can run the script in the terminal. 
## A brief validation check informs you that things are workings as intended. 
## From the Ref_dict for example, the ‘Reference_sequences_ID’ keys match up correctly to their corresponding ‘Reference_sequences’ values: 
## ‘{‘A’: ‘AAAAGCGCGAGGGGGGA’, ‘K’: ‘GGGAGAGAGGG’, ‘Y’: ‘CGGAGCGTTT’…..}


print(Ref_dict)
print(Unknown_dict)


### Output:
  
### {'A': 'AAAAGCGCGAGGGGGGA', 'K': 'GGGAGAGAGGG', 'Y': 'CGGAGCGTTT', 'T': 'TTTTAGAGAGCTCTG', 'P': 'TAGAGAGCGGCC', 'E': 'GAAGGCGCT', 'V': 'TATAGCGCGCG', 'M': 'TAGAGCGCGA', 'N': 'GGCTCCGGGAGA', 'Q': 'GGGGCCCCCATA'}
### {1: 'AGCGCGAGGGGGGA', 2: 'GGGAGAGA', 3: 'CGGAGCGTTT', 4: 'TAGCTGAGA', 5: 'TAGAGAGCGGCC', 6: 'GAAGGCGCT', 7: 'TATAGCGCGCG', 8: 'TAGAGCGCGA', 9: 'GAGGCTCCGGGAGA', 10: 'GGGGCCCCCATA'}



# FIND YOUR MATCHES
## You can now compare your two 2 dictionaries against one another. 
## To do so, the codes runs a for loop to iterate though the ‘Unknown_dict’ and a nested for loop to iterate through the Ref_dict. 
## At each iteration, you want to know whether the sequence in the Unknown_dict matches to any of the sequences in the Ref_dict 
## Some will, the files include 8 matches. 
## To check for matches, the code uses the re.search() function from the re module (regular expression module).
## When there is a match, it is useful to know, what sequence matched, where that match appeared in the DNA sequence, 
## and most importantly what ‘Unknown_sample_no’ matches to which ‘Reference_sequences_ID’.

# SAVE YOUR MATCHES TO A .cvs FILE FOR VISUALIZATION AND DATA INTERPRETATION
## The code below also saves all the matches to a single csv file. This will make it clear which sequences match, what the matching sequence is and where did it match.
## Now, you know for example, that Query_ID: 1 corresponds to Ref_species A, and this match starts at position 4 in the sequence.


import re
filename = 'seq_match_compare.csv'
f = open(filename, 'w')


headers = 'Query_ID, Query_Seq, Ref_species, Ref_seq, Match, Match start Position\n'
f.write(headers)

for ID, seq in Unknown_dict.items():
    for species, seq1 in Ref_dict.items():
        m = re.search(seq, seq1)
        if m:
            match = m.group()
            pos = m.start() + 1
            f.write(str(ID) + ',' + seq + ',' + species + ',' + seq1 + ',' + match + ',' + str(pos) + '\n')

f.close()





