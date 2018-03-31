def traceBack(node) :
    if (node.word is not None) :
        return node.pos + " " + node.word
    else :
        leftNode = node.lNode
        rightNode = node.rNode
        return node.pos + "(" + traceBack(leftNode) + ")" + "(" + traceBack(rightNode) + ")"

