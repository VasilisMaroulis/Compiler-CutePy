#SPYRIDON MOTSENIGOS AM:4426 cse84426
#VASILEIOS MAROULIS  AM:4573 cse84573
import os
import sys

file_name =sys.argv[1]
file = open(file_name,"r")
endiamesos = open('Endiamesos.int', 'w')
pinakas_sum = open('Pinakas.symb', 'w')
telikos_arxeio = open('telikos.asm','w')
telikos_arxeio.write("j L    \n")


line=1

# Keywords
keywords = ['"__main__"', 'input', 'int','if','else','return', '__name__','while','or',
            'and','not','def','#declare','print']

#Oi katastaseis tou automatou mas.
start_state = 0
dig_state = 1
letter_state = 2
diff_state = 3
assignment_state = 4
smaller_state = 5
larger_state = 6
division_state = 7
hashtag_state = 8
comment_state = 9
closing_hashtag_state = 10

#----Ta Tokens mas ----

#Reloperators
smaller = 100
smaller_or_equal = 101
larger = 102
larger_or_equal = 103
equal = 104
different = 105

#Arithmetic
plus =200
minus = 201
multiplication = 202
division = 203


#Symbols
left_parenthesis = 300
right_parenthesis = 301
left_square_bracket = 302
right_square_bracket = 303
left_curly_bracket = 304
right_curly_bracket = 305

#Delimeter
colon = 400
comma = 401
semicolon = 402
exclMark = 403

#Keywords
main_key = 500
input_key = 501
int_key = 502
if_key = 503
else_key = 504
return_key = 505
name_key = 506
while_key = 507
or_key = 508
and_key = 509
not_key = 510
def_key = 511
declare_key = 512
print_key = 513


id = 600
number = 601
assignment = 602
hashtag = 603
EOF = 604

#errors
error_underscore = -400
error_digitFolowedByLetter = -401
error_integerOutBounds = -402
error_tooBigWord = -403
error_unacceptableSymbol = -404
error_soloHashtag = -405
error_CommentMissingHashtag = -406
error_CommentEOF = -407
error_Division = -408
error_leftCurly = -409
error_rightCurly = -410
error_exclMark = -411
error_hashdec = -412
error_quotes = -413

transition=[
    #start_state
    [start_state, smaller_state, larger_state, assignment_state, plus, minus, multiplication , division_state,
     left_parenthesis, right_parenthesis, left_square_bracket, right_square_bracket, error_leftCurly, error_rightCurly, start_state, colon, comma, semicolon,
    letter_state,diff_state, letter_state, dig_state, hashtag_state, error_CommentMissingHashtag, letter_state, EOF, error_unacceptableSymbol],

     #dig_state
    [number,  number, number, number, number, number, number, number, number, number, number, number, number, number,
     number, number, number,number, number, number, error_digitFolowedByLetter, dig_state, number, number, number, number, error_unacceptableSymbol],

     #letter_state
    [id,  id, id, id, id, id, id, id, id,
     id, id, id, id, id, id, id, id, id, letter_state, id ,letter_state, letter_state , id, id, letter_state, id, error_unacceptableSymbol],

     #diff_state
     [error_exclMark,error_exclMark,error_exclMark,different,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,
      error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,
      error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_exclMark,error_unacceptableSymbol],

     #assignment_state
    [assignment, assignment, assignment, equal, assignment, assignment, assignment, assignment, assignment, assignment, assignment,
     assignment, assignment, assignment, assignment, assignment, assignment, assignment, assignment,
     assignment, assignment, assignment,assignment , assignment, assignment, assignment, error_unacceptableSymbol],

     #smaller_state
    [smaller, smaller , smaller, smaller_or_equal, smaller,  smaller, smaller, smaller, smaller,  smaller, smaller,
     smaller, smaller, smaller, smaller, smaller, smaller, smaller, smaller,
     smaller,smaller, smaller, smaller, smaller, smaller, smaller, error_unacceptableSymbol],

     #larger_state
    [larger, larger, larger, larger_or_equal, larger, larger, larger, larger,  larger, larger, larger,larger,
     larger, larger, larger, larger, larger, larger, larger, larger,
     larger, larger, larger, larger, larger, larger, larger, larger, error_unacceptableSymbol],


     #division_state
    [error_Division, error_Division, error_Division, error_Division, error_Division, error_Division,
     error_Division, division, error_Division, error_Division, error_Division,
     error_Division, error_Division, error_Division, error_Division, error_Division,error_Division, error_Division, error_Division, error_Division,
     error_Division, error_Division, error_Division, error_Division, error_Division, error_Division, error_unacceptableSymbol],

     #hashtag_state
    [error_soloHashtag, error_soloHashtag, error_soloHashtag, error_soloHashtag, error_soloHashtag,
     error_soloHashtag, error_soloHashtag, error_soloHashtag, error_soloHashtag, error_soloHashtag, error_soloHashtag,
     error_soloHashtag, left_curly_bracket, right_curly_bracket, error_soloHashtag, error_soloHashtag, error_soloHashtag, error_soloHashtag,error_soloHashtag,
     error_soloHashtag, letter_state, error_soloHashtag, error_soloHashtag, comment_state, error_soloHashtag, error_soloHashtag, error_unacceptableSymbol],

     #comment_state
    [comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,
     comment_state, comment_state, comment_state, comment_state, comment_state,
     comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,comment_state,
     comment_state, comment_state, closing_hashtag_state, comment_state, comment_state, error_CommentEOF, comment_state],

     #closing_hashtag_state
    [comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,
     comment_state, comment_state, comment_state, comment_state, comment_state,
     comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,comment_state,
     comment_state, comment_state, closing_hashtag_state, start_state, comment_state, error_CommentEOF, comment_state]

     ]



def lex():
    global line
    global recognized_string    #Global -> Gia tin makeFamily
    global current_state        #Global -> Gia tin printErrors
    recognized_string =''
    current_state = start_state
    linenumber = line
    token = []

    #Trexw oso den briskw token
    while(current_state >= 0 and current_state <= 10):
        input_char = file.read(1)

        if (input_char == ' ' or input_char == '\t'):  # white_char
            char =  0

        elif (input_char == '<'):   # smaller
            char  = 1

        elif (input_char == '>'):   # larger
            char =  2

        elif (input_char == '='):   # equal
            char = 3

        elif (input_char == '+'):   # plus
            char = 4

        elif (input_char == '-'):   # minus
            char = 5

        elif (input_char == '*'):   # multipication
            char  = 6

        elif (input_char == '/'):   # division
            char =  7

        elif (input_char == '('):   # left_parenthesis
            char = 8

        elif (input_char == ')'):   # right_parenthesis
            char =  9

        elif (input_char == '['):   # left_square_bracket
            char = 10

        elif (input_char == ']'):   # right_square_bracket
            char = 11

        elif (input_char == '{'):   # left_curly_bracket
            char = 12

        elif (input_char == '}'):   # right_curly_bracket
            char = 13

        elif (input_char == '\n'):  # changing_line
            linenumber = linenumber + 1
            char = 14

        elif (input_char == ':'):    # colon
            char = 15

        elif (input_char == ','):   # comma
            char = 16

        elif (input_char == ';'):   # semicolon
            char = 17

        elif (input_char == '"'):   #  quotes
            char = 18

        elif (input_char == '!'):   #thaumastiko (gia to diaforo)
            char = 19

        elif (input_char.isalpha()==True):  # letters
            char = 20

        elif (input_char.isdigit()==True):  # num
            char = 21

        elif (input_char == '#'):   # hashtag
            char = 22

        elif (input_char == '$'):   # dollar
            char = 23

        elif (input_char == '_'):   # underscore
            char = 24

        elif (input_char == ''):    # EOF
            char = 25

        else:
            char  = 26         # unacceptable symbol


        #Me basi ton xaraktira pou blepw kanw tin metabasi stin katastasi pou prepei.
        current_state =transition[current_state][char]

        #Mh typwneis sxolia , mh typwneis ta kena sthn arxh
        if(current_state!= start_state and current_state!= comment_state and current_state!= closing_hashtag_state):
            recognized_string = recognized_string + input_char

        else:
            recognized_string = ''



    #Opisthodromsi paw ena xarktira pisw.
    if(current_state == number or current_state == id or current_state == larger or current_state == smaller or current_state == assignment ):
        if (input_char == '\n'):
            linenumber =linenumber - 1
        recognized_string = recognized_string[:-1]
        input_char = file.seek(file.tell()-1,0)


    #elegxos an o ariumos einai ektos oriou.
    if (current_state == number):
        checkingOutofBounds()

    #elegxos lexis megalyterh apo 30 xaraktires
    if(current_state == id or current_state ==number):
        if(len(recognized_string) > 30):
            current_state = error_tooBigWord



    if(current_state == id):

        if(recognized_string[0] == '"' and  len(recognized_string) != 10):
            current_state = error_quotes
        elif(recognized_string[0] == '"'
            and  len(recognized_string) == 10
            and recognized_string[1] != '_'
            and recognized_string[2] != '_'
            and recognized_string[3] != 'm'
            and recognized_string[4] != 'a'
            and recognized_string[5] != 'i'
            and recognized_string[6] != 'n'
            and recognized_string[7] != '_'
            and recognized_string[8] != '_'
            and recognized_string[9] != '"'):

                current_state = error_quotes



        if(recognized_string[0] == '#' and  len(recognized_string) != 8):
            current_state = error_hashdec

        elif(recognized_string[0] == '#'
            and  len(recognized_string) == 8
            and recognized_string[1] != 'd'
            and recognized_string[2] != 'e'
            and recognized_string[3] != 'c'
            and recognized_string[4] != 'l'
            and recognized_string[5] != 'a'
            and recognized_string[6] != 'r'
            and recognized_string[7] != 'e'):

                current_state = error_hashdec
        #edw kleinei to mesa if-elif

        #Otan exw dei id koitazw an einai keyword
        current_state = recognizeKeywords()



    makeFamily(current_state)
    token.append(family)
    token.append(recognized_string)
    token.append(current_state)
    token.append(linenumber)
    line=linenumber
    printErrors(current_state)

    #print(token)                   #An thelw na printarw kai tis lektikes monades
    return token


