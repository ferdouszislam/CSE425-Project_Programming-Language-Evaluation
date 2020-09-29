import functions

def split_lines(file_objects):
    contents = file_objects.read()
    test = contents.splitlines()
    return test


def split_comma(splitLine, appended_list):
    for splits in splitLine:
        appended_list.append(splits.split(","))


count = 0

appended_list = []

with open("COVID-19 BD Dataset-4 april.csv") as file_objects1, \
        open("COVID-19 BD Dataset-5 april.csv") as file_objects2, \
        open("COVID-19 BD Dataset-5 May.csv") as file_objects3, \
        open("COVID-19 BD Dataset-6 april.csv") as file_objects4, \
        open("COVID-19 BD Dataset-7 april.csv") as file_objects5, \
        open("COVID-19 BD Dataset-8 april.csv") as file_objects6, \
        open("COVID-19 BD Dataset-9 april.csv") as file_objects7, \
        open("COVID-19 BD Dataset-10 april.csv") as file_objects8, \
        open("COVID-19 BD Dataset-11 april.csv") as file_objects9, \
        open("COVID-19 BD Dataset-12 april.csv") as file_objects10, \
        open("COVID-19 BD Dataset-15 april.csv") as file_objects11, \
        open("COVID-19 BD Dataset-18 april.csv") as file_objects12, \
        open("COVID-19 BD Dataset-25 april.csv") as file_objects13:
        splitLine = split_lines(file_objects1)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects2)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects3)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects4)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects5)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects6)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects7)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects8)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects9)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects10)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects11)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects12)
        split_comma(splitLine, appended_list)

        splitLine = split_lines(file_objects13)
        split_comma(splitLine, appended_list)


# remove all headers except the first one from appended list
functions.remove_headers(appended_list)

functions.main_menu(appended_list)

