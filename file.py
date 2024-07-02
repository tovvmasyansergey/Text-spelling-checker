"""
This file is check words
Create by: Sergey Tovmasyan
Date: 21.06.2024
"""
import argparse
import re
import enchant
import string
def get_arguments():
    """
    Function: get_arguments
    Brief: The function is get 2 argument,filename for
           read text,output file for read
    Params: filename`name of file with text,
             output file `name of file for write correct text
    Return: filename,output filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True,
                             help="This is a input file name with text")
    parser.add_argument('-o', '--output',required = True,
                              help="Please input file for finish text")
    args = parser.parse_args()
    filename = args.file
    output_file = args.output
    return filename,output_file
def open_file(filename):
    """
    Function: open_file
    Brief: The function is open file and read text
    Params: filename`name of file with text
    Return: list of linse with words
    """
    with open(filename,encoding = 'utf-8') as ffile:
        list_lines = ffile.readlines()
    return list_lines
def check_words(content):
    """
    Function: check_words
    Brief: The function is check every word and if word not
           correct,user input word and in text change
    Params: content `list of lines with words
    Return: list of words with correct words
    """
    dicnary = enchant.Dict("en_US")
    list_words = []
    for line in content:
        correct_line = ""
        words = re.findall(r'\b\w+\b|[^\w\s]',line)
        for word in words:
            if word.isalpha() and word.strip() and re.match(r'\w+',word) and not dicnary.check(word):
                print("The wrong word: ",word)
                print("choose the right word",word,
                          " ".join(dicnary.suggest(word)[:5]))
                flag = True
                new_word = ""
                while flag:
                    new_word = input()
                    if new_word in dicnary.suggest(word)[:5]:
                        flag = False
                    else:
                        print("please choose from list of words")
                correct_line += " "
                correct_line += new_word
#                else:
#                    correct_line += " "
#                    correct_line += word
#                    correct_line += " "
            elif word in string.punctuation:
                correct_line += word
            else:
                correct_line += " "
                correct_line += word
        list_words.append(correct_line)
    return list_words
def write_in_file(filename,content):
    """
    Function: write_in_file
    Brief: The function is open file and write correct text
    Params: output file for new text,content`with new correct words
    Return:None
    """
    with open(filename,"w",encoding = 'utf-8') as ffile:
        for line in content:
            ffile.write(line.strip())
            ffile.write("\n")
def main():
    """
    Function: main
    """
    filename,output_file = get_arguments()
    content = open_file(filename)
    cnt = check_words(content)
    print(cnt)
    write_in_file(output_file,cnt)
if __name__ == "__main__":
    main()
