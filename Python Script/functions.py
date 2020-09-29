import os


def split_comma(splitLine, appended_list):
    for splits in splitLine:
        appended_list.append(splits.split(","))


def split_lines(file_objects):
    contents = file_objects.read()
    test = contents.splitlines()
    del test[0]
    return test


def remove_headers(list_with_headers):
    for x in range(1, len(list_with_headers) - 13):
        if list_with_headers[x][0] == 'Date' or list_with_headers[x][0] == '':
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
    
    Press 11 to show all data
     
    """
    print(message)

    option = int(input("    Select option from 1-11: "))

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
    elif option == 11:
        for x in appended_list:
            print(x)


def search_by_date(appended_list):
    search = input("Enter date: ")
    flag = 0

    for x in appended_list:
        if x[0] == search:
            print(x)
            flag = 1
        if flag == 0:
            print("No search values matched")


def search_by_dncc(appended_list):
    search = input("Enter daily new confirmed case value: ")
    flag = 0

    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[1]) > int(splitted[0])) and (int(x[1]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[1]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[1]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_tcc(appended_list):
    search = input("Enter total confirmed case value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[2]) > int(splitted[0])) and (int(x[2]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[2]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[2]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_dnd(appended_list):  # dnd = daily new deaths
    search = input("Enter daily new deaths value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[3]) > int(splitted[0])) and (int(x[3]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[3]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[3]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_td(appended_list):  # td = total deaths
    search = input("Enter total deaths value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[4]) > int(splitted[0])) and (int(x[4]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[4]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[4]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_dnr(appended_list):  # dnr = daily new recovered
    search = input("Enter daily new recovered value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[5]) > int(splitted[0])) and (int(x[5]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[5]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[5]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_tr(appended_list):  # tr = total recovered
    search = input("Enter total recovered value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[6]) > int(splitted[0])) and (int(x[6]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[6]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[6]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_dnt(appended_list):  # dnt = daily new tests
    search = input("Enter daily new tests value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[7]) > int(splitted[0])) and (int(x[7]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[7]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[7]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_tt(appended_list):  # tt = total test
    search = input("Enter total tests value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[8]) > int(splitted[0])) and (int(x[8]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[8]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[8]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")


def search_by_ac(appended_list):  # ac = active cases
    search = input("Enter total tests value: ")
    flag = 0
    if "-" in search:
        splitted = search.split("-")
        for x in appended_list:
            if (int(x[9]) > int(splitted[0])) and (int(x[9]) < int(splitted[1])):
                print(x)
                flag = 1

    else:
        for x in appended_list:
            if search[0] == '<':
                if int(x[9]) < int(search[1:]):
                    print(x)
                    flag = 1
            elif search[0] == '>':
                if int(x[9]) > int(search[1:]):
                    print(x)
                    flag = 1

    if flag == 0:
        print("No search values matched")

