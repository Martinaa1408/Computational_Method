'''Write a python program that takes two filenames from the command
line. It reads from the first file, which contains dates in the format
dd/mm/yyyy (one per line), and for each date in the first file, it
writes on the second file the number of days after 01/01/2000, or
Error in case the format is not correct. Assume all the years have 365
days (i.e., assume there are no leap years).

YOU CANNOT USE LIBRARY FUNCTIONS FOR DATE ELABORATION (e.g., from
datetime, calendar, time or dateutil libraries).

Ex.

Input file:          Output file:

01/01/2000      0
02/01/2000      1
31/12/2000      364
01/01/2001      365
15/06/2025      9288
32/01/2000      Error
1/2/2001        Error
12-03-2005      Error
01/01/1999      Error
0A/01/2001      Error '''


def read_filename(filename):
    dates = []
    try:
        with open(filename) as reader:
            for line in reader:
                line = line.rstrip()
                dates.append(line)
    except FileNotFoundError:
        print('warning')
        exit()
    print(dates)
    return dates


def compute(dates):
    year_ref = 2000
    days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # list of months days
    day_ref = 1

    results = []

    for parts in dates:
        parts = parts.strip()

        # controllo formato base con split
        pieces = parts.split('/')
        if len(pieces) != 3:
            results.append('Error')
            continue

        day_str = pieces[0]
        month_str = pieces[1]
        year_str = pieces[2]

        # formato esatto dd/mm/yyyy
        if len(day_str) != 2 or len(month_str) != 2 or len(year_str) != 4:
            results.append('Error')
            continue

        # devono essere solo cifre
        if not day_str.isdigit() or not month_str.isdigit() or not year_str.isdigit():
            results.append('Error')
            continue

        day = int(day_str)
        month = int(month_str)
        year = int(year_str)

        # anno minimo
        if year < year_ref:
            results.append('Error')
            continue

        # mese valido
        if month < 1 or month > 12:
            results.append('Error')
            continue

        # giorno valido rispetto al mese
        if day < 1 or day > days_in_year[month - 1]:
            results.append('Error')
            continue

        # calcolo giorni dopo 01/01/2000 (no leap years)
        result = ((year - year_ref) * 365) + sum(days_in_year[:month - 1]) + (day - day_ref)
        results.append(result)

    return results


def write_file(filename, results):
    try:
        with open(filename, 'w') as writer:
            for r in results:
                writer.write(str(r) + '\n')
    except FileNotFoundError:
        print('warning')
        exit()


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 3:
        print('usage python3 script.py input.txt output.txt')
        exit()
    dates = read_filename(argv[1])
    results = compute(dates)
    write_file(argv[2], results)
