def c_for(DEC,LIM,INC,ACT):
    exec(str(DEC))
    INC+="\n"
    for NUM in ACT:
        INC+=str(("  "+NUM+"\n"))
    exec(str("while {0}:\n"
             "  {1}").format(
             str(LIM),str(INC)))
'''
This function acts as a for loop from C or C++.
All semicolons must be removed, and lines must be in quotes with commas.

Example:
c_for('x=0','x<50','x+=1',[
      'print(x)',
      'if x>30:',
      '   print("x is greater than 30!")'
      ])
'''

def toBase(n,b):
    a=""
    while n:
            a+=str(n%b)
            n//=b
    return(a[::-1])
'''
This function returns a base-10 number in another base.
'''


