def get_book_text(path):
    with open(path) as f: # open file information based on the current local file system
        return f.read()
    
def get_num_words(text):
    words = text.split() # split on the ' ' charecter to get words
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        c = char.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(d):
    # return d["num"] # sorted list by char count
    return d["char"] # sorted by char


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    
    for ch in num_chars_dict:
        sorted_list.append({ "char": ch, "num": num_chars_dict[ch] })
    
    # sorted_list.sort(reverse=True, key=sort_on)
    sorted_list.sort(reverse=False, key=sort_on)

    return sorted_list

def print_alpha_chars(text_dict, isDynamic = False):
    if isDynamic:
        # Dynamic Solution
        chars_sorted_list = chars_dict_to_sorted_list(text_dict)
        
        print("Dynamic")
        for item in chars_sorted_list:
            if item["char"].isalpha():
                print(f"The '{item['char']}' character was found {item['num']} times")
    else:
        # Simple Solution
        alpha_chars = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
        
        for char in alpha_chars:
            if text_dict.get(char) is not None:
                value = text_dict[char]
                print(f"The '{char}' character was found {value} times")            
            

def book_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    print_alpha_chars(chars_dict)
    print(f"--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    # Tasks

    # Task(1) - print book text
    # print(text)

    # Task(2) - print number of works in the book
    # print(f"{num_words}") # (2)
    # print(f"{num_words} words found in the document") # (2)

    # Task(3) - print the dictionary of all characters used by the book
    # print(chars_dict) # (3)

    # Task(4) - print book report about:
    # - file path; 
    # - numbers of words
    # - the count of each alpha character used by the book
    book_report(book_path, num_words, chars_dict)
    
main()