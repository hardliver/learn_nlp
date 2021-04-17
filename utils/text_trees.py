from nltk.tree import Tree
import svgling


def draw_text_trees(text):
    tree = Tree.fromstring(str(text))
    return svgling.draw_tree(tree)
