#1: Get 1 - 255
# for i in range(1,256):
#     print(i);

#2: Get even 1000
# for i in range (1, 1001):
#     if i % 2 == 0:
#         print i;

#3: Sum odd 5000
# sum = 0
# for i in range (1, 5001):
#     if i % 2 == 1:
#         sum = sum + i
# print sum

# 4: Iterate an array

# myArr = ["peter","piper","picked"];
# myArr2 = ["milk","bread","eggs"]

# for i in range (0,len(myArr)):
#     if myArr[i] == "peter":
#         print i

# for value in myArr:
#     print value;

#5: Find Max
# newArr = [10,4,7,65,3,43,2,12];
# for i in range (0,len(newArr)):
# print max(newArr)

# max = 0
# for i in range (0,len(newArr)):
#     if newArr[i] > max:
#         max = newArr[i];
# print max

#6: Find Average
# newArr = [10,4,7,65,3,43,2,12];
# sum = 0
# for i in range (0, len(newArr)):
#     sum += newArr[i]
# print sum / len(newArr)

#7: Array odd
# newArr = [10,4,7,65,3,43,2,12];
# y = 45

# for i in range (0, len(newArr)):
#     if newArr[i] % 2 != 0:
#         print newArr[i]

#8: Greater Than Y
# def greatThanY(y,arr):
#     for i in arr:
#         if i > y:
#             print i
# greatThanY(y,newArr)

#9: Squares
# newArr = [10,4,7,65,3,43,2,12];

# for i in range(len(newArr)):
#     print newArr[i] * newArr[i]

#10: Negatives
# newArr = [-10,4,7,-65,-3,43,-2,12];
# for i in range(0, len(newArr)):
#     if newArr[i] < 0:
#         print newArr[i];

#11: Min/Max/Avg
# def minmaxavg(newArr):
#     max = int()
#     min = int()
#     avg = int()
#     for i in range(0, len(newArr)):
#         if newArr[i] > max:
#             max = newArr[i]
#         if newArr[i] < min:
#             min = newArr[i]
#         avg += newArr[i]
#     avg = avg / len(newArr)

#     print "Max:" , max
#     print "Min:" , min
#     print "Avg:" , avg

# minmaxavg(newArr)

#12: Swap Values
# newArr = [-10,4,7,-65,-3,43,-2,12];

# for i in range (0, len(newArr)-1):
#     newArr[i] = newArr[i+1];
# newArr[len(newArr)-1] = 0

# print newArr

#13: Number To String
# myNum = 123
# print type(myNum)
# print type(str(myNum))

#Check what the type of a variable is:
myList = [];
print type(myList)
