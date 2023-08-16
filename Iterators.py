#there is some logic mistakes
class Fibonacci:
    def __init__(self,limit):
        self.previous=0
        self.current=1
        self.limit=limit


    def __iter__(self):
        return self

    def __next__(self):
        result=self.current
        if result<self.limit:
            result=self.current+self.previous
            self.previous=self.current
            self.current=result
            return result
        else:
            raise StopIteration

fib_iterator = iter(Fibonacci(100))
while True:
    try:
        print(next(fib_iterator))
    except StopIteration:
            break
