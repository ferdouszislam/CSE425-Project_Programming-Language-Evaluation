//Rifat Islam
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<String> data;
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) throws IOException {

        char option;
        data = new ArrayList<>();
        mergeCSV(); //Merging data sets

        while(true)
        {
            showMenu();
            option = scanner.next().charAt(0);
            switch (option)
            {
                case '0':
                    searchDataSet(0);
                    break;

                case '1':
                    searchDataSet(1);
                    break;

                case '2':
                    searchDataSet(2);
                    break;

                case '3':
                    searchDataSet(3);
                    break;
                case '4':
                    searchDataSet(4);
                    break;
                case '5':
                    searchDataSet(5);
                    break;
                case '6':
                    searchDataSet(6);
                    break;

                case '7':
                    searchDataSet(7);
                    break;
                case '8':
                    searchDataSet(8);
                    break;
                case '9':
                    searchDataSet(9);
                    break;

                case '#':
                    System.exit(0);
                    break;
                default:
                    System.out.println("\n\n***Invalid option!***");
                    break;
            }
        }
    }



    public static void searchDataSet(int option)
    {
        System.out.print("\033[H\033[2J");
        System.out.flush();

        if(option==0)
        {
            System.out.println("\n\nSearch data set by 'Date'");
            System.out.print("Enter date (dd/mm/yyyy): ");
        }
        else if(option==1)
        {
            System.out.println("\n\nSearch data set by 'Daily new confirmed cases'");
            System.out.print("Enter case number: ");
        }
        else if(option==2)
        {
            System.out.println("\n\nSearch data set by 'Total confirmed cases'");
            System.out.print("Enter total case number: ");
        }
        else if (option==3)
        {
            System.out.println("\n\nSearch data set by 'Daily new deaths'");
            System.out.print("Enter number of deaths: ");
        }
        else if (option==4)
        {
            System.out.println("\n\nSearch data set by 'Total deaths'");
            System.out.print("Enter total number of deaths: ");
        }
        else if (option==5)
        {
            System.out.println("\n\nSearch data set by 'Total deaths'");
            System.out.print("Enter total number of deaths: ");
        }
        else if (option==6)
        {
            System.out.println("\n\nSearch data set by 'Total recovered'");
            System.out.print("Enter total number of recovered: ");
        }
        else if (option==7)
        {
            System.out.println("\n\nSearch data set by 'Daily New Tests'");
            System.out.print("Enter number of daily new tests: ");
        }
        else if (option==8)
        {
            System.out.println("\n\nSearch data set by 'Total Tests'");
            System.out.print("Enter total number of tests: ");
        }
        else {
            System.out.println("\n\nSearch data set by 'Active Cases'");
            System.out.print("Enter number of active cases: ");
        }


        String key = scanner.next();
        Boolean isFound = false;

        try {
            for(int i=1;i<data.size();i++)
            {
                String[] entry = data.get(i).split(",");
                if(entry[option].equals(key))
                {
                    isFound = true;

                    for (String s: entry)
                    {
                        System.out.print(s+"    ");
                    }
                    System.out.println("");

                }
            }
            if(!isFound) { System.out.println("***Data not found!***"); }

        }catch (Exception e){}

    }


    public static void showMenu()
    {
        System.out.println("\n\nSearch data set by following criteria");
        System.out.println("0. Search by 'Date'");
        System.out.println("1. Search by 'Daily new confirmed cases'");
        System.out.println("2. Search by 'Total confirmed cases'");
        System.out.println("3. Search by 'Daily new deaths'");
        System.out.println("4. Search by 'Total deaths'");
        System.out.println("5. Search by 'Daily new recover'");
        System.out.println("6. Search by 'Total recovered'");
        System.out.println("7. Search by 'Daily New Tests'");
        System.out.println("8. Search by 'Total Tests'");
        System.out.println("9. Search by 'Active Cases'");
        System.out.println("#. Close");
        System.out.print("Select an option(by serial no.): ");
    }

    //Method for merging multiple .csv files into one file
    public static void mergeCSV() throws IOException {
        readCsv("./data/COVID-19 BD Dataset-4 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-5 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-6 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-7 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-8 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-9 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-10 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-11 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-12 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-15 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-18 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-25 april.csv",data);
        readCsv("./data/COVID-19 BD Dataset-5 May.csv",data);

        //storing a copy of merged/combined data file
        if(data.size()!=0)
        {
            FileWriter csvWriter = new FileWriter("./data/mergedDataSet.csv");
            for(int i=0;i<data.size();i++)
            {
                csvWriter.append(data.get(i));
                csvWriter.append("\n");
            }
            csvWriter.close();
        }
    }

    //Method for reading single csv file
    public static void readCsv(String path, ArrayList<String> list) throws IOException {
        String row;
        BufferedReader csvReader = new BufferedReader(new FileReader(path));
        while ((row = csvReader.readLine()) != null) {
            if(!list.contains(row))
            {
                list.add(row);
            }
        }
        csvReader.close();
    }

}
