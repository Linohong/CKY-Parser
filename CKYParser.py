import CKYNode as N

def writeUsedRule(combined, left, right, fout) :
    if (right == None) :
        fout.write(combined + " -> " + left + '\n')
    else :
        fout.write(combined + " -> " + left + " " + right + '\n')

# This Matrix will hold CKYNodes
def CKYMatrix(size) :
    Mat = []
    for i in range(size+1) :
        Mat.append([])
        for j in range(size+1) :
            Mat[i].append([])

    return Mat

def CKYParser(line, CNFpos, CNFword, fout) :
    fout = fout
    line = line.split(' ') # make it list of words
    size = len(line)
    Mat = CKYMatrix(size)

    for e in range(1, size+1) :
        for s in range(e-1, -1, -1) :
            # s~e = s~k + k~e
            ParseEkS(line, s, e, CNFpos, CNFword, Mat, fout)

    return Mat


def ParseEkS(line, s, e, CNFpos, CNFword, Mat, fout) :
    # k between 's to e'
    if ( e-s == 1 ) :
        word = line[s]
        for pos in CNFword[word]:  # ['v', 'n']
            writeUsedRule(pos, word, None, fout)
            for _, combined in CNFpos[pos] : # NP -> n
                newNode = N.Node(combined, word)
                writeUsedRule(combined, pos, None, fout)
                Mat[s][e].append(newNode)
        return

    for k in range(s+1, e) :
        leftNodes = Mat[s][k]
        rightNodes = Mat[k][e]

        # Both are empty
        if (leftNodes==[] or rightNodes==[]) :
            continue

        # left and right Nodes both are not empty
        for leftNode in leftNodes :
            for rightNode in rightNodes :
                leftpos = leftNode.pos
                rightpos = rightNode.pos

                try :
                    for(op_right, combined) in CNFpos[leftpos] :
                        if op_right == rightpos :
                            newNode = N.Node(combined)
                            newNode.rNode = rightNode
                            newNode.lNode = leftNode
                            writeUsedRule(combined, leftpos, rightpos, fout)
                            Mat[s][e].append(newNode)
                except KeyError :
                    continue