# Author: Michael Sheridan
# QAP 4

import datetime

while True:

    default_file = open('OSICDef.dat', 'r')
    default_file.read()

    province_list = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

    policy_num = 1944

    curr_date = datetime.datetime.today()
    if curr_date.month == 12:
        pay_date = datetime.date(curr_date.year + 1, 1, 1)
    else:
        pay_date = datetime.date(curr_date.year, curr_date.month + 1, 1)
    invoice_date = curr_date.strftime("%x")
    pay_date = pay_date.strftime("%x")

    # First name
    while True:
        first_name = str(input("Enter the customer's first name: ")).title()
        if first_name == "":
            print("Name can't be blank - please reenter.")
        elif not first_name.isalpha():
            print("Name must only include alphabetic characters - please reenter.")
        else:
            break

    # Last name
    while True:
        last_name = str(input("Enter the customer's last name: ")).title()
        if last_name == "":
            print("Name can't be blank - please reenter.")
        elif not last_name.isalpha():
            print("Name must only include alphabetic characters - please reenter.")
        else:
            break

    fullName = first_name + " " + last_name
    if len(fullName) < 20:
        fullName += " " * (20 - len(fullName))
    
    # Address
    while True:
        address = str(input("Enter the customer's residental address: ")).title()
        if address == "":
            print("Address can't be blank - please reenter.")
        else:
            break
    if len(address) < 20:
        address += " " * (20 - len(address))
    # City
    while True:
        city = str(input("Enter the customer's residental city: ")).title()
        if city == "":
            print("City can't be blank - please reenter.")
        elif not city.isalpha():
            print("City must be all alphabetical characters - please reenter.")
        else:
            break

    # Province
    while True:
        province = str(input("Enter the customer's residential province: ")).upper()
        if province not in province_list:
            print("Please enter valid Canadian province (NL, NS, ON, etc.).")
        else:
            break

    # Postal Code
    while True:
        postal = str(input("Enter the customer's residential postal code: ")).upper()
        postal = postal.replace(" ", "")
        if postal == "":
            print("Postal code can't be blank - please reenter.")
        elif len(postal) != 6:
            print("Postal code must be 6 characters - please reenter.")     
        else:
            break

    # Full CPP
    fullCPP = city + ", " + province + " " + postal
    if len(fullCPP) < 30:
        fullCPP += " " * (30 - len(fullCPP))
    # Phone number
    while True:
        phone_num = str(input("Enter the customer's phone number: "))
        phone_num = phone_num.replace(" ", "")
        phone_num = phone_num.replace("(", "")
        phone_num = phone_num.replace(")", "")
        phone_num = phone_num.replace("-", "")
        if phone_num == "":
            print("Phone number can't be blank - please reenter.")
        elif not phone_num.isdigit():
            print("Phone number must only contain numeric characters - please reenter.")
        elif len(phone_num) != 10:
            print("Phone number must be 10 characters - please reenter.")
        else:
            phone_num = "(" + phone_num[0:3] + ") " + phone_num[3:6] + "-" + phone_num[6:]
            phone_num += " " * (20 - len(phone_num))
            break


    # Number of cars 
    while True:
        insured_car = (input("Enter the number of customer's insured cars: "))
        if insured_car == "":
            print("Value can't be blank - please reenter.")
        elif not insured_car.isdigit():
            print("Value must be a valid number - please reenter.")
        else: 
            break

    # Xtra Liability
    while True:
        xtra_liab = str(input("Would the customer like to opt in for extra liability for up to $1,000,000 (Y/N)? ")).upper()
        if xtra_liab == "":
            print("Value can't be blank - please reenter.")
        elif xtra_liab == "Y":
            break
        elif xtra_liab == "N":
            break
        else:
            print("Entered value not valid - please reenter.")

    # Glass coverage
    while True:
        glass_cov = str(input("Would the customer like to opt in for the glass coverage option (Y/N)? ")).upper()
        if glass_cov == "":
            print("Value can't be blank - please reenter.")
        elif glass_cov == "Y":
            break
        elif glass_cov == "N":
            break
        else:
            print("Entered value not valid - please reenter.")

    # Loaner car
    while True:
        loaner = str(input("Would the customer be needing a loaner vehicle (Y/N)? ")).upper()
        if loaner == "":
            print("Value can't be blank - please reenter.")
        elif loaner == "Y":
            break
        elif loaner == "N":
            break
        else:
            print("Entered value not valid - please reenter.")

    # Amount of loaner car
    while True:
        loaner_num = str(input("Enter the amount of loaner cars needed for customer: "))
        if loaner_num == "":
            print("Value can't be blank - please reenter.")
        elif not loaner_num.isdigit():
            print("Value must be numerical characters - please reenter.")
        else:
            break



    # Insurance premium calc
    i_premium = 869.00
    if int(insured_car) > 1:
        i_premium = i_premium + (i_premium*.75) * (int(insured_car) - 1)

    if xtra_liab == "Y":
        liab_cost = 130.00 * int(insured_car)
        bool_liab = "Yes"
    else:
        liab_cost = 0
        bool_liab = "No"

    if glass_cov == "Y":
        glass_cost = 86.00 * int(insured_car)
        bool_glass = "Yes"
    else:
        glass_cost = 0
        bool_glass = "No"

    if loaner == "Y":
        loaner_cost = 58.00 * int(loaner_num)
        bool_loaner = "Yes"
    else:
        loaner_cost = 0
        bool_loaner = "No"

    # Total extra cost
    total_xtra = liab_cost + glass_cost + loaner_cost

    # Total insurance premium
    total_insure = i_premium + total_xtra

    # HST
    tax = total_insure * .15

    # Total cost
    total_cost = total_insure + tax

    # Payment option
    while True:
        pay_option = str(input("Would the customer like to pay in full or monthly (F/M)? ")).upper()
        if pay_option == "":
            print("Value can't be blank - please reenter.")
        elif pay_option == "F":
            strPay = "Full"
            month_pay = 0
            break
        elif pay_option == "M":
            strPay = "Monthly"
            process_fee = 39.99
            month_pay = (process_fee + total_cost) / 8
            break
        else:
            print("Entered value not valid - please reenter.")

    # Reciept print
    print()
    print(f'One Stop Insurance Company {" "*18} Invoice Date:   {invoice_date}')
    print(f'Insurance Summary and Receipt {" "*15} Policy No:          {policy_num}')
    print("")
    print(f'Customer information: {(" " * 31)} No. of cars = {insured_car:>2}')
    print(f'{(" " * 49)} Extra Liability? {bool_liab:>3}')
    print(f'{fullName} {(" " * 28)} Glass Coverage? {bool_glass:>4}')
    print(f'{address} {(" " * 28)} Loaner vehicle? {bool_loaner:>4}')
    print(f'{fullCPP} {(" " * 15)} No. of loaner cars = {loaner_num:>2}')
    print(f'{phone_num} {(" " * 15)} Full or Monthly Payments? {strPay:>7}')
    print()
    print("=" * 70)
    print()
    print(f'Insurance premium: {"${:,.2f}".format(i_premium):>12s}   Total Extra Cost: {"${:,.2f}" .format(total_xtra):>18}')
    print(f'Extra Liability: {"${:,.2f}".format(liab_cost):>14s}   Total Insurance Premium: {"${:,.2f}".format(total_insure):>11}')
    print(f'Glass Coverage: {"${:,.2f}".format(glass_cost):>15s}   HST: {"${:,.2f}" .format(total_xtra):>31}')
    print(f'Loaner Cost: {"${:,.2f}".format(loaner_cost):>18s}   Total Cost: {"${:,.2f}" .format(total_cost):>24}')
    print()
    if month_pay != 0:
        print(f'{" " * 33} Monthly Payment: {"${:,.2f}".format(month_pay):>19s}')

    policies = open('Policies.dat', 'a')
    policies.write(str(policy_num))
    policies.write(str(curr_date))
    policies.write(first_name)
    policies.write(last_name)
    policies.write(address)
    policies.write(city)
    policies.write(province)
    policies.write(postal)
    policies.write(phone_num)
    policies.write(insured_car)
    policies.write(xtra_liab)
    policies.write(glass_cov)
    policies.write(loaner)
    policies.write(loaner_num)
    policies.write(pay_option)
    policies.write(str(total_insure))
    print("Policy information processed and saved.")
    policy_num += 1

    endIndicator = str(input("Would you like to enter another policy (Y/N)? ")).upper()
    if endIndicator == "N":
        break

policies.close()
default_file.write(policies)
default_file.close() 
quit()
'''
Make file called Policies.dat:
    - Save policy number, all input values, and total insurance premium
    - Display the message "Policy information processed and saved."
    - Increase the policy number by 1 after file is compiled
    - Take a user input to end policy entering and add to defaut file when program ends
'''
'''
          1         2         3         4         5         6         
0123456789012345678901234567890123456789012345678901234567890123456789
One Stop Insurance Company                   Invoice Date: 03-27-2023
Insurance Summary and Receipt                Policy No:          1944

Customer Information:                                 No. of cars = 2
                                                 Extra Liability? Yes
John Smith                                       Glass Coverage?   No
12 Main St.                                      Loaner vehicle?  Yes
St. John's, NL A1A8H4                          No. of loaner cars = 2
(123) 123-1234                         Full or Monthly Payments? Full

=====================================================================

Insurance Premium:       $1000.00   Total Extra Cost:         $300.00
Extra Liability:          $100.00   Total Insurance Premium: $1300.00
Glass Coverage:           $100.00   HST:                       $18.00
Loaner Cost:              $100.00   Total Cost:              $1318.00

Monthly Payment:          $150.00 (if applicable)

                                   

'''
 