def printErrors(current_state):
    #Printarw to katallilo minima error.
    if(current_state == error_underscore):
        print("LEKTIKO error: H lexi arxizei me  '_' , line : ",line)

    elif(current_state == error_digitFolowedByLetter):
        print("LEKTIKO error: Akolouthei xaraktiras meta apo  psifio, line : ",line)

    elif(current_state == error_hashdec):
        print("LEKTIKO error: arxizei lexi me '#' line : ",line)

    elif(current_state == error_integerOutBounds):
        print("LEKTIKO error: O akeraios einai ektos diastimatos [-(2^32-1),2^32-1], line : ",line)

    elif(current_state == error_tooBigWord):
        print("LEKTIKO error: H lexi upervainei tous 30 xaraktires, line : ",line)

    elif(current_state == error_unacceptableSymbol):
        print("LEKTIKO error: To simbolo den iparxei sto alfabito, line : ",line)

    elif(current_state == error_soloHashtag):
        print("LEKTIKO error: monaxiko hashtag (#), line : ",line)

    elif(current_state == error_CommentMissingHashtag):
        print("LEKTIKO error: monaxiko dollario ($), line : ",line)

    elif(current_state == error_exclMark):
        print("LEKTIKO error: thaumastiko '!' mono tou , line : ",line)

    elif(current_state == error_CommentEOF):
        print("LEKTIKO error: To arxeio teleiwse kai den ekleisan ta sxolia, line : ",line)

    elif(current_state == error_Division):
        print("LEKTIKO error: Den exw brei to deutero slash (/) gia na einai diairesi, line : ",line)

    elif(current_state == error_leftCurly):
        print("LEKTIKO error: Den parxei to hashtag prin to leftCurly ( { ) , line : ",line)

    elif(current_state == error_rightCurly):
        print("LEKTIKO error: Den parxei to hashtag prin to rightCurly ( } ) , line : ",line)

    elif(current_state == error_quotes):
        print("LEKTIKO error: lexi arxizei me quotes ",line )


def makeFamily(current_state):
    global family

    if (current_state == id):
        family = "Family: id"

    elif (current_state == number):
        family = "Family: number"

    elif (current_state == plus):
        family = "Family: addOperator"

    elif (current_state == minus):
        family = "Family: addOperator"

    elif (current_state == multiplication):
        family = "Family: mulOperator"

    elif (current_state == division):
        family = "Family: mulOperator"

    elif (current_state == equal):
        family = "Family: relOperator"

    elif (current_state == smaller):
        family = "Family: relOperator"

    elif (current_state == smaller_or_equal):
        family = "Family: relOperator"

    elif (current_state == larger):
        family = "Family: relOperator"

    elif (current_state == larger_or_equal):
        family = "Family: relOperator"

    elif (current_state == colon):
        family = "Family: delimiter"

    elif (current_state == comma):
        family = "Family: delimiter"

    elif (current_state == semicolon):
        family = "Family: delimiter"

    elif (current_state == left_parenthesis):
        family = "Family: groupSymbol"

    elif (current_state == right_parenthesis):
        family = "Family: groupSymbol"

    elif (current_state == left_square_bracket):
        family = "Family: groupSymbol"

    elif (current_state == right_square_bracket):
        family = "Family: groupSymbol"

    elif (current_state == left_curly_bracket):
        family = "Family: groupSymbol"

    elif (current_state == right_curly_bracket):
        family = "Family: groupSymbol"

    elif (current_state == assignment):
        family = "Family: assignment"

    elif (current_state == different):
        family = "Family: relOperator"

    elif (current_state == hashtag):
        family = "Family: groupSymbol"

    elif (current_state == EOF):
        family = "EOF"

    else :
        family = "Family: keyword"

    return family


def recognizeKeywords():
    global current_state

    if(recognized_string in keywords):

        if (recognized_string == '"__main__"'):
            current_state = main_key

        elif (recognized_string == 'input'):
            current_state = input_key

        elif (recognized_string == 'int'):
            current_state = int_key

        elif (recognized_string == 'if'):
            current_state = if_key

        elif (recognized_string == 'else'):
            current_state = else_key

        elif (recognized_string == 'return'):
            current_state = return_key

        elif (recognized_string == '__name__'):
            current_state = name_key

        elif (recognized_string == 'while'):
            current_state = while_key

        elif (recognized_string == 'or'):
            current_state = or_key

        elif (recognized_string == 'and'):
            current_state = and_key

        elif (recognized_string == 'not'):
            current_state = not_key

        elif(recognized_string =='def'):
            current_state = def_key

        elif(recognized_string =='#declare'):
            current_state = declare_key

        elif (recognized_string == 'print'):
            current_state = print_key

    elif (recognized_string[0] == '_'):
        current_state = error_underscore

    return current_state


def checkingOutofBounds():
    global current_state
    if (int(recognized_string) >= pow(2,32) or int(recognized_string) <= -pow(2,32)):
        current_state = error_integerOutBounds
    return current_state

#-------------------------------------------------------------------------------
#----------------------SYNARTHSEIS ENDIAMESOU KWDIKA----------------------------
#-------------------------------------------------------------------------------

global quadList
quadList = []
quadListForgenerate_final = []
quadCounter = 1    #Grammh tetradwn
i = 0              #To xrisimopooiw gia tin dimioyrgia twn %1 %2 %3...

#ftiaxnw mia keni lista apo 4ades
def emptyList():
    pointerEmptyList = []

    return pointerEmptyList

#ftiaxnw mia  lista apo 4ades poy  periexei to x
def makeList(x):
    flist = [x]

    return flist

#Synenwnei tis duo listes list1 list2
def merge(list1, list2):

    mergedList = list1 + list2
    return (mergedList)

#O arithmos tis kate 4adas
def nextQuad():
    global quadCounter

    return quadCounter

#Ftiaxnw thn 4ada.
def genQuad(op, x, y, z):
    global quadCounter
    global quadList

    #telikos
    global quadListForgenerate_final

    quad = [nextQuad(), op, x, y, z]
    quadCounter += 1
    quadList.append(quad)

    #telikos
    #Kratame tis 4ades gia ton teliko afou kathe fora pou ekteloume tin generate_final auti mou adeiazei thn quadlist
    quadListForgenerate_final.append(quad)

    return quad

#Ftiaxw ta %1 , %i poy xreiazomai.
def newTemp():
    global i
    global variablesList
    temporary = "%"
    tempVar = temporary+str(i)
    i = i + 1

    #pinakas sumbolwm
    #Afou ftiaxnw mia proswrini metabliti ftiaxnw ena entity gia auti.
    myNewEntity = Entity()
    myNewEntity.name = tempVar
    myNewEntity.type = 'temporary'
    myNewEntity.tempVar.offset = find_offset()
    add_entity(myNewEntity)

    return tempVar

#Symplhrwsh twn tetradwn mou.
def backPatch(list, z):
    global quadList

    length_a = len(list)
    length_b =len(quadList)
    for i in range(length_a):
    	for j in range(length_b):
    		if(list[i]==quadList[j][0] and quadList[j][4]=='_'):
    			quadList[j][4] = z
    			break;
    return

#Ektypwsh tetradwn se arxeio.
def printIntCode(intFile):
    length_b =len(quadListForgenerate_final)

    for i in range(length_b):
        y = quadListForgenerate_final[i]         #1H terrada 2H tetrada 3H tetrada klp.
        tetrada = str(y[0]) + ":"
        for j in range(1,5):
            tetrada = tetrada + "  " + str(y[j])
        intFile.write(tetrada)
        intFile.write("\n")
#-------------------------------------------------------------------------------
#-------------------TELOS SYNARTHSEIS ENDIAMESOU KWDIKA-------------------------
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
#----------------------SYNARTHSEIS PINAKA SYMBOLWN -----------------------------
#-------------------------------------------------------------------------------

