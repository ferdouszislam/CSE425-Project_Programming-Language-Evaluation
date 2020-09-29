import os


def remove_headers(list_with_headers):
    header = list_with_headers[0]
    for x in range(1, len(list_with_headers) - 12):
        if header == list_with_headers[x]:
            del list_with_headers[x]


def main_menu(appended_list):
    message = """    Print 1 to search by Date
    Press 2 to search by Daily New Confirmed Cases
    Press 3 to search by Total Confirmed Cases
    Press 4 to search by Daily New Deaths
    Press 5 to search by Total Deaths
    Press 6 to search by Daily New Recovered
    Press 7 to search by Total Recovered
    Press 8 to search by Daily New Tests
    Press 9 to search by Total Tests
    Press 10 to search by Active Cases
     
    """
    print(message)

    option = int(input("    Select option from 1-10: "))

    if option == 1:
        os.system('cls')
        search_by_date(appended_list)
    elif option == 2:
        os.system('cls')
        search_by_dncc(appended_list)
    elif option == 3:
        os.system('cls')
        search_by_tcc(appended_list)
    elif option == 4:
        os.system('cls')
        search_by_dnd(appended_list)
    elif option == 5:
        os.system('cls')
        search_by_td(appended_list)
    elif option == 6:
        os.system('cls')
        search_by_dnr(appended_list)
    elif option == 7:
        os.system('cls')
        search_by_tr(appended_list)
    elif option == 8:
        os.system('cls')
        search_by_dnt(appended_list)
    elif option == 9:
        os.system('cls')
        search_by_tt(appended_list)
    elif option == 10:
        os.system('cls')
        search_by_ac(appended_list)


def search_by_date(appended_list):
    search_date = input("Enter date: ")
    flag = 0
    for x in appended_list:
        if x[0] == search_date:
            print(x)
            flag = 1
        if flag == 0:
            print("No search values matched")


def search_by_dncc(appended_list):
    search_dncc = input("Enter daily new confirmed case value: ")
    flag = 0
    for x in appended_list:
        if x[1] == search_dncc:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_tcc(appended_list):
    search_tcc = input("Enter total confirmed case value: ")
    flag = 0
    for x in appended_list:
        if x[2] == search_tcc:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_dnd(appended_list):  # dnd = daily new deaths
    search_dnd = input("Enter daily new deaths value: ")
    flag = 0
    for x in appended_list:
        if x[3] == search_dnd:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_td(appended_list):  # td = total deaths
    search_td = input("Enter total deaths value: ")
    flag = 0
    for x in appended_list:
        if x[4] == search_td:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_dnr(appended_list):  # dnr = daily new recovered
    search_dnr = input("Enter daily new recovered value: ")
    flag = 0
    for x in appended_list:
        if x[5] == search_dnr:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_tr(appended_list):  # tr = total recovered
    search_tr = input("Enter total recovered value: ")
    flag = 0
    for x in appended_list:
        if x[6] == search_tr:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_dnt(appended_list):  # dnt = daily new tests
    search_dnt = input("Enter daily new tests value: ")
    flag = 0
    for x in appended_list:
        if x[7] == search_dnt:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_tt(appended_list):  # tt = total test
    search_tt = input("Enter total tests value: ")
    flag = 0
    for x in appended_list:
        if x[8] == search_tt:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_ac(appended_list):  # ac = active cases
    search_tt = input("Enter total tests value: ")
    flag = 0
    for x in appended_list:
        if x[9] == search_tt:
            print(x)
            flag = 1

    if flag == 0:
        print("No search values matched")
