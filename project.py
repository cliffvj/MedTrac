import os
import csv
import click 
import pandas as pd 
from tabulate import tabulate 
from termcolor import cprint 
from pyfiglet import figlet_format 
from datetime import datetime, timedelta 


def main():
    clearscreen()
    star("MedTrac")

    db = None
    mainloop = True

    while mainloop:
        action = get_input(db)

        if action == "S":
            clearscreen()
            allfiles = os.listdir(".")
            csv_files = list(filter(lambda f: f.endswith(".csv"), allfiles))
            print(tabulate([[i] for i in csv_files], headers=["CSV Files"], 
                        tablefmt="rounded_outline"))
        
        elif action == "L":
            try:
                db_name = input("What's the list name?: ").strip()
                db = get_database(db_name)
                clearscreen()
                alert(f"{db} LOADED!!!")
                med_list(db)
            except Exception:
                alert("CSV file not found")

        elif action == "V":
            try:
                clearscreen()
                med_list(db)
            except Exception:
                clearscreen()
                alert("NO FILE LOADED. Try Loading a file or create one.\n")
                
        elif action == "U":
            try:
                clearscreen()
                db = update_list(db)
                clearscreen()
                alert(f"{db} UPDATED!!!\n")
                med_list(db)
            except Exception:
                clearscreen()
                alert("NO FILE LOADED. Try Loading a file or create one.\n")

        elif action == "C":
            clearscreen()
            db = create_file()
            alert(f"{db} LOADED!!!\n")

        elif action == "D":
            # clearscreen()
            try:
                old_csv_name = input("CSV file to copy? ").strip()
                new_csv_name = click.prompt("New CSV filename? ", default=f"copy_{str(old_csv_name)}")
                dup_file(old_csv_name, new_csv_name)
                clearscreen()
                alert(f"New copy of {old_csv_name} saved as {new_csv_name}")
            except FileNotFoundError:
                clearscreen()
                alert("File not found.\n")

        elif action == "R":
            try:
                # clearscreen()
                del_csv = input("CSV file to delete: ").strip()
                del_file(del_csv)
                clearscreen()
                alert(f"{del_csv} DELETED!!!\n")
                if db == del_csv:
                    db = None
            except FileNotFoundError:
                clearscreen()
                alert("File not found.\n")

        else:
            clearscreen()
            star("Medtrac")
            alert("GOODBYE!!!\n")
            mainloop = False


def get_input(db):
    commands = [{"Key": " S ", "Action": "Show CSV List"},
                {"Key": " L ", "Action": "Load/View List"},
                {"Key": " V ", "Action": "View Active List"},
                {"Key": " U ", "Action": "Update Active List"},
                {"Key": "***", "Action": "******************"},
                {"Key": " C ", "Action": "Create New List"},
                {"Key": " D ", "Action": "Duplicate File"},
                {"Key": " R ", "Action": "Remove File"},
                {"Key": " X ", "Action": "Exit"}]


    while True:
        print(" MENU ")
        print(tabulate(commands, headers="keys", tablefmt="rounded_outline",stralign="center"))
        alert(f"ACTIVE LIST: {db}")

        action = input("Select Key: ").upper()

        if action in ["S", "L", "V", "U", "C", "D", "R", "X"]:
            return action
        else:
            clearscreen()
            alert("INVALED KEY, Try again.")


def alert(message):
    return cprint(message, 'yellow', attrs=['bold','blink'])


def star(message):
    return cprint(figlet_format(message, font='starwars'),
                  'blue', attrs=['bold','blink'])

def clearscreen():
    print("\033[H\033[J")


def get_database(db):
    if os.path.exists(db):
        return db
    else:
        return "NO FILE"


def dv_entry():
    """
    Future feature to change default data entry
    """


def row_data(default_value):
    dv = default_value
    medicine = click.prompt("Medicine:", default=dv[0]).strip()
    dosage = click.prompt("Dosage: ", default=dv[1]).strip()
    duration = int(click.prompt("Duration (days)?: ", default=dv[2]).strip())
    while True:
        try:
            if duration != dv[2]:
                start_date = click.prompt("Start date: ", default=dv[3]).strip()
                if start_date != dv[3]:
                    end_date = click.prompt("End date: ", default=new_end_date(start_date,duration)).strip()
                else:
                    end_date = click.prompt("End date: ", default=new_row_dv(duration)[4]).strip()
            else:
                end_date = click.prompt("End date: ", default=dv[4]).strip()
            
            row = [medicine, dosage, duration, start_date, end_date]
            return row
        except ValueError:
            print("Invalid entry")


def new_end_date(date_start_str, n):
    date_format = "%Y-%m-%d"
    date_start = datetime.strptime(date_start_str, date_format).date()
    date_ndays = date_start + timedelta(days=n)
    return f"{date_ndays}"


def new_row_dv(n):
    date_now = datetime.now().date()
    date_ndays = date_now + timedelta(days=n)
    date_now = f'{date_now}'
    date_ndays = f'{date_ndays}'
    default_value = ['Medicine Name', 'Daily', str(n), date_now, date_ndays]    
    return default_value


def create_file():
    db_name = str(input("File name without extension: ").strip()+".csv")
    if not(os.path.exists(db_name)):
        answer = True
        with open(db_name, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=['medicine', 
                'dosage', 'duration', 'start_date', 'end_date'], lineterminator="\n")
            writer.writeheader()
            while answer:
                dv = new_row_dv(n=7)
                row = row_data(dv)
                writer.writerow({"medicine":row[0], "dosage":row[1], 
                    "duration":row[2], "start_date":row[3], "end_date":row[4]})
                if answer := click.prompt("Enter new medicine? (Y/n): ", default="Y").upper() == "N":
                    answer = False
                else:
                    answer = True
            return db_name
    else:
        alert("FILE ALREADY EXIST")


def med_list(db):
    df = pd.read_csv(db)
    df.index += 1 # index starts at 1
    print(tabulate(df, headers=["ID", "Medicine","Dosage","Duration(d)", 
                                "Start Date", "End Date"], tablefmt="rounded_grid"))


def update_list(db):
        med_list(db)
        
        update = input("(A)ppend | (R)ow update | (D)elete a row? ").strip().upper()
        if update == "A":
            # row_id = len(pd.read_csv(db)) - 1
            with open(db, "a") as writefile:
                dv = new_row_dv(n=7)
                row = row_data(dv)
                writer = csv.writer(writefile,lineterminator="\n")
                writer.writerow(row)

        elif update == "R":
            row_id = int(input("Which row(ID) you'd like to update? ").strip())

            with open(db, "r") as readfile:
                reader = csv.reader(readfile)
                lines = list(reader)
                default_value = lines[row_id]
                lines[row_id] = row_data(default_value)

                with open(db, "w") as writefile:
                    writer = csv.writer(writefile, lineterminator="\n")
                    writer.writerows(lines)

        elif update == "D":
            row_id = int(input("Which row(ID) you'd like to delete? ").strip())
            df = pd.read_csv(db)
            df = df.drop(df.index[row_id-1])
            df.to_csv(db, index=False)
        
        return db


def dup_file(old_name, new_name):
    df = pd.read_csv(old_name)
    df.to_csv(new_name, index=False)
    

def del_file(db):
    os.remove(db)


if __name__ == "__main__":
    main()
