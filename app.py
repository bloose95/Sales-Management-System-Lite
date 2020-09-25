# Program: Sales Management System Lite
# Description: A small management system that I was asked to build as my first university assignment
# Created Date: 09.21.2020
# Modified Date: 09.25.2020
# Developer: Jordan Min Kive
# File: app.py

# required os to enable clearing of terminal
import os

# global constants

# Menu Choices hold all the menu that can be chosen by the user
MenuChoices: list = ["MainMenu", "CreateItemMenu", "SearchItemMenu", "PurchaseItem", "SalesSummary"]

# global variable

# Items holds the list of items that should be available throughout the session
Items: list = \
[ \
    {"Id": 1, "Name": "Cup", "Price": "100.00", "Sold": False}, \
    {"Id": 2, "Name": "Sofa", "Price": "1500.00", "Sold": False}, \
    {"Id": 3, "Name": "Coffee", "Price": "20.00", "Sold": False} \
]

# ItemIndex holds the next id for the next item. it is used as an identifier which increments with each new items added
ItemIndex: int = 4

# Name: Clear
# Description: Generic code to clear terminal
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Name: PageTitle
# Description: Generic Title Constructor
# Parameters:
#   title - string
def PageTitle(title: str):
    # decorator is just a constant that holds the size of the row and the border style
    decorator: str = "****************************************"
    # Title length
    titleLength: int = len(title)
    # Length difference between decorator's length and title's length
    diffLength: int = len(decorator) - titleLength
    # index holds the current position in the row
    index: int = 1
    # text holds the title row that should be displayed within the title holder
    text: str = ""
    
    print(decorator)
    
    # loop until index is less or equal to diffLength
    while index <= diffLength:
        # if diffLength divide by 2 is not equal to index print a new space
        if (int(diffLength / 2) != index):
            text += " "
        # if diffLength divide by 2 is equal to index either print a new space and the title or just the title
        else:
            # if diffLength divide by 2 is not a multiple of 2 then we add a new space as we are 1 character short
            if diffLength % 2 != 0:
                text += " "
                
            text += title
            
        index += 1
    # print the concatenated text    
    print(text)

    # print the decorator with a new line
    print(decorator + "\n")

# Name: DisplayTableHeader
# Description: Generate Item Table Header
def DisplayTableHeader():
	print("****************************************")
	print("*      Name        *       Price       *")
	print("****************************************")

# Name: DisplaySummaryHeader
# Description: Generate Summary Table Header
def DisplaySummaryHeader():
	print("****************************************")
	print("*   No. of item    *    Total Amount   *")
	print("****************************************")

# Name: DisplayTableRecord
# Description: Display records in Item Table
# Parameters:
#   item: dictionary
#   withIndex: bool
def DisplayTableRecord(item: dict, withIndex: bool):
    # decorator is just a constant that holds the size of the row and the border style
    decorator: str = "****************************************"
    # decorator length holds the length of the decorator
    decoratorLength: int = len(decorator)
    # mid index hold the middle character index of the row size
    midIndex: int = int(decoratorLength / 2)
    # record holds the row containing the item information
    record: str = ""
    i: int = 0
    
    # loop through each field of the item
    for field in item:
        # index defines the current character position starting at 1
        index: int = 1
        # field length defines the number of character the field will have
        fieldLength: int = 0
        
        # make sure not to print the field id in the record
        if field != "Id":
            # if first column get field length until mid index
            if i == 0:
                fieldLength = midIndex - len(item[field])
            # if there is more than 2 fields break the loop
            elif i > 1:
                break
            # if second field get field length from mid index to end of the last character of decorator
            else:
                fieldLength = decoratorLength - midIndex
            
            #loop through each character of the field
            while index <= fieldLength:
                # if first index and second field print "*"
                if index == 1 and i == 1:
                    record += "*"
                # if first index and widthIndex flag is true the print the Id
                elif index == 1 and withIndex:
                    record += str(item["Id"])
                # if we are at the center of the field we print the field value
                elif int(fieldLength / 2) == index:
                    record += item[field]
                # if all the conditions are not met then we print a new space
                else:
                  record += " "

                # increment index
                index += 1

            #increment i
            i += 1
    
    # print the concatened row
    print(record)

    # print the decorator constant
    print(decorator)
	

