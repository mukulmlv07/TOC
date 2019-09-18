class stack():
        def __init__(self): 
            self.stack=[]
            self.stack.append('z0')
        def push(self,e):
            self.stack.append(e)
        def pop(self):
            self.stack.pop()
        def size(self):
            return len(self.stack)
class pda(stack):
    def __init__(self,a):
        self.string=a
        self.current='p0'
        stack.__init__(self)
        self.t=0
    def check(self):
        for i in self.string:
            self.top=self.stack[self.size()-1]
            if(i=='a' and self.current=='p0'):
                self.push(i)
                self.next='p1'
                print(i,' ',self.top,'/',i,self.top)
            elif(i=='a' and self.current=='p1'):
                self.push(i)
                self.next='p1'
                print(i,' ',self.top,'/',i,self.top)
            elif(i=='b' and self.current=='p1' and self.size()!=0):
                self.pop()
                self.next='p2'
                print(i,' ',self.top,'/','epsilon')
            elif(i=='b' and self.current=='p2' and self.size()!=0):
                self.pop()
                self.next='p2'
                print(i,' ',self.top,'/','epsilon')
            elif(i=='e' and self.current=='p2'):
                print(i,' ',self.top,'/',self.top)
                self.next='final'
                break
            elif(self.size()==1 and i=='b'):
                self.t=1
            self.current=self.next
            print(self.stack)
        print(self.next)
        if(self.size()==1 and self.t==0):
            print('excepted')
        else:
            print('not excepted')
s=input('enter a string')
s=s+'e'
x=pda('aaabbb')
x.check()
            
        
        
        
        
        
    
    
    
        
        
