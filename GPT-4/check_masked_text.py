'''
This program will compare the length of the "text" fields for both Actual Text and the Text with Heading Masked. 
If any mismatch is found, the line number will be printed.
The masking is done in order not to hint the LM/LLM about the Topic of the given file e.g., Symptoms, Treatment etc.,
'''

import json

# input file paths
input_file_path1 = 'input/2.Text_Only_Test_Mayo.json'
input_file_path2 = 'output/GPT_Pred.json'

# open both files in read mode
with open(input_file_path1, 'r', encoding='utf-8') as infile1, open(input_file_path2, 'r', encoding='utf-8') as infile2:
    line_number = 1
    mismatch = 0
    for line1, line2 in zip(infile1, infile2):
        # parse the lines as JSON objects
        data1 = json.loads(line1)
        data2 = json.loads(line2)
        
        len1 = len(data1['text'])
        len2 = len(data2['text'])



        # compare the length of the 'text' fields
        if len1 != len2:
            print(f'Mismatch found at line {line_number}.')
            mismatch += 1

        line_number += 1
    
    if mismatch == 0:
        print('No Mismatch found')