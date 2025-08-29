import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

class Data_analysis:
    def __init__(self):
        self.pdf = None 
        pass

#  Load dataset 
    def load_dataset(self):
        print("Load dataset")
        self.file_name = input("Enter the file name of the dataset: ")
        self.df = pd.read_csv(self.file_name)
        print(self.df.head())
        print("Dataset loaded successfully")
        
# Explore data
    def Display_the_frist_5_rows(self):
        print("======== Display the first 5 rows ========")
        print(self.df.head(5))
        
    def Display_the_last_5_rows(self):
        print("======= Display the last 5 rows =========")
        print(self.df.tail(5))
        
    def Display_the_column_name(self):
        print("========= Column names ========")
        print(self.df.columns.tolist())
        
    def Display_data_type(self):
        print("========= Data types ============")
        print(self.df.dtypes)
        
    def Display_basic_info(self):
        print("========== Basic info ============")
        print(self.df.info())
        
#  Handle missing data 
    def show_missing_data(self):
        print("Rows with missing data:")
        print(self.df[self.df.isnull().any(axis=1)])
        
    def Fill_missing_mean(self):
        print("========== Filling missing data with mean =========")
        self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
        print("Missing values filled with mean")
        
    def drop_missing(self):
        print("========== Dropping rows with missing values =========")
        self.df.dropna(inplace=True)
        print("Rows dropped successfully")
        
    def replace_missing(self):
        value = input("Enter value to replace missing data with: ")
        self.df.fillna(value, inplace=True)
        print(f"Missing values replaced with {value}")

# Data visualization
    def bar_chart(self):
        top_customers = self.df.groupby("CUSTOMERNAME", as_index=False)["SALES"].sum().sort_values("SALES", ascending=False).head(10)
        plt.figure(figsize=(10,6))
        plt.bar(top_customers["CUSTOMERNAME"], top_customers["SALES"], color="skyblue", edgecolor="black")
        plt.title("Top 10 Customers by Sales")
        plt.xlabel("Customer Name")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        # plt.tight_layout()
        plt.savefig("all_data.pdf")
        plt.show()
        
    def Line_chart(self):
        plt.figure(figsize=(10,6))
        for name, group in self.df.groupby("CUSTOMERNAME"):
            plt.plot(group.index, group["SALES"], marker="o", label=name)
        plt.title("Sales Trend per Customer")
        plt.xlabel("Record Index")
        plt.ylabel("Sales Amount")
        plt.legend()
        plt.tight_layout()
        plt.savefig("all_data.pdf")
        plt.show()
        
    def Pie_chart(self):
        print("============ Pie chart =========")
        country_sales = self.df.groupby("COUNTRY")["SALES"].sum()
        plt.figure(figsize=(8,8))
        plt.pie(country_sales, labels=country_sales.index, autopct="%1.1f%%", startangle=140)
        plt.title("Sales Distribution by Country")
        plt.savefig("all_data.pdf")
        plt.show()
        
    def Histograme(self):
        print("======== Histogram ==========")
        plt.figure(figsize=(10,6))
        plt.hist(self.df["SALES"], bins=20, color="green", edgecolor="black", alpha=0.7)
        plt.title("Distribution of Sales Amounts")
        plt.xlabel("Sales")
        plt.ylabel("Frequency")
        plt.savefig("all_data.pdf")
        plt.show()
        
    def scatter_chart(self):
        print("======== Scatter Plot ==========")
        plt.figure(figsize=(10,6))
        plt.scatter(self.df["QUANTITYORDERED"], self.df["SALES"], color="red", alpha=0.6, edgecolor="black")
        plt.title("Quantity Ordered vs Sales")
        plt.xlabel("Quantity Ordered")
        plt.ylabel("Sales")
        plt.savefig("all_data.pdf")
        plt.show()
        
    def stack_plot(self):
        print("======== Stack Plot ==========")
        country_sales = self.df.groupby("COUNTRY")[["SALES", "QUANTITYORDERED"]].sum()
        plt.figure(figsize=(10,6))
        plt.stackplot(country_sales.index, country_sales["SALES"], country_sales["QUANTITYORDERED"], labels=["Sales", "Quantity Ordered"])
        plt.legend(loc="upper left")
        plt.title("Stack Plot of Sales and Quantity by Country")
        plt.xticks(rotation=45)
        plt.savefig("all_data.pdf")
        plt.show()
        
    def start_pdf(self, filename="all_charts.pdf"):
        self.pdf = PdfPages(filename)
        print(f"PDF file '{filename}' opened for saving charts.")

    # Close PDF
    def close_pdf(self):
        if self.pdf:
            self.pdf.close()
            print("PDF file saved and closed successfully.")


# ================= Main Program ==================
da = Data_analysis()
while True:
    print("\n=============== Data Analysis & Visualization Program ====================")
    print("Please select an option: ")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform Dataframe Operation")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            da.load_dataset()
        case 2:
            while True:
                print("\n======= Explore Data ========")
                print("1. Display the first 5 rows")
                print("2. Display the last 5 rows")
                print("3. Display column names")
                print("4. Display data type")
                print("5. Display basic info")
                print("6. Back to main menu")

                sub_choice = int(input("Enter your choice: "))
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
            print("Perform DataFrame operations (not implemented yet)")
            pass
        case 4:
            while True:
                print("\n======== Handle Missing Data =========")
                print("1. Display rows with missing values ")
                print("2. Fill missing values with mean")
                print("3. Drop rows with missing values")
                print("4. Replace missing values with a specific value")
                print("5. Back to main menu ")

                sub_choice = int(input("Enter your choice: "))
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
            print(da.df.describe())
        case 6:
            while True:
                print("\n====== Data Visualization ============")
                print("1. Bar plot")
                print("2. Line plot")
                print("3. Scatter plot")
                print("4. Pie chart")
                print("5. Histogram")
                print("6. Stack plot")
                print("7. Back to main menu")

                sub_choice = int(input("Enter your choice: "))
                match sub_choice:
                    case 1:
                        da.bar_chart()
                        da.start_pdf()
                    case 2:
                        da.Line_chart()
                        da.start_pdf()
                    case 3:
                        da.scatter_chart()
                        da.start_pdf()
                    case 4:
                        da.Pie_chart()
                        da.start_pdf()
                    case 5:
                        da.Histograme()
                        da.start_pdf()
                    case 6:
                        da.stack_plot()
                        da.start_pdf()
                    case 7:
                        break
        case 7:
            pass
            
        case 8:
            print("Exiting program. Goodbye!")
            break
