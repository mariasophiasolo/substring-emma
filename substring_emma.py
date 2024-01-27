# write a program to find how many times substring "Emma" appears in given string

def count_emma_occurrences(input_string):
    # convert the input string to lowercase for case-insensitive matching
    input_string_lower = input_string.lower()
    # check how many times substring "Emma" occured
    count = input_string_lower.count("emma")

    return count

given_string = "Emma is a good developer. Emma is a writer"
result = count_emma_occurrences(given_string)

print ("Number of occurrences of 'Emma':", result)

