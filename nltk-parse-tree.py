import nltk

#sentence = """At eight o'clock on Thursday morning
#... Arthur didn't feel very good."""

#tokens = nltk.word_tokenize(sentence)
#print("tokens:",tokens)

#tagged = nltk.pos_tag(tokens)
#print("tagged:",tagged)

#entities = nltk.chunk.ne_chunk(tagged)
#print("entities:",entities)

#from nltk.corpus import treebank
#t = treebank.parsed_sents('/tmp/sentences.txt')[0]
#t.draw()

def quicktree(sentence):
    """Parse a sentence and return a visual representation"""
    from nltk import Tree
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget
    from stat_parser import Parser
    from IPython.display import display
    from IPython.display import Image
    parser = Parser()
    parsed = parser.parse(sentence)
    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(),parsed)
    cf.add_widget(tc,10,10) # (10,10) offsets
    cf.print_to_file('tree.ps')
    cf.destroy()
#   ! convert tree.ps tree.png
#   ! rm tree.ps
#   return Image(filename='tree.png')
#   ! rm tree.png
  
quicktree("This is a parse tree.")

