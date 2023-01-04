from playsound import playsound

while True:
    student_name = input("Insert the name of sudent: ")
    student_name = student_name.lower()
    student_name = student_name.capitalize()

    with open('Percatage_output.txt','a') as file_write:
        with open('Percatage_output.txt') as file_read:
            read = file_read.read()
            if len(str(read))!=0:
                file_write.write("\n")
        file_write.write(f"{str(student_name)}\n")

        total_marks = 0
        subject_list = ['Maths','Hindi','English','Sst','Science']

        for subject in subject_list:
            while True:
                try:
                    marks = float(input(f"Inset the mark of {student_name} in subject {subject}: "))
                    if 0<=marks and 100>=marks: # Enter a number that is geater then 0 and smaller 100 then this sentex will break the while loop 
                        break
                    else:
                        print("\tError: The marks must be between 0 and 100.")
                        playsound('Contents/Error.wav')
                except ValueError:
                    print("\tError: The Insert Value must be a number.the")
                    playsound('Contents/Error.wav')
            total_marks += marks
            file_write.write(str(f"  {subject}_{marks}\n"))
        percentage = (total_marks / 500) * 100
        file_write.write(str(f"{student_name} got {'%.2f'% percentage}%\n"))

    if percentage>=60:
        print(f"\t{student_name} got {'%.2f'% percentage}% and passed with first divison.\n")
    elif percentage>=40:
        print(f"\t{student_name} got {'%.2f'% percentage}% and passed with secound divison.\n")
    elif percentage>=33:
        print(f"\t{student_name} got {'%.2f'% percentage}% and passed with third divison.\n")
    else:
        print(f"\t{student_name} got {'%.2f'% percentage}% and {student_name} is fail\n")