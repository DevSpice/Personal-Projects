"""
CMSC 14200: trie-based spell-checker and tab-completer Distribution

Adam Shaw
Winter 2023

Trent Houle
"""


class Trie:
    """
    Class for representing tries
    """

    def __init__(self, root):
        """
        Constructor

        Parameters:
         root : str (a character, but Python does not have a "char" type)

        Initialize root to given char, empty dict of children, final to False.
        """
        self.root = root
        self.children = {}
        self.final = False

    def insert(self, word):
        """
        Insert the word into the trie.

        Parameters:
             word : str

        Returns: (does not return a value)
        """
        if len(word) > 1: 
          if word[1] not in self.children:
            self.children[word[1]] = Trie(word[1])
          word2 = word[1:]
          self.children[word[1]].insert(word2)
        else:
            self.final = True

    def contains(self, word):
        """
        Check presence of given word in the trie.

        Parameters:
         word : str

        Returns: boolean
        """
        if word[0] != self.root:
          return False

        if len(word) == 1:
          return self.final

        if word[1] in self.children:
            word2 = word[1:]
            return self.children[word[1]].contains(word2)
        else:
            return False

    def all_words(self):
        """
        Return all the words in the trie. Returned list not guaranteed
        in any particular order.

        Parameters:
         none

        Returns: list[str]
        """
        word_list = []
        current_word = self.root
        
        if self.children:
          for child in self.children:
            word_list.extend(self.children[child].all_words())

          for i in range(len(word_list)):
            word_list[i] = current_word + word_list[i]

        if self.final:
          word_list.append(current_word)
        
        return word_list

    def num_words(self):
        """
        Return the number of words in the trie.

        Parameters:
          none

        Returns: int
        """
        total_words = 0
        if self.final == True:
          total_words += 1
        if self.children:
          for child in self.children:
            total_words += self.children[child].num_words()
        return total_words

    def completions(self, prefix):
        """
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        """
        if prefix[0] != self.root:
          return []

        return self._compl(prefix, "")

    def _compl(self, prefix, acc):
        """
        Private method. Return all completions given prefix. The
        variable acc stores the string seen thus far in traversal of
        the trie. The returned list is not guaranteed to be in any
        particular order.

        Parameters:
          prefix : str
          acc : str

        Returns: list[str]
        """
        word_lst = []
        acc += self.root

        if acc != prefix:
          next_char = prefix[len(acc)]
          if next_char not in self.children:
            return []
          word_lst.extend(self.children[next_char]._compl(prefix, acc))
        
        else:
          for word in self.all_words():
            word_lst.append(prefix[:-1] + word)
        
        return word_lst

    def num_completions(self, prefix):
        """
        Return the number of completions of the given prefix.

        Parameters:
          prefix : str

        Returns: int
        """
        if prefix[0] != self.root:
          return 0

        if len(prefix) > 1:
          next_child = prefix[1]
          new_prefix = prefix[1:]
          return self.children[next_child].num_completions(new_prefix)

        else:
          return self.num_words()


class TrieOrthographer:
    """
    Class for a trie-based orthographer
    """

    def __init__(self):
        """
        Constructor

        Parameters:
          none

        Initialize dictionary of empty tries, one per letter.
        """
        self.tries = {}
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.tries[char] = Trie(char)

    def insert(self, word):
        """
        Insert the word into the orthographer if it consists only of lowercase
        letters.

        Parameters:
          word : str

        Returns: (does not return a value)
        """
        if len(word) == 0 or not word.isalpha() or not word.islower():
          return
        self.tries[word[0]].insert(word)

    def insert_from_file(self, filename):
        """
        Read the named file, insert words (one per line in file).

        Parameters:
          filename : str

        Returns: (does not return a value)
        """
        with open(filename) as word_file:
          for word in word_file:
              word = word.strip()
              if word.isalpha() and word.islower():
                self.insert(word)

    def contains(self, word):
        """
        Check presence of given word in the orthographer.

        Parameters:
          word : str

        Returns: boolean
        """
        return self.tries[word[0]].contains(word)

    def completions(self, prefix):
        """
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        """
        if len(prefix) == 0 or prefix[0] not in self.tries:
          return []
        return self.tries[prefix[0]].completions(prefix)

    def num_completions(self, prefix):
        """
        Return the number of completions given prefix.

        Parameters:
          prefix : str

        Returns: int
        """

        if len(prefix) == 0 or prefix[0] not in self.tries:
          return []
        return self.tries[prefix[0]].num_completions(prefix)

    def all_words(self):
        """
        Return all the words in the orthographer. Returned list not
        guaranteed in any particular order.

        Parameters:
          none

        Returns: list[str]
        """
        word_lst = []
        for trie in self.tries:
          word_lst.extend(self.tries[trie].all_words())
        return word_lst

    def num_words(self):
        """
        Return the number of words in the orthographer.

        Parameters:
          none

        Returns: int
        """
        count = 0
        for trie in self.tries:
          count += self.tries[trie].num_words()
        return count
