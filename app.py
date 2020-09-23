# Program: Sales Management System Lite
# Description: A small management system that I was asked to build as my first university assignment
# Created Date: 09.21.2020
# Modified Date: 09.22.2020
# Developer: Jordan Min Kive
# File: test.py

#required os to enable clearing of terminal
import os

#global constants
MenuChoices: list = ["MainMenu", "CreateItemMenu", "SearchItemMenu", "PurchaseItem", "SalesSummary"]

#global variable
Items: list = \
[ \
    {"Id": 1, "Name": "Cup", "Price": "100.00", "Sold": False}, \
    {"Id": 2, "Name": "Sofa", "Price": "1500.00", "Sold": False}, \
    {"Id": 3, "Name": "Coffee", "Price": "20.00", "Sold": False} \
]

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
    # Decorator holder
    decorator: str = "****************************************";
    # Title length
    titleLength: int = len(title)
    # Length difference between decorator's length and title's length
    diffLength: int = len(decorator) - titleLength
    index: int = 1
    text: str = ""
    
    print(decorator);
    
    while index <= diffLength:
        if (int(diffLength / 2) != index):
            text += " "
        else:
            if diffLength % 2 != 0:
                text += " "
                
            text += title
            
        index += 1
        
    print(text)
    print(decorator + "\n")

# Name: DisplayTableHeader
# Description: Generate Item Table Header
def DisplayTableHeader():
	print("****************************************")
	print("*      Name        *       Price       *")
	print("****************************************")

# Name: DisplayTableHeader
# Description: Generate Item Table Header
def DisplaySummaryHeader():
	print("****************************************")
	print("*   No. of item    *   Total Amount    *")
	print("****************************************")

# Name: DisplayTableRecord
# Description: Display records in Item Table
# Parameters:
#   item: dictionary
#   withIndex: bool
def DisplayTableRecord(item: dict, withIndex: bool):
    decorator: str = "****************************************"
    decoratorLength: int = len(decorator)
    midIndex: int = int(decoratorLength / 2)
    diffIndex: int = decoratorLength - midIndex
    record: str = ""
    i: int = 0
    
    for field in item:
        index: int = 1
        fieldLength: int = 0
        
        if field != "Id":
            if i == 0:
                fieldLength = midIndex - len(item[field])
            elif i > 1:
                break
            else:
                fieldLength = decoratorLength - midIndex
                
            while index <= fieldLength:
                if index == 1 and i == 1:
                    record += "*"
                elif index == 1 and withIndex:
                    record += str(item["Id"])
                elif int(fieldLength / 2) == index:
                    record += item[field]
                elif fieldLength % 2 == 0:
                    record += " "
                else:
                  record += " "
              
                index += 1
            
            i += 1
            
    print(record)
    print("****************************************")
	

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
    print("")
    
    if choice.isdigit():
        try:
            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                if choice == "1":
                    text = GetUserInput("Search available item by name: ")
                    GetItems(text, False, 1)
                elif choice == "2":
                    text = GetUserInput("Search sold item by name: ")
                    GetItems(text, False, 2)
                elif choice == "3":
                    text = GetUserInput("Search available item by price: ")
                    GetItems(text, True, 1)
                elif choice == "4":
                    text = GetUserInput("Search sold item by price: ")
                    GetItems(text, True, 2)
                    
                text: str = GetUserInput("Write: \"Reset\" to reset the operation.\nYou can also go to the main menu by pressing Enter")
        
                if text == "Reset":
                    MenuChoiceSelector(MenuChoices[2])
                elif text == "":
                    MenuChoiceSelector(MenuChoices[0])
                else:
                    SaveItemState()
            else:
                MenuChoiceSelector(MenuChoices[2])
        except:
            # Display menu again if choice is invalid
            MenuChoiceSelector(MenuChoices[2])
    else:
        # Display menu again if choice is invalid
        MenuChoiceSelector(MenuChoices[2])

# Name: MenuChoiceSelector
# Description: Select Menu and action to perform
# Parameters:
#   choice - string
def MenuChoiceSelector(choice: str):
    Clear()

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
        {"Id": 1, "Name": "Input item", "Function": MenuChoices[1]}, \
        {"Id": 2, "Name": "Search item", "Function": MenuChoices[2]}, \
        {"Id": 3, "Name": "Purchase item", "Function": MenuChoices[3]}, \
        {"Id": 4, "Name": "Sales summary", "Function": MenuChoices[4]}, \
    ]
    
    #Display Main Menu with generic menu builder
    Clear()
    DisplayMenu(title, menuItems)
    print("");
    GetItems("", False, 1)
    ProcessMenuChoice(title, menuItems)

# Name: CreateItemMenu
# Description: Input Menu Builder
def CreateItemMenu():
    # Menu Title
    title: str = "Create Item"
    # Item
    item: dict = {"Id": ItemIndex, "Name": "", "Price": "0.00", "Sold": False}
    
    PageTitle(title)
    
    print("Please fill in the following details: \n")
    
    item["Name"] = GetUserInput("Item Name:")
    item["Price"] = GetUserInput("Item Price:")
    
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
    
    #Display Main Menu with generic menu builder
    Clear()
    DisplayMenu(title, menuItems)
    ProcessSearchCriteria();

