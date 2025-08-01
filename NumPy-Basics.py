import numpy as np
print("NunPy V",np.__version__)

print("\n############ NumPy Array ###############")
# 0D Array
print ("\n>> 0D Array ---------------------------")
arr = np.array("A")
print ("Dimention -",arr.ndim,"D")
print (arr)

# 1D Array
print ("\n>> 1D Array ---------------------------")
arr = np.array(["A","B","C","D","E","F","G"])
print ("Dimention -",arr.ndim,"D")
print (arr)
print ("- Accessing single element")
print (arr[4])
print ("- Accessing multiple element return array")
print (arr[-6:4])
print ("- Accessing multiple element stepwise")
print (arr[1::2]) # (start:end:step)

# 2D Array (Matrix)
print ("\n>> 2D Array (Matrix) ------------------")
arr = np.array([
    [11,12,13,14,15,16],
    [21,22,23,24,25,26],
    [31,32,33,34,35,36],
    [41,42,43,44,45,46],
    [51,52,53,54,55,56],
    [61,62,63,64,65,66]
])
print ("Dimention -",arr.ndim,"D")
print (arr)
print ("- Accessing single element")
# print (arr[1][2])
print (arr[1,2])
print ("- Accessing multiple element from row")
print (arr[2,1:3])
print ("- Accessing multiple element stepwise from row")
print (arr[2,::2])
print ("- Accessing single row")
print (arr[0,])
print ("- Accessing multiple row")
print (arr[1:3,])
print ("- Accessing multiple row stepwise")
print (arr[::2,])
print ("- Accessing single column")
print (arr[:,0:1])
print ("- Accessing multiple column")
print (arr[:,0:2])
print ("- Accessing multiple column stepwise")
print (arr[:,::2])
print ("- Accessing inner Sub-matrix no Border")
print (arr[1:5,1:5])
print ("- Accessing stepwise Grid")
print (arr[::2,::2])

# 3D Array (Cubic = Depth,Row,Column)
print ("\n>> 3D Array -------------------------")
arr = np.array([
    [[11,12,13],[14,15,16],[17,18,19],
    [21,22,23],[24,25,26],[27,28,29],
    [31,32,33],[34,35,36],[37,38,39],
    [41,42,43],[44,45,46],[47,48,49],
    [51,52,53],[54,55,56],[57,58,59],
    [61,62,63],[64,65,66],[67,68,69]]
])
print ("Dimention -",arr.ndim,"D")
