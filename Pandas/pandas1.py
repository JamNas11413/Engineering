# # PANDAS:
# #     a pyhton library built on top of numpy 
# #     name:
# #         derives from: panel data
# # uses:
# #     used in DS, ML, DA


# # usnig this library:
#     # we are working with obj like:
#         # series and dataframe

# # series:
#     # its like 1D labeled column

# # dataframe:
# #     like 2D labeled grid/table

# # with the lib:
# #     we can import, display, manipulate and export tabular data
# #     like :
# #         pandas is python ms excel



import pandas as pd 

# print(pd.__version__)




# # SERIES:
#     # a pandas 1 dimensional labeled array that can hold any data type 
#     # think of it like a single column in s spreedsheet (1D)


# data = [1,2,3,4,5,6,7,8,9]
# # to convert the list to a series
# series = pd.Series(data)   # constructer not  a func as the "s" is upper case
# print(series)
# # 0    1
# # 1    2
# # 2    3
# # 3    4        # the left side is the index and the right side is the value of the series
# # 4    5
# # 5    6
# # 6    7
# # 7    8
# # 8    9
# # dtype: int64    ## meta data(data about the data)

# # we can also set indexs with custom labels
# # DEFAUL behaviour for the labels is to start at 0 and increment by 1
# labels = ['a','b','c','d','e','f','g','h','i']
# series = pd.Series(data, index=labels)
# print(series)
# # a    1
# # b    2
# # c    3
# # d    4
# # e    5
# # f    6
# # g    7
# # h    8
# # i    9
# # dtype: int64


# # to acces a value in series via lable 
# print(series.loc["e"])  # loc => location by lable  ## 5
# # to change values via key 
# series.loc["e"] = 200
# print(series.loc["e"]) 

# # if the  key doesnot match we will get  key error


# # locating by index 
# print(series.iloc[6])   # ioc => integer/index location



# # filter by values
# print(series[series >= 200])




# dictionary = {"day1": 1750,
#               "day2": 4537,
#               "day3": 45367,
#               "day4":4536}

# print(pd.Series(dictionary))        # keys will be labels
# # day1     1750
# # day2     4537
# # day3    45367
# # day4     4536
# # dtype: int64


# # can do the filtering and the accesiing stuff here also





# DATAFRAME:
    # as tabular data structure with rows abd columns, its 2 dimensional similer to an excel spreed sheet 

dic = {
    "name":["jamla", "nasra", "marya"],
    "age":[18,18,34]
}
df = pd.DataFrame(dic)
print(df)
#     name  age
# 0  jamla   18
# 1  nasra   18
# 2  marya   34

# custome laables at indexes
df = pd.DataFrame(dic, index=["emp1","emp2","emp3"])
print(df)
#        name  age
# emp1  jamla   18
# emp2  nasra   18
# emp3  marya   34

# # can do the filtering and the accesiing stuff here also

# to add new column
df["job"] =[5436,435678,53678]
print(df)

#        name  age     job
# emp1  jamla   18    5436
# emp2  nasra   18  435678
# emp3  marya   34   53678


# add new row 
row = pd.DataFrame({5467:54637,546789:5467,456378290:5467},{435627:5463,3562789:5467,3672890:647})   # each dictionary for each new row

df = df.concat([df,row])   # concat => concatenate
print(df)

