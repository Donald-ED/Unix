# # An encoder for our spies to secretly send messages.

# # Ask the user for their message and cipher number.
# cipher_num = int(input())
# cipher_message = input()

import sys
cipher_num = int(sys.argv[1])
cipher_message = input("Input the message: ")
cipher_message = cipher_message.upper()
empty_str = ""
for i in cipher_message:
  if ord(i) >= 65 and ord(i) <= 90: 
    num = ord(i) + cipher_num
    if num > 90:
      empty_str += chr(num - 26)
    elif num < 65:
      empty_str += chr(num + 26)
    else:    
      empty_str += chr(num)
  else:
    empty_str += chr(ord(i))
#using list comprehension
ls = [j for i in empty_str for j in i if j!=" "]
to_print = ""
length = len(ls)-1
counter5 = 0
counter10=0
change = False
#using for loops to output 5 alphabets,10 words per line
for i in range(length):
    if counter5 == 5:
        to_print+=" "
        #to_print+=i
        counter5 =1
        counter10+=1
        change=True
    elif counter10 ==10:
        to_print+="\n"
        counter10 =1
        counter5+=1
        to_print+=ls[i]
    elif change:
        to_print+=ls[i-1]
        to_print+=ls[i]
        change= False
        counter5+=1
    else:
        to_print+=ls[i]
        counter5+=1

print(to_print)
