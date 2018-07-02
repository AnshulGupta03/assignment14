f = open('myfile.txt','w')
f.write('''“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. 
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” 
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. 
“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. 
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. 
That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird''')

f.close()


#Q.1- Write a Python program to read last n lines of a file

def read_last_lines(filename, lines):
    with open(filename, "r") as f:
        contents = f.readlines()[-lines:]
        for line in contents:
            print(line)

f = open('myfile.txt','r')
length = len(f.readlines())
n = int(input("how many lines you want to read? Number should be less than %d \n"%(length)))
if n > length:
    print("the file does not contain %d lines"%(n))
else:
    read_last_lines("myfile.txt", n)
f.close()


print("\n\n",10*"*")




#Q.2- Write a Python program to count the frequency of words in a file.
with open('myfile.txt','r') as f:
    data = f.readlines()
    words = []
    for line in data:
        words += line.split()
    #print(words)
    count_freq = {}
    for w in words:
        
        count_freq[w] = words.count(w)

    for k,v in count_freq.items():
        print (k,":",v)


print("\n\n",10*"*")






#Q.3- Write a Python program to copy the contents of a file to another file
file1 = open('myfile.txt','r')
file2 = open('copied.txt','w')

line = file1.readlines()
file2.writelines(line)

file1.close()
file2.close()


print("\n\n",10*"*")






#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

file1 = open('myfile.txt','r')
file2 = open('second.txt','w')
file3 = open('third.txt','w')
file2.writelines('you are beautiful\nkohli played well.\nambani gave a grand party\ndelhi is capital of India.\nShakespeare was a greater writer\ni like to sleep.')

list1 = []
file2.close()
file2 = open('second.txt','r')

while 1:
    line1 = file1.readline()
    file3.write(line1)
    print(line1)
    line2 = file2.readline()
    file3.write(line2)
    print(line2)
    if not line1 and not line2:
        break
    
    

file1.close()
file2.close()
file3.close()

print("\n\n",10*"*")








#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random

f = open("Random.txt", "w" )

for i in range(10):
    line = str(random.randint(0, 100))
    f.write(line)
    f.write("\n")
    
f.close()

f1 = open("Random.txt", "r" )
f2 = open("sorted.txt", "w" )
list1 = f1.readlines()
list1.sort()
f2.writelines(list1)

f1.close()
f2.close()


print("\n\n",10*"*")
