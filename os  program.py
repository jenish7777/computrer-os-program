import os
print("hy my friend")
print("what to want thish progran")
print('''A:make folder
B:delet folder
c:list out folder''')
a=input("enter your answer(a-c):-")
if(a=="a"):
    a=int(input("how many folder you want to make :-"))
    b=input("enter path to for where is make folder:-")
    print("you want to same name or different")
    print("A:same name")
    print("B:Different name")
    x=input("enter your answer(a or b):-")
    if (x=="a"):
          c=input("enter name over folder:-")
          for i in range(1,a+1):
              os.mkdir(f"{b}/{c} folder number-{i}")
    else:
         l=[]
         for i in range(1,a+1):
              y=input(f"enter your folder name {i}:-")
              l.append(y)    
         for i in range(0,a):
                   os.mkdir(f"{b}/{l[i]}")
    print("program make file sucessfuly")

elif(a=="b"):
     print("which one you are delet:-")
     print("A.file")
     print("B.folder")
     c=input("enter your answer(a or b):-")
     if(c=="a"):
          f=input("enter your file path for delet file:-")
          print(os.remove(f))
          print("program delet file sucessfuly")
     else:
          print("folder must be empty")
          f=input("enter path for delet folder:-")
          os.rmdir(f)
          print("program delet folder sucessfuly")
else:
     l=input("enter path for find list over folder:-")
     b=os.listdir(l)
     for i in b:
         print(f"[{i}]")
     
          


