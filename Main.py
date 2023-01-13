from playsound import playsound

mylist = ['Name','English','Maths','Hindi','Sst','Science','Total Marks','Percentage']

with open('Percentage_Output.csv', 'w') as f:
    for hedder in mylist:
        f.write(str(hedder))
        if hedder != 'Percentage':
            f.write(str(','))

while True:
    student_name = input("Insert the name of sudent or enter exit to close: ")
    student_name = student_name.lower().capitalize()
    if student_name.find("Exit") == 0:
        break
    else:
        with open('Percentage_Output.csv','a') as file_write:
            file_write.write(f"\n{str(student_name)},")

            total_marks = 0
            subject_list = ['English','Maths','Hindi','Sst','Science']

            for subject in subject_list:
                while True:
                    try:
                        marks = float(input(f"Inset the mark of {student_name} in subject {subject}: "))
                        if 0<=marks and 100>=marks:
                            break
                        else:
                            print("\tError: The marks must be between 0 and 100.")
                            playsound('Porgram_Data/Error.wav')
                    except ValueError:
                        print("\tError: The Insert Value must be a number.")
                        playsound('Porgram_Data/Error.wav')
                total_marks += marks
                file_write.write(str(f"{marks},"))
            percentage = (total_marks / 500) * 100
            file_write.write(str(f"{total_marks}/500,"))
            file_write.write(str(f"{'%.2f'% percentage}%"))

        if percentage>=60:
            print(f"\t{student_name} got {'%.2f'% percentage}% and passed with first divison.\n")
        elif percentage>=40:
            print(f"\t{student_name} got {'%.2f'% percentage}% and passed with secound divison.\n")
        elif percentage>=33:
            print(f"\t{student_name} got {'%.2f'% percentage}% and passed with third divison.\n")
        else:
            print(f"\t{student_name} got {'%.2f'% percentage}% and {student_name} is fail\n")