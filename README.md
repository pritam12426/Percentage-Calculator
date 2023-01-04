# PERCENTAGE CALCULATOR :heavy_division_sign:

### The function Percentage calculator asks the user for their marks in 5 subjects, calculate the percentage, and prints the result and provide the result in a Percentage_output.txt file.

* Inside the function, we first initialize two variables: `total_marks` and `obtained_marks.` `Total_marks` represents the total number of marks that can be obtained for the 5 subjects, and `obtained_marks` represents the number of marks the user has obtained. We set `total_marks` to 0 and `obtained_marks` to 0 at the beginning, since no marks have been obtained yet.

* Next, the program uses a for loop to iterate over the 5 subjects. For each subject, the user is prompted to enter their marks using the `input` function. The program then converts the user's `input` to an integer using the `int` function, since the `input` function returns a string.

```python
total_marks = 0
subject_list = ['Maths','Hindi','English','Sst','Science']

for subject in subject_list:
    marks = float(input(f"Inset the mark of {student_name} in subject {subject}: "))
    total_marks total_marks + mark
    file_write.write(str(f"  {subject}_{marks}\n"))
```

* After the marks have been obtained, the program adds 100 to the `total_marks` (since each subject is worth 100 marks) and adds the user's marks to `obtained_marks`. This allows us to keep track of the total number of marks available and the number of marks the user has obtained.

* After the for loop finishes, the program calculates the percentage by dividing `obtained_marks` by `total_marks` and multiplying the result by 100. This gives us the user's percentage as a decimal.

* Finally, the program prints the percentage to the user using the `print` function and the `f` string format. The `f` string allows us to embed the value of the `percentage` variable directly into the string, so that the user can see their percentage.

## THIS IS THE OUTPUT EXAMPLE OF *Percentage_output.txt*
![Percentage_output.txt](https://user-images.githubusercontent.com/84720825/210390900-c4122141-ba8a-4984-80d6-970e62b26e80.png)

## INSTALLATION INSTRUCTIONS
### The easiest way to install this Percentage calculator:
1. Install [`Python compiler`](https://www.python.org/downloads/) :snake: on your local machine.
2. Clone this project or download this repo.
3. Delete all content of `Percentage_output.txt.`
4. Fire :fire: or run this command in bash to install a `External module` called [`Play sound.`](https://pypi.org/project/playsound/)
```bash
pip install playsound
``` 
3. And you are good to go

## KNOWN ISSUES
- [x] You have to use terminal to run this program.
- [ ] Currently not any *`GUI,`* **(Graphical user interface)** is Ceated for this project.