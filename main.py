def count_letters(text):
    
    letter_box = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in letter_box :
                letter_box[char] +=1
            else:
                letter_box[char] =1
    return (letter_box)
def print_to_console(letter_count, words_count):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f" {words_count} words found in the document")
    letter_count_list = list(letter_count.items())
    letter_count_list.sort(key=lambda x: x[1], reverse=True)
    for letter_count in letter_count_list:
        print (f"The {letter_count[0]} character was found {letter_count[1]} times")
    
   

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    words_count = len(words)
    letter_count = count_letters( file_contents)
    print_to_console(letter_count,words_count)


    

    
    


