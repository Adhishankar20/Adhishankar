# program to return the file extension proram
#If the input is given as end the loop will stop
for x in range(1):
txt = input("Enter the File with Extension ")
  a = ".py" in txt
  b = ".html" in txt
  c = ".php " in txt
  d =".txt" in txt
  
  if txt == 'end':
    break
  elif a == True:
    print(" .py is extension of Python")
  elif b == True:
    print(" .html is extension of Hypertext Markup Language") 
  elif c == True:
    print(" .php is extension of Hypertext Preprocessor")
  elif d ==True:
    print(" .txt is extension of Text")
  else:
    print("You HAVE ENTERED WRONG ! Check The Extension ")
    
