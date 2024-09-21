calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    _Tuple = (len(string), string.upper(), string.lower())
    count_calls()
    return _Tuple

def is_contains (string, list_to_search):
    string = string.upper()
    for i in list_to_search:
        if i.upper() in string:
            count_calls()
            return True
    count_calls()
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
