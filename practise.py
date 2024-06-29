#1.Reversing a String using an Extended Slicing techniques
# def reverseString (value):
#     return value[::-1]
# userInput = str(input("Enter the string: "))
# result = reverseString(userInput)
# print(result)

#2.Count Vowels from Given words .
# def vowel_count(str):
#     count = 0
#     vowel = set("aeiouAEIOU")
#     for alphabet in str:
#         if alphabet in vowel:
#             count = count + 1
     
#     print("No. of vowels :", count)
# str = "Rishabh"
# vowel_count(str)

#3.Find the highest occurrences of each word from string
# test_str = "testString"
 
# print ("The original string is : " + test_str)
 
# all_freq = {}
# for i in test_str:
#  if i in all_freq:
#   all_freq[i] += 1
#  else:
#   all_freq[i] = 1
# res = max(all_freq, key = all_freq.get) 
 
# print ("The maximum of all characters in given string is : " + str(res))

#4.Remove Duplicates from List
# test_list = [1, 5, 3, 6, 3, 5, 6, 1]
# print ("The original list is : " + str(test_list))
# test_list = list(set(test_list))
# print ("The list after removing duplicates : " + str(test_list))

#5.Sort a List without using Sort keyword
# oList=[76, 23, 45, 12, 54, 9] 
# print("Original List:", oList)
 
# for i in range(0, len(oList)):
#     for j in range(i+1, len(oList)):
#         if oList[i] >= oList[j]:
#             oList[i], oList[j] = oList[j],oList[i]
 
# print("Sorted List", oList)


#6.Find the max and min no in the list without using inbuilt functions
# def findMinMaxValue():
#    lst=[1,2,3,4,5,6,7,8,9] 
#    minimum=1000000 
#    maximum=-1000000 
#    for i in lst: 
#        if(i < minimum): 
#            minimum=i 
#        if(i > maximum): 
#            maximum=i  
  
#    print("Minimum is:",minimum)
#    print("Maximum is:",maximum)

# findMinMaxValue()