#klasi gia ta Scopes
class Scope():
    def __init__(self):
        self.ListEntity = []		#H lista me ta entities mou.
        self.nestingLevel = 0	    #Bathos fwliasmatos.
        self.name = ""              #To onoma tou scope.

#klasi gia ta Entities mou
class Entity():

    def __init__(self):
        self.type = ""			#O tupos (function,variable,temporary,parameter).
        self.name = ""			#To onoma tou entity
        self.variable = self.Variable()
        self.parameter = self.Parameter()
        self.tempVar = self.TemporaryVariable()
        self.function = self.Function()




    #klasi gia tis MH proswrines metablites
    class Variable:
        def __init__(self):
            self.offset = 0

    #klasi gia tis parametrous
    class Parameter:
        def __init__(self):
            self.offset = 0

    #Klasi gia tis proswrines metablites (T1,T2..)
    class TemporaryVariable:
        def __init__(self):
            self.offset = 0

    #klasi gia tis sunartiseis mas.
    class Function:
        def __init__(self):
            self.startQuad = 0			#Etiketa tis prwtis tetrades tis  synartiseis.
            self.ListArgument = []		#H lista parametrwn.
            self.frameLength = 0		#Mikos eggrafimatos drastiriopoiisis.

            #telikos
            self.nestingLevel = 0

#klasi gia ta Arguments
class Argument():
    def __init__(self):
        self.name = ""

#Lista me ta scopes mas.
scopesTable = []

#Prosthiki neou scope.
#Otan xekinaw tin metafrasi mia neas sinartisis
def add_scope(nameOfScope):
    global scopesTable
    #Ftiaxnw to Scope.
    newScope = Scope()
    newScope.name = nameOfScope
    scopesTable.append(newScope)  #Bazw to neo scope mou sto telos tis listas.

    newScope=scopesTable[len(scopesTable)-1] #To scope poy einai pio psila mexri stigmis


    #βρισκω το nestingLevel αυτου που προσθεσα μολις.
    #An exw mono ena scope stin lista tote einai tis main kai exei nestingLevel = 0
    #Alliws to nestinglevel einai to nesting level tou apo  katw + 1
    if(len(scopesTable)==1):
    	newScope.nestingLevel = 0
    else:
    	newScope.nestingLevel = scopesTable[len(scopesTable)-2].nestingLevel + 1



#Diagrafi Scope.
#Otan teleiwnoume ti metafrasi mias sunartisis.
def delete_scope():
    global scopesTable
    freeScope = scopesTable[len(scopesTable)-1]
    scopesTable[len(scopesTable)-1] = scopesTable[len(scopesTable)-2]
    scopesTable.pop()

#Prosthiki neou entity otan synantame:
    #Dilwsi metablitis.
    #Dimiorourgeite mia proswrini metabliti
    #Dilwsi mia neas sunartisis
    #Dilwsi tupikis parametrou sunartiseis
def add_entity(new_ent):
    scopesTable[len(scopesTable)-1].ListEntity.append(new_ent)  #Bazw sto telos to kainourgio mou entity.

#Prosthiki neou argument otan sunantame:
    #Dilwsi tupikis parametrou sunartiseis
def add_argument(new_arg):
    global scopesTable
    length_ent = len(scopesTable[len(scopesTable)-1].ListEntity)

    #Bazw sto telos to kainourgio mou argument.(Sto teleytaio entity)
    scopesTable[len(scopesTable)-1].ListEntity[length_ent-1].function.ListArgument.append(new_arg)


#Gia kathe argument dimiourgw ston apo panv epiedo ena neo entity.
def add_parameters():
    global scopesTable
    length_ent = len(scopesTable[len(scopesTable)-2].ListEntity)

    for arg in scopesTable[len(scopesTable)-2].ListEntity[length_ent-1].function.ListArgument:
        myNewEntity = Entity()
        myNewEntity.name = arg.name
        myNewEntity.type = 'parameter'
        myNewEntity.parameter.offset = find_offset()
        add_entity(myNewEntity)

#Briskw to offset
def find_offset():
    global scopesTable
    bytes = 4
    count=0

    #Na exw toylaxiston ena entity.
    if(len(scopesTable[len(scopesTable)-1].ListEntity) !=0 ):
        #Diatrexw ola ta entities tou epipedou.
        for x in (scopesTable[len(scopesTable)-1].ListEntity):

            #Metraw posa entities uparxoun pou den einai function
            if(x.type !='function'):
                count = count + 1

    offset = 12 + (count*bytes)
    return offset

#Briskw to framlength tis sunartisis
def find_framelength():
    global scopesTable
    length_ent = len(scopesTable[len(scopesTable)-2].ListEntity)

    #Briskw to framelentgh tis sunartisis sto katw epipedo.
    scopesTable[len(scopesTable)-2].ListEntity[length_ent-1].function.frameLength = find_offset()



#Briskw to startQuad.
def find_startQuad():
    global scopesTable
    length_ent = len(scopesTable[len(scopesTable)-2].ListEntity)

    #Briskw to startQuad tis sinartisis sto katv epipedo.
    scopesTable[len(scopesTable)-2].ListEntity[length_ent-1].function.startQuad = nextQuad()

