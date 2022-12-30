import os
from shutil import rmtree


if __name__=='__main__':
    print("The student files must be there in folder named student_codes\n\nThe code must contain the main function given in file mainFunc.txt ,also there should not be any printf statements other than required output",end='\n\n')
    
    nTestCases = int(input("Enter the number of test cases you want to make"))

    if(os.path.exists(f'{os.getcwd()}\\inputs')):
        rmtree(f'{os.getcwd()}\\inputs')
    if(os.path.exists(f'{os.getcwd()}\\expected')):
        rmtree(f'{os.getcwd()}\\expected')
    if(not(os.path.exists(f'{os.getcwd()}\\student_codes'))):
        os.mkdir('student_codes')
        
    os.mkdir('inputs')
    os.mkdir('expected')

    for i in range(0,nTestCases):
        strInput = input(f"Enter test case for test case number {i+1}: ")
        fInput = open(os.getcwd() + f"\\inputs\\input{i+1}.txt", "w")
        fInput.write(strInput)
        strExpected = input(f"Enter expected output for test case {strInput}:")
        fExpected = open(os.getcwd() + f"\\expected\\expected{i+1}.txt", "w")
        fExpected.write(strExpected)
        fInput.close()
        fExpected.close()
        print('\n')
    print(f'\n\nMade by Harsh Sonegra Bharatbhai Enr: 206270307079\nStudent Of Computer Engineering Year:2020-2023\nIdea suggested by Charag Nathwani Sir \nGovernment Polytechnic Porbandar ')
    x = input("Enter any key to exit")