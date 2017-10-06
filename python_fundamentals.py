>>> words = "It's thanksgiving day.  It's my birthday, too!"
>>> words.find("day")
18
>>> words.replace("day","month")
"It's thanksgiving month.  It's my birthmonth, too!"
>>> x = [2, 54, -2, 7, 12, 98]
>>> print min(x)
-2
>>> print max(x)
98
>>> x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
>>> x[0], x[-1]
('hello', 'world')
>>> y = x[0], x[-1]
>>> y
('hello', 'world')
>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]
>>> sorted(x)
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> x = sorted(x)
>>> x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> print x[:len(x)/2], x[len(x)/2:]
[-3, -2, 2, 6, 7] [10, 12, 19, 32, 54, 98]
>>> 
