import functions



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
        splitLine = functions.split_lines(file_objects1)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects2)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects3)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects4)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects5)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects6)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects7)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects8)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects9)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects10)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects11)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects12)
        functions.split_comma(splitLine, appended_list)

        splitLine = functions.split_lines(file_objects13)
        functions.split_comma(splitLine, appended_list)


# remove all headers/nulls from appended list
functions.remove_headers(appended_list)


functions.main_menu(appended_list)



