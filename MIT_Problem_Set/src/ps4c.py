# Problem Set 4C ----------------------> Substitution Cipher
# Name: <Rituram Ojha>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'MIT_Problem_Set/src/words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        cpy_valid_words = self.valid_words
        return cpy_valid_words

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        # pass  # delete this line and replace with your code here
        dict = {}
        vowels_permutation = vowels_permutation.lower()

        for letter in CONSONANTS_LOWER:
            dict[letter] = letter
        for letter in CONSONANTS_UPPER:
            dict[letter] = letter

        for i in range(len(VOWELS_LOWER)):
            dict[VOWELS_LOWER[i]] = vowels_permutation[i]
        for i in range(len(VOWELS_UPPER)):
            dict[VOWELS_UPPER[i]] = vowels_permutation[i].upper()

        return dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        enc_msg = ''
        for letter in self.message_text:
            if letter in transpose_dict:
                enc_msg += transpose_dict[letter]
            else:
                enc_msg += letter
        return enc_msg


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    

        Hint: use your function from Part 4A
        '''

        # get list of possible permutations on 'aeiou'
        list_perm = get_permutations('aeiou')

        # stores the decrypted messages on list of possible permutations of 'aeiou'
        dec_msg = []

        # stores the no. of real words in each of the decrypted messages
        count_list = [0]*len(list_perm)

        # count of real word for each sentence
        count_real_word = 0

        for perm in list_perm:
            transpose_dict = self.build_transpose_dict(perm)
            dec_msg.append(self.apply_transpose(transpose_dict))

        for index, sentence in enumerate(dec_msg):
            count_real_word = 0
            for word in sentence.split():
                if is_word(self.valid_words, word):
                    count_real_word += 1
            count_list[index] = count_real_word

        # get the index of count_list that has maximum real words
        max_val = max(count_list)
        for i in range(len(count_list)):
            if count_list[i] == max_val:
                break

        return (list_perm[i], dec_msg[i])


if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:", message.get_message_text(),
          "Permutation:", permutation)
    print("\nExpected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))

    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("\nDecrypted message:", enc_message.decrypt_message())
