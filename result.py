#RESULT using  if 
name=input("enter your name ")
standared=input("enter your class ")
roll=input("enter your roll number")
maths=int(input("enter your math mask"))
science=int(input("enter your maths mask "))
hindi=int(input("enter your hindi mask"))
english=int(input("enter your english mask"))
total=maths+science+hindi+english
percentage=total/4
if percentage>=33 and hindi>=33:
    if science>=33  and hindi>=33:
        if maths>=33 :
             print("pass")
             print ("congrats you got ",percentage)
else :
    print("try nest time")
    print("paisa barbaad b***** ",percentage)










