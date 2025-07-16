def input_validation():
    while True:
        try:
            # Input tanggal
            while True:
                date = int(
                    input("Please enter the day in which you were born (1-31): ")
                )
                if 1 <= date <= 31:
                    break
                print(
                    "If there's a date beyond 31, we might have just entered the multiverse calendar!"
                )

            # Input bulan
            while True:
                month = int(
                    input("Please enter the month in which you were born (1-12): ")
                )
                if 1 <= month <= 12:
                    break
                print(
                    "Hmm, I don't think that month exists in our calendar system. Try entering the correct one!"
                )

            # Input tahun
            while True:
                year = int(input("Please enter the year in which you were born: "))
                if year >= 1:
                    break
                print("Dude, seriously? That year isn't from our dimension, try again!")

            return date, month, year
        except ValueError:
            print(
                "Whoa, this system is allergic to letters! Just put in numbers so it doesn't crash!"
            )


print(
    "Welcome to my very first project—let's make it epic!\nDrop a date, and I'll guess your birthday and whether it was a leap year!"
)
date, month, year = input_validation()
print(f"input valid : {date}/{month}/{year}")


print(
    "\nHere's the list of leap years in a given range, so you don't get lost planning ur jumps!"
)
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
