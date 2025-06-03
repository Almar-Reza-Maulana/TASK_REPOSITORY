# Birthday and Leap Year Calculator
Yo, what’s up! Welcome to my chill project that’s all about celebrating your birth date in style. This script is not your average calculator—it validates your birthday input, checks out leap years, and even drops the day of the week you were born on, all served with a fun twist.
## What's inside ? 🔎

- Input Validation:
  This bad boy prompts you to enter your day, month, and year of birth. It makes sure your numbers are on point—if you mess up, you'll get a quirky reminder to try again.
- Leap Year Lowdown:
  Wanna know if a year is special? The script loops through a few years around your birth year and lets you know which ones are leap years. It’s all about that rule: divisible by 4, except if it's a century not divisible by 400.
- Day of the Week Magic:
  Using some slick math with Zeller's Congruence, the program figures out the day of the week you made your debut.
- Final Output:
  At the end, this script will print your validated birth date, complete with leap year info and the day-of-the-week result. Bam!
## How it Rolls 👨‍💻
1. input Time : \
You get asked for your birth details—day (1-31), month (1-12), and the year. Numbers only !
2. Leap Year Check : \
The script rides through a range of years (a couple before and after your input year) to drop the lowdown on which ones are leap years. Perfect if you're into those time-travel vibes!
3. Crunching the Day: \
Zeller's Congruence does its magic by adjusting and calculating the right day numbers. In the end, you’ll know if you were born on a Monday, Tuesday, or any other day.
4. Final Drop: \
It spits out your validated birth date along with the leap year deets and the day-of-the-week result. Boom!
## How to run 🏃‍♂️
1. Open Visual Studio Code:\
Launch VS Code on your computer.
2. Create a New Python File:\
Create a new file (for example, name it zeller_congruence.py) and copy-paste all of your Python code into this file.
4. Save the File:\
Save the file (using Ctrl + S or File > Save).
5. Run the File in the Terminal:\
- Open the integrated terminal in VS Code by going to View > Terminal or by using the shortcut (Ctrl +  `).
- Make sure the terminal is in the same folder as your Python file.
- Type the following command and press Enter:

```python
def input_validation():
    while True:
        try:
            # Input tanggal
            while True:
                date = int( input("Please enter the day in which you were born (1-31): "))
                if 1 <= date <= 31:
                    break
                print("If there's a date beyond 31, we might have just entered the multiverse calendar!")

            # Input bulan
            while True:
                month = int(input("Please enter the month in which you were born (1-12): "))
                if 1 <= month <= 12:
                    break
                print("Hmm, I don't think that month exists in our calendar system. Try entering the correct one!")

            # Input tahun
            while True:
                year = int(input("Please enter the year in which you were born: "))
                if year >= 1:
                    break
                print("Dude, seriously? That year isn't from our dimension, try again!")

            return date, month, year
        except ValueError:
            print("Whoa, this system is allergic to letters! Just put in numbers so it doesn't crash!")

print("Welcome to my very first project—let's make it epic!\nDrop a date, and I'll guess your birthday and whether it was a leap year!")
date, month, year = input_validation()
print(f"input valid : {date}/{month}/{year}")

print("\nHere's the list of leap years in a given range, so you don't get lost planning ur jumps!")
for i in range(year - 2, year + 3):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(f" {i} is a leap year!")
    else:
        print(f"{i} isn't a leap year!")

if month == 1 or month == 2:
    month += 12
    year -= 1
K = year % 100
J = year // 100
h = (date + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7
print("\n Here is the result:")
if h == 0:
    print(f"On {date}/{month}/{year} you were definitely born on a Saturday!")
elif h == 1:
    print(f"On {date}/{month}/{year} you were definitely born on a Sunday!")
elif h == 2:
    print(f"On {date}/{month}/{year} you were definitely born on a monday!")
elif h == 3:
    print(f"On {date}/{month}/{year} you were definitely born on a tuesday!")
elif h == 4:
    print(f"On {date}/{month}/{year} you were definitely born on a wednesday!")
elif h == 5:
    print(f"On {date}/{month}/{year} you were definitely born on a thursday!")
else:
    print(f"On {date}/{month}/{year} you were definitely born on a friday!")
```
P.S. Feel free to clone, star, and contribute if you’re feeling this vibe. This project isn’t just about numbers—it’s about bringing a little fun and flair to coding. Drop me a line if you have ideas or wanna collab. Peace out and happy coding!





