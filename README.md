## Pandas for column matching
This script allows comparison between column values in different Excel files to search for matches and/or similarity. This script uses the Pandas library from Python.The example below uses Excel files (as .cvs files) containing DNA sequences as an example, but no genetic knowledge is required to use this script. 

Context: You have some unknown samples of DNA sequences (simple strings composed of the letters A,T,G and C) in a file called [sampled_seqs.csv](https://github.com/elianabuenaventura/data_curation_tools/blob/main/sampled_seqs.cvs). Each DNA sequence is assigned a unique identifier. To simplify the example, the unique identifiers are numbers from 1 to 10. You also have some reference sequences in a file called [ref_seqs.csv](https://github.com/elianabuenaventura/data_curation_tools/blob/main/ref_seqs.cvs) where each DNA sequence is assign a unique identifier as capital letters. You want to compare your sampled sequences against known reference sequences. So, here your quesitons is do any of the sampled sequences match against the reference sequences? If they do, which sequence(s) do they match up with?

match_column_values.py also saves all the matches to a single csv file. This will make it clear which sequences match, what the matching sequence is and where did it match. This script also saves the results in a .cvs file, which eases visualization and data interpretation.

## Search for keywords in selected PubMed abstracts
This Python script searches for keywords in a series of PubMed abstracts

This example can be applied to perform very simple text mining and can be compared to the “find” tool in Microsoft Word.
It might stop on the first occurence.

## Find transcription factor binding sites
This Python script searches for transcription factor binding sites using the library re
