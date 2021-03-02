def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    '''
    cleaned = ""
    for letter in word:
        if letter.isalpha():
            cleaned = cleaned + letter.lower()

    # YOUR CODE GOES HERE
    return cleaned


def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise
    '''
    same = True
    i = 0
    while same and i < len(w2):
        if (w2[i] not in w1) or (len(w1) != len(w2)) or w2.count(w2[i]) != w1.count(w2[i]):
            same = False
        i = i + 1
    return same


def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    '''
    s = s.split()
    s = list(map(clean_word, s))
    s.sort()
    length = len(s)
    i = 0
    while i < length-1:
        if s[i] == s[i+1]:
            s.pop(i+1)
            length = len(s)
        i += 1

    return sorted(s)


def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    '''
    # YOUR CODE GOES HERE
    list1 = []
    for words in wordbook:
        answer = test_letters(word, words)
        if answer == True and not (word == words):
            list1.append(words)
    return sorted(list1)


def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    Whenever a word in l is the same as a word in wordbook, that is not counted.

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''

    anagram_count = []
    for char in l:
        count = 0
        for words in wordbook:
            answer = test_letters(char, words)
            if answer == True and not (char == words):
                count = count + 1
        anagram_count.append(count)
    return anagram_count


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)
    '''


    klist = []
    for i in range(len(l)):
        if anagcount[i] == k:
            klist.append(l[i])
    return sorted(klist)


def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    '''
    largest_anagram = k_anagram(l, anagcount, max(anagcount))
    return sorted(largest_anagram)


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    ['year']
    '''
    smallest_anagram = k_anagram(l,anagcount,0)
    return sorted(smallest_anagram)


def scrabble_words(word, wordbook):
    '''
    (string, list) -> list

     preconditions: input must be a string with no spaces
    - This function takes a string(word) and a list as input and returns all
      the words possible that can be made from these letters in a list
    '''
    list1 = []
    for words in wordbook:
        condition = test_letters(word, words)
        if condition:
            list1.append(words)
    return list1
##############################
# main
##############################


if __name__ == "__main__":

    print(create_clean_sorted_nodupicates_list("cat sheet silt slit trace boat cat crate slit"))
    wordbook = open("english_wordbook.txt").read().lower().split()
    list(set(wordbook)).sort()
    wordbook.sort(key=len)

    print("Would you like to:")
    print("1. Analize anagrams in a text -- given in a file")
    print("2. Get small help for Scrabble game")
    print("Enter any character other than 1 or 2 to exit: ")
    choice = input()

    if choice == '1':
        file_name = get_file_name()
        rawtx = open(file_name).read()
        l = create_clean_sorted_nodupicates_list(rawtx)
        anagcount = count_anagrams(l, wordbook)

        print("\nOf all the words in your file, the following words have the most anagrams:")
        highest = max_anagram(l, anagcount)
        print(highest)
        print("Here are their anagrams")
        for i in range(len(highest)):
            print("anagrams of ", highest[i], " are:", word_anagrams(highest[i], wordbook))
        print("Here are the words in your file that have no anagrams")
        print(zero_anagram(l, anagcount))
        print("Say you are interested in a word with exactly K anagrams")
        k = int(input("Enter an integer for k: "))
        print("Here is a word (words) in your file thats with exactly ",k," anagrams: \n",k_anagram(l,anagcount,k))
    elif choice == '2':

        # YOUR CODE GOES HERE
        wrong_input = True
        while wrong_input:
            print("Enter the letters you have with no spaces: ",end="")
            letters = input()

            if " " in letters:
                print("Error:you entered space(s)")
            else:
                confliction = True
                while confliction:
                    print("Would you like help forming a word with\n 1. all these letters \n 2. all but one of these letters?")
                    decision = input()
                    if not(decision.strip() == "1" or decision.strip() == "2"):
                        print("you must choose 1 or 2. Please try again")
                    else:
                        decision = int(decision)
                        confliction = False
                        if decision == 1:
                            words = scrabble_words(letters, wordbook)
                            print("Here are the words that are compromised of exactly these letters: \n",words)
                        else:
                            print("The letters you gave us are: ", letters, "\n Lets see what we get if we omit one of these letters")
                            for i in range(len(letters)):
                                words = []
                                char = letters[:i]
                                char = char+letters[i+1:]
                                anagrams = scrabble_words(char, wordbook)
                                words = words+anagrams
                                if len(words) == 0:
                                    print("Without letters in position", i+1, "we have letters", char)
                                    print("There are no words compromised with letters: ", char)
                                else:
                                    print("Without letters in position", i + 1, "we have letters", char)
                                    print("The following word/words compromise of these letters", char,": ", words)
                wrong_input = False
    else:
        print("Good bye")