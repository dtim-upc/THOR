import json

# input and output file paths
input_file_path = 'input/1.Test_Mayo_Combined.json'
output_file_path = 'input/2.Text_Only_Test_Mayo.json'

# open the input file in read mode and output file in write mode
with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
    # read each line in the input file
    for line in infile:
        # parse the line as a JSON object
        data = json.loads(line)
        # create a new dictionary with only 'text' fields
        reduced_data = {'text': data['text']}
        # write the reduced data to the output file
        outfile.write(json.dumps(reduced_data, ensure_ascii=False) + '\n')
