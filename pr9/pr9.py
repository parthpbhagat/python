import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Data_analysis:
    def __init__(self):
        self.df = None   
        self.x = None
        self.y = None

#LOAD DATASET 
    def load_dataset(self):
        print("Load dataset")
        self.file_name = input("Enter the file name of the dataset: ")
        try:
            self.df = pd.read_csv(self.file_name)
            print(self.df)
            print("Dataset loaded successfully")
        except Exception as e:
            print("Error loading dataset:", e)

#  EXPLORE DATA 
    def Display_the_frist_5_rows(self):
        print("======== Display the first 5 rows ========")
        print(self.df.head(5))

    def Display_the_last_5_rows(self):
        print("======= Display the last 5 rows =========")
        print(self.df.tail(5))

    def Display_the_column_name(self):
        print("========= Column names ========")
        print(self.df.columns)

    def Display_data_type(self):
        print("========= Data types ============")
        print(self.df.dtypes)

    def Display_basic_info(self):
        print("========== Basic info ============")
        print(self.df.info())

#  HANDLE MISSING DATA 
    def show_missing_data(self):
        print(self.df[self.df.isnull().any(axis=1)])

    def Fill_missing_mean(self):
        print("========== Filling missing data with mean =========")
        self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
        print("Missing values filled")

    def drop_missing(self):
        print("========== Dropping rows with missing values =========")
        self.df.dropna(inplace=True)
        print("Missing rows dropped")

    def replace_missing(self):
        value = input("Enter the value to replace missing data with: ")
        self.df.fillna(value, inplace=True)
        print("Missing values replaced")

# DATA VISUALIZATION 
# set x axis and y axis
# to select frist 10 customer
    def set_xy(self):
        try:
            self.x = self.df["CUSTOMERNAME"].head(10)
            self.y = self.df["SALES"].head(10)
        except Exception as e:
            print("Error setting x and y:", e)

    def bar_chart(self):
        self.set_xy()
        plt.bar(self.x, self.y, color="skyblue")
        plt.xlabel("Customer Name")
        plt.ylabel("Sales")
        plt.title("Bar Chart")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("bar.pdf")
        plt.show()

    def line_chart(self):
        self.set_xy()
        plt.plot(self.x, self.y)
        plt.xlabel("Customer Name")
        plt.ylabel("Sales")
        plt.title("Line Plot")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("line.pdf")
        plt.show()

    def Scatter_plot(self):
        self.set_xy()
        plt.scatter(self.x, self.y, color="red")
        plt.xlabel("Customer Name")
        plt.ylabel("Sales")
        plt.title("Scatter Plot")
        plt.savefig("scatter.pdf")
        plt.show()

    def pie_chart(self):
        self.set_xy()
        plt.pie(self.y, labels=self.x, autopct="%1.1f%%")
        plt.title("Pie Chart")
        plt.savefig("pie.pdf")
        plt.show()

    def Histogram(self):
        try:
            plt.hist(self.df["SALES"], bins=10, color="blue", edgecolor="black")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")
            plt.title("Histogram Chart")
            plt.savefig("histogram.pdf")
            plt.show()
        except Exception as e:
            print("Error creating histogram:", e)

    def stack_plot(self):
        self.set_xy()
        sns.boxplot(x=self.x, y=self.y)
        plt.title("Box Plot")
        plt.savefig("stack.pdf")
        plt.show()


# ====================== main menu ======================
da = Data_analysis()
while True:
    print("=============== Data Analysis & Visualization Program ====================")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform Dataframe Operation")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    match choice:
        case 1:
            da.load_dataset()
        case 2:
            while True:
                print("======= Explore Data ========")
                print("1. Display the first 5 rows")
                print("2. Display the last 5 rows")
                print("3. Display column names")
                print("4. Display data types")
                print("5. Display basic info")
                print("6. Back to main menu")

                try:
                    sub_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue

                match sub_choice:
                    case 1:
                        da.Display_the_frist_5_rows()
                    case 2:
                        da.Display_the_last_5_rows()
                    case 3:
                        da.Display_the_column_name()
                    case 4:
                        da.Display_data_type()
                    case 5:
                        da.Display_basic_info()
                    case 6:
                        break
        case 3:
            print("Perform dataframe operations (not implemented yet).")
        case 4:
            while True:
                print("======== Handle Missing Data =========")
                print("1. Display rows with missing values")
                print("2. Fill missing values with mean")
                print("3. Drop rows with missing values")
                print("4. Replace missing values with a specific value")
                print("5. Back to main menu")

                try:
                    sub_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue

                match sub_choice:
                    case 1:
                        da.show_missing_data()
                    case 2:
                        da.Fill_missing_mean()
                    case 3:
                        da.drop_missing()
                    case 4:
                        da.replace_missing()
                    case 5:
                        break
        case 5:
            print("=========== Descriptive Statistics ===========")
            if da.df is not None:
                print(da.df.describe())
            else:
                print("Please load dataset first.")
        case 6:
            while True:
                print("====== Data Visualization ===========")
                print("1. Bar plot")
                print("2. Line plot")
                print("3. Scatter plot")
                print("4. Pie chart")
                print("5. Histogram")
                print("6. Box plot")
                print("7. Back to main menu")

                try:
                    sub_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue

                match sub_choice:
                    case 1:
                        da.bar_chart()
                    case 2:
                        da.line_chart()
                    case 3:
                        da.Scatter_plot()
                    case 4:
                        da.pie_chart()
                    case 5:
                        da.Histogram()
                    case 6:
                        da.stack_plot()
                    case 7:
                        break
        case 7:
            pass
        case 8:
            print("Exiting program. Goodbye!")
            break


