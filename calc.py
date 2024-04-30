""" USER INPUT """
print(""" 
    \t\t CALCULATOR
    \t\t----------\n
    Select the operation:
    \t The long versions are for sums involving more than two numbers.\n
    \t1: Addition
    \t2: Long Addition
    \t3: Subtraction
    \t4: Long Subtraction
    \t5: Multiplication
    \t6: Long Multiplication
    \t7: Division
    \t8: Long Division
    \t9: Combined Operartion (BODMAS)
 """)



answer = 0
#COMPLEX CALCULATIONS (2,4,6,8,9)
def comp_calc_math():
    eqn = input("Enter the whole sum as it is then press enter: ")

    return f"\t\n{eqn} = {eval(eqn)}\n"

#SIMPLE CACULATIONS (1,3,5,7)
def calc_math(u_input):
    num_1 = int(input("Enter the first number and press enter: ")) 
    num_2 = int(input("Enter the second number and press enter: "))

    if u_input==1:
        return f"\n\t{num_1} + {num_2} = {num_1+num_2}\n"
    
    elif u_input==3:
        if num_1>num_2:
            return f"\n\t{num_1} - {num_2} = {num_1-num_2}\n"
        else:
           return f"\n\t{num_2} - {num_1} = {num_2-num_1}\n"
        
    elif u_input==5:
        return f"\n\t{num_1} * {num_2} = {num_1*num_2}\n"
    
    elif u_input==7:
        return f"\n\t{num_1} / {num_2} = {num_1/num_2}\n"
    


user_selection = int(input("select option: "))

if user_selection== 1 or user_selection== 3 or user_selection==5 or user_selection ==7:
    answer=calc_math(user_selection)

elif user_selection== 2 or user_selection == 4 or user_selection == 6 or user_selection == 8 or user_selection == 9:
    answer=comp_calc_math()

else: 
    print("Invalid selection!")

print(answer)
    