# Name: DisplayMenu
# Description: Generic Menu constructor
# Parameters:
#   title - string
#   menuItems - list
def DisplayMenu(title: str, menuItems: list):
    # Display Page Title
    PageTitle(title)
    
    # Looping through menuItems to display the menu choices
    for item in menuItems:
        print(str(item["Id"]) + ". " + item["Name"])

# Name: ProcessMenuChoice
# Description: Validate user menu choice
# Parameters:
#   title - string
#   menuItems - list
def ProcessMenuChoice(title: str, menuItems: list):
    # Store user choice in variable choice
    choice: str = GetUserInput("Please select an action:")
    
    if choice.isdigit():
        try:
            # Get index of the selected item
            choice = int(choice) - 1
            # Call generic choice selection function
            MenuChoiceSelector(menuItems[choice]["Function"])
        except:
            # Display menu again if choice is invalid
            MenuChoiceSelector(MenuChoices[0])
    else:
        # Display menu again if choice is invalid
        MenuChoiceSelector(MenuChoices[0])

# Name: ProcessSearchCriteria
# Description: Display records based on search criteria
def ProcessSearchCriteria():
    text: str = ""
    # Store user choice in variable choice
    choice: str = GetUserInput("Please select search criteria:")
    # print a new line to add a space after the user made his choice
    print("")
    
    # check if choice is a numerical value
    if choice.isdigit():
        # use of try catch statement to ensure that the app wont crash in case of type mismatch
        try:
            # check if choice is equal to 1, 2, 3 or 4
            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                # if choice equal 1 then ask for user to input a name then display the items that matches the criteria
                if choice == "1":
                    text = GetUserInput("Search available item by name: ")
                    GetItems(text, False, 1)
                # if choice equal 2 then ask for user to input a name then display the items that matches the criteria
                elif choice == "2":
                    text = GetUserInput("Search sold item by name: ")
                    GetItems(text, False, 2)
                # if choice equal 3 then ask for user to input a price then display the items that matches the criteria
                elif choice == "3":
                    text = GetUserInput("Search available item by price: ")
                    GetItems(text, True, 1)
                # if choice equal 4 then ask for user to input a price then display the items that matches the criteria
                elif choice == "4":
                    text = GetUserInput("Search sold item by price: ")
                    GetItems(text, True, 2)
                
                # await for use input to return to main menu
                text: str = GetUserInput("Press Enter to return to Main Menu")
                MenuChoiceSelector(MenuChoices[0])
            # if choice is not within range then display the menu again
            else:
                MenuChoiceSelector(MenuChoices[2])
        # if we catch an exception then display menu again
        except:
            MenuChoiceSelector(MenuChoices[2])
    # if choice is not a numerical value then display menu again
    else:
        MenuChoiceSelector(MenuChoices[2])

# Name: MenuChoiceSelector
# Description: Select Menu and action to perform
# Parameters:
#   choice - string
def MenuChoiceSelector(choice: str):
    # Clear terminal before display a new menu
    Clear()

    # check if the choice input reflects the Menu Choice in menu choices otherwise send him back to Main Menu
    if choice == MenuChoices[1]:
        CreateItemMenu()
    elif choice == MenuChoices[2]:
        SearchItemMenu()
    elif choice == MenuChoices[3]:
        PurchaseItemMenu()
    elif choice == MenuChoices[4]:
        SalesSummaryMenu()
    else:
        MainMenu()

# Name: GetUserInput
# Description: Ask User for input
# Return: string (optional)
def GetUserInput(text: str = None):
    #Put an empty for readability
    print("")
    
    if text != None:
        print(text)
        
    # Store user input in variable userInput
    userInput: str = input()
    return userInput

# Name: MainMenu
# Description: Main Menu Constructor
def MainMenu():
    # Menu Title
    title: str = "Main Menu"
    # List of menu items
    menuItems: list = \
    [ \
        {"Id": 1, "Name": "Create item", "Function": MenuChoices[1]}, \
        {"Id": 2, "Name": "Search item", "Function": MenuChoices[2]}, \
        {"Id": 3, "Name": "Purchase item", "Function": MenuChoices[3]}, \
        {"Id": 4, "Name": "Sales summary", "Function": MenuChoices[4]}, \
    ]
    
    # Clear terminal before showing menu
    Clear()
    # Display Main Menu with generic menu builder
    DisplayMenu(title, menuItems)
    # Add a new line
    print("")
    # Get all available items
    GetItems("", False, 1)
    # Ask user what menu he want to be displayed
    ProcessMenuChoice(title, menuItems)

