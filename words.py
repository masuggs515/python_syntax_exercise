def print_words_upper(names, must_start_with):
    """Takes a list of strings/names and a list of letters that each name must start with and returns a string 
    in all uppercase letters of each name that starts with the letters given"""
    for name in names:
        for letter in must_start_with:
            if name.startswith(letter):
                print(name.upper())





name_list = ["John", "Bill", "Joe", "Bob", "Mark", "Elaine"]
start_letter = {"B", "J"}
print_words_upper(name_list, start_letter)