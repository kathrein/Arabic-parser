# Introduction to Formal Linguistics Lab 1: Context-free grammar

# Author: Stergios Chatzikyriakidis using Simon Dobnik's code
# Email: stergios.chatzikyriakidis@gu.se



import nltk



# Uncomment/comment the appropriate lines below

draw_trees = True # Also draws trees graphically: you can comment this out (and uncomment the next line) if you are just testing the grammar
#draw_trees = False

GRAMMAR = "file:part3-grammar.fcfg" # example grammar
#GRAMMAR = "file:grammar.fcfg" # your grammar
CORPUS = "sentences.txt" # sentences parsed by the example grammar
#CORPUS = "sentences.txt" # sentences for the assignment



# You do not need to change anything below this line.


def main():
    parser = nltk.load_parser(GRAMMAR)
    counter = 0
    c=0
    with open(CORPUS) as F:
        for line in F:
            sent = line.split()
            if sent:
                trees = list(parser.parse(sent))
                print(counter)
                counter += 1
                print('{0}:  {1}\n'.format(len(trees)," ".join(sent)))
                if(draw_trees):
                    nltk.draw.tree.draw_trees(*trees)
                for tree in trees:
                   print(tree)
                   print('\n')



if __name__ == '__main__':
    main()



# eof
