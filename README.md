# MedTrac
A command-line interface Medicine Prescription List Management using Python

[Video Demo](https://youtu.be/So1xMXIydfY)

---

## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the packages in `requirements.txt`
```
$ pip install -r requirements.txt
```
---

## Usage

You can layout your prescription in a table and set duration and date to monitor your medicine intake.

You can keep as many record as you like say per doctor (e.g Cardio, Pediatrics, Urologist, etc) or a list for yourselves and family.

Future development for this will be implemented on the web or mobile apps.
(For CS50W and CS50X Courses)

This may include other features like tracking your meds intake. Will alert you if you've missed a meds.

Even doctors can utilize this to write their prescriptions to their patients.


---


## Running the application
Use [python](https://www.python.org/) to run the application
```
$ python .\project.py
```

#### The following output will be displayed
```
.___  ___.  _______  _______  .___________..______          ___       ______
|   \/   | |   ____||       \ |           ||   _  \        /   \     /      |
|  \  /  | |  |__   |  .--.  |`---|  |----`|  |_)  |      /  ^  \   |  ,----'
|  |\/|  | |   __|  |  |  |  |    |  |     |      /      /  /_\  \  |  |
|  |  |  | |  |____ |  '--'  |    |  |     |  |\  \----./  _____  \ |  `----.
|__|  |__| |_______||_______/     |__|     | _| `._____/__/     \__\ \______|


 MENU
╭───────┬────────────────────╮
│  Key  │       Action       │
├───────┼────────────────────┤
│   S   │   Show CSV List    │
│   L   │   Load/View List   │
│   V   │  View Active List  │
│   U   │ Update Active List │
│  ***  │ ****************** │
│   C   │  Create New List   │
│   D   │   Duplicate File   │
│   R   │    Remove File     │
│   X   │        Exit        │
╰───────┴────────────────────╯
ACTIVE LIST: None
Select Key:
```
---
### S-key
Shows a list of currently saved files together with the main MENU is displayed (not shown here).
```
╭───────────────╮
│ CSV Files     │
├───────────────┤
│ baby.csv      │
│ doctor_c.csv  │
│ doctor_x.csv  │
│ doctor_y.csv  │
│ med1.csv      │
│ medtest.csv   │
│ optal.csv     │
│ to_delete.csv │
╰───────────────╯
```
---
### L-key
Load the list indicated and shows it.
```
Select Key: L
What's the list name?: baby.csv

baby.csv LOADED!!!
╭──────┬──────────────────────────────┬─────────────────────────┬───────────────┬──────────────┬────────────╮
│   ID │ Medicine                     │ Dosage                  │   Duration(d) │ Start Date   │ End Date   │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    1 │ Fludexil                     │ Given every 4 hours     │             7 │ 2023-10-19   │ 2023-10-26 │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    2 │ Tylenol Suspension 160mg/5mL │ Given every 4 hours     │             7 │ 2023-10-19   │ 2023-10-26 │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    3 │ Wexilimacin                  │ 2x a day every 12 hours │             7 │ 2023-10-19   │ 2023-10-26 │
╰──────┴──────────────────────────────┴─────────────────────────┴───────────────┴──────────────┴────────────╯
 MENU
╭───────┬────────────────────╮
│  Key  │       Action       │
├───────┼────────────────────┤
│   S   │   Show CSV List    │
│   L   │   Load/View List   │
│   V   │  View Active List  │
│   U   │ Update Active List │
│  ***  │ ****************** │
│   C   │  Create New List   │
│   D   │   Duplicate File   │
│   R   │    Remove File     │
│   X   │        Exit        │
╰───────┴────────────────────╯
ACTIVE LIST: baby.csv
Select Key:
```
---

### V-key
Note of the ACTIVE LIST showing. You can view (V-key), update (U-key) anytime. To change an active list, chose (L-key) to load a new list.


---

### U-key
Update gives you 3 options:
```
(A)ppend | (R)ow update | (D)elete a row?
```
Append adds new row to the active list.

Row update gives you option to chose the row to update. Also, comes with the default value and just press enter to preserve old values or enter new value.

"Duration" in days, "Start Date" change auto adjust with "End Date"

```
╭──────┬──────────────────────────────┬─────────────────────────┬───────────────┬──────────────┬────────────╮
│   ID │ Medicine                     │ Dosage                  │   Duration(d) │ Start Date   │ End Date   │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    1 │ Fludexil                     │ Given every 4 hours     │             7 │ 2023-10-19   │ 2023-10-26 │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    2 │ Tylenol Suspension 160mg/5mL │ Given every 4 hours     │             7 │ 2023-10-19   │ 2023-10-26 │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    3 │ Wexilimacin                  │ 2x a day every 12 hours │             7 │ 2023-10-19   │ 2023-10-26 │
╰──────┴──────────────────────────────┴─────────────────────────┴───────────────┴──────────────┴────────────╯
(A)ppend | (R)ow update | (D)elete a row? R
Which row(ID) you'd like to update? 3
Medicine: [Wexilimacin]:
Dosage:  [2x a day every 12 hours]: 
Duration (days)?:  [7]: 2
Start date:  [2023-10-20]: 
End date:  [2023-10-22]:

╭──────┬──────────────────────────────┬─────────────────────────┬───────────────┬──────────────┬────────────╮
│   ID │ Medicine                     │ Dosage                  │   Duration(d) │ Start Date   │ End Date   │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    1 │ Fludexil                     │ Given every 4 hours     │             7 │ 2023-10-19   │ 2023-10-26 │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    2 │ Tylenol Suspension 160mg/5mL │ Given every 4 hours     │             7 │ 2023-10-19   │ 2023-10-26 │
├──────┼──────────────────────────────┼─────────────────────────┼───────────────┼──────────────┼────────────┤
│    3 │ Wexilimacin                  │ 2x a day every 12 hours │             2 │ 2023-10-20   │ 2023-10-22 │
╰──────┴──────────────────────────────┴─────────────────────────┴───────────────┴──────────────┴────────────╯
```
#### Delete Row, deletes row you wish to delete
---
### C-key
Create key creates a file and give you parameters to enter a record. Same default values shows when you Update and Append to an existing file.
It will ask you if you wish to add more records.
```
File name without extension: medlist
Medicine: [Medicine Name]:
Dosage:  [Daily]:
Duration (days)?:  [7]: 30
Start date:  [2023-10-19]:
End date:  [2023-11-18]:
Enter new medicine? (Y/n):  [Y]: 
Medicine: [Medicine Name]: Medicol
Dosage:  [Daily]: 3x a day
Duration (days)?:  [7]: 1 
Start date:  [2023-10-19]: 
End date:  [2023-10-20]: 
Enter new medicine? (Y/n):  [Y]: n
```
The newly created file will be an ACTIVE LIST and gives you options to View and Update.
```
medlist.csv LOADED!!!

 MENU 
╭───────┬────────────────────╮
│  Key  │       Action       │
├───────┼────────────────────┤
│   S   │   Show CSV List    │
│   L   │   Load/View List   │
│   V   │  View Active List  │
│   U   │ Update Active List │
│  ***  │ ****************** │
│   C   │  Create New List   │
│   D   │   Duplicate File   │
│   R   │    Remove File     │
│   X   │        Exit        │
╰───────┴────────────────────╯
ACTIVE LIST: medlist.csv
Select Key: V

╭──────┬───────────────┬──────────┬───────────────┬──────────────┬────────────╮
│   ID │ Medicine      │ Dosage   │   Duration(d) │ Start Date   │ End Date   │
├──────┼───────────────┼──────────┼───────────────┼──────────────┼────────────┤
│    1 │ Medicine Name │ Daily    │            30 │ 2023-10-19   │ 2023-11-18 │
├──────┼───────────────┼──────────┼───────────────┼──────────────┼────────────┤
│    2 │ Medicol       │ 3x a day │             1 │ 2023-10-19   │ 2023-10-20 │
╰──────┴───────────────┴──────────┴───────────────┴──────────────┴────────────╯

```
---
### D-key
Duplicate file. Enter file to copy. If you wish the default name copy_<old_name> just press enter or enter a new name.

```
Select Key: D
CSV file to copy? optal.csv
New CSV filename?  [copy_optal.csv]: optal2.csv

New copy of optal.csv saved as optal2.csv
```
---
### R-key
Remove (delete) a file.
```
Select Key: R
CSV file to delete: optal2.csv

optal2.csv DELETED!!!
```
---
### X-key
Exit the program. Shows the MedTrac logo and a GOODBYE message.
```
.___  ___.  _______  _______  .___________..______          ___       ______ 
|   \/   | |   ____||       \ |           ||   _  \        /   \     /      |
|  \  /  | |  |__   |  .--.  |`---|  |----`|  |_)  |      /  ^  \   |  ,----'
|  |\/|  | |   __|  |  |  |  |    |  |     |      /      /  /_\  \  |  |     
|  |  |  | |  |____ |  '--'  |    |  |     |  |\  \----./  _____  \ |  `----.
|__|  |__| |_______||_______/     |__|     | _| `._____/__/     \__\ \______|


GOODBYE!!!
