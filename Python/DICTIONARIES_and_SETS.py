# DICTIONARIES AND SETS

# DICTI0NARIES:
#     BUIL-IN DATA TYPE/data structure USE TO STORE DATA VALUES IN KEY-VALUE PAIRS
#     THEY ARE UNORDERD ,MUTABLE AND DIDN'T ALLOW DUPLICATE FOR KEYS
#         WORD+MEANING
#         KEY=VALUE
#         KEY=WORD     # we sirch by world in dic
#         VALUE=MEANING
#     SYNTAX: "KEY":VALUE
#     DIC={
#        "NAME": "Apna College",
#        "CGPA": 9.6,
#        "MARKS": [98,97,95]
#         }
#         elements/key-value pair are sep by ","
# can have all data types as valve but can't have list  or dic as a key  b\c they are mutable and key should be immutable
# it means we can,t use mutable d.type as key
# value can be: lists, dics, sets, str,int,tuple etc  (almost all)
#key: can be all except: lists, dictionaries,set    (b\c dic key must be hashable-> meaning their value can't change over time) mutable types can change so they can't use as a key
# key=immutabble
# value=both
dic={"NAME": "Apna College",58:"oeace","CGPA":9.6,"MARKS":[98,97,95], "is adult":True, "topics":("sets", "tuples"),(12,34):"tuple as key"}
print(type(dic))

# unorderd means no index  -> we can access thew value by key
print(dic["NAME"])   # Apna College
# if key not exist then we got erroe=keyerror

# mutable = dict
# dic["Apna College"]="jamal"  # wrong
# dic["key"]="vaue"
dic["NAME"]="jamal"         # value are changable   # old val is overwite by new value
# print(dic)
#{'NAME': 'Apna College', to    {'NAME': 'jamal',

# adding element
dic["surname"]="jamal"    # add in last
print(dic)  # {'NAME': 'jamal', 58: 'oeace', 'CGPA': 9.6, 'MARKS': [98, 97, 95], 'is adult': True, 'topics': ('sets', 'tuples'), (12, 34): 'tuple as key', 'surname': 'jamal

# key shpuld be unique

# null dict
null_dic={}
print(null_dic)    # {}
# add ele to it
null_dic["10th"]="Blue"
print(null_dic) #{'10th': 'Blue'}

# NESTED DICT:
     # TO MAKE VALUE OF A KEY A DICT
std={"name":"jamal","score":{
    "phy":97,
    "che":95,
    "M.Quran":99
}}
print(std)
print(std["score"]["phy"])   # 97    # std->score->phy

## METHSDS:
print(std.keys())   # dict_keys(['name', 'score']) # return alll keys in alist formate (not listed keys only outer)
print(std["score"].keys() )   # if we want keys of nested dic   #dict_keys(['phy', 'che', 'M.Quran'])
print(list(std.keys()))#we can cast the keys to a list       # ['name', 'score']
print(std.values()) # dict_values(['jamal', {'phy': 97, 'che': 95, 'M.Quran': 99}])   # n.dict=value
print(list(std.values()))  # DICT INSIDE A LIST IS POSSIBLE  # ['jamal', {'phy': 97, 'che': 95, 'M.Quran': 99}]
# no. of ele (key-val pair)
print(len(std)) # 2
# print(len(std["score"])+len(std)) # 5
print(std.items())    # return all element (key+value) as a tuple   # dict_items([('name', 'jamal'), ('score', {'phy': 97, 'che': 95, 'M.Quran': 99})])
## "dict_item" means "item of dictionary"

# ([{}])  => dict in list and list in tuple
print(list(std.items()))    # [('name', 'jamal'), ('score', {'phy': 97, 'che': 95, 'M.Quran': 99})]
# TWO TUPLES IN THE ABOVE LIST, WE CAN ACCES ONE OF YHEN BY INDEX AS THEY ARE IN A LIST
pairs=print(list(std.items()))      # it's wrong b\c print return None as void func
# pairs=list(std.items())
print(pairs[0])     # ('name', 'jamal')
# we can change the paires list
pairs[0]="jaaml"
print(pairs)        # ['jaaml', ('score', {'phy': 97,