#Tupwse sto arxeio ton pinaka sumbolwn.
def write_Symbol_Table(file2):
    global scopesTable
    file2.write("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    i =1

    scope=scopesTable[len(scopesTable)-1]

    for x in range(len(scopesTable)):
        file2.write("\nSCOPE: "+"name:"+scope.name+"\t nestingLevel:"+str(scope.nestingLevel))
        file2.write("\n")
        file2.write("\n\tENTITIES:")

        for entity in scope.ListEntity:
            if(entity.type == 'function'):
                file2.write("\n")
                file2.write("\n\tENTITY: "+" name:"+entity.name+"\t type:"+entity.type+"\t startQuad:"+str(entity.function.startQuad)+"\t frameLength:"+str(entity.function.frameLength))
                file2.write("\n")
                file2.write("\t\tARGUMENTS:")
                file2.write("\n")
                for arg in entity.function.ListArgument:
                    file2.write("\t\t\tARGUMENT: "+" name:"+arg.name)
                    file2.write("\n")

            elif(entity.type == 'variable'):
                file2.write("\n")
                file2.write("\n\tENTITY: "+" name:"+entity.name+"\t type:"+entity.type+"\t offset:"+str(entity.variable.offset))
                file2.write("\n")

            elif(entity.type == 'parameter'):
                file2.write("\n")
                file2.write("\n\tENTITY: "+" name:"+entity.name+"\t type:"+entity.type+"\t offset:"+str(entity.parameter.offset))
                file2.write("\n")

            elif(entity.type == 'temporary'):
                file2.write("\n")
                file2.write("\n\tENTITY: "+" name:"+entity.name+"\t type:"+entity.type+"\t offset:"+str(entity.tempVar.offset))
                file2.write("\n")
        i = i + 1
        scope = scopesTable[len(scopesTable)-i]

    file2.write("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

#-------------------------------------------------------------------------------
#---------------------TELOS SYNARTHSEIS PINAKA SYMBOLWN-------------------------
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
#----------------------SYNARTHSEIS TELIKOY KWDIKA ------------------------------
#-------------------------------------------------------------------------------

#Psaxnei ena entity - argment , me basi to onoma tou.
def search_entity(name):
    global scopesTable

    scope_on_top =scopesTable[len(scopesTable)-1]
    while scope_on_top:
        for entities in scope_on_top.ListEntity:
            if(entities.name == name):
                return (scope_on_top,entities)
        scope_on_top=scopesTable[len(scopesTable)-2]

    print("Den uparxei entity me onoma  " + str(x))
    exit()

#gnvlcode sel 22 - 24
#μεταφέρει στον t0 την διεύθυνση μιας μη τοπικής μεταβλητής
#από τον πίνακα συμβόλων βρίσκει πόσα επίπεδα επάνω βρίσκεται η μη τοπική
#μεταβλητή και μέσα από τον σύνδεσμο προσπέλασης την εντοπίζει
def gnlvcode(name):
    global telikos_arxeio

    telikos_arxeio.write("lw" + " t0"+ "-4(sp)" + "\n") #στοίβα του γονέα

    #Ψαχνουμε στον πινακα συμβολων να βρει το "ζευγαρι"  (scope_i,entity_i) της μη τοπικης μεταβλιτης.
    (scope_i,entity_i)=search_comb(name)

    #βρίσκει πόσα επίπεδα επάνω βρίσκεται η μη τοπική μεταβλητή
    floors= scopesTable[len(scopesTable)-1].nestingLevel - scope_i.nestingLevel;

    #Αφαιρω ενα επιπεδο αφου εχω "παει σε αυτο εκτελοντας την εντολη lw t0, 4(sp) παραπάνω".
    floors=floors -1

    #όσες φορές χρειαστεί:

    for i in range(floors):

        #στοίβα του προγόνου που έχει τη μεταβλητή οσες φορες χρειαζεται για να φτασω.
        telikos_arxeio.write("lw" + " t0"+ "-4(t0)" + "\n")

    if entity_i.type=='parameter':
        #διεύθυνση της μη τοπικής μεταβλητής.
        telikos_arxeio.write("addi" + " t0"+","+"t0"+ "-"+str(entity_i.parameter.offset) + "\n")

    if entity_i.type=='variable':

        #διεύθυνση της μη τοπικής μεταβλητής.
        telikos_arxeio.write("addi" + " t0"+","+"t0"+ "-"+str(entity_i.variable.offset) + "\n")

#loadvr sel 26-31
def loadvr(v,r):
    global telikos_arxeio
    global scopesTable
    #Aν v είναι σταθερά li tr,v sel 26
    if v.isdigit():
        telikos_arxeio.write("li " +str(r) + "," +str(v) + " \n")

    #Aν v είναι καθολική μεταβλητή
    else:
        (scope_i,entity_i)=search_entity(v)

        #Aν v είναι καθολική μεταβλητή δηλαδή ανήκει στο κυρίως πρόγραμμα. sel 26.
        #lw tr, offset gp
        #scope_i.nestingLevel==0 to scope tis main.
        if scope_i.nestingLevel==0 and entity_i.type=='variable':
            telikos_arxeio.write("lw " +str(r) + "," + "-"+str(entity_i.variable.offset)+"(gp)"+"\n")

        #Aν v είναι καθολική μεταβλητή δηλαδή ανήκει στο κυρίως πρόγραμμα. sel 26.
        #lw tr, offset gp
        elif scope_i.nestingLevel==0 and entity_i.type=='temporary':
            telikos_arxeio.write("lw " +str(r) + "," + "-"+str(entity_i.tempVar.offset)+"(gp)"+"\n")

        #Aν η v έχει δηλωθεί στη συνάρτηση που αυτή τη στιγμή εκτελείται και είναι τοπική sel 28
        #μεταβλητή, ή τυπική παράμετρος , ή προσωρινή μεταβλητή.
        #Δηλαδη το βαθος φωλιασματος ειναι ισο με την συναρτηση που εκτελείται.
        elif scope_i.nestingLevel == scopesTable[len(scopesTable)-1].nestingLevel:

            #τοπική μεταβλητή
            if entity_i.type=='variable':

                telikos_arxeio.write("lw " +str(r) + "," + "-"+str(entity_i.variable.offset)+"(sp)"+"\n")

            #τυπική παράμετρος
            elif entity_i.type=='parameter':

                telikos_arxeio.write("lw " +str(r) + "," + "-"+str(entity_i.parameter.offset)+"(sp)"+"\n")

            #προσωρινή μεταβλητή
            elif entity_i.type=='temporary':

                telikos_arxeio.write("lw " +str(r) + "," + "-"+str(entity_i.tempVar.offset)+"(sp)"+"\n")

        #αν η v έχει δηλωθεί σε κάποιο πρόγονο και εκεί είναι τοπική μεταβλητή, ή τυπική παράμετρος sel 30
        #gnlvcode  /// lw tr,(t0)
        #Αρα το βαθος φωλιάσματος  ειναι μικρότερο από της τρεχουας συναρτησης.
        elif scope_i.nestingLevel < scopesTable[len(scopesTable)-1].nestingLevel:

            #τοπική μεταβλητή
            if entity_i.type=='variable':
                gnlvcode(v)
                telikos_arxeio.write("lw " +str(r) + "," + "(t0)" + "\n")

            #τυπική παράμετρος
            elif entity_i.type=='parameter':
                gnlvcode(v)
                telikos_arxeio.write("lw " +str(r) + "," + "(t0)" + "\n")


#storerv sel 33-36
#μεταφορά δεδομένων από τον καταχωρητή r στη μνήμη (μεταβλητή v)
def storerv(r,v):
    global telikos_arxeio

    (scope_i,entity_i)=search_entity(v)

    #αν v είναι καθολική μεταβλητή – δηλαδή ανήκει στο κυρίως πρόγραμμα sel 34
    #sw tr, -offset(gp)
    if scope_i.nestingLevel==0 and entity_i.type=='variable':

        telikos_arxeio.write("sw " +str(r) + "," + "-"+str(entity_i.variable.offset)+"(gp)"+"\n")

    elif scope_i.nestingLevel==0 and entity_i.type=='temporary':

        telikos_arxeio.write("sw " +str(r) + "," + "-"+str(entity_i.tempVar.offset)+"(gp)"+"\n")

    #αν v είναι τοπική μεταβλητή, ή τυπική παράμετρος  και βάθος φωλιάσματος
    #ίσο με το τρέχον, ή προσωρινή μεταβλητή. sel 35
    #sw tr, -offset(sp)

    elif scope_i.nestingLevel == scopesTable[len(scopesTable)-1].nestingLevel:

        #τοπική μεταβλητή
        if entity_i.type=='variable':

            telikos_arxeio.write("sw " +str(r) + "," + "-"+str(entity_i.variable.offset)+"(sp)"+"\n")

        #τυπική παράμετρος
        elif entity_i.type=='parameter':

            telikos_arxeio.write("sw " +str(r) + "," + "-"+str(entity_i.parameter.offset)+"(sp)"+"\n")

        #προσωρινή μεταβλητή
        elif entity_i.type=='temporary':

            telikos_arxeio.write("sw " +str(r) + "," + "-"+str(entity_i.tempVar.offset)+"(sp)"+"\n")

    #αν v είναι τοπική μεταβλητή, ή τυπική παράμετρος και βάθος φωλιάσματος μικρότερο από το τρέχον sel 36
    #gnlvcode(v) ////// sw tr, (t0)
    elif scope_i.nestingLevel < scopesTable[len(scopesTable)-1].nestingLevel:

        #τοπική μεταβλητή
        if entity_i.type=='variable':

            gnlvcode(v)
            telikos_arxeio.write("sw " +str(r) + "," + "(t0)" + "\n")

        #τυπική παράμετρος
        elif entity_i.type=='parameter':

            gnlvcode(v)
            telikos_arxeio.write("sw " +str(r) + "," + "(t0)" + "\n")








parameter_list = []
parameter_flag = False
def generate_final():
    global quadList, j
    global telikos_arxeio
    global scopesTable ,parameter_list,parameter_flag
    for i in range(len(quadList)):
        telikos_arxeio.write("\n"+"L" + str(quadList[i][0]) + ": \n")
#~~~~~~~~~~~~~~~~~~Είσοδος και έξοδος δεδομένων SEL 15~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (quadList[i][1] == "inp"):
            telikos_arxeio.write("li a7,5"+"\n")
            telikos_arxeio.write("ecall"+"\n")
            storerv("a0", quadList[i][2])


        elif (quadList[i][1] == "out"):
            loadvr(quadList[i][2], "a0")
            telikos_arxeio.write("li a7,1"+"\n")
            telikos_arxeio.write("ecall"+"\n")

#~~~~~~~~~~~~Τερματισμός προγράμματος με επιστροφή τιμής 0  SEL 16~~~~~~~~~~~~~~~

        elif (quadList[i][1] == "halt"):
            telikos_arxeio.write("li a0,0"+"\n")
            telikos_arxeio.write("li a7,93"+"\n")
            telikos_arxeio.write("ecall"+"\n")

#~~~~~~~~~~~~~~~~~~~~~~~~Εντολές Αλμάτων  SEL 38~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            #loadvr(x,t1)
                            #loadvr(y,t2)
        elif (quadList[i][1] == "jump"):
            telikos_arxeio.write("j L"+str(quadList[i][4])+"\n")

        elif (quadList[i][1] == ">"):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("bgt,t1,t2,L"+str(quadList[i][4])+"\n")

        elif (quadList[i][1] == ">="):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("bge,t1,t2,L"+str(quadList[i][4])+"\n")

        elif (quadList[i][1] == "<"):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("blt,t1,t2,L"+str(quadList[i][4])+"\n")

        elif (quadList[i][1] == "<="):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("ble,t1,t2,L"+str(quadList[i][4])+"\n")

        elif (quadList[i][1] == "!="):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("bne,t1,t2,L"+str(quadList[i][4])+"\n")

        elif (quadList[i][1] == "=="):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("beq,t1,t2,L"+str(quadList[i][4])+"\n")

#~~~~~~~~~~~~~~~~~~~~~~~~#Εκχώρηση sel 39~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        elif (quadList[i][1] == "="):
            loadvr(quadList[i][2],"t1")
            storerv("t1",quadList[i][4])

#~~~~~~~~~~~~~~~~~~~~~~~~Εντολές Αριθμητικών Πράξεων sel 40~~~~~~~~~~~~~~~~~~~~~
                            #loadvr(x,t1)
                            #loadvr(y,t2)
                            #op,t1,t1,t2
                            #storerv(t1,z)
        elif (quadList[i][1] == "//"):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("div,t1,t1,t2"+"\n")
            storerv("t1",quadList[i][4])

        elif (quadList[i][1] == "*"):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("mul,t1,t1,t2"+"\n")
            storerv("t1",quadList[i][4])

        elif (quadList[i][1] == "-"):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("sub,t1,t1,t2"+"\n")
            storerv("t1",quadList[i][4])

        elif (quadList[i][1] == "+"):
            loadvr(quadList[i][2],"t1")
            loadvr(quadList[i][3],"t2")
            telikos_arxeio.write("add,t1,t1,t2"+"\n")
            storerv("t1",quadList[i][4])

#~~~~~~~~~~~~~~~~~~~~~~~Επιστροφή Τιμής Συνάρτησης sel 41~~~~~~~~~~~~~~~~~~~~~~~
        #αποθηκεύεται ο x στη διεύθυνση που είναι αποθηκευμένη στην 3 η θέση του
        #εγγραφήματος δραστηριοποίησης
        elif (quadList[i][1] == "retv"):
            loadvr(quadList[i][2],"t1")
            telikos_arxeio.write("lw t0,-8(sp)\n")
            telikos_arxeio.write("sw t1,(t0)\n")
            telikos_arxeio.write("lw ra, (sp)\n") # sel 61
            telikos_arxeio.write("jr ra \n")      #Μέσω του ra επιστρέφουμε στην καλούσα.

#~~~~~~~~~~~~~~~~~~~~~ Παράμετροι Συνάρτησης sel 42-54~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif (quadList[i][1] == "par"):
             #πριν από την πρώτη παράμετρο, τοποθετούμε τον $fp να δείχνει
             #στην στοίβα της συνάρτησης που θα δημιουργηθεί
            if parameter_flag == False:
                temp = i
                Counter = 0
                #Βρίσκω ποιος καλεσε την συναρτηση .
                while temp:
                    if (quadList[temp][1] == 'call'):
                        caller_name = str(quadList[temp][2])
                        break
                    Counter = Counter + 1
                    parameter_list.append(Counter)
                    temp=temp+1

                (scope_i,entity_i)=search_entity(caller_name)
                #βρισκω το frame length αυτης.
                telikos_arxeio.write("addi fp,sp,"+str(entity_i.function.frameLength)+"\n")
                parameter_flag = True
            #par,x,CV , sel 44
            if (quadList[i][3] == "CV"):
                loadvr(quadList[i][2],"t0")    #loadvr(x,t0) sw t0,-(12+4i)(fp)

                parameter_index = parameter_list.pop(0) - 1
                #i = j ο αύξων αριθμός της παραμέτρου
                j = 12+4*parameter_index
                telikos_arxeio.write("sw t0,"+"-"+str(j)+"(fp) \n")

            #par,x,RET,_
            #γεμίζουμε το 3ο πεδίο του εγγραφήματος δραστηριοποίησης της κληθείσας συνάρτησης
            #με τη διεύθυνση της προσωρινής μεταβλητής στην οποία θα επιστραφεί η τιμή
            elif (quadList[i][3] == "RET"):
                #Ψαχνω την συναρτηση για να βρω το offset της ΠΡΟΣΩΡΙΝΗΣ ΜΕΤΑΒΛΗΤΗΣ...
                (scope_i,entity_i)=search_entity(quadList[i][2])
                telikos_arxeio.write("addi t0,sp,-"+str(entity_i.tempVar.offset)+"\n")
                telikos_arxeio.write("sw t0,-8(fp)\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~ Κλήση Συνάρτησης sel 55 - 61~~~~~~~~~~~~~~~~~~~~~~~~
                             #call,_,_,f
        elif (quadList[i][1] == "call"):
            parameter_flag = False
            parameter_list = []

            (callee_scope,callee_entity)=search_entity(quadList[i][2])

            #αν καλούσα και κληθείσα έχουν το ίδιο βάθος φωλιάσματος, τότε έχουν τον ίδιο γονέα
            if scopesTable[len(scopesTable)-1].nestingLevel==callee_entity.function.nestingLevel:
                telikos_arxeio.write("lw t0,-4(sp)\n")
                telikos_arxeio.write("sw t0,-4(fp)\n")

            #αν καλούσα και κληθείσα έχουν διαφορετικό βάθος φωλιάσματος, τότε η καλούσα είναι ο γονέας της κληθείσας
            else:
                telikos_arxeio.write("sw sp,-4(fp)\n")

            #στη συνέχεια μεταφέρουμε τον δείκτη στοίβας στην κληθείσα σελ 60
            telikos_arxeio.write("addi sp,sp,"+str(callee_entity.function.frameLength)+"\n")
            #καλούμε τη συνάρτηση σελ 60
            telikos_arxeio.write("jal"+" L"+str(callee_entity.function.startQuad)+"\n")
            #όταν επιστρέψουμε παίρνουμε πίσω τον δείκτη στοίβας στην καλούσα   σελ 60
            telikos_arxeio.write("addi sp,sp,-"+str(callee_entity.function.frameLength)+"\n")

        #στην αρχή κάθε συνάρτησης - "υποπογραμματος"" αποθηκεύουμε στην πρώτη θέση του εγγραφήματος δραστηριοποίησης
        #την διεύθυνση επιστροφής της την οποία έχει τοποθετήσει στον ra
        elif ( quadList[i][1] == "begin_block"):

        #Αν ειμαστε στο begin block της ΜΑΙΝ.
        #στην αρχή του προγράμματος χρειάζεται ένα άλμα που να οδηγεί στην πρώτη ετικέτα του κυρίως προγράμματος


#~~~~~~~~~~~~~~~~ Αρχή Προγράμματος και Κυρίως Πρόγραμμα σελ 62~~~~~~~~~~~~~~~~~

            if(scopesTable[len(scopesTable)-1].nestingLevel==0):
                #Παω στην πρωτη γραμμη στην θεση 3 και βαζω το νουμερο της 4αδας
                telikos_arxeio.seek(3)
                telikos_arxeio.write(str((quadList[i][0])))
                telikos_arxeio.seek(0, os.SEEK_END)
                #πρέπει να κατεβάσουμε τον sp κατά framelength της main
                telikos_arxeio.write("addi sp,sp,"+str(find_offset())+"\n")
                #και να σημειώσουμε στον gp το εγγράφημα δραστηριοποίησης της main ώστε να
                #έχουμε εύκολη πρόσβαση στις global μεταβλητές
                telikos_arxeio.write("mv gp,sp\n")

            #Αν ειμαστε σε οποιαδηποτε αλλη συναρτηση.
            else:
                telikos_arxeio.write("sw ra,(sp)\n") #sel 61 διεύθυνση επιστροφής της συναρτησης

        elif (quadList[i][1] == "end_block"):
            if(scopesTable[len(scopesTable)-1].nestingLevel!=0):
                telikos_arxeio.write("lw ra,(sp)\n")
                telikos_arxeio.write("jr ra\n")

    #Στο τελος καθε end block διαγραφω τα quads για να μη τα ξανα παραγω.
    quadList = []


#-------------------------------------------------------------------------------
#-------------------TELOS SYNARTHSEWN  TELIKOY KWDIKA --------------------------
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
#------------------SYNTAKTIKOS-ENDIAMESOS-PINAKAS SYMBOLWN----------------------
#-------------------------------------------------------------------------------
def syntax_analyzer():
    global results_lex
    global line
    results_lex = lex()


    def startRule():
        #πινακας συμβολων.
        add_scope('"__main__"')
        def_main_part()
        call_main_part()


    def def_main_part():
        global results_lex
        def_main_function()
        while(results_lex[2] == def_key):
             def_main_function()


    def def_main_function():
        global line
        global results_lex
        linetemp = line

        if(results_lex[2] == def_key):
            linetemp = line
            results_lex = lex()


            if(results_lex[2] == id):
                #Onoma sinartisis (arxi kai telos  block sel 8)
                func_name = results_lex[1] #endiamesos
                linetemp = line
                results_lex = lex()


                if(results_lex[2] == left_parenthesis):
                    linetemp = line
                    results_lex = lex()


                    if(results_lex[2] == right_parenthesis):
                        linetemp = line
                        results_lex = lex()


                        if(results_lex[2] == colon):
                            linetemp = line
                            results_lex = lex()


                            if(results_lex[2] == left_curly_bracket):
                                linetemp = line
                                results_lex = lex()


                                #pinakas sumbolwn
                                #Ftiaxnw ena  Entity
                                myNewEntity = Entity()
                                myNewEntity.type = 'function'
                                myNewEntity.name = func_name

                                #telikos
                                #scopesTable[len(scopesTable)-1] == To pio panw scope
                                myNewEntity.function.nestingLevel = scopesTable[len(scopesTable)-1].nestingLevel + 1

                                add_entity(myNewEntity)
                                add_scope(func_name)

                                declarations()

                                while(results_lex[2] == def_key):
                                      def_function()


                                find_startQuad()  #pinakas sumbolwn briskw to Quad.

                                #endiamesos (arxi kai telos  block sel 8)
                                genQuad('begin_block',func_name,'_','_')



                                statements()
                                find_framelength() #pinakas sumbolwn

                                genQuad('end_block',func_name,'_','_')

                                write_Symbol_Table(pinakas_sum) #pinakas sumbolwn

                                #telikos
                                generate_final()

                                delete_scope()                  #pinakas sumbolwn


                                if(results_lex[2] == right_curly_bracket):
                                    linetemp = line
                                    results_lex = lex()

                                else:
                                    print("SYNTAX error: Missing '#}' opened on line:",linetemp)
                                    exit(-1)
                            else:
                                 print("SYNTAX error: Missing '#{'on MAIN line:",linetemp)
                                 exit(-1)
                        else:
                              print("SYNTAX error: Missing ':' on MAIN line:",linetemp)
                              exit(-1)
                    else:
                        print("SYNTAX error: Missing ')' on MAIN line:",linetemp)
                        exit(-1)
                else:
                    print("SYNTAX error: Missing '(' on MAIN line:",linetemp)
                    exit(-1)
            else:
                print("SYNTAX error: Den edwses onoma stin MAIN line:",linetemp)
                exit(-1)
        else:
             print("SYNTAX error: Missing 'def' on MAIN line:",linetemp)
             exit(-1)


    def def_function():
        global line
        global results_lex
        linetemp = line

        if(results_lex[2] == def_key):
            linetemp = line
            results_lex = lex()


            if(results_lex[2] == id):

                #Onoma sinartisis (arxi kai telos  block sel 8)
                func_name = results_lex[1]
                linetemp = line
                results_lex = lex()
                #pinakas sumbolwn
                myNewEntity = Entity()
                myNewEntity.type = 'function'
                myNewEntity.name = func_name

                #telikos
                myNewEntity.function.nestingLevel = scopesTable[len(scopesTable)-1].nestingLevel + 1

                add_entity(myNewEntity)

                if(results_lex[2] == left_parenthesis):
                    linetemp = line
                    results_lex = lex()
                    id_list('argum')

                    if(results_lex[2] == right_parenthesis):
                        linetemp = line
                        results_lex = lex()

                        if(results_lex[2] == colon):
                            linetemp = line
                            results_lex = lex()

                            if(results_lex[2] == left_curly_bracket):
                                linetemp = line
                                results_lex = lex()

                                #pinakas sumbolwn
                                add_scope(func_name)
                                add_parameters()

                                declarations()
                                while(results_lex[2] == def_key):
                                      def_function()

                                find_startQuad()   #pinakas sumbolwn

                                #endiamesos (arxi kai telos  block sel 8
                                genQuad('begin_block',func_name,'_','_')

                                statements()
                                find_framelength() #pinakas sumbolwn
                                genQuad('end_block',func_name,'_','_')

                                #pinakas sumbolwn
                                write_Symbol_Table(pinakas_sum)

                                generate_final()

                                delete_scope()

                                if(results_lex[2] == right_curly_bracket):
                                    linetemp = line
                                    results_lex = lex()

                                else:
                                    print("SYNTAX error: Missing '#}' on FUNCTION opened on line:",linetemp) ##
                                    exit(-1)
                            else:
                                 print("SYNTAX error: Missing '#{'on FUNCTION line:",linetemp)
                                 exit(-1)
                        else:
                              print("SYNTAX error: Missing ':' on FUNCTION line:",linetemp)
                              exit(-1)
                    else:
                        print("SYNTAX error: Missing ')' on FUNCTION line:",linetemp)
                        exit(-1)
                else:
                    print("SYNTAX error: Missing '(' on FUNCTION line:",linetemp)
                    exit(-1)
            else:
                print("SYNTAX error: Den edwses onoma stin FUNCTION line:",linetemp)
                exit(-1)
        else:
             print("SYNTAX error: Missing 'def' on FUNCTION line:",linetemp)
             exit(-1)


    def declarations():
        global results_lex

        while(results_lex[2] == declare_key):
            declaration_line()


    #Den kanw if==declare_key , to exw dei apo thn declations.
    def declaration_line():
        global results_lex
        results_lex = lex()
        id_list('entit')


    def statement():
       global line
       global results_lex
       linetemp = line
       if(results_lex[2]==id
            or results_lex[2]==print_key
            or results_lex[2]==return_key):

           simple_statement()


       elif(results_lex[2]==if_key or results_lex[2]==while_key):
           structured_statement()
       else:
           print("SYNTAX error: no proper statement line:", linetemp)
           exit(-1)


    def statements():
       global results_lex
       statement()

       while(results_lex[2]==id
               or results_lex[2]==print_key
               or results_lex[2]==return_key
               or results_lex[2]==if_key
               or results_lex[2]==while_key):

           statement()


    def simple_statement():
        global results_lex

        if(results_lex[2]==id):
            assignment_stat()
        elif(results_lex[2]==print_key):
            print_stat()
        elif(results_lex[2]==return_key):
            return_stat()


    def structured_statement():
       global results_lex

       if(results_lex[2]==if_key):
           if_stat()
       elif(results_lex[2]==while_key):
           while_stat()


#Den kanw if==id_key afou to exw dei stin simple_statement.
#S -> id := E {P1}; ekxorisi sel 37
#S -> input (id) {P1} sel 57
    def assignment_stat():
        global results_lex
        global line
        linetemp = line
        temp_id = results_lex[1]
        results_lex = lex()


        if(results_lex[2] == assignment):

            linetemp = line
            results_lex = lex()


            if(results_lex[2] == int_key):
                linetemp = line
                results_lex = lex()
             #{P1}: genquad(“inp”,id.place,”_”,”_”)
                genQuad('inp',temp_id,'_','_')


                if(results_lex[2] == left_parenthesis):
                    linetemp = line
                    results_lex = lex()


                    if(results_lex[2] == input_key):
                        linetemp = line
                        results_lex = lex()



                        if(results_lex[2] == left_parenthesis):
                             linetemp = line
                             results_lex = lex()


                             if(results_lex[2] == right_parenthesis):
                                  linetemp = line
                                  results_lex = lex()


                                  if(results_lex[2] == right_parenthesis):
                                      linetemp = line
                                      results_lex = lex()



                                      if(results_lex[2] == semicolon):
                                          linetemp = line
                                          results_lex = lex()

                                      else:
                                          print("SYNTAX error: Missing colon ';' on assignment_stat line:",linetemp)
                                          exit(-1)
                                  else:
                                      print("SYNTAX error: Missing  ')' on assignment_stat line:",linetemp)
                                      exit(-1)
                             else:
                                 print("SYNTAX error:  Missing  ')' on assignment_stat",linetemp)
                                 exit(-1)
                        else:
                            print("SYNTAX error:  Missing '(' on assignment_stat",linetemp)
                            exit(-1)
                    else:
                        print("SYNTAX error: Missing  'input' on assignment_stat line:",linetemp)
                        exit(-1)
                else:
                   print("SYNTAX error: Missing '(' on assignment_stat line:",linetemp)
                   exit(-1)
            else:
             #{P1} : genQuad(“:=“,E.place,”_”,id)
                Eplace = expression()
                genQuad('=', Eplace, '_', temp_id)
                if(results_lex[2] == semicolon):
                    linetemp = line
                    results_lex = lex()

                else:
                    print("SYNTAX error: The Expression does not finish with ';' on  assignment_stat line:",linetemp)
                    exit(-1)
        else:
            print("SYNTAX error: Meta apo ID prepei na yparxei '=' epeidi tha ginei anathesi line:", linetemp)
            exit(-1)


#Den kanw if==print_key afou to exw dei stin simple_statement.
#S -> print (E) {P2} sel 57
    def print_stat():
        global results_lex
        global line
        linetemp = line
        results_lex = lex()


        if(results_lex[2] == left_parenthesis):
            linetemp = line
            results_lex = lex()

          #{P2}:genquad(“out”,E.place,”_”,”_”)
            Eplace = expression()
            genQuad('out', Eplace, '_', '_')

            if(results_lex[2] == right_parenthesis):
                linetemp = line
                results_lex = lex()


                if(results_lex[2] == semicolon):
                    linetemp = line
                    results_lex = lex()


                else:
                    print("SYNTAX error: Missing colon ';' on print_stat line:",linetemp)
                    exit(-1)
            else:
                print("SYNTAX error: Missing  ')' on print_stat line:",linetemp)
                exit(-1)
        else:
            print("SYNTAX error: Missing colon '(' on print_stat line:", linetemp)
            exit(-1)



#Den kanw if==return_key afou to exw dei stin simple_statement.
#S -> return (E) {P1}
    def return_stat():
        global results_lex
        global line
        linetemp = line
        results_lex = lex()


        if(results_lex[2] == left_parenthesis):
            linetemp = line
            results_lex = lex()

         #{P1}: genquad(“retv”,E.place,”_”,”_”)
            Eplace = expression()
            genQuad('retv', Eplace, '_', '_')


            if(results_lex[2] == right_parenthesis):
                linetemp = line
                results_lex = lex()


                if(results_lex[2] == semicolon):
                    linetemp = line
                    results_lex = lex()

                else:
                    print("SYNTAX error: Missing colon ';' on return_stat line:",linetemp)
                    exit(-1)
            else:
                print("SYNTAX error: Missing  ')' on return_stat line:",linetemp)
                exit(-1)
        else:
            print("SYNTAX error: Missing colon '(' on return_stat line:", linetemp)
            exit(-1)


#Den kanw if==if_key afou to exw dei stin structured_statement.
#S -> if B then {P1} S1 {P2} TAIL {P3} ,  TAIL -> else S2 | TAIL -> ε sel 51
    def if_stat():
        global results_lex
        global line
        linetemp = line
        results_lex= lex()

        if(results_lex[2] == left_parenthesis):
            linetemp = line
            results_lex = lex()

        #{P1}:backpatch(B.true,nextquad())
            cond = condition()
            backPatch(cond[0], nextQuad())

            if(results_lex[2]== right_parenthesis):
                linetemp = line
                results_lex = lex()

                if(results_lex[2] == colon):
                    linetemp = line
                    results_lex = lex()

                    if(results_lex[2] == left_curly_bracket):
                        linetemp = line
                        results_lex = lex()
                        statements()

                  #{P2}:
                        #ifList=makelist(nextquad())
                        #genquad(“jump”,”_”,”_”,”_”)
                        #backpatch(B.false,nextquad())

                        ifList = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')
                        backPatch(cond[1], nextQuad())

                        if(results_lex[2] == right_curly_bracket):
                            linetemp = line
                            results_lex = lex()

                        else:
                            print("SYNTAX error: Missing  '#}' on if statements line:",linetemp )
                            exit(-1)
                    else:
                        statement()

                  #{P2}: (An exw mono mia entoli pou akolouthei)
                        #ifList=makelist(nextquad())
                        #genquad(“jump”,”_”,”_”,”_”)
                        #backpatch(B.false,nextquad())

                        ifList = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')
                        backPatch(cond[1], nextQuad())

                    if(results_lex[2] == else_key):
                        linetemp = line
                        results_lex = lex()

                        if(results_lex[2] == colon):
                            linetemp = line
                            results_lex = lex()


                            if(results_lex[2] == left_curly_bracket):
                                linetemp = line
                                results_lex = lex()
                                statements()

                            #{P3}: backpatch(ifList,nextquad())
                                backPatch(ifList, nextQuad())

                                if(results_lex[2] == right_curly_bracket):
                                    linetemp = line
                                    results_lex = lex()

                                else:
                                    print("SYNTAX error: Missing  '#}' on if statements line:",linetemp)
                                    exit(-1)
                            else:
                                statement()

                             #{P3}: backpatch(ifList,nextquad()) (a exw mono mia entoli )
                                backPatch(ifList, nextQuad())
                        else:
                            print("SYNTAX error: Missing  ':' on else statement line:",linetemp)
                            exit(-1)
                    else:

                    #{P3}: backpatch(ifList,nextquad())
                        backPatch(ifList, nextQuad())

                else:
                    print("SYNTAX error: Missing  ':' on if condition line:",linetemp)
                    exit(-1)

            else:
                print("SYNTAX error: Missing  ')' on if condition line:", linetemp)
                exit(-1)
        else:
            print("SYNTAX error: Missing  '(' on if condition line:", linetemp)
            exit(-1)


#Den kanw if==while_key afou to exw dei stin structured_statement.
#S -> while {P1} B do {P2} S1 {P3} sel 42
    def while_stat():
        global results_lex
        global line
        linetemp = line
        results_lex= lex()

        if(results_lex[2] == left_parenthesis):
            linetemp = line
            results_lex = lex()


        #{P1}:Bquad:=nextquad()
            Bquad=nextQuad()

            cond = condition()

         #{P2}:backpatch(B.true,nextquad())
            backPatch(cond[0], nextQuad())


            if(results_lex[2]== right_parenthesis):
                linetemp = line
                results_lex = lex()


                if(results_lex[2] == colon):
                    linetemp = line
                    results_lex = lex()


                    if(results_lex[2] == left_curly_bracket):
                        linetemp = line
                        results_lex = lex()
                        statements()

                    #{P3}:
                        #genquad(“jump”,”_”,”_”,Bquad)
                        #backpatch(B.false,nextquad())

                        genQuad('jump', '_', '_', Bquad)
                        backPatch(cond[1], nextQuad())

                        if(results_lex[2] == right_curly_bracket):
                            linetemp = line
                            results_lex = lex()

                        else:
                            print("SYNTAX error: Missing  '#}' on while statements line:",linetemp)
                            exit(-1)
                    else:
                        statement()

                    #{P3}:(Ean den exei '{' diladi akolouthei mono mia entoli)
                        #genquad(“jump”,”_”,”_”,Bquad)
                        #backpatch(B.false,nextquad())

                        genQuad('jump', '_', '_', Bquad)
                        backPatch(cond[1], nextQuad())
                else:
                    print("SYNTAX error: Missing  ':' on while condition line:",linetemp)
                    exit(-1)
            else:
                print("SYNTAX error: Missing  ')' on while condition line:", linetemp)
                exit(-1)
        else:
            print("SYNTAX error: Missing  '(' on while condition line:", linetemp)
            exit(-1)


    def id_list(str):
        global line
        global results_lex

        if(results_lex[2] == id):
            func_name = results_lex[1]
            results_lex = lex()
            linetemp = line

            # str == "argum"  to kalese i def_function etsi einai ena  argument
            if (str == "argum"):

                #pinakas sumbolwn ftiaxnw argument
                myNewArguent = Argument()
                myNewArguent.name = func_name
                add_argument(myNewArguent)

            #to kalese i declaration_line etsi einai Entity
            else:
                #pinakas sumbolwn ftiaxnw entity
                myNewEntity = Entity()
                myNewEntity.name = func_name
                myNewEntity.variable.offset = find_offset()
                myNewEntity.type = 'variable'
                add_entity(myNewEntity)

            while(results_lex[2] == comma):
                results_lex = lex()

                if(results_lex[2] == id and linetemp == line ):
                    func_name = results_lex[1]
                    results_lex = lex()

                    if (str == "argum"):

                        #pinakas sumbolwn ftiaxnw argument.
                        myNewArguent = Argument()
                        myNewArguent.name = func_name
                        add_argument(myNewArguent)
                    else:
                        #pinakas sumbolwn ftiaxnw entity
                        myNewEntity = Entity()
                        myNewEntity.name = func_name
                        myNewEntity.variable.offset = find_offset()
                        myNewEntity.type = 'variable'
                        add_entity(myNewEntity)

                else:
                    print("SYNTAX error: Missing ID after comma line:", linetemp)
                    exit(-1)


#Aritmitikes parastaseis.
#Ε -> T1 ( + T2 {P1})* {P2} sel 14
    def expression():
        global results_lex
        global line

        optional_sign()

        T1place = term() #T1

        while(results_lex[2]==plus or results_lex[2]==minus):
            addOperators = ADD_OP()
            T2place = term() #T2

            #{P1}:
            w = newTemp()
            genQuad(addOperators, T1place, T2place, w)
            T1place = w

        #{P2}:
        Eplace = T1place
        return Eplace


#Aritmitikes parastaseis pollaplasiasmos.
#T -> F1 (× F2 {P1})* {P2} sel 15
    def term():
        global results_lex
        global line

        F1place = factor() #F1

        while(results_lex[2]==multiplication or results_lex[2]==division):
            mulOperators= MUL_OP()

            F2place = factor() #F2
            #{P1}:
            w=newTemp()
            genQuad(mulOperators, F1place, F2place, w)
            F1place = w

        #{P2}:
        Tplace =F1place
        return Tplace

#F -> ( E ) {P1} ||  F -> id {P1} sel16
    def factor():
        global results_lex
        global line
        linetemp = line

        if(results_lex[2]==number):
            Fplace = results_lex[1]
            linetemp = line
            results_lex = lex()


        elif(results_lex[2]==left_parenthesis):
            linetemp = line
            results_lex = lex()

            #{P1}: endiamesos sel16
            Eplace = expression()
            Fplace = Eplace


            if(results_lex[2]==right_parenthesis):
                linetemp = line
                results_lex = lex()
            else:
                print("SYNTAX error: Missing  ')' on  end of the factor line:",linetemp)
                exit(-1)

        elif(results_lex[2]==id):
            factor_t = results_lex[1]
            linetemp = line
            results_lex = lex()

            ##{P1}: endiamesos sel16
            Fplace = idtail(factor_t) #factor_t onoma syn/sis

        else:
            print("SYNTAX error: Missing constant OR expression OR variable on factor line:",linetemp)
            exit(-1)

        return Fplace


    def idtail(id_param):
        global results_lex
        global line
        linetemp = line
        if(results_lex[2] == left_parenthesis ):
            linetemp = line
            results_lex = lex()
            actual_par_list()

            #endiamesos
            w=newTemp()
            genQuad('par', w, 'RET', '_')
            genQuad('call', id_param, '_', '_')

            if(results_lex[2]==right_parenthesis):
                linetemp = line
                results_lex = lex()

                #endiamesos
                return w

            else:
                print("SYNTAX error: Missing  ')' on line:",linetemp)
                exit(-1)

        else:
            #endiamesos
            return id_param


    def actual_par_list():
        global results_lex
        global line

        if (results_lex[2]==number
            or results_lex[2]==left_parenthesis
            or results_lex[2]==id):

            #endiamesos
            expr = expression()
            genQuad('par', expr, 'CV', '_')


            while(results_lex[2] == comma):
                results_lex  = lex()

                #endiamesos
                expr = expression()
                genQuad('par', expr, 'CV', '_')


    def optional_sign():
        global results_lex
        global line

        if(results_lex[2] == plus or results_lex[2] == minus):
            ADD_OP()

#B -> Q1 {P1} ( or {P2} Q2 {P3})* sel 26. || R -> ( B ) {P1}
    def condition():
        global results_lex
        global line

        #endiamesos
        Btrue = []
        Bfalse = []

        Q1 = bool_term()
     #{P1}:

        #B.true = Q1.true     || R.true=B.true
        #B.false = Q1.false   ||R.false=B.false

        Btrue = Q1[0]
        Bfalse = Q1[1]


        while(results_lex[2]==or_key):
            results_lex=lex()

     #{P2}: backpatch(B.false, nextquad())
            backPatch(Bfalse, nextQuad())

            Q2 = bool_term()
     #{P3}: B.true = merge(B.true, Q2.true)
           #B.false = Q2.false

            Btrue = merge(Btrue, Q2[0])
            Bfalse = Q2[1]

        #endiamesos
        return Btrue, Bfalse


#Q -> R1 {P1} ( and {P2} R2 {P3})* sel 27.
    def bool_term():
        global results_lex
        global line

        #endiamesos
        Qtrue = []
        Qfalse = []
        R1 = bool_factor()

     #{P1}:
        #Q.true = R1.true
        #Q.false = R .false

        Qtrue = R1[0]
        Qfalse = R1[1]

        while(results_lex[2]==and_key):
            results_lex=lex()
            linetemp = line

     #{P2}: backpatch(Q.true, nextquad())
            backPatch(Qtrue, nextQuad())

            R2 = bool_factor()
     #{P3}:  Q.false = merge(Q.false, R2.false)
            #Q.true = R2.true

            Qfalse = merge(Qfalse, R2[1])
            Qtrue = R2[0]

        #endiamesos
        return Qtrue, Qfalse

# R -> not ( B ) {P1} ---NOT--- sel 31 || R -> E1 relop E2 {P1}  sel 33
    def bool_factor():
        global results_lex
        global line
        linetemp = line

        #endiamesos
        Rtrue = []
        Rfalse = []

        if(results_lex[2]==not_key):
            linetemp = line
            results_lex=lex()


            if(results_lex[2]==left_square_bracket):
                linetemp = line
                results_lex = lex()

                #endiamesos
                cond = condition()


                if(results_lex[2]==right_square_bracket):
                    linetemp = line
                    results_lex = lex()

                #{P1}:  ---GIA NOT---
                   #R.true=B.false
                   #R.false=B.true

                    Rtrue = cond[1]
                    Rfalse = cond[0]


                else:
                    print("SYNTAX error: Missing  ']' on boolfactor condition line:",linetemp)
                    exit(-1)
            else:
                print("SYNTAX error: Missing  '[' on boolfactor condition line:", linetemp)
                exit(-1)

        elif(results_lex[2]==left_square_bracket):
            linetemp = line
            results_lex = lex()

            #endiamesos
            cond = condition()



            if(results_lex[2]==right_square_bracket):
                linetemp = line
                results_lex = lex()

                #endiamesos
                Rtrue = cond[0]
                Rfalse = cond[1]

            else:
                print("SYNTAX error: Missing  ']' on boolfactor condition line:", linetemp)
                exit(-1)
        else:

            #endiamesos
            E1place = expression()
            relop = REL_OP()
            E2place = expression()

        #{P1}:
            #R.true=makelist(nextquad())
            #genQuad(relop, E1.place, E2.place, “_”)
            #R.false=makelist(nextquad())
            #genQuad(“jump” , “_” , “_” , “_”)

            Rtrue=makeList(nextQuad())
            genQuad(relop, E1place, E2place, '_')
            Rfalse=makeList(nextQuad())
            genQuad('jump', '_', '_', '_')

        return Rtrue, Rfalse

    def call_main_part():
        global results_lex
        global line
        linetemp = line

        if(results_lex[2] == if_key):
            linetemp = line
            results_lex = lex()


            if(results_lex[2] == name_key):
                linetemp = line
                results_lex = lex()


                if(results_lex[2] == equal):
                    linetemp = line
                    results_lex = lex()

                    if(results_lex[2] == main_key):
                        linetemp = line
                        results_lex = lex()

                        if(results_lex[2] == colon):
                            linetemp = line
                            results_lex = lex()
                            genQuad('begin_block','"__main__"','_','_')
                            main_function_call()

                            while(results_lex[2] == id):
                                main_function_call()
                            genQuad('halt','_','_','_')
                            genQuad('end_block','"__main__"','_','_')

                            #pinakas sumbolwm
                            write_Symbol_Table(pinakas_sum)
                            generate_final()

                            delete_scope()

                        else:
                            print("SYNTAX error: Missing ':' on call_main_part line:",linetemp)
                            exit(-1)

                    else:
                       print("SYNTAX error: Missing \"__main__\" on call_main_part line:",linetemp)
                       exit(-1)

                else:
                        print("SYNTAX error: Missing '==' on call_main_part line:",linetemp)
                        exit(-1)

            else:
                    print("SYNTAX error: Missing ' __name__' on call_main_part line:",linetemp)
                    exit(-1)
        else:
                 print("SYNTAX error: Missing keyword 'if' on call_main_part line:",linetemp)
                 exit(-1)


    def main_function_call():
        global line
        global results_lex
        linetemp = line

        if(results_lex[2] == id):
            genQuad('call', results_lex[1], '_', '_')
            linetemp = line
            results_lex = lex()


            if(results_lex[2] == left_parenthesis):
                linetemp = line
                results_lex = lex()


                if(results_lex[2] == right_parenthesis):
                    linetemp = line
                    results_lex = lex()


                    if(results_lex[2] == semicolon):
                        linetemp = line
                        results_lex = lex()

                    else:
                        print("SYNTAX error: Missing ';' on MAIN CALL line:",linetemp)
                        exit(-1)
                else:
                    print("SYNTAX error: Missing ')' on MAIN CALL line:",linetemp)
                    exit(-1)
            else:
                print("SYNTAX error: Missing '(' on MAIN CALL line:",linetemp)
                exit(-1)

        else:
            print("SYNTAX error: Missing 'name of main_function' on MAIN CALL line:",linetemp)
            exit(-1)


    def ADD_OP():
        global results_lex
        global line

        if(results_lex[2]==plus):
            addOper = results_lex[1]
            results_lex = lex()


        elif(results_lex[2]==minus):
            addOper = results_lex[1]
            results_lex = lex()


        return addOper


    def MUL_OP():
        global results_lex
        global line

        if (results_lex[2] == multiplication):
            mulOper = results_lex[1]
            results_lex = lex()


        elif (results_lex[2] == division):
            mulOper = results_lex[1]
            results_lex = lex()

        return mulOper


    def REL_OP():
        global results_lex
        global line
        linetemp = line

        if(results_lex[2]==equal):
            rel_op = results_lex[1]
            linetemp = line
            results_lex = lex()


        elif(results_lex[2]==smaller):
            rel_op = results_lex[1]
            linetemp = line
            results_lex = lex()


        elif(results_lex[2]==smaller_or_equal):
            rel_op = results_lex[1]
            linetemp = line
            results_lex = lex()


        elif(results_lex[2]==different):
            rel_op = results_lex[1]
            linetemp = line
            results_lex = lex()


        elif(results_lex[2]== larger):
            rel_op = results_lex[1]
            linetemp = line
            results_lex = lex()


        elif(results_lex[2]==larger_or_equal):
            rel_op = results_lex[1]
            linetemp = line
            results_lex = lex()


        else:
            print("SYNTAX error: Missing Reloperator on the expression line:",linetemp )
            exit(-1)

        return rel_op



    startRule()

syntax_analyzer()
print("-----------------TELOS SYNTAKTIKOU ELEGXOU-----------------")
print("-------------------DEN BRETHIKAN LATHI---------------------")
print("-------------------FINAL CODE GENERATED--------------------")

printIntCode(endiamesos)
endiamesos.close()
pinakas_sum.close()
telikos_arxeio.close()
