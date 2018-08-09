
def inicio():

 def game_1(values):
    c=int(input('digite a linha onde inserir x de 0 a 2:'))
    d=int(input('digite a coluna onde inserir x de 0 a 2:'))
    if (0<=c<=2) and (0<=d<=2):
        if values[c][d]=='x|' or values[c][d]=='o|':
              print('jogada invalida')
              return game_1(values)
        else:
              values[c][d]='x|'
              global a
              a=0

              for i in range(0,3):
                for j in range(0,3):
                    if values[i][j]=='x|':
                        a+=1




              for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
              return (values)
    else:
        print('jogada invalida')
        return game_1(values)

 def game_2(values,a):

    if a==1:
        if values[1][1]=='x|':
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        else:
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
    elif a==2:
        if (values[0][0]=='x|' and values[0][1]=='x|' and values[0][2]==' |'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[0][1]==' |' and values[0][2]=='x|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[0][1]=='x|' and values[0][2]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")





        elif (values[1][0]==' |' and values[1][1]=='x|' and values[1][2]=='x|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='x|' and values[1][1]==' |' and values[1][2]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='x|' and values[1][1]=='x|' and values[1][2]==' |'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]==' |' and values[2][1]=='x|' and values[2][2]=='x|'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='x|' and values[2][1]==' |' and values[2][2]=='x|'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='x|' and values[2][1]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][1]==' |' and values[1][1]=='x|' and values[2][1]=='x|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='x|' and values[1][1]==' |' and values[2][1]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='x|' and values[1][1]=='x|' and values[2][1]==' |'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][2]=='x|' and values[2][2]=='x|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][2]==' |' and values[2][2]=='x|'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][2]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")














        elif (values[0][0]=='x|' and values[1][0]=='x|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[1][0]==' |' and values[2][0]=='x|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][0]=='x|' and values[2][0]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][0]=='x|' and values[1][1]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[1][1]==' |' and values[2][2]==' |'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][1]=='x|' and values[2][2]==' |'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][1]=='x|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][1]==' |' and values[2][0]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][1]=='x|' and values[2][0]=='x|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        else:
            if values[0][0]=='o|':
                if values[0][2]==' |':
                    values[0][2]='o|'
                    for i in range(0,len(values)):
                         output=""
                         for j in range(0,len(values[i])):
                             output+=str(values[i][j]) + "\t"
                         print (output + "\n")
            elif values[1][1]=='o|':
                if (values[0][0].count('x|'))+(values[0][2].count('x|'))+(values[2][0].count('x|'))+(values[2][2].count('x|'))==2:
                    values[2][1]='o|'
                    for i in range(0,len(values)):
                        output=""
                        for j in range(0,len(values[i])):
                            output+=str(values[i][j]) + "\t"
                        print (output + "\n")
                elif (values[0][0].count('x|'))+(values[0][2].count('x|'))+(values[2][0].count('x|'))+(values[2][2].count('x|'))==1 and values[1][2]=='x|':
                    values[0][1]='o|'
                    for i in range(0,len(values)):
                        output=""
                        for j in range(0,len(values[i])):
                           output+=str(values[i][j]) + "\t"
                        print (output + "\n")
                elif (values[0][0].count('x|'))+(values[0][2].count('x|'))+(values[2][0].count('x|'))+(values[2][2].count('x|'))==1 and values[1][0]=='x|':
                    values[0][1]='o|'
                    for i in range(0,len(values)):
                         output=""
                         for j in range(0,len(values[i])):
                            output+=str(values[i][j]) + "\t"
                         print (output + "\n")
                elif (values[0][0].count('x|'))+(values[0][2].count('x|'))+(values[2][0].count('x|'))+(values[2][2].count('x|'))==1 and values[2][1]=='x|':
                    values[1][0]='o|'
                    for i in range(0,len(values)):
                         output=""
                         for j in range(0,len(values[i])):
                            output+=str(values[i][j]) + "\t"
                         print (output + "\n")

                elif (values[0][0].count('x|'))+(values[0][2].count('x|'))+(values[2][0].count('x|'))+(values[2][2].count('x|'))==1 and values[0][1]=='x|':
                    values[1][0]='o|'
                    for i in range(0,len(values)):
                         output=""
                         for j in range(0,len(values[i])):
                            output+=str(values[i][j]) + "\t"
                         print (output + "\n")

                elif (values[0][0].count('x|'))+(values[0][2].count('x|'))+(values[2][0].count('x|'))+(values[2][2].count('x|'))==0 and values[2][0]==' |':
                    values[0][2]='o|'
                    for i in range(0,len(values)):
                         output=""
                         for j in range(0,len(values[i])):
                            output+=str(values[i][j]) + "\t"
                         print (output + "\n")

    elif a==3:
        if (values[0][0]=='o|' and values[0][1]=='o|' and values[0][2]==' |'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")







        elif (values[1][0]==' |' and values[1][1]=='o|' and values[1][2]=='o|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='o|' and values[1][1]==' |' and values[1][2]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='o|' and values[1][1]=='o|' and values[1][2]==' |'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]==' |' and values[2][1]=='o|' and values[2][2]=='o|'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='o|' and values[2][1]==' |' and values[2][2]=='o|'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='o|' and values[2][1]=='o|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][1]==' |' and values[1][1]=='o|' and values[2][1]=='o|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='o|' and values[1][1]==' |' and values[2][1]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='o|' and values[1][1]=='o|' and values[2][1]==' |'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][2]=='o|' and values[2][2]=='o|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][2]==' |' and values[2][2]=='o|'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][2]=='o|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")








        elif (values[0][0]=='o|' and values[0][1]==' |' and values[0][2]=='o|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[0][1]=='o|' and values[0][2]=='o|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='o|' and values[1][0]=='o|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='o|' and values[1][0]==' |' and values[2][0]=='o|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][0]=='o|' and values[2][0]=='o|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][0]=='o|' and values[1][1]=='o|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='o|' and values[1][1]==' |' and values[2][2]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][1]=='o|' and values[2][2]=='o|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][1]=='o|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][1]==' |' and values[2][0]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][1]=='o|' and values[2][0]=='o|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")


        elif (values[0][0]=='x|' and values[0][1]=='x|' and values[0][2]==' |'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[0][1]==' |' and values[0][2]=='x|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[0][1]=='x|' and values[0][2]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[1][0]==' |' and values[1][1]=='x|' and values[1][2]=='x|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='x|' and values[1][1]==' |' and values[1][2]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='x|' and values[1][1]=='x|' and values[1][2]==' |'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]==' |' and values[2][1]=='x|' and values[2][2]=='x|'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='x|' and values[2][1]==' |' and values[2][2]=='x|'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='x|' and values[2][1]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][1]==' |' and values[1][1]=='x|' and values[2][1]=='x|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='x|' and values[1][1]==' |' and values[2][1]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='x|' and values[1][1]=='x|' and values[2][1]==' |'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][2]=='x|' and values[2][2]=='x|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][2]==' |' and values[2][2]=='x|'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][2]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")


        elif (values[0][0]=='x|' and values[1][0]=='x|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[1][0]==' |' and values[2][0]=='x|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][0]=='x|' and values[2][0]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][0]=='x|' and values[1][1]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[1][1]==' |' and values[2][2]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][1]=='x|' and values[2][2]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][1]=='x|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][1]==' |' and values[2][0]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][1]=='x|' and values[2][0]=='x|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        else:
            if values[0][0]==' |':
                values[0][0]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[0][2]==' |':
                values[0][2]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[2][0]==' |':
                values[2][0]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[2][2]==' |':
                values[2][2]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[2][0]==' |':
                values[2][0]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")



    elif a==4:
        if (values[0][0]=='o|' and values[0][1]=='o|' and values[0][2]==' |'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='o|' and values[0][1]==' |' and values[0][2]=='o|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]==' |' and values[1][1]=='o|' and values[1][2]=='o|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='o|' and values[1][1]==' |' and values[1][2]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='o|' and values[1][1]=='o|' and values[1][2]==' |'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]==' |' and values[2][1]=='o|' and values[2][2]=='o|'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='o|' and values[2][1]==' |' and values[2][2]=='o|'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='o|' and values[2][1]=='o|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][1]==' |' and values[1][1]=='o|' and values[2][1]=='o|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='o|' and values[1][1]==' |' and values[2][1]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='o|' and values[1][1]=='o|' and values[2][1]==' |'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][2]=='o|' and values[2][2]=='o|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][2]==' |' and values[2][2]=='o|'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][2]=='o|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][0]==' |' and values[0][1]=='o|' and values[0][2]=='o|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='o|' and values[1][0]=='o|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='o|' and values[1][0]==' |' and values[2][0]=='o|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][0]=='o|' and values[2][0]=='o|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][0]=='o|' and values[1][1]=='o|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='o|' and values[1][1]==' |' and values[2][2]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][1]=='o|' and values[2][2]=='o|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][1]=='o|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='o|' and values[1][1]==' |' and values[2][0]=='o|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][1]=='o|' and values[2][0]=='o|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")


        elif (values[0][0]=='x|' and values[0][1]=='x|' and values[0][2]==' |'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[0][1]==' |' and values[0][2]=='x|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[0][1]=='x|' and values[0][2]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[1][0]=='x|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[1][0]==' |' and values[2][0]=='x|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][0]=='x|' and values[2][0]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][0]=='x|' and values[1][1]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]=='x|' and values[1][1]==' |' and values[2][2]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][0]==' |' and values[1][1]=='x|' and values[2][2]=='x|'):
            values[0][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][1]=='x|' and values[2][0]==' |'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][1]==' |' and values[2][0]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]==' |' and values[1][1]=='x|' and values[1][2]=='x|'):
            values[1][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='x|' and values[1][1]==' |' and values[1][2]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[1][0]=='x|' and values[1][1]=='x|' and values[1][2]==' |'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]==' |' and values[2][1]=='x|' and values[2][2]=='x|'):
            values[2][0]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='x|' and values[2][1]==' |' and values[2][2]=='x|'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[2][0]=='x|' and values[2][1]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][1]==' |' and values[1][1]=='x|' and values[2][1]=='x|'):
            values[0][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='x|' and values[1][1]==' |' and values[2][1]=='x|'):
            values[1][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][1]=='x|' and values[1][1]=='x|' and values[2][1]==' |'):
            values[2][1]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]==' |' and values[1][2]=='x|' and values[2][2]=='x|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][2]==' |' and values[2][2]=='x|'):
            values[1][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        elif (values[0][2]=='x|' and values[1][2]=='x|' and values[2][2]==' |'):
            values[2][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

        elif (values[0][2]==' |' and values[1][1]=='x|' and values[2][0]=='x|'):
            values[0][2]='o|'
            for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
        else:
            if values[0][0]==' |':
                values[0][0]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[0][1]==' |':
                values[0][1]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[0][2]==' |':
                values[0][2]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[1][0]==' |':
                values[1][0]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[2][0]==' |':
                values[2][0]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[1][1]==' |':
                values[1][1]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[1][2]==' |':
                values[1][2]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[2][1]==' |':
                values[2][1]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")
            elif values[2][2]==' |':
                values[2][2]='o|'
                for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")








 values=[]
 values.append([" |"," |"," |"])
 values.append([" |"," |"," |"])
 values.append([" |"," |"," |"])
 q=values[0][0]
 w=values[0][1]
 e=values[0][2]
 r=values[1][0]
 t=values[1][1]
 y=values[1][2]
 u=values[2][0]
 i=values[2][1]
 p=values[2][2]

 for i in range(0,len(values)):
                   output=""
                   for j in range(0,len(values[i])):
                        output+=str(values[i][j]) + "\t"
                   print (output + "\n")

 print('player_1')
 game_1(values)
 print('------------------------------')
 print('computador')
 game_2(values,a)
 print('------------------------------')
 q=values[0][0]
 w=values[0][1]
 e=values[0][2]
 r=values[1][0]
 t=values[1][1]
 y=values[1][2]
 u=values[2][0]
 i=values[2][1]
 p=values[2][2]
 if (q=='x|' and w=='x|' and e=='x|') or (q=='x|' and r=='x|' and u=='x|') or (q=='x|' and t=='x|' and p=='x|') or (w=='x|' and t=='x|' and i=='x|') or (r=='x|' and t=='x|' and y=='x|') or (u=='x|' and i=='x|' and p=='x|') or (e=='x|' and y=='x|' and p=='x|') or (e=='x|' and t=='x|' and u=='x|'):
    print ('player_1 venceu')
    k=input('para novo jogo digite s:')
    if k=='s':
          return inicio()
    else:
          print('fim de jogo')
          return 0

 elif (q=='o|' and w=='o|' and e=='o|') or (q=='o|' and r=='o|' and u=='o|') or (q=='o|' and t=='o|' and p=='o|') or (w=='o|' and t=='o|' and i=='o|') or (r=='o|' and t=='o|' and y=='o|') or (u=='o|' and i=='o|' and p=='o|') or (e=='o|' and y=='o|' and p=='o|') or (e=='o|' and t=='o|' and u=='o|'):
    print ('computador venceu')
    k=input('para novo jogo digite s:')
    if k=='s':
        return inicio()
    else:
        print('fim de jogo')
        return 0

 else:
    print('player_1')
    game_1(values)
    print('------------------------------')

    print('computador')
    game_2(values,a)
    print('------------------------------')
    q=values[0][0]
    w=values[0][1]
    e=values[0][2]
    r=values[1][0]
    t=values[1][1]
    y=values[1][2]
    u=values[2][0]
    i=values[2][1]
    p=values[2][2]
    if (q=='x|' and w=='x|' and e=='x|') or (q=='x|' and r=='x|' and u=='x|') or (q=='x|' and t=='x|' and p=='x|') or (w=='x|' and t=='x|' and i=='x|') or (r=='x|' and t=='x|' and y=='x|') or (u=='x|' and i=='x|' and p=='x|') or (e=='x|' and y=='x|' and p=='x|') or (e=='x|' and t=='x|' and u=='x|'):
       print ('player_1 venceu')
       k=input('para novo jogo digite s:')
       if k=='s':
          return inicio()
       else:
          print('fim de jogo')
          return 0
    elif (q=='o|' and w=='o|' and e=='o|') or (q=='o|' and r=='o|' and u=='o|') or (q=='o|' and t=='o|' and p=='o|') or (w=='o|' and t=='o|' and i=='o|') or (r=='o|' and t=='o|' and y=='o|') or (u=='o|' and i=='o|' and p=='o|') or (e=='o|' and y=='o|' and p=='o|') or (e=='o|' and t=='o|' and u=='o|'):
       print ('computador venceu')
       k=input('para novo jogo digite s:')
       if k=='s':
        return inicio()
       else:
        print('fim de jogo')
        return 0

    else:
       print('player_1')
       game_1(values)
       print('------------------------------')
       q=values[0][0]
       w=values[0][1]
       e=values[0][2]
       r=values[1][0]
       t=values[1][1]
       y=values[1][2]
       u=values[2][0]
       i=values[2][1]
       p=values[2][2]
       if (q=='x|' and w=='x|' and e=='x|') or (q=='x|' and r=='x|' and u=='x|') or (q=='x|' and t=='x|' and p=='x|') or (w=='x|' and t=='x|' and i=='x|') or (r=='x|' and t=='x|' and y=='x|') or (u=='x|' and i=='x|' and p=='x|') or (e=='x|' and y=='x|' and p=='x|') or (e=='x|' and t=='x|' and u=='x|'):
                    print ('player_1 venceu')
                    k=input('para novo jogo digite s:')
                    if k=='s':
                         return inicio()
                    else:
                         print('fim de jogo')
                         return 0

       elif (q=='o|' and w=='o|' and e=='o|') or (q=='o|' and r=='o|' and u=='o|') or (q=='o|' and t=='o|' and p=='o|') or (w=='o|' and t=='o|' and i=='o|') or (r=='o|' and t=='o|' and y=='o|') or (u=='o|' and i=='o|' and p=='o|') or (e=='o|' and y=='o|' and p=='o|') or (e=='o|' and t=='o|' and u=='o|'):
                    print ('computador venceu')
                    k=input('para novo jogo digite s:')
                    if k=='s':
                        return inicio()
                    else:
                        print('fim de jogo')
                        return 0

       print('computador')
       game_2(values,a)
       print('------------------------------')
       q=values[0][0]
       w=values[0][1]
       e=values[0][2]
       r=values[1][0]
       t=values[1][1]
       y=values[1][2]
       u=values[2][0]
       i=values[2][1]
       p=values[2][2]
       if (q=='x|' and w=='x|' and e=='x|') or (q=='x|' and r=='x|' and u=='x|') or (q=='x|' and t=='x|' and p=='x|') or (w=='x|' and t=='x|' and i=='x|') or (r=='x|' and t=='x|' and y=='x|') or (u=='x|' and i=='x|' and p=='x|') or (e=='x|' and y=='x|' and p=='x|') or (e=='x|' and t=='x|' and u=='x|'):
           print ('player_1 venceu')
           k=input('para novo jogo digite s:')
           if k=='s':
                  return inicio()
           else:
                  print('fim de jogo')
                  return 0
       elif (q=='o|' and w=='o|' and e=='o|') or (q=='o|' and r=='o|' and u=='o|') or (q=='o|' and t=='o|' and p=='o|') or (w=='o|' and t=='o|' and i=='o|') or (r=='o|' and t=='o|' and y=='o|') or (u=='o|' and i=='o|' and p=='o|') or (e=='o|' and y=='o|' and p=='o|') or (e=='o|' and t=='o|' and u=='o|'):
           print ('computador venceu')
           k=input('para novo jogo digite s:')
           if k=='s':
              return inicio()
           else:
              print('fim de jogo')
              return 0

       else:
          print('player_1')
          game_1(values)
          print('------------------------------')
          q=values[0][0]
          w=values[0][1]
          e=values[0][2]
          r=values[1][0]
          t=values[1][1]
          y=values[1][2]
          u=values[2][0]
          i=values[2][1]
          p=values[2][2]
          if (q=='x|' and w=='x|' and e=='x|') or (q=='x|' and r=='x|' and u=='x|') or (q=='x|' and t=='x|' and p=='x|') or (w=='x|' and t=='x|' and i=='x|') or (r=='x|' and t=='x|' and y=='x|') or (u=='x|' and i=='x|' and p=='x|') or (e=='x|' and y=='x|' and p=='x|') or (e=='x|' and t=='x|' and u=='x|'):
                    print ('player_1 venceu')
                    k=input('para novo jogo digite s:')
                    if k=='s':
                         return inicio()
                    else:
                         print('fim de jogo')
                         return 0
          elif (q=='o|' and w=='o|' and e=='o|') or (q=='o|' and r=='o|' and u=='o|') or (q=='o|' and t=='o|' and p=='o|') or (w=='o|' and t=='o|' and i=='o|') or (r=='o|' and t=='o|' and y=='o|') or (u=='o|' and i=='o|' and p=='o|') or (e=='o|' and y=='o|' and p=='o|') or (e=='o|' and t=='o|' and u=='o|'):
                    print ('computador venceu')
                    k=input('para novo jogo digite s:')
                    if k=='s':
                        return inicio()
                    else:
                        print('fim de jogo')
                        return 0
          print('computador')
          game_2(values,a)
          print('------------------------------')
          q=values[0][0]
          w=values[0][1]
          e=values[0][2]
          r=values[1][0]
          t=values[1][1]
          y=values[1][2]
          u=values[2][0]
          i=values[2][1]
          p=values[2][2]
          if (q=='x|' and w=='x|' and e=='x|') or (q=='x|' and r=='x|' and u=='x|') or (q=='x|' and t=='x|' and p=='x|') or (w=='x|' and t=='x|' and i=='x|') or (r=='x|' and t=='x|' and y=='x|') or (u=='x|' and i=='x|' and p=='x|') or (e=='x|' and y=='x|' and p=='x|') or (e=='x|' and t=='x|' and u=='x|'):
              print ('player_1 venceu')
              k=input('para novo jogo digite s:')
              if k=='s':
                 return inicio()
              else:
                 print('fim de jogo')
                 return 0
          elif (q=='o|' and w=='o|' and e=='o|') or (q=='o|' and r=='o|' and u=='o|') or (q=='o|' and t=='o|' and p=='o|') or (w=='o|' and t=='o|' and i=='o|') or (r=='o|' and t=='o|' and y=='o|') or (u=='o|' and i=='o|' and p=='o|') or (e=='o|' and y=='o|' and p=='o|') or (e=='o|' and t=='o|' and u=='o|'):
              print ('computador venceu')
              k=input('para novo jogo digite s:')
              if k=='s':
                  return inicio()
              else:
                  print('fim de jogo')
                  return 0

          else:
              print('player_1')
              game_1(values)
              print('------------------------------')
              q=values[0][0]
              w=values[0][1]
              e=values[0][2]
              r=values[1][0]
              t=values[1][1]
              y=values[1][2]
              u=values[2][0]
              i=values[2][1]
              p=values[2][2]
              if (q=='x|' and w=='x|' and e=='x|') or (q=='x|' and r=='x|' and u=='x|') or (q=='x|' and t=='x|' and p=='x|') or (w=='x|' and t=='x|' and i=='x|') or (r=='x|' and t=='x|' and y=='x|') or (u=='x|' and i=='x|' and p=='x|') or (e=='x|' and y=='x|' and p=='x|') or (e=='x|' and t=='x|' and u=='x|'):
                    print ('player_1 venceu')
                    k=input('para novo jogo digite s:')
                    if k=='s':
                         return inicio()
                    else:
                         print('fim de jogo')
                         return 0
              elif (q=='o|' and w=='o|' and e=='o|') or (q=='o|' and r=='o|' and u=='o|') or (q=='o|' and t=='o|' and p=='o|') or (w=='o|' and t=='o|' and i=='o|') or (r=='o|' and t=='o|' and y=='o|') or (u=='o|' and i=='o|' and p=='o|') or (e=='o|' and y=='o|' and p=='o|') or (e=='o|' and t=='o|' and u=='o|'):
                    print ('computador venceu')
                    k=input('para novo jogo digite s:')
                    if k=='s':
                        return inicio()
                    else:
                        print('fim de jogo')
                        return 0
              elif (q=='x|'or q=='o|') and (w=='x|'or w=='o|') and (e=='x|'or e=='o|') and (r=='x|'or r=='o|') and (t=='x|'or t=='o|') and (y=='x|'or y=='o|') and (u=='x|'or u=='o|') and (i=='x|'or i=='o|') and (p=='x|'or p=='o|'):
                    print ('velha')
                    k=input('para novo jogo digite s:')
                    if k=='s':
                       return inicio()
                    else:
                       print('fim de jogo')
                       return 0

inicio()



