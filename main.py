import CKYParser as C
import createGrammar as CG
import traceBack as T

# create Grammar from 'grammar.txt' file
CNFgrammars = open('grammar.txt').read().strip().split('\n')
CNFpos, CNFword = CG.createGrammar(CNFgrammars)

# Read input of lines
lines = open('input.txt').read().strip().split('\n')
lines = [line.strip('.') for line in lines]
fout = open('output.txt', 'w')

# CKY Parse !
for line in lines :
    Mat = C.CKYParser(line, CNFpos, CNFword, fout)
    size = len(line.split(' '))

    rootNodes = Mat[0][size]
    for node in rootNodes :
        if ( node.pos == 'S' ) :
            fout.write(T.traceBack(node) + '\n')

fout.close()