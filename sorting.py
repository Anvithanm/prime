number=[5,1,6,2,7,3,8,4,9]
for i in range(len(number)):
        for j in range(len(number) - 1):
                if number[j]>number[j+1]:
                        a=number[j]
                        number[j]=number[j+1]
                        number[j+1]=a
print number
#for i in number:
        #print number
~                                                                               
~                         
