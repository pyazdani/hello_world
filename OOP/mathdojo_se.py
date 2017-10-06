class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for x in i:
                    self.result += x
            else:
                self.result += i
        return self

    def subtract(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for x in i:
                    self.result -= x
            else:
                self.result -= i
        return self

    def result():
        print self.result

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()