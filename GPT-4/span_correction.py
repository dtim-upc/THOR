# Define a function to count the spaces and special characters before each entity in the text
def count_spaces_before_entity(text, entity_start):
    return len([char for char in text[:entity_start] if char in [' ', '\n']])

# Correct the entity spans by adding the count of spaces and special characters before each entity
for entry in data:
    text = entry['text']
    for entity in entry['entities']:
        if entity[2] != 'Disease_E':  # Skip the first entity (Disease_E)
            spaces_count = count_spaces_before_entity(text, entity[0])
            entity[0] += spaces_count
            entity[1] += spaces_count

# Let's examine the first few corrected entries
data[:5]