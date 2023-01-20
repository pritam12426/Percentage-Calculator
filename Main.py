import os
from playsound import playsound
from plyer import notification


if(not os.path.exists("Output")):
    os.mkdir("Output")
while True:
    try:
        max_marks = int(input("Inset the maximum of a single subject: "))
        break
    except:
        print("\tError: Maximum single subject makrs must be number")
        playsound('Porgram_Data/Error.wav') 

while(True):
    try:
        Class = int(input("Inset only Class name in numbers: "))
        if 1<=Class and 12>=Class:
            break
        else:
            print("\tError: The Class must be between 1 and 12.")
            playsound('Porgram_Data/Error.wav') 
    except:
        playsound('Porgram_Data/Error.wav')
        print("\tError: Class must be a number")

while True:
    Class_section = input(f"Inset the the section fo class: ")
    if Class_section.isalpha():
        if len(Class_section) == 1:
            break
        else:
            print("\tError: Section must be a single 'alphabetic characters'")
            playsound('Porgram_Data/Error.wav')
    else:
        print("\tError: section must be a 'alphabetic characters'")
        playsound('Porgram_Data/Error.wav')

file_name = "Class_"

if(not os.path.exists(f'Output/{file_name}{Class}{Class_section.title()}.csv')):

    mylist = ['Name','English','Maths','Hindi','Sst','Science','Total Marks','Percentage']
    with open(f'Output/{file_name}{Class}{Class_section.title()}.csv', 'w') as f:
        for hedder in mylist:
            f.write(str(hedder))
            if hedder != 'Percentage':
                f.write(str(','))

h = 0
while True:
    student_name = input("Insert the name of sudent or enter exit to close: ")
    student_name = student_name.title()
    if student_name.find("Exit") == 0:
        if not h==0:
            notification.notify(
            title = "Percentage calculator",
            message = f"A file of name {Class}_{Class_section.upper()} is save in Output folder.",
            app_icon = "Porgram_Data/icon.ico",
            timeout = 5)
        break
    else:
        with open(f'Output/{file_name}{Class}{Class_section.title()}.csv','a') as file_write:
            file_write.write(f"\n{str(student_name)},")

            total_marks = 0
            subject_list = ['English','Maths','Hindi','Sst','Science']

            for subject in subject_list:
                while True:
                    try:
                        marks = float(input(f"Inset the mark of {student_name} in subject {subject}: "))
                        if 0<=marks and max_marks>=marks:
                            break
                        else:
                            print(f"\tError: The marks must be between 0 and {max_marks}.")
                            playsound('Porgram_Data/Error.wav')
                    except ValueError:
                        print("\tError: The Insert Value must be a number.")
                        playsound('Porgram_Data/Error.wav')
                total_marks += marks
                file_write.write(str(f"{marks},"))

            a = max_marks*len(subject_list)
            percentage = (total_marks / a) * 100
            percentage = float('%.2f'% percentage)
            file_write.write(str(f"{total_marks}/{max_marks*len(subject_list)},"))
            file_write.write(str(f"{percentage}%,"))
            playsound('Porgram_Data/pop.wav')
            h +=1

        if percentage>=60:
            print(f"\t{student_name} got {percentage}% and passed with first divison.\n")
        elif percentage>=40:
            print(f"\t{student_name} got {percentage}% and passed with secound divison.\n")
        elif percentage>=33:
            print(f"\t{student_name} got {percentage}% and passed with third divison.\n")
        else:
            print(f"\t{student_name} got {percentage}% and {student_name} is fail\n")

# if not h ==0:
#     notification.notify(
#     title = "Percentage calculator",
#     message = f"A file {Class ,Class_section} save in Output folder",
#     app_icon = "Porgram_Data/icon.ico",
#     timeout = 3
# )