# Name: CreateItemMenu
# Description: Input Menu Builder
def CreateItemMenu():
    # Item
    item: dict = {"Id": ItemIndex, "Name": "", "Price": "0.00", "Sold": False}
    # Menu Title
    title: str = "Create Item"
    PageTitle(title)
    
    # Ask user to fill the different field
    print("Please fill in the following details: \n")
    
    item["Name"] = GetUserInput("Item Name:")
    item["Price"] = GetUserInput("Item Price:")
    
    # Call function to save the item
    SaveItemState(item)

# Name: SearchItemMenu
# Description: Search Menu Builder
def SearchItemMenu():
    # Menu Title
    title: str = "Search Item"
    # Item
    menuItems: list = \
    [ \
        {"Id": 1, "Name": "Search available item by name"}, \
        {"Id": 2, "Name": "Search sold item by name"}, \
        {"Id": 3, "Name": "Search available item by price"}, \
        {"Id": 4, "Name": "Search sold item by price"}, \
    ]
    
    # Display Main Menu with generic menu builder
    DisplayMenu(title, menuItems)
    # Process search criteria
    ProcessSearchCriteria()

# Name: PurchaseItemMenu
# Description: Purchase Menu Builder
def PurchaseItemMenu():
    # Menu Title
    title: str = "Purchase Item"
    # Display Title
    PageTitle(title)
    
    # Display available items with an index
    GetItems("", False, 1, True)
    
    # Ask user for what item he wants to purchase
    choice: str = GetUserInput("Please select the item you want to purchase:")

    # Add a new line
    print("")

    # using try catch statement to cater for type missmatch
    try:
        # loop through items
        for item in Items:
            # set selected item to the reference of current item if it is the right item
            if item["Id"] == int(choice):
                selectedItem = item
                break
    # reload menu if we catch an exception
    except:
        MenuChoiceSelector(MenuChoices[3])
        
    # clear terminal
    Clear()
    # call function PurchasingMenu with selectedItem
    PurchasingMenu(selectedItem)
    
    # bring user back to main menu
    MenuChoiceSelector(MenuChoices[0])

# Name: PurchaseItemMenu
# Description: Purchasing Menu Builder
def PurchasingMenu(selectedItem: dict = {}):
    # total holds the record for total price
    total: dict = {"Name": "Total", "Price": ""}
    # total amount
    totalAmount: float = 0
    # Menu Title
    title = "Purchasing " + selectedItem["Name"]
    # Display Title
    PageTitle(title)
    
    # Display Table Header
    DisplayTableHeader()
    # Display Selected Item for purchase without index
    DisplayTableRecord(selectedItem, False)
    
    # if selected item price is greated than 1000 apply discount and calculate total price
    if float(selectedItem["Price"]) > 1000:
        totalAmount = float(selectedItem["Price"]) + CalculateDiscount(float(selectedItem["Price"]))
        total["Price"] = str(totalAmount)
    # otherwise set total price to item price
    else:
        total["Price"] = selectedItem["Price"]
    
    # display total price
    DisplayTableRecord(total, False)
    
    # set a new field called SalePrice to the calculated total price
    selectedItem["SalePrice"] = total["Price"]
    
    # ask for user to validate action
    text: str = GetUserInput("Write:\"Agree\" to save item details or \"Cancel\" to cancel the operation.\n")
    
    # if user typed Agree set the selected item sold flag to true
    if text == "Agree":
        selectedItem["Sold"] = True
    # otherwise if user typed Cancel then bring him back to main menu
    elif text == "Cancel":
        MenuChoiceSelector(MenuChoices[0])

