#Jordan Fonseca
#Program assingment 4, section 2.4
#it said to submit as seperate file


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
