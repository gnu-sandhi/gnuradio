#!/usr/bin/python

import sciscipy


# u is a TUPLE vector of width w

def csim(P,I,D,n0,n1,d0,d1,u):
        code_string1 = "s=%s;"
        code_string2 = "Gc=syslin('c',("+str(P*I+D)+"*s)"+","+str(I)+"*s);"
        code_string3 = "G=syslin("
        code_string4 = "'c'"+","+str(n0)+"*s"+"+"+str(n1)+","+str(d0)+"*s"+"+"+str(d1)+");"
        code_string5 = "r=tf2ss(G*Gc);"
        code_string6 = "u="+str((u))+";"
        code_string7 = "y=csim(u,1:length(u),r)"
        code_string = code_string1+code_string2+code_string3+code_string4+code_string5+code_string6+code_string7

	import sciscipy
        sciscipy.eval(code_string)
        y = sciscipy.read("y")
        return y
	#print "y"

if __name__ == "__main__":
        u = [0]*100
        u[50] = 1
	out = csim(2,0.5,0.6,1,1,2,1,u)
        print out

	import matplotlib.pyplot as plt
        plt.plot(out)
        plt.show()

