import nltk
from nltk import CFG
from nltk.parse.generate import generate

# Define the context-free grammar (CFG)
cfg = CFG.fromstring("""
S -> NP VP
NP -> DT NN | DT JJ NN
VP -> VB NP | VB
DT -> 'the' | 'a'
NN -> 'dog' | 'cat' | 'park'
JJ -> 'big'
VB -> 'chases' | 'barks'
""")

# Create a parser
parser = nltk.ChartParser(cfg)

# Define a sentence
sentence = "the big dog chases a cat".split()

# Generate parse tree(s)
parse_trees = list(parser.parse(sentence))

# Display parse tree(s)
for tree in parse_trees:
    print(tree)
    tree.draw()
