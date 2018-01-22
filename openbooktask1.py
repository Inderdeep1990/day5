
fname = input("Enter file name that you need: ")
word=input("Enter word to be searched:")
m = 0
  
with open(fname, 'r') as f:
     for line in f:
         words = line.split()
         for i in words:
             if(i==word):
                 m=m+1
		 print("Occurrences of the word:")
		 print(m)