# Name: PurchaseItemMenu
# Description: Purchase Menu Builder
def PurchaseItemMenu():
    # Menu Title
    title: str = "Purchase Item"
    PageTitle(title)
    
    GetItems("", False, 1, True)
    
    choice: str = GetUserInput("Please select the item you want to purchase:")
    print("")

    for item in Items:
        if item["Id"] == int(choice):
            selectedItem = item
            break
        
    Clear()
    PurchasingMenu(selectedItem)
        
    MenuChoiceSelector(MenuChoices[0])

def PurchasingMenu(selectedItem: dict = {}):
    total: dict = {"Name": "Total", "Price": ""}
    totalAmount: float = 0
    # Menu Title
    title = "Purchasing " + selectedItem["Name"]
    PageTitle(title)
                
    DisplayTableHeader()
    DisplayTableRecord(selectedItem, False)
    
    if float(selectedItem["Price"]) > 1000:
        totalAmount = float(selectedItem["Price"]) + CalculateDiscount(float(selectedItem["Price"]))
        total["Price"] = str(totalAmount)
        DisplayTableRecord(total, False)
    else:
        total["Price"] = selectedItem["Price"]
        DisplayTableRecord(total, False)
        
    selectedItem["SalePrice"] = total["Price"]
    
    text: str = GetUserInput("Write:\"Agree\" to save item details or \"Cancel\" to cancel the operation.\n")
    
    if text == "Agree":
        selectedItem["Sold"] = True
    elif text != "Cancel":
        Clear()
        PurchasingMenu(selectedItem)

# Name: PurchaseItemMenu
# Description: Sales Menu Builder
def SalesSummaryMenu():
    # Menu Title
    title: str = "Sales Summary"
    record: dict = {"ItemCount": "", "Amount": ""}
    count: int = 0
    totalAmount: float = 0
    
    PageTitle(title)
    
    DisplaySummaryHeader()
    
    for item in Items:
        if item["Sold"] == True:
            count += 1
            totalAmount += float(item["SalePrice"])
            
    record["ItemCount"] = str(count)
    record["Amount"] = str(totalAmount)
    DisplayTableRecord(record, False)
    
    GetUserInput("Press Enter to return to Main Menu")
    MenuChoiceSelector(MenuChoices[0])
    
def CalculateDiscount(itemAmount: float, discountPerc: float = 10):
    discount: dict = {"Name": "Discount(" + str(discountPerc) + "%)", "Price": ""}
    discountAmount: float = -1 * (itemAmount * (discountPerc/100))
    discount["Price"] = str(discountAmount)
    DisplayTableRecord(discount, False)
    
    return discountAmount
        
# Name: ValidateItem
# Description: Validate the different property of items to check if they have the right variable type
# Parameters:
#   item - dictionary    
def ValidateItem(item: dict):
    try:
        str(item["Name"])
        float(item["Price"])
        return True;
    except:
        return False;

# Name: SaveItemState
# Description: Validate user action
# Parameters:
#   item - dictionary
def SaveItemState(item: dict):
    # Validate user action
    text: str = GetUserInput("Write:\"Agree\" to save item details or \"Cancel\" to cancel the operation.\nYou can also reset the operation by pressing Enter")
        
    if text == "Agree":
        # Validate Item
        if ValidateItem(item):
            Items.append(item)
            ItemIndex += 1
            GetUserInput("Item Saved Successfully.")
            MenuChoiceSelector(MenuChoices[0])
        else:
            # If item is not valid ask user to input item details again
            GetUserInput("Item is not valid.")
            MenuChoiceSelector(MenuChoices[1])
    elif text == "Cancel":
        MenuChoiceSelector(MenuChoices[0])
    elif text == "":
        MenuChoiceSelector(MenuChoices[1])
    else:
        SaveItemState()

# Name: GetItems
# Description: Display all Items or by criteria
# Parameters:
#   text: string
#   isPrice: bool
#   sold: integer (optional)
#   withIndex: boolean (optional)
def GetItems(text: str, isPrice: bool, sold: int = 0, withIndex: bool = False):
    DisplayTableHeader()
    
    for item in Items:
        try:
            if sold == 1 and item["Sold"] == False:
                if text == "":
                    DisplayTableRecord(item, withIndex)
                elif isPrice == False and text.lower() == item["Name"].lower():
                    DisplayTableRecord(item, withIndex)
                elif isPrice and float(text) == float(item["Price"]):
                    DisplayTableRecord(item, withIndex)
            elif sold == 2 and item["Sold"]:
                if text == "":
                    DisplayTableRecord(item, withIndex)
                elif isPrice == False and text.lower() == item["Name"].lower():
                    DisplayTableRecord(item, withIndex)
                elif isPrice and float(text) == float(item["Price"]):
                    DisplayTableRecord(item, withIndex)
            elif sold == 0:
                DisplayTableRecord(item, withIndex)
        except:
            return False;

#Display Main Program 
MenuChoiceSelector(MenuChoices[0])
