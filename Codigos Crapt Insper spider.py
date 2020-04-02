dinheiro=1000
x= True
   
while x==True:
    if dinheiro==0:
        print("Que pena, você está sem crédito")
        break
    
    print("Você tem: {}".format(dinheiro))
    pergunta=input("Você gostaria de continuar apostando? Se sim digite (s) se não digite (n): ")
     
    if pergunta == "n":
            print("Obrigado por jogar!")
            print("Você acabou com: {}".format(dinheiro))
            break
       
        
    elif pergunta == "s":
        come_out= input("O que você deseja apostar? Opções: pass line bet, field, any craps ou twelve: ")
        
        
        #PASS LINE BET
        if come_out=="pass line bet":
            aposta1= int(input("Quanto você deseja apostar? "))
            import random
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            s1 = dado1 + dado2
            
            if s1 == "7" or s1== "11":
                print ("Você venceu!!!")
                dinheiro = dinheiro + aposta1
                
            elif s1 =="2" or s1=="3" or s1=="12":
                    print ("Você Perdeu")
                    dinheiro = dinheiro - aposta1
                    
            else:
                print ("Você entrou no modo Point")
            
        
        #FIELD
        elif come_out=="field":
            aposta2= int(input("Quanto você deseja apostar? "))
            import random
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            s2 = int (dado1 + dado2)
           
            if s2=="5" or s2=="6" or s2=="7" or s2=="8":
                print("Que pena, você perdeu")
                dinheiro = dinheiro - aposta2
            
            elif s2=="3" or s2=="4" or s2=="9" or s2=="10" or s2=="11":
                print("Você ganhou")
                dinheiro = dinheiro
                
            elif s2=="2":
                print("Você ganhou o dobro!!")
                dinheiro = dinheiro + 2*aposta2
                
            elif s2=="12":
                print("Você ganhou o triplo!!!!")
                dinheiro = dinheiro + 3*aposta2
        
        
        
        #ANY CRAPS
        elif come_out=="any craps":
            aposta3= int(input("Quanto você deseja apostar? "))
            import random
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            s3 = dado1 + dado2
            
            if s3=="2" or s3=="3" or s3=="12" :
                print("Parabens!!! Vocé acaba de ganhar 7x o apostado")
                dinheiro = dinheiro + 7*aposta3
                
            else:
                print("Que pena, você perdeu")
                dinheiro = dinheiro - aposta3
        
        
        #TWELVE
        elif come_out=="twelve":
            aposta4= int(input("Quanto você deseja apostar? "))
            import random
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            s4 = dado1 + dado2
            
            if s4=="12":
                print("!!SORTE GRANDE!! 30X O APOSTADO!!")
                dinheiro = dinheiro + 30*aposta4
                
            else:
                print("Que pena, você perdeu")
                dinheiro = dinheiro - aposta3
