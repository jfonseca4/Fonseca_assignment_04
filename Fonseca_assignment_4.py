#Jordan Fonseca assignment 4


#2.1

number1 = input("enter number 1:   ") #Asks user for componenets of an expression
num1 = float(number1)
operator = input("enter operator:   ")
number2 = input("enter number 2:   ")
num2 = float(number2)

def SimpleExpressionIsValid(): #function for the different operatins
    if operator is "+":
        answer = num1 + num2
        print("True")
        return answer
    elif operator is "-":
        answer = num1 - num2
        print("True")
        return answer
    elif operator is "*":
        answer = num1 * num2
        print("True")
        return answer
    elif operator is "/":
        answer = num1 / num2
        print("True")
        return answer  #prints true for all valid expressions
    else:
        print("False") #prints false for all invalid expressions 
 
ans = SimpleExpressionIsValid()

print(ans) #prints out answer

#2.2

number1 = input("enter number 1:   ") #Asks user for componenets of an expression
num1 = float(number1)
operator = input("enter operator:   ")
number2 = input("enter number 2:   ")
num2 = float(number2)

def evaluateSimpleExpression(): #function for the different operatins
    if operator is "+":
        answer = num1 + num2
        return answer
    elif operator is "-":
        answer = num1 - num2
        return answer
    elif operator is "*":
        answer = num1 * num2
        return answer
    elif operator is "/":
        answer = num1 / num2
        return answer  
 
ans = evaluateSimpleExpression()

print(ans) #prints out answer

#2.3

number1 = input("enter number 1:   ") #Asks user for componenets of an expression
num1 = float(number1)
operator = input("enter operator:   ")
number2 = input("enter number 2:   ")
num2 = float(number2)

def evaluateSimpleExpression(): #function for the different operatins
    if operator is "+":
        answer = num1 + num2
        return answer
    elif operator is "-":
        answer = num1 - num2
        return answer
    elif operator is "*":
        answer = num1 * num2
        return answer
    elif operator is "/":
        answer = num1 / num2
        return answer
    else:
        print("Invalid Expression")
 
ans = evaluateSimpleExpression()

print(ans) #prints out answer
#I could not figure out how to have the user say "end" to stop the code.

#2.4

number1 = input("enter number 1:   ") #Asks user for componenets of an expression
num1 = float(number1)
operator = input("enter operator:   ")
number2 = input("enter number 2:   ")
num2 = float(number2)

def evaluateSimpleExpression(): #function for the different operatins
    if operator is "+":
        answer = num1 + num2
        return answer
    elif operator is "-":
        answer = num1 - num2
        return answer
    elif operator is "*":
        answer = num1 * num2
        return answer
    elif operator is "/":
        answer = num1 / num2
        return answer
 
ans = evaluateSimpleExpression()

value = input("You can also type 'last' to see recently stored value: ")

if value == "last": #prints previous answer
    store = [ans]
    for i in store:
        print(i)
  
#i was not sure what it meant by submit a seperate file so i
    #submitted it on here and in its own file on github.

#3.0 - 3.2
#I was not able to figure out and finish the rest of this assignment.
