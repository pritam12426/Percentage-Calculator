import os  # Os is bulit in module
from playsound import playsound  # Pip install playsound
from plyer import notification  # Pip install plyer
import colorama

os.system("clear")

if (not os.path.exists("Output")):
    os.mkdir("Output")

while (True): # This will take input for maximum of a single subject
    try:
        max_marks = int(input("Inset the maximum of a single subject >  "))
        break
    except:
        print("\tError: Maximum single subject makrs must be number")
        playsound('Porgram_Data/Error.wav')

while (True): # This will take input for class 1 to 12
    try:
        Class = int(input("Inset only Class name in numbers >  "))
        if 1 <= Class and 12 >= Class:
            break
        else:
            print("\tError: The Class must lise between 1 and 12.")
            playsound('Porgram_Data/Error.wav')
    except:
        print("\tError: Class must be a number")
        playsound('Porgram_Data/Error.wav')

while (True): # Will take input for sec of class
    Class_section = input(f"Inset the the section fo class > ")
    if Class_section.isalpha(): # Will check the Class_section is not carring any "alphabetic characters"
        if len(Class_section) == 1:
            break
        else:
            print("\tError: Section must be a single 'alphabetic characters'")
            playsound('Porgram_Data/Error.wav')
    else:
        print("\tError: section must be a 'alphabetic characters'")
        playsound('Porgram_Data/Error.wav')

file_name = "Class_"

if (not os.path.exists(f'Output/{file_name}{Class}{Class_section.title()}.csv')): # Will add heading for file. If it is not availabe is the output folder

    mylist = ['Name', 'English', 'Maths', 'Hindi','Sst', 'Science', 'Total Marks', 'Percentage']
    with open(f'Output/{file_name}{Class}{Class_section.title()}.csv', 'w') as f:
        for hedder in mylist:
            f.write(str(hedder))
            if hedder != 'Percentage':
                f.write(str(','))

h = 0
while (True):
    student_name = input("Insert the name of sudent or just hit enter to close > ")
    student_name = student_name.title()
    if student_name == "":

        if h != 0:
            notification.notify(
                title="Percentage calculator",
                message=f"A file of name {Class}_{Class_section.upper()} is save in Output folder.",
                app_icon="Porgram_Data/icon.ico",
                timeout=3)
        break
    else:
        with open(f'Output/{file_name}{Class}{Class_section.title()}.csv', 'a') as file_write:
            file_write.write(f"\n{str(student_name)},")

            total_marks = 0
            subject_list = ['English', 'Maths', 'Hindi', 'Sst', 'Science'] # Will help to user to input the date

            for subject in subject_list:
                while True:
                    
                    try:
                        marks = float(input(f"Inset the mark of {student_name} in subject {subject} > "))
                        if 0 <= marks and max_marks >= marks:
                            break
                        else:
                            print(f"\tError: The marks must lise between 0 and {max_marks}.")
                            playsound('Porgram_Data/Error.wav')
                    except ValueError:
                        print("\tError: The Insert Value must be a number.")
                        playsound('Porgram_Data/Error.wav')

                total_marks += marks
                file_write.write(str(f"{marks},"))

            a = max_marks*len(subject_list)
            percentage = (total_marks / a) * 100
            percentage = float('%.2f' % percentage)

            file_write.write(
                str(f"{total_marks}/{max_marks*len(subject_list)},"))

            file_write.write(str(f"{percentage}%,"))
            playsound('Porgram_Data/pop.wav')
            h += 1

        if percentage >= 60:
            print(f"\t{student_name} got {percentage}% and passed with first divison.\n")
        elif percentage >= 40:
            print(f"\t{student_name} got {percentage}% and passed with secound divison.\n")
        elif percentage >= 33:
            print(f"\t{student_name} got {percentage}% and passed with third divison.\n")
        else:
            print(f"\t{student_name} got {percentage}% and {student_name} is fail\n")
