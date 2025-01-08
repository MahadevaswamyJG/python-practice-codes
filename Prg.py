print('hello')

def message():
    print('God is a hope')
message()

a = input('Enter a value')
print(a)
print('printed A')

class Prg:
    def message1(self):
        print('Inside message Prg class')
    def message2(self,a):
        print('Inside message Prg class',a)
prg = Prg()
prg.message1()
prg.message2(a)
