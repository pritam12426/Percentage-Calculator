# Percentage-calculator

### The function Percentage calculator asks the user for their marks in 5 subjects, calculate the percentage, and prints the result and provide the result in a *Percentage_output.csv* file.
----
* Inside the function, we first initialize two variables: `total_marks` and `marks.` `Total_marks` represents the total number of marks that can be obtained for the 5 subjects, and `marks` represents the number of marks the user has obtained. We set `total_marks` to 0 and `marks` to 0 at the beginning, since no marks have been obtained yet.

* Next, the program uses a for loop to iterate over the 5 subjects. For each subject, the user is prompted to enter their marks using the `input` function. The program then converts the user's `input` to an integer using the `int` function, since the `input` function returns a string.

```python
total_marks = 0
subject_list = ['English','Maths','Hindi','Sst','Science']

for subject in subject_list:
    marks = float(input(f"Inset the mark of {student_name} in subject {subject}: "))
    total_marks = total_marks + marks
    file_write.write(str(f"{marks},"))
```

* After the marks have been obtained, the program adds 100 to the `total_marks` (since each subject is worth 100 marks) and adds the user's marks to `marks`. This allows us to keep track of the total number of marks available and the number of marks the user has obtained.

* After the for loop finishes, the program calculates the percentage by dividing `marks` by `total_marks` and multiplying the result by 100. This gives us the user's percentage as a decimal.

* Finally, the program prints the percentage to the user using the `print` function and the `f` string format. The `f` string allows us to embed the value of the `percentage` variable directly into the string, so that the user can see their percentage.

## This is the output example of *Percentage_output.csv*
![CHOTI-DHNNO_EXCEL_2023_01_11_70](https://user-images.githubusercontent.com/84720825/211838001-d27f2a20-c98d-43c9-87a2-1ef6c53d2e37.png)

## Installation instructions
### The easiest way to use this Percentage calculator:
1. Click [here](https://github.com/pritam12426/Percentage-Calculator/releases) to download the last portable version
2. Eextract the `Percentege.zip`
3. After that open Percentege
![CHOTI-DHNNO_2023_01_12_75](https://user-images.githubusercontent.com/84720825/211976108-d58549a6-6550-459c-9987-d75d770d1500.png)
4. Run this **`.exe`** file of that folder  
5. then you will see this screen
![CHOTI-DHNNO_2023_01_12_69](https://user-images.githubusercontent.com/84720825/211970030-f0f68caa-152b-4cbe-8414-9e3b28fc1795.png)
6. Start Inserting the data as per given ***instruction***
7. And you are good to go

## Known issues
- [x] You have to use terminal to run this program.
- [ ] Currently **`GUI`** **(Graphical user interface)** is not Ceated for this project.