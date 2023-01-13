![temporary](https://user-images.githubusercontent.com/84720825/212024726-9a0f0c47-597c-4683-bc81-880949263eb2.png)

### The function Percentage calculator asks the user for their marks in 5 subjects, calculate the percentage, and prints the result and provide the result in a *Percentage_output.csv* file.
----
* Inside the function, we first initialize two variables: `total_marks` and `marks.` `Total_marks` represents the total number of marks that can be obtained for the 5 subjects, and `marks` represents the number of marks the user has obtained. We set `total_marks` to 0 and `marks` to 0 at the beginning, since no marks have been obtained yet.

* Next, the program uses a for loop to iterate over the 5 subjects. For each subject, the user is prompted to enter their marks using the `input` function. The program then converts the user's `input` to an integer using the `int` function, since the `input` function returns a string.

```python
total_marks = 0
subject_list = ['English','Maths','Hindi','Sst','Science']

for subject in subject_list:
    marks = float(input(f"Inset the mark of {student_name} in subject {subject}: "))
    total_marks +=1
    file_write.write(str(f"{marks},"))
```

* After the marks have been obtained, the program adds 100 to the `total_marks` (since each subject is worth 100 marks) and adds the user's marks to `marks`. This allows us to keep track of the total number of marks available and the number of marks the user has obtained.

* After the for loop finishes, the program calculates the percentage by dividing `marks` by `total_marks` and multiplying the result by 100. This gives us the user's percentage as a decimal.

* Finally, the program prints the percentage to the user using the `print` function and the `f` string format. The `f` string allows us to embed the value of the `percentage` variable directly into the string, so that the user can see their percentage.

## Installation instructions
### The easiest way to use this Percentage calculator:
1. Click [here](https://github.com/pritam12426/Percentage-Calculator/releases) to download Percantage Calculater
2. Eextract the `Percentege.zip` file
3. After that open `Percantage_Calculater` folder

![CHOTI-DHNNO_2023_01_12_75](https://user-images.githubusercontent.com/84720825/211976108-d58549a6-6550-459c-9987-d75d770d1500.png)

4. Run this **`.exe`** file of `Percantage_Calculater` folder  
5. Start Inserting the data as per given ***instruction***
6. At last you will get `Percentage_Output.csv` just behind of that `.exe` and look like this in Excel 👇

![CHOTI-DHNNO_2023_01_12_71](https://user-images.githubusercontent.com/84720825/212041632-814f0704-3797-4f66-b458-226e1c65bf9f.png)

## Known issues ❗
- [x] You have to use terminal to run this program.
- [ ] Currently **`GUI`** **(Graphical user interface)** is not Ceated for this project.
<!-- ## Need help 
### Can some one help me to Ceate the gui for this program -->