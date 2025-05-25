from stats import get_num_words, get_char_dict, sort_list

def get_book_text(file_path):
    print(f"Analyzing book found at{file_path}")
    with open(file_path) as f:
        file_contents = f.read()
        return(file_contents)
 


def main():
    import sys
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
     
    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    char_dict = get_char_dict(book_text)
    print("--------- Character Count -------")
    sorted_list = sort_list(char_dict)

    for item in sorted_list:
        if item['char'].isalpha():
         print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")
    return

main()

