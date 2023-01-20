![Percentage Calculate](https://user-images.githubusercontent.com/84720825/213391657-b3ca1797-37be-4562-bddf-748ac8a72ec1.png)

### The function Percentage calculator asks the user for their marks in 5 subjects, calculate the percentage, and prints the result and provide the result in a *Excel* file.
----
* Inside the function, we first initialize two variables: `total_marks` and `marks.` `Total_marks` represents the total number of marks that can be obtained for the 5 subjects, and `marks` represents the number of marks the user has obtained. We set `total_marks` to 0 and `marks` to 0 at the beginning, since no marks have been obtained yet.

* Next, the program uses a for loop to iterate over the 5 subjects. For each subject, the user is prompted to enter their marks using the `input` function. The program then converts the user's `input` to an integer using the `int` function, since the `input` function returns a string.

```python
total_marks = 0
subject_list = ['English','Maths','Hindi','Sst','Science']

for subject in subject_list:
>>> marks = float(input(f"Inset the mark of {student_name} in subject {subject}: "))
>>> total_marks +=1
>>> file_write.write(str(f"{marks},"))

# open Main.py to know more
```

* After the marks have been obtained, the program adds 100 to the `total_marks` (since each subject is worth 100 marks) and adds the user's marks to `marks`. This allows us to keep track of the total number of marks available and the number of marks the user has obtained.

* After the for loop finishes, the program calculates the percentage by dividing `marks` by `total_marks` and multiplying the result by 100. This gives us the user's percentage as a decimal.

* Finally, the program prints the percentage to the user using the `print` function and the `f` string format. The `f` string allows us to embed the value of the `percentage` variable directly into the string, so that the user can see their percentage.

## :package: **Installation instructions**
### The easiest way to use this Percentage calculator:
1. Click [**here**](https://github.com/pritam12426/Percentage-Calculator/releases) to download the `Package.zip` file
2. Unzip the `Package.zip` file
3. After that open `Percantage_Calculater` folder
4. Run this **`.exe`** file of`Percantage_Calculater` at last of that foler
5. Start Inserting the data as per given ***instruction***
6. At last you will get `Percentage_Output.csv` in output file and it will look like this in Excel 👇
![CHOTI-DHNNO_Visual-Studio-Code_2023_01_20_9](https://user-images.githubusercontent.com/84720825/213683162-4b5cf19f-434a-44cd-bd72-767ac8b6c36d.png)* If you wants to save the program Inset `exit` while Inset the name of student.

## :traffic_light: **Known issues**
- [x] You have to use terminal to run this program.
- [ ] Currently **`GUI`** **(Graphical user interface)** is not Ceated for this project.

## Feedback
If you have any feedback, please reach out to us at [here](https://github.com/pritam12426/Percentage-Calculator/issues/new)