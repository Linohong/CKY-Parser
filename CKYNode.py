class Node :
    def __init__(self, pos, word=None) :
        self.pos = pos
        self.word = word
        self.lNode = None # left Node
        self.rNode = None # Right Node