# Name: PurchaseItemMenu
# Description: Sales Menu Builder
def SalesSummaryMenu():
    # record holds the detail row
    record: dict = {"ItemCount": "", "Amount": ""}
    # count holds the number of sold items
    count: int = 0
    # total amount holds the sum of the sold items price
    totalAmount: float = 0
    # Menu Title
    title: str = "Sales Summary"
    # Display Title
    PageTitle(title)

    # Display Summary Header
    DisplaySummaryHeader()
    
    # loop through items
    for item in Items:
        # if item is sold then increment count and add the amount to total amount
        if item["Sold"] == True:
            count += 1
            totalAmount += float(item["SalePrice"])
    
    # set item count of the record
    record["ItemCount"] = str(count)
    # set amount of the record
    record["Amount"] = str(totalAmount)
    # display record details
    DisplayTableRecord(record, False)
    
    # Await for user input before sending him back to Main Menu
    GetUserInput("Press Enter to return to Main Menu")
    MenuChoiceSelector(MenuChoices[0])

# Name: CalculateDiscount
# Description: Calculate the discount of an item based on its item price
# Parameters:
#   itemAmount: float
#   discountPerc: float (optional)
def CalculateDiscount(itemAmount: float, discountPerc: float = 10):
    # dicount holds the discount details
    discount: dict = {"Name": "Discount(" + str(discountPerc) + "%)", "Amount": ""}
    # discount amount holds the calculated discount
    discountAmount: float = -1 * (itemAmount * (discountPerc/100))
    # set discount amount
    discount["Amount"] = str(discountAmount)
    # display discount details
    DisplayTableRecord(discount, False)
    
    # return the discount amount
    return discountAmount
        
# Name: ValidateItem
# Description: Validate the different property of items to check if they have the right variable type
# Parameters:
#   item - dictionary    
def ValidateItem(item: dict):
    # use of try catch statement to validate data type
    try:
        str(item["Name"])
        float(item["Price"])
        return True
    except:
        return False

# Name: SaveItemState
# Description: Validate user action
# Parameters:
#   item - dictionary
def SaveItemState(item: dict):
    # Validate user action
    text: str = GetUserInput("Write:\"Agree\" to save item details or \"Cancel\" to cancel the operation.")
    
    # if user typed "Agree" then validate the Item
    if text == "Agree":
        # If item is valid then print success message and await user input before bringing him back to Main Menu
        if ValidateItem(item):
            Items.append(item)
            GetUserInput("Item Saved Successfully.")
            MenuChoiceSelector(MenuChoices[0])
        # If item is not valid ask user to input item details again
        else:
            GetUserInput("Item is not valid.")
            MenuChoiceSelector(MenuChoices[1])
    # If user typed cancel bring him back to Main Menu
    elif text == "Cancel":
        MenuChoiceSelector(MenuChoices[0])
    # if condition are not met then ask user to validate action again
    else:
        SaveItemState(item)

# Name: GetItems
# Description: Display all Items or by criteria
# Parameters:
#   text: string
#   isPrice: bool
#   sold: integer (optional)
#   withIndex: boolean (optional)
def GetItems(text: str, isPrice: bool, sold: int = 0, withIndex: bool = False):
    # display table header
    DisplayTableHeader()
    
    # loop through items
    for item in Items:
        # check if item is available
        if sold == 1 and item["Sold"] == False:
            # if text is empty display all available items
            if text == "":
                DisplayTableRecord(item, withIndex)
            # if is not price and text is equal to name then display available item
            elif isPrice == False and text.lower() == item["Name"].lower():
                DisplayTableRecord(item, withIndex)
            # if is price and text is equal to price then display available item
            elif isPrice and float(text) == float(item["Price"]):
                DisplayTableRecord(item, withIndex)
        # check if item is sold
        elif sold == 2 and item["Sold"]:
                # if text is empty display all sold items
            if text == "":
                DisplayTableRecord(item, withIndex)
            # if is not price and text is equal to name then display sold item
            elif isPrice == False and text.lower() == item["Name"].lower():
                DisplayTableRecord(item, withIndex)
            # if is price and text is equal to price then display sold item
            elif isPrice and float(text) == float(item["Price"]):
                DisplayTableRecord(item, withIndex)
        # otherwise display all items
        elif sold == 0:
            DisplayTableRecord(item, withIndex)

#Display Main Program 
MenuChoiceSelector(MenuChoices[0])
