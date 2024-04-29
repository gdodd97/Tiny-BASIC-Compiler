import enum

class Lexer:
    def __init__(self, source):
        self.source = source + '\n' #Source code to lex as a string. Append a newline to simplify lexing/parsing the last token/statement.
        self.curChar = '' #Current character in the string.
        self.curPos = -1 #Current Position in the string. 
        self.nextChar()

    #Process the next character.
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]
    
    #Return the lookahead character
    def peek(self):
        if self.curPos +1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    #Invalid token found, print error message
    def abort(self, message):
        pass

    #Skip whitespace except newlines, which we will use to indicate the end of a statement
    def skipWhitespace(self):
        pass

    #Skip comments in the code
    def skipComments(self):
        pass

    #Return the next token
    def getToken(self):
        #Check the first character of this token to see if we can decide what it is. 
        #If it is a multiple character operator (e.g., !=), number, identifier, or keyword then we will process the rest. 
        if self.curChar == '+':
            pass #Plus token. 
        elif self.curChar == '-':
            pass #Minus token. 
        elif self.curChar == '*':
            pass #Asterisk token. 
        elif self.curChar == '/':
            pass #slash token.
        elif self.curChar == '\n':
            pass #Newline token. 
        elif self.curChar == '\0':
            pass #EOF token.
        else:
            #Unknown token! 
            pass
        self.nexChar()

#Token contains the original text and the type of token.
class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText #The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind #the TokenType that this token is classified as.

#TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3

    #Keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111

    
