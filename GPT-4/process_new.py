import json
import os
import glob

# Define the list of valid entity types
ENTITY_TYPES = ['Disease_E', 'Anatomy_E', 'Cause_E', 'Diagnosis_E', 'Precaution_E', 'Riskfactor_E', 'Symptom_E', 'Medicine_E', 'Composition_E', 'Complication_E', 'Surgery_E']

def process_data(data, line_number):
    # Loop over the entities in reverse order so we can remove elements without affecting the loop
    for i in range(len(data['entities']) - 1, -1, -1):
        entity_type = data['entities'][i][2]
        if entity_type not in ENTITY_TYPES:
            # Print the line number and the mismatched entity
            print(f'Mismatched entity at line {line_number}: {entity_type}')

            # Remove the entity from the 'entities' list
            del data['entities'][i]

    return data


def process_entity_spans(data):
    text = data['text']
    entities = data['entities']
    corrected_entities = []

    # Find the actual start and end indices of the first entity in the text
    actual_start = text.index(' - ') + 3
    actual_end = text.index(' - ', actual_start)

    # Get the reported start and end from the entities list
    reported_start, reported_end, _ = entities[0]

    # Calculate the differences to adjust the other entities
    start_diff = actual_start - reported_start
    end_diff = actual_end - reported_end

    # Correct the start and end indices of each entity
    for entity in entities:
        start, end, label = entity

        # Adjust the start and end indices based on the difference
        start += start_diff
        end += end_diff

        # Check if start and end indices are within the length of the text
        if start > len(text) or end > len(text):
            continue

        # Add the corrected entity to the list
        corrected_entities.append([start, end, label])

    data['entities'] = corrected_entities
    return data


def process_file(input_file, output_file):
    # Initialize an empty list to hold the data
    data_list = []

    # Read the file line by line
    with open(input_file, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            try:
                # Try to parse the line as JSON
                data = json.loads(line)

                # If successful, add the data to the list
                data_list.append(data)
            except json.JSONDecodeError:
                # If an error occurs, print the line number
                print(f'Error decoding JSON at line {i} of file {input_file}')

    # Process the data
    processed_data_list = [process_data(data, i+1) for i, data in enumerate(data_list)]

    corrected_entity_spans = [process_entity_spans(processed_data) for processed_data in processed_data_list]

    # Write the processed data back to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for data in corrected_entity_spans:
            file.write(json.dumps(data, ensure_ascii=False) + '\n')

def main():
    # Get the list of all JSON files in the 'input' directory
    input_files = glob.glob(os.path.join('input', '*.json'))

    # Make sure the 'output' directory exists
    os.makedirs('output', exist_ok=True)

    # Loop over all input files
    for input_file in input_files:
        # Prepare the output filename
        output_file = os.path.join('output', os.path.basename(input_file))

        # Process the input file and write to the output file
        process_file(input_file, output_file)

if __name__ == '__main__':
    main()
