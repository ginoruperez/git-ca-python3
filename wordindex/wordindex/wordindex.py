# This program reads the text file sample.txt which contains words in every line. 
# The program create a dictionary in which key-pair is the individual word found in file as key 
# while the values is the list of line numbers where the word is found


# The main function
def main():

    # initialize the variables for dictionary and list 
    dict = {}
    word_list = []

    # This variable determines if error is encountered, when reading the file
    no_error = True


    try : 
    
        # Read the text file containing words
        # prefix the file with the absolute path if the text file is located in another folder
        # example 'C:\temp\sample.txt'
        input_file = open(r'sample.txt', 'r')

        # Set up the list containing the line number and line sentence 
        # list for the line number
        word_list = input_file.readlines()

        # remove the extra '\n' and other special characters like '.', '?', '!', and ';' 
        # make all words in lower case for easy search
        for i in range(len(word_list)):
            word_list[i] = word_list[i].rstrip('\n').lower().replace(".", "")
            word_list[i] = word_list[i].replace("?", "")
            word_list[i] = word_list[i].replace("!", "")
            word_list[i] = word_list[i].replace(";", "")
               
    
        # get the line number for each element in word_list using enumerate e.g. (1, 'first line'), (2, 'second line')
        # then convert them into a list [(1, 'all words in first line'), (2, 'all words in secondline')]
        word_list=list(enumerate(word_list))        

        # close the input_file
        input_file.close()

    # Capture the error if file is not found.
    except IOError as e:
        print('File not found!')
        print(e)

        # switch the no_error to false
        no_error=False
        
        
    # Populate the dictionary with keys and values. 
    # Iterate to word_list that contains of line number and line sentence or group of words
    # where 'i' is the line number while 'l' is the group of words in each line
    for i, l in word_list:

        # split the words in each line
        for word in l.split():

            # populate the dictionary with the word as key and list of line numbers as the values
            if word in dict.keys():
                
                # Add the line number in the list. 
                # As word can occur multiple times in a line 
                # it should indicate each occurences of the word 
                # for example word 'robot' appears 3x in line 17, the list will have element like robot [17,17,17]
                dict[word].append(i+1)

            else:
                
                # add the first key as the word and line number as first element of the list for its value
                dict[word]=[i+1] 

    try : 
        # Write the dictionary in file word_index.txt 
        output_file = open(r'word_index.txt','w')

        # Sort by keys the dictionary and Iterate to a sorted dictionary
        for i in sorted(dict.keys()):

            # print in the console the keys and values
            print(i,dict[i])

            # write to a file formatted like ' word [ 7,18,19... ] '
            output_file.write(i + " ")
            output_file.write("[ "+listToString(dict[i])+" ]"+"\n")  # call another function to format the values

        # close the output_file
        output_file.close()

        # display successful creation of word index if no error
        if no_error:
            print()
            print('Word index file word_index.txt is successfully created.')
    
    # Capture the error if there is file error like write permission
    except IOError as e:
        print('Failed to create a word index file!')
        print(e)


# This is a function that convert the list to string, it accepts list with numeric elements
def listToString(s):

    #initialize the variable
    str1= ""
    for ele in s:
        str1 += str(ele)+","
    
    # return the formatted list e.g. '7,18,19...'
    return str1.rstrip(",")

# Call the main function
main()
