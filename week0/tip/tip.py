# This program aims to calculate how many dollars to leave as a tip
# Given the price of the meal and the percentage of it the customer wants to leave
# Assumes that the user will input values in expected formats
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = float(d.replace('$',''))
    return dollars

def percent_to_float(p):
    percent = float(p.replace('%',''))
    percent = percent / 100
    return percent

if __name__ == '__main__':
    main()
