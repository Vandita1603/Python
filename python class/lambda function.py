#===LAMBDA FUNCTION ==============
'''s=lambda a: a*a
x=s(4)
print(x)'''
#=============================
'''add=lambda a,b: a+b
x=add(4,5)
print(x)'''
#=filter function====================
item_cost=[900,888,1100,1200,1300,777]
gt_thousand=filter(lambda x:x>1000,item_cost)
x=list(gt_thousand)
print("eligible for discount:",x)
#MAP FUNCTION========================
without_gt_cost=[100,200,300,400]
with_gt_cost=map(lambda x: x+10,without_gt_cost)
x=list(with_gt_cost)
print("without GST items costs:",without_gt_cost)
print("with gst item cost:",x)
#REDUCE FUNCTION====
from functools import reduce
each_item_cost=[111,222,333,444]
total_cost=reduce(lambda x,y: x+y, each_item_cost)
print(total_cost)
