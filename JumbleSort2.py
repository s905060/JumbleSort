# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

#Check if number is valid
def is_number_valid(numer):
    lower = -999999
    high = 999999
    try:
        if (lower <= int(number)) and (int(number) <= high):
            return True
        else:
            return False
    except Exception, e:
        pass
    
#Check if string is valid
def is_string_valid(string):
    if (string.islower() and string.isalpha()):
        return True
    else:
        return False

#Check if the input length is valid
def check_length(string):
    limitation = 1000
    if len(userinput) < limitation:
        return True
    else: 
        print "Input characters at most %d long only." % limitation
        exit()

#Check if the input is mixed type(String + Number)
def is_mixed(userinput):
    digit_check = False
    lower_string_check = False
    digit_status = 0
    lower_string_status = 0
    
    for word in userinput:
        digit_check = is_number_valid(word)
        if digit_check == True:
            digit_status += 1
            
        lower_string_check = is_string_valid(word)
        if lower_string_check == True:
            lower_string_status += 1
            
        if (digit_status > 0) or (lower_string_status > 0):
            return True

#Starts Here
userinput = raw_input()
check_length_status = check_length(userinput)

if check_length_status == True:
    try:
        userinput = userinput.split()
        userinput = list(userinput)
        result = is_mixed(userinput)
        index_list = []
        str_list = []
        num_list = []
        list_length = 0
            
        #Seperate string and number into two lists
        while list_length != len(userinput):
            if userinput[list_length].isalpha():
                index_list.append("str")
                str_list.append(userinput[list_length])
                list_length += 1
            else:
                index_list.append("num")
                num_list.append(int(userinput[list_length]))
                list_length += 1

        #Sort String and Number lists individually
        str_list.sort()
        num_list.sort()

        #Join two sorted list into original list by index
        for i in xrange(len(userinput)):
            if index_list[i] == "str":
                userinput[i] = str_list.pop(0)
            if index_list[i] == "num":
                userinput[i] = int(num_list.pop(0))
        
        print (" ".join(str(x) for x in userinput))
        
    except Exception as instance:
        print instance