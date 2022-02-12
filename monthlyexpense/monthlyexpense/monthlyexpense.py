# This program creates a pie chart report based on a text file containing last month expenses
# Each expense in the file is delimited by ':' this separate the 
# name of expense and the amount


# Import the graphical plotting library  
import matplotlib.pyplot as plt

# The main function
def main():

    # Initialize the list variables
    expense_amt = []   # this holds the expense amount
    expense_label = [] # this holds the expense label
    expenses=[]        # this holds both expense label and amount
    temp_list=[]       # this holds the temp elements when label and amount is split
   
    # This variable holds the delimeter value
    delimeter=':' 

    try: 
        # Read the text file containing expsenses delimeted by ':'
        # Prefix the file with absolute path if location of 
        # text file is not the same with python source code 
        # example 'C:\temp\monthlyexpense.txt'
        input_file =  open(r'monthlyexpense.txt','r')

        # Put each line as an element into a list
        expenses = input_file.readlines()
   
        # close the input file
        input_file.close()

    # capture the error if file is not existed
    except IOError as e: 
        print('File does not exist!')
        print(e)
        
    
    # Loop through the list expenses
    for i in range(len(expenses)):

        # Strip the trailing '\n' from each element of the expenses list
        expenses[i] = expenses[i].rstrip('\n')

        #split each element for label and amount based on defined delimeter
        temp_list = expenses[i].split(delimeter)
        
        # populate the label and amount expense list, get the first and last element of temp_list
        expense_label.append(temp_list[0])
        expense_amt.append(float(temp_list[-1]))

        
    # display the content of lists in the console
    print(expense_label)
    print(expense_amt)
    

    # Configure the pie chart
    # adjust the size of the figure
    plt.figure(figsize =(10, 6))

    # Create a pie chart based on expsense_label and expense_amt list
    # format each pie with percentage and label
    wedges,texts, autotext = plt.pie(expense_amt, labels=expense_label, 
                                     autopct = '%1.2f%%')

    # Add legend to the pie chart and include the actual expense amount
    # bbox_to_anchor is use to adjust space between legend and pie chart
    plt.legend(wedges,expenses, title='Expenses in (€)', loc = 'best',  
               bbox_to_anchor =(1, 0, 0.5, 1))

    # Add title to the pie chart
    plt.title('Last Month Expenses')

    # Display the pie chart
    plt.show()


# Call the main function
main()
