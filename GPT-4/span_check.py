# Define the JSON data
data = {"text":"#Overview - Acanthosis nigricans - ED51.00\nAcanthosis nigricans is a condition that causes areas of dark, thick velvety skin in body folds and creases. It typically affects the armpits, groin and neck. Acanthosis nigricans (ak-an-THOE-sis NIE-grih-kuns) tends to affect people with obesity. Rarely, the skin condition can be a sign of cancer in an internal organ, such as the stomach or liver. Treating the cause of acanthosis nigricans might restore the usual color and texture of the skin.",
        "entities":[[0,17,"Disease_E"],[80,87,"Anatomy_E"],[89,94,"Anatomy_E"],[99,104,"Anatomy_E"],[134,141,"Riskfactor_E"],[184,190,"Disease_E"],[213,219,"Anatomy_E"],[225,230,"Anatomy_E"]]
        }

def process_entity_spans(data):
    # Find the actual start and end indices of the first entity in the text
    actual_start = data['text'].index(' - ') + 3
    actual_end = data['text'].index(' - ', actual_start)
    
    # Get the reported start and end indices of the first entity
    reported_start, reported_end, _ = data['entities'][0]

    # Calculate the difference between the reported and actual indices
    start_diff = reported_start - actual_start
    end_diff = reported_end - actual_end

    # Adjust the start and end indices of each entity based on the calculated differences
    for i in range(len(data['entities']) - 1, -1, -1):
        entity = data['entities'][i]
        entity[0] -= start_diff
        entity[1] -= end_diff

        # If the start index is out of bounds, remove the entity
        if entity[0] < 0 or entity[0] > len(data['text']):
            print(f'Removed entity with out-of-bounds start index: {entity[0]}')
            del data['entities'][i]
            continue

        # If the end index is out of bounds, remove the entity
        if entity[1] < entity[0] or entity[1] > len(data['text']):
            print(f'Removed entity with out-of-bounds end index: {entity[1]}')
            del data['entities'][i]

    return data

# Process the data
processed_data = process_entity_spans(data)

print(processed_data)