print(std.get("name"))    # TWO WAYS 1) STD["NAME"] 2) MTHD        # WHY NEED TWO
print(std["name"])     # same result as above ie jamal
# BUT if i enter an exception i.e key that is not availible
print(std["name2"])  # error    ... *
print(std.get("name2"))   # None   -> so programe will not break      ...$    # A GOOD WAY TO DEAL WITH EXCEPTION
# IF THE ERROR FOUND THEN THE PROGRAME WILL BREAK AND THE CODE AFTER THIS WILL NOT EXECUTE AND THUS BREAK THE PROGRAME  as a programe rum from top to bottom left to right
# IT IS GOOD TO ALWAYS USE GET MTHD

std.update({"add":"Swat"})        #insert the specified element(pair/dict) to the dict at end inside curly braces {}
print(std)
#OR
new_std={"add":"Swat"}
std.update(new_std)
print(std)  # same as above

## NO DULICATE KEY I.E IF I ENTER NAME = MARYAM IT WILL OVER WRITE JAMAL, NOT CREAT NEW ELEMENT
new_std.update({"name":"Maryam"})     # add new value at the same palce of key ie in before in this eg
std.update(new_std)
print(std)      # {'name': 'jamal', 'sco     to       #  {'name': 'Maryam', 'sco



# SET:
#     BUIL-IN DATA STRUCUTURE/DATA TYPE
#     SET IS A COLLECTION OF THE UNORDERD ITEMS.  -> NO INDEX
#     EACH ITEM/ELEMENT IN THE SET MUST BE UNIQUE & IMMUTABLE
#     WE CAN STORE INT, FLOAT, STR, TUPLE B/C THEY ARE IMMUTABLE BUT CAN'T STOR LIST OR DICT IN SETS B\C THEY ARE MUTABlE

# collection={1,2,3,4,5,6,7, "jamal"," nasar"}
# print(collection,type(collection))
# RESULT WILL BE UNORDERD IE. the set are un ordered it is because i set we use a concept of hash and with it we improve the performance, we wanna fetch the elements as fast as possible , so it simply go with the flow, HENCE WE WANT SPEED THAN SEQUENCE HERE
    # {1, 2, 3, 4, 5, 6, 7, 'jamal', 'nasar'} <class 'set'>
    # {' nasar',1, 2, 3, 4, 5, 6, 7, 'jamal'}
    # {1, 2, 3, 4, 5, 6, 7, ' nasar', 'jamal'}
    # NO ORDER        we can make it ordered sequence using sorting, but how?????
#
# IF WE ENTER DUPLICATE elements only store once
coll={1,2,3,3, "kamal", (3,4,5), (3,4,5)}   # no error just simpy ignore like in this one the tuple and 3
print(coll) #{1, 2, 3, (3, 4, 5), 'kamal'}
print(len(coll)) # even lenght ignore duplicate values b\c its a set

#MPT SEt
st={}     # syntax of dict
print(type(st))     # <class 'dict'>
# TO CREAT AN MPT SET WE SPECIFICALLY SAY THAT IT'S A SET with round braces
st1=set()   # syntax of set
print(type(st1))    # <class 'set'>

## SET METHODS:
st1.add("jamal")        # add an element
print(st1)      # {'jamal'}
st1.remove("jamal")     # remove the passed element
print(st1) # set()


## *** NOTICE:
    # SET SRE MUTABLE -> WE CAN ADD OR REMOVE ELEMENTS/ENTRIES
    # SET'S ELEMENT ARE IMMUTABLE -> LIKE WE CAN'T PASS LIST/dict IN ADD METD
    ## IT MEANS THAT WE CAN CHANGE IN THE SET(ADDIND OR REMOVING OF ELEMENTS) BUT CAN'T CHANGE THE ENTRIES(LIKE STR, TUPLES
st2={1,2,3,"jamal", (2,3)}
st2.add(4)
print(st2)      # {'jamal', 1, 2, 3, (2, 3), 4}  # POSSIBLE
# BUT
st2["jamal"]="nasar"
print(st2)   # TypeError: 'set' object does not support item assignment
# OR
# CAN'T CHANGE IN THE TUPLE OR STR OR INT ETC


collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)   # {1, 2} # duplicates are ignored

# removing an element that not exist
collection.remove(7)
print(collection)       # KeyError: 7  # 7 is bot key and value

## if we want to add a mutable d.type in set
# collection.add([2,5,6])     # TypeError: unhashable type: 'list'

## UNHASHIBLE:
    # IMMUTABLE->HASHABLE(SETS ENTRIES, DICT KEYS, STRINGS ETC)
    # UNHASHHIBLE->MUTABLE(DICT,LIST, SET)
        # HASHING IS AN ALGORITHM IN WHICH  WE CHANGE ORIGINAL VALUE INTO SOMETHING ELSE
            # LIKE IF WE HAVE [1,2] AND OTHER [1,2]: THEY WILL HAVE SAME VALUE IN HASH FORMATE
                # BUT IF WE CHANGE IN ONE OF THEM THE HASH VAL;UE WILL BCOME DIFFER
                    # IN MUTATION WHEN ANY  CHANGE HAPPENING IN ORIGINAL VALUE THEIR HASH VALUE WILL CHANGE
                        # DUE TO THIS THE IMPLEMENTATIN OF OUR SET WILL BE NOT WORKING


print(len(collection))  # 2
collection.clear()  # empties the set
print(collection)  # set()
print(len(collection))  # 0

print(collection.pop()) # #  remove ad return a rendom value     # pop is fruitful one in set method b/c since it need to give you the removed element, it must return something->its fruitful
# practical scenario of pop() can be where we have a set of unique values and we have to gen a random value
print(collection)

# UNION OF SETS:
    # TOTAL UNIQUE VALUES IN THE SET  OR COMBINE BOTH SET VALUES AND RETURN NEW
st1={1,2,3}
st2={3,4,5}
print(st1.union(st2))   # {1, 2, 3, 4, 5}  # return a new set and don't update old ones
print(st1,st2)  # {1, 2, 3} {3, 4, 5}   # still unchanged

# INTERSECTION:
    # MEANS COMMON VALUES
    #COMBINE COMMON VALUES AND RETURN NEW
print(st1.intersection(st2))    # {3}  # it also return new and no update in old ie
print(st1,st2)  # {1, 2, 3} {3, 4, 5}


# PRACTICE:
#1. STORE THE FOLLOWING WORD MEANING IN A PYTHON DICT
dic={"table":["furniture","facts and figure"], "cat":"animal"}
print(dic)
print(dic["table"])
gf=dic.get("table")
print(gf)


#2,you are given a list of sub for std. assume one classrome for 1 sub. how many class are needed by all stds, given.
#given:
    # lst_sub=["python","c++","java","javascript","python","java","python","java","c++","c"]
    # one class== one sub
#req:
    # no. cls=?
# sol:
sit={"python","c++","java","javascript","python","java","python","java","c++","c"}          # "C++"!="c++"
print("total; cls required are: ",len(sit))


# #3. WAP TO ENTER MARKS OF 3 SUBS FROM USER AND STORE THEM IN A DICT, START WITH AN MPT DICT AND ADD ONE BY ONE TO IT, USE SUB NAME AS A KEY AND MARKS AS AVALUE.
p=float(input("phy: "))
c=float(input("che: "))
m=float(input("math: "))

dic={}
dic.update({"physics":p,"chemistry":c,"maths":m})
print(dic)

#4. FIGURE OUT A WAY TO STORE 9 AND 9.0 AS A SEP ENTRIES IN SET (can take help of buil-in d.types)
x=9.0
st={9,x}
print(st) # {9} # wrong   # b\c 9.0 and 9 have same hash value through which they are store in a set

st={9,"9.0"}
print(st)   #{9, '9.0'} # one uproach -> when we have to store values of same  hash value we can cast one to str
#OR
st={
    ("float",9.0),                # we use tuple as pair b\c we can't add dict to set as dic are mutable
    ("int",9)
}
print(st)   # {('int', 9), ('float', 9.0)}
