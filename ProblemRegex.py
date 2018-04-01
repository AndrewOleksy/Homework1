##### Problem #####
##### CNS-380/597 - Ryan Haley####
##### Andrew Oleksy Homework #1 2018-04-01 #####
import re

#Write a regular expression to fit the following:

#1 Phone number in the format of
#  xxx-xxx-xxxx
def phone1(num):
    num = str(num)
    regex = '\d{3}\-\d{3}\-\d{4}'
    match = re.findall(regex,num)
    if match:
        print('Phone 1')
        print(match)

#2 Phone number in the format of
#  (xxx) xxx-xxx
def phone2(num):
    num = str(num)
    regex = '\(\d{3}\)\s\d{3}\-\d{3}'
    match = re.findall(regex,num)
    if match:
        print('Phone 2')
        print(match)



#3 Phone number in the format of
#  +x xxx.xxx.xxxx
def phone3(num):
    num = str(num)
    regex = '\+\d{1}\s\d{3}\.\d{3}\.\d{4}'
    match = re.findall(regex,num)
    if match:
        print('Phone 3')
        print(match)



#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
def ssn(num):
    num = str(num)
    
    regex = '\d{3}\-\d{2}\-\d{4}'
    match = re.findall(regex,num)
    
    regex2 = '\d{9}'
    match2 = re.findall(regex2,num)
    
    if match:
        print('SSN broken up with -')
        print(match)
        
    elif match2:
        print('SSN 9 in a row')
        print(match2)



