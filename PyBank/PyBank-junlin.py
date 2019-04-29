#import dependency
import os
import csv

#set file path
csvpath = os.path.join("Resources", "budget_data.csv")
# file_to_output = os.path.join("analysis", "budget_analysis.txt")

#set all initial value to 0 
total_months = 0 
total_profit = 0 
previous_month_profit = 0

# create empty lists to store the value while iterating through rows 
all_months_list = []
all_profit_list = []
rev_change_list = []

# open csv, 
with open(csvpath) as budgetdata: 
    csvreader = csv.reader(budgetdata)

#skip header
    header = next(csvreader)

    #for each_month in data: 
    for row in csvreader:
    #iterate through the row and add the value in all_months ["Oct -12","Nov-12",,,,]
        all_months_list.append(row[0]) 

    # interate through the Revenue row and cast string to int 
    # this_month_profit will be used to calculate revenue changes later  
        this_month_profit = int(row[1])   
    #add value to all_profit 
        all_profit_list.append(int(row[1]))   
       
    #get the revenue change for each two months 
        revenue_change = this_month_profit - previous_month_profit   
    #every loop through, thismonth will become previous value 
        previous_month_profit = this_month_profit   
    # changelist 
        rev_change_list.append(revenue_change)  


#len()to get value count of all_months_list
total_months = len(all_months_list)
print(f"total month:{total_months}  ")

#summing all value in all_profit_list 
total_profit = sum(all_profit_list)
print(f"total profit: ${total_profit}")

#replace "frist month revenue change 0"  
rev_change_list[0] = 0 
#calculate averge change by sum/len 
#print(rev_change_list)
# [116771, -662642, -391430, 379920, 212354, 510239, -428211, -821271, 693918, 416278, -974163, 860159, -1115009, 1033048, 95318, -308093, 99052, -521393, 605450, 231727, -65187, -702716, 177975, -1065544, 1926159, -917805, 898730, -334262, -246499, -64055, -1529236, 1497596, 304914, -635801, 398319, -183161, -37864, -253689, 403655, 94168, 306877, -83000, 210462, -2196167, 1465222, -956983, 1838447, -468003, -64602, 206242, -242155, -449079, 315198, 241099, 111540, 365942, -219310, -368665, 409837, 151210, -110244, -341938, -1212159, 683246, -70825, 335594, 417334, -272194, -236462, 657432, -211262, -128237, -1750387, 925441, 932089, -311434, 267252, -1876758, 1733696, 198551, -665765, 693229, -734926, 77242, 532869]
new_list = rev_change_list
ave_rev_change = sum(rev_change_list)/(total_months - 1)
print(f"the average change is :${ave_rev_change}")

# #use max() and min() to find max and min change in rev_change_list
max_rev_change = max(rev_change_list)

min_rev_change = min(rev_change_list)
# use index() searches the value in rev_change_list and find index 
max_rev_index = rev_change_list.index(max_rev_change)
min_rev_index = rev_change_list.index(min_rev_change)

max_rev_change_month = rev_change_list.index(max_rev_change)

print(f"The Greatest Increase is {all_months_list[max_rev_index]} ${max_rev_change}")
print(f"The Greatest Decrese is {all_months_list[min_rev_index]} ${min_rev_change}")

# total month:86  
# total profit: $38382578
# the average change is :$-2315.1176470588234
# The Greatest Increase is Feb-2012 $1926159
# The Greatest Decrese is Sep-2013 $-2196167


# with open(output, 'r') as readfile:
#     print(readfile.read())
