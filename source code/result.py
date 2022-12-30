import os
import filecmp
import pandas as pd

counter=0
def check(inpFile,expectedOutput):
    os.system(f'{os.getcwd()}\\stu.exe {inpFile}')
    f1 = f"{os.getcwd()}\\output.txt"
    f2 = f"{expectedOutput}"
    # shallow comparison
    result = filecmp.cmp(f1, f2)
    # deep comparison
    result = filecmp.cmp(f1, f2, shallow=False)
    if(result==True):
        global counter
        counter+=1

def checkForEveryFile():
    cwd = os.getcwd()
    expectedPath = cwd + "\\expected"
    inputPath = cwd + "\\inputs"
    studentCodePath = cwd + "\\student_codes\\"
    res = 0
    listOfInputFile = os.listdir(inputPath)
    listOfExpectedFile = os.listdir(expectedPath)
    
    for i in range(len(listOfInputFile)):
        check(f'{inputPath}\\{listOfInputFile[i]}',f'{expectedPath}\\{listOfExpectedFile[i]}')
    global counter
    res = counter
    counter = 0
    return res

if __name__ == "__main__":
    cwd = os.getcwd()
    expectedPath = cwd + "\\expected\\"
    inputPath = cwd + "\\inputs\\"
    studentCodePath = cwd + "\\student_codes\\"
    totalCases = len(os.listdir(inputPath))
    StudentCodeList = os.listdir(studentCodePath)
    data = {
        "Enrollment" : [],
        "PassedCases" : [],
        "TotalCases": totalCases
    }
    if(not(os.path.exists(f'{os.getcwd()}\\output.txt'))):
        f = open(f'{os.getcwd()}\\output.txt',"x")
        f.close()

    for stuCode in  StudentCodeList:
        # compiling the code
        os.system(f'g++ {studentCodePath}\\{stuCode} -o stu.exe')
        studentEnr = stuCode.split('.')[0]
        studentPassedCases = checkForEveryFile()
        print(f'{studentEnr} passed {studentPassedCases} cases out of {totalCases}')
        data["Enrollment"].append(studentEnr)
        data["PassedCases"].append(studentPassedCases)
    
    data = pd.DataFrame(data) 
    data.to_excel("output.xlsx")

    os.remove(cwd + "\\output.txt")
    if(os.path.exists(f'{os.getcwd()}\\stu.exe')):
        os.remove(cwd + "\\stu.exe")

    print(f'\n\nMade by Harsh Sonegra Bharatbhai Enr: 206270307079\nStudent Of Computer Engineering Year:2020-2023\nIdea suggested by Charag Nathwani Sir \nGovernment Polytechnic Porbandar ')
    x = input("Enter any key to exit")