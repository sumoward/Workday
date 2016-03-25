# -*- coding: utf-8 -*-
"""

PYTHON  VERSION 2.7.10

Problem - Word Paths
Outline
The problem is to find “word paths”. What this means is that you find a path from one word to
another word, changing one letter each step, and each intermediate word must be in the
dictionary.
We tend to use the dictionary file on a unix/linux/mac in /usr/share/dict/words. If you do not
have a copy of this file, please let us know.
Some example solutions:
rial ­> real ­> feal ­> foal ­> foul ­> foud
dung ­> dunt ­> dent ­> gent ­> geet ­> geez
jehu ­> jesu ­> jest ­> gest ­> gent ­> gena ­> guna ­> guha
yagi ­> yali ­> pali ­> palp ­> paup ­> plup ­> blup
bitt ­> butt ­> burt ­> bert ­> berm ­> berm ­> germ ­> geum ­> meum
jina ­> pina ­> pint ­> pent ­> peat ­> prat ­> pray
fike ­> fire ­> fare ­> care ­> carp ­> camp
The program should take as input the path to the word file, a start word and an end word and
print out at least one path from start to end, or something indicating there is no possible path if
appropriate.

e.g.
need to get this working with linux
$ python ./wordpaths.py /usr/share/dict/words flux alem
cat ­> cot ­> cog ­> dog
python C:\Users\desktop1\PycharmProjects\Workday\src\wordpaths.py ../resources/test.txt cat dog

Requirements
● Please send your output as one .tar.gz file to your recruitment contact
● Your software should have an appropiate basic command line utility to run
● Try to demonstrate OO methodologies where possible (e.g. encapsulation)
● Where your program is written in an interpreted language like ruby or python, please
say which version you’ve used
● Include appropriate testing routines.
● No use of third party libraries for the main code. The intent of the problem is to
demonstrate the ability to write the particular data structures & algorithms that are
most applicable to solve this problem.
"""

from collections import defaultdict, deque
import string
import pickle
import time
import sys


class WordPath:
    def __init__(self, path=None, start_word=None, end_word=None):
        """
            constructor for WordPath
        """
        self.path = path
        self.start_word = start_word
        self.end_word = end_word
        self.dictionary = []
        self.graph = defaultdict(list)
        self.paths = deque([[self.start_word]])
        self.pickle_path = r'../resources/graphs.pkl'
        self.cached_graphs = {}
        self.main()

    def are_valid_words(self):
        """
          To check that the start and end words are in the dictionary supplied
          :return: boolean
        """
        if self.start_word in self.dictionary and self.end_word in self.dictionary:
            return True

    def import_dictionary(self):
        """
            Read in the dictionary from the supplied path
        """
        try:
            print self.path
            with open(self.path) as inputfile:
                self.dictionary = inputfile.read().splitlines()
        except IOError:
            print 'A valid path for the Dictionary was not supplied.'

    def graph_exists(self):
        """
            Check if a graph for this dictionary already exists
        :return:
        """
        # check if we have persisted the graph for this dictionary path in our pickle file
        with open(self.pickle_path, 'rb') as file:
            self.cached_graphs = pickle.load(file)

        if self.path in self.cached_graphs:
            self.graph = self.cached_graphs[self.path]
            return True
        return False

    def persist_graph(self):
        """
            Pickle our graph for future use
        :return:
        """
        with open(self.pickle_path, 'wb') as file:
            self.cached_graphs[self.path] = self.graph
            pickle.dump(self.cached_graphs, file)

    def create_graph(self):
        """
            The graph is a hash table where the key is a word and the value is the list of valid
            transformations of that word. Creating the graph has an overhead but if we persist
            it then all future word searches on it benefit. Creating the graph takes 7705385 iterations.
            There are 58,110 words of average length 5.1 and we substitute in all the letters of the alphabet
        """

        alphabet = string.lowercase
        # Out of curiosity we will check how long creating a graph takes
        print 'START: ' + time.ctime()
        for word in self.dictionary:
            for i in range(len(word)):
                # change 1 character
                for char in alphabet:
                    change = word[:i] + char + word[i + 1:]
                    if change in self.dictionary and change != word:
                        print time.ctime()
                        self.graph[word].append(change)

        print 'END: ' + time.ctime()
        self.persist_graph()

    def search_graph(self):
        """
            Breath first search of the graph
        """
        while len(self.paths) != 0:
            current_path = self.paths.popleft()
            current_word = current_path[-1]
            if current_word == self.end_word:
                self.paths = [current_path]
                return
            next_step = self.graph[current_word]
            for word in next_step:
                if word not in current_path:
                    self.paths.append(current_path[:] + [word])

    def __str__(self):
        """
            :return: string - format the path into the format, cat -> cot -> cog -> dog
        """
        if self.paths[0]:
            return ' -> '.join(self.paths[0])
        else:
            return ''

    def main(self):
        """
            find the path between two words
            :return: string in format, cat -> cot -> cog -> dog
        """
        # import the dictionary if we have a path
        if self.path:
            self.import_dictionary()
        else:
            print "No dictionary path was supplied."
            return
        if self.start_word == self.end_word:
            print "Your starting word and ending word are identitical : " + self.start_word
            return

        # check the Start and end words are in the Imported Dictionary
        if not self.are_valid_words():
            print "You have not chosen valid words for the supplied dictionary: " + self.start_word + ', ' + self.end_word
        else:
            # if we have not created a graph for the dictionary and persisted it, create it now
            if not self.graph_exists():
                self.create_graph()
            # search for our path
            self.search_graph()
            print self.__str__()
            return self.__str__()


if __name__ == "__main__":
    try:
        WordPath(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        print 'Please supply valid arguments.'
