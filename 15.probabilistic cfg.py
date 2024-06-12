import nltk
from nltk import PCFG

# Define the probabilistic context-free grammar (PCFG)
pcfg = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> DT NN [0.6] | DT JJ NN [0.4]
VP -> VBZ NP [0.5] | VBP NP [0.5]
DT -> 'the' [0.8] | 'a' [0.2]
NN -> 'dog' [0.5] | 'dogs' [0.2] | 'cat' [0.2] | 'cats' [0.1]
JJ -> 'big' [0.5] | 'small' [0.5]
VBZ -> 'chases' [0.5] | 'barks' [0.5]
VBP -> 'chase' [0.5] | 'bark' [0.5]
""")

# Create a Viterbi parser
parser = nltk.ViterbiParser(pcfg)

# Define a sentence
sentence = "the big dog chases a cat".split()

# Parse the sentence
parse_trees = list(parser.parse(sentence))

# Display the parse tree(s) with probabilities
for tree in parse_trees:
    print(tree)
    tree.pretty_print()
    tree.draw()
