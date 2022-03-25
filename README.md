# data_curation_tools
Simple python scripts for finding matches between datasets

## Comparing column values in different Excel files using Pandas

### Pandas for column matching
This script allows comparison between column values in different Excel files to search for matches and/or similarity. This script uses the Pandas library from Python.The example below uses Excel files containing DNA sequences as an example, but no genetic knowledge is required to use this script. 

Context: You have some unknown samples of DNA sequences (simple strings composed of the letters A,T,G and C) in a file called sampled_seqs.csv. Each DNA sequence is assigned a unique identifier. To simplify the example, the unique identifiers are numbers from 1 to 10. You also have some reference sequences in a file called ref_seqs.csv where each DNA sequence is assign a unique identifier as capital letters. You want to compare your sampled sequences against known reference sequences. So, here your quesitons is do any of the sampled sequences match against the reference sequences? If they do, which sequence(s) do they match up with?


