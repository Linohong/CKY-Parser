------------------------------------------------
이름 : LinoHong
사용언어 : python 3.6
사용환경 : Pycharm 2017.1
------------------------------------------------
input : 'input.txt', 'grammar.txt' 두 개의 파일
output : 'grammar.txt'
동작방법 : main.py 파일을 Run 하면 output 이 생성됩니다.
------------------------------------------------
내부 구조 설명
* main.py
    - 'grammar.txt' 파일을 읽어들여 grammar 를 생성하도록 함수 호출 (createGrammar.py)
    - 'input.txt' 파일을 읽어들임.
    - CKY parsing algorithm 을 사용하여 문장별 parsing을 하도록 함수 호출 (CKYParser.py)
    - line별로 return한 CKY matrix 를 back tracking 하며 tree 구조 출력 (traceBack.py)

* CKYNode.py
    - CKY Matrix 내부의 rule들은 노드들로 이루어져있다. 이 노드를 정의한다.

* createGrammar.py
    * def addPOSrule(line) :
        - 'grammar.txt' 파일의 POS -> POS POS 부분을 읽어들인 후 grammar rule 을 생성한다.
        - grammar rule은 dictionary 자료구조로 저장한다.
            => A -> B C 와 같은 규칙이 존재할 경우,
               'B' : (C, A) 와 같이 key는 B, value는 (C, A) 튜플이다.
    * def addWordrule(line) :
        - 'grammar.txt' 파일의 POS -> word 부분을 읽어들인 후 grammar rule 을 생성한다.
        - grammar rule 은 dictionary 자료구조로 저장한다.
            => pos -> word 와 같은 규칙이 존재할 경우,
                'word' : 'pos' 와 같이 key는 word, value는 pos 꼴이다.

* CKYParser.py
    * def CKYMatrix(size) :
        - CKY algorithm 을 사용하여 결과를 저장하는 자료구조의 형태를 미리 만들어놓는다.
    * def CKYParser(line, CNFpos, CNFword, fout) :
        - 입력 문장의 길이를 따라서 CKYMatrix 를 채워나가도록 for loop 을 돌려준다.
    * def ParseEkS(line, s, e, CNFpos, CNFword, Mat, fout) :
        - 현재 채우려는 Matrix의 인덱스가 시작점, 끝점이 각각 s,e 일때, s와 e 사이의 k 값을 가지고서
          문법 규칙을 적용해본다.
    * def writeUsedRule(combined, left, right, fout) :
        - 사용된 규칙을 파일 출력하도록 한다.

* traceBack.py
    * def traceBack(node) :
        - recursive 형태로 tree를 출력하도록 한다.
