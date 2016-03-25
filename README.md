# Workday
Word path game

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
appropiate.
