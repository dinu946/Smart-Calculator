
HISTORY = "history.txt"
def show_history():
    file =open(HISTORY,"r")
    line=file.readlines()
    if len(line)==0:
        print("no history found :")
    else :
        for line in reversed(line):
            print(line.strip())
    file.close()


def clear_history():
    file=open(HISTORY,"w") 
    file.close() 
    print("History cleared:")

def save_history(equation,result):
    file=open(HISTORY,"a")
    file.write(equation +"="+str(result)+"3\n")
    file.close()


def calculate(user_input):
     parts=user_input.split()

     if len(parts)!=3:
         print ("Invalid input. use formate number opretor number(e.g 7+7)")
         return
     num1=float(parts[0])
     ope=parts[1]  
     num2=float(parts[2])


     if ope =="+":
        result = num1+num2
     elif ope =="-":
        result = num1-num2
        
     elif ope =="*":
         result = num1*num2 

     elif ope =="/" :
         if num2 == 0:
             print("cannot divided by zero :")
             return
         result =num1/num2

     else :
         print("invelate operetor .use only(+,-,*,/):")
         return
     if int(result)==result:
         result=int(result)
         print("Result:",result)
         save_history(user_input,result) 
def main():
    print("____SIMPLE CELCULATOR (type history, clear or exit):")
    while True :
        user_input=input("Enter calculation(+,-,*,/) or command (history,clear,exit,save)=")    

        if user_input=="exit":
         print("Goodbye:")
         break
        elif user_input =="history":

          show_history()

        elif user_input=="clear":
          clear_history() 

        else :
          calculate(user_input)     

main()


