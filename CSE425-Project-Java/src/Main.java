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
                    System.out.println("\n\nSearch data set by 'Date'");
                    System.out.print("Enter date (mm/dd/yyyy): ");
                    performSearch(0);
                    break;

                case '1':
                    System.out.println("\n\nSearch data set by 'Daily new confirmed cases'");
                    System.out.print("Enter case number: ");
                    performSearch(1);
                    break;

                case '2':
                    System.out.println("\n\nSearch data set by 'Total confirmed cases'");
                    System.out.print("Enter total case number: ");
                    performSearch(2);
                    break;

                case '3':
                    System.out.println("\n\nSearch data set by 'Daily new deaths'");
                    System.out.print("Enter number of deaths: ");
                    performSearch(3);
                    break;
                case '4':
                    System.out.println("\n\nSearch data set by 'Total deaths'");
                    System.out.print("Enter total number of deaths: ");
                    performSearch(4);
                    break;
                case '5':
                    System.out.println("\n\nSearch data set by 'Total deaths'");
                    System.out.print("Enter total number of deaths: ");
                    performSearch(5);
                    break;
                case '6':
                    System.out.println("\n\nSearch data set by 'Total recovered'");
                    System.out.print("Enter total number of recovered: ");
                    performSearch(6);
                    break;

                case '7':
                    System.out.println("\n\nSearch data set by 'Daily New Tests'");
                    System.out.print("Enter number of daily new tests: ");
                    performSearch(7);
                    break;
                case '8':
                    System.out.println("\n\nSearch data set by 'Total Tests'");
                    System.out.print("Enter total number of tests: ");
                    performSearch(8);
                    break;
                case '9':
                    System.out.println("\n\nSearch data set by 'Active Cases'");
                    System.out.print("Enter number of active cases: ");
                    performSearch(9);
                    break;

                case '#':

                    System.exit(0);
                    break;
                case '*':
                    Help();
                    break;
                default:
                    System.out.println("\n\n***Invalid option!***");
                    break;
            }
        }
    }


    public static void searchDataSetComp(int option,int value,String sign)
    {
        Boolean isFound = false;

        try {
            for(int i=1;i<data.size();i++)
            {
                String[] entry = data.get(i).split(",");
                if(sign.equals(">"))
                {
                    if(Integer.parseInt(entry[option])>value)
                    {
                        isFound = true;

                        for (String s: entry)
                        {
                            System.out.print(s+"    ");
                        }
                        System.out.println("");

                    }
                }
                else
                {
                    if(Integer.parseInt(entry[option])<value)
                    {
                        isFound = true;

                        for (String s: entry)
                        {
                            System.out.print(s+"    ");
                        }
                        System.out.println("");

                    }
                }

            }
            if(!isFound) { System.out.println("***Data not found!***"); }

        }catch (Exception e){}
    }


    public static void searchDataSetRangeInput(int option, int start, int end)
    {
        Boolean isFound = false;

        try {
            for(int i=1;i<data.size();i++)
            {
                String[] entry = data.get(i).split(",");
                if(Integer.parseInt(entry[option])>=start && Integer.parseInt(entry[option])<=end)
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



    public static void searchDataSetSingleInput(int option, String key)
    {


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

    public static void performSearch(int option)
    {
        long startTime = System.currentTimeMillis();
        String key = scanner.next();
        if(option==0)
        {
            searchDataSetSingleInput(option,key);
        }
        else
        {
            if(key.contains(","))
            {
                String[] temp = key.split(",");
                searchDataSetRangeInput(option,Integer.parseInt(temp[0]),Integer.parseInt(temp[1]));
            }
            else if(key.contains(">"))
            {
                String value = key.replace(">","");
                searchDataSetComp(option,Integer.parseInt(value),">");
            }
            else if(key.contains("<"))
            {
                String value = key.replace("<","");
                searchDataSetComp(option,Integer.parseInt(value),"<");
            }
            else
            {
                searchDataSetSingleInput(option,key);
            }
        }
        System.out.println("Execution time for searching: "+ (System.currentTimeMillis()-startTime)+"ms");

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
        System.out.println("*. Show help");
        System.out.println("#. Close");
        System.out.print("Select an option(by serial no.): ");
    }

    //Method for merging multiple .csv files into one file
    public static void mergeCSV() throws IOException {
        long startTime = System.currentTimeMillis();
        //Reading all the files of the directory
        File directoryPath = new File("./data/provided");
        File filesList[] = directoryPath.listFiles();
        for(File file : filesList)
        {
            readCsv(file.getAbsolutePath(),data);
        }

        //storing a copy of merged/combined data file
        if(data.size()!=0)
        {
            FileWriter csvWriter = new FileWriter("./data/merged/mergedDataSet.csv");
            for(int i=0;i<data.size();i++)
            {
                csvWriter.append(data.get(i));
                csvWriter.append("\n");
            }
            csvWriter.close();
        }
        System.out.println("Execution time for merging the data set: "+ (System.currentTimeMillis()-startTime)+"ms");
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

    public static void Help()
    {
        System.out.println("\n\nSelect options using the row number on the left of the main menu");
        System.out.println("For special searches use the example below:");
        System.out.println("1. Single input search input format: 10");
        System.out.println("2. Range search input format: 20,50");
        System.out.println("3. Comparison search input format: >20");
    }
}
