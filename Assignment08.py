# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JRiley,11.26.2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JRiley,11.26.2019,Modified code to complete assignment 8
    """

    def __init__(self, ProductName, ProductPrice):
        self.Name = ProductName
        self.Price = ProductPrice

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        SaveDataToFile(strfile_name, list_of_product_objects):

        ReadDataFromFile(strfile_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JRiley,11.26.2019,Modified code to complete assignment 8
    """
    @staticmethod
    def ReadDataFromFile(strFileName):
        """  Reads data utilizing the Product Class
        :return: string
        """
        lstOfProductObjects = []
        file = open(strFileName, "r")
        for line in file:
            data = line.split(",")
            objProduct = Product(data[0].strip(), float(data[1].strip()))
            row = {"Name":objProduct.Name, "Price":objProduct.Price}
            lstOfProductObjects.append(row)
        file.close()
        return lstOfProductObjects

    @staticmethod
    def SaveDataToFile(strfilename, lstOfProductObjects):
        """  Saves/appends product name and price to a file
        :return: string
        """
        with open(strfilename, 'a') as file:
            for row in lstOfProductObjects:
                file.write(row["Name"] + ", " + str(row["Price"]) + "\n")
        return "Data saved to file."

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Presenting user a menu, user option, reading current data, and adding data...

    Methods:
        Menu: Showing the menu of options for the user
        Choice: Receiving the choice option the user input
        ReadData: Reading the current data in the file to the user
        AddData: Receiving new data to be added from the user input

    Changelog:
        JRiley,11.26.2019,Modified code to complete assignment 8
    """

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: string
        """
        print('''
            Menu of Options
            1) Show current data
            2) Add a new item.
            3) Save data to file and exit program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentData(self):
        """ Shows the current items in the file

        :param lstOfProductObjects: (list) of rows you want to display
        :return: nothing
        """
        print("The current items in the file are: ***********\n")
        lstOfProductObjects = FileProcessor.ReadDataFromFile(self)
        for row in lstOfProductObjects:
            print(row["Name"] + ", $" + str(row["Price"]))
        print("\n***********************************************")

    @staticmethod
    def GetProductData(lstOfProductObjects):
        """ Gives the prompt to the user
        input: Product and Price of product.
        """
        newProduct = input("Add a product: ")
        newPrice = float(input("Add a price for the product: "))
        row = {"Name": newProduct, "Price": newPrice}
        lstOfProductObjects.append(row)
        return lstOfProductObjects
    print()

# Main Body of Script  ---------------------------------------------------- #

while True:
    # Show the menu of options to the user
    IO.OutputMenuItems()
    # Receive user's choice from menu
    option = IO.InputMenuChoice()

    # Option 1 is to show the current data within the file.
    if option == '1':
        IO.ShowCurrentData(strFileName)

    # Option 2 is to have the user add data to the file.
    elif option == '2':
        lstOfProductObjects = IO.GetProductData(lstOfProductObjects)

    # Option 3 is to allow the user to either save the data to a text file or exit without saving.
    elif option == '3':
        FileProcessor.SaveDataToFile(strFileName, lstOfProductObjects)
        break
    else:
        try:
            raise TypeError("Invalid Option")
        except TypeError as te:
            print(te, "\nChoose 1 to 3 only.")