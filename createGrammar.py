def createGrammar(lines) :
    Posflag = True
    pos_rule = {} # A -> B C   =>  B : (C, A)
    word_rule = {}

    for line in lines :
        if ( line == '' ) :
            Posflag = False
            continue

        if Posflag == True:
            key, value = addPOSrule(line)
            try :
                pos_rule[key].append(value)
            except KeyError :
                pos_rule[key] = [value]
        else :
            key, value = addWordrule(line)
            try :
                word_rule[key].append(value)
            except :
                word_rule[key] = [value]

    return pos_rule, word_rule


def addPOSrule(line) :
    '''
        :param line: line that contains grammar rule   
        :return: 
            if grammar rule -> return key, (value1, value2) 
             key : left operand
             value1 : right operand
             value2 : result of the operation of the grammar rule
    '''
    res = line.split('->')
    # S -> NP VP
    combined = res[0].strip() # 'S'
    combinee = res[1].strip().split(' ') # [NP, VP]
    if ( len(combinee) == 1 ) :
        combinee = (combinee[0], None) # leftOperand + RightOperand
    else :
        combinee = (combinee[0], combinee[1]) # LeftOperand + RightOperand

    return combinee[0], (combinee[1], combined)


def addWordrule(line) :
    '''
        :param line: line that contains word rule 
        :return: word and POS
    '''
    res = line.split('->')
    return res[1].strip(), res[0].strip()
