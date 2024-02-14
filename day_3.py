# Words and Letter Counter 

while True:
    x = input("Enter Sentence : ")
    char_count = f"No. of charaters in sentence : {len(x)}"
    print(char_count)
    
    y = x.split()
    
    total_count = len(x.replace(" ", "").replace(".", "").replace(",", ""))
    x = f"No. of letters in your sentence : {total_count}"
    print(x)
    
    print("No. of letters in each word :")
    for x in y:
        print(x,  "-",  len(x))
        
    a = input("Want to count one more sentence (yes/no) : ").lower()
    
    if a == "yes":
        print 
    else:
        print("thank you")
        break 

# need to work on naming variables 