#name func
def nme():
    global a
    global ans
    print("Hey there new user! Whats your name?")
    a=input("...")
    print(f"Hey!{a} What would you like to do?")
    ans = input("...").lower()
#function add
def add():
    print("so you picked addition uh? alright give me the numbers ")
    b=int(input("..."))
    c=int(input("...and? "))
    print(f"alright,lets add {b} and {c}")
    add=b+c
    print(f"so the answer is {add}, {a} Hope that helps!")
#function sub
def sub():
    print("so you picked subtraction uh? alright give me the numbers ")
    b=int(input("..."))
    c=int(input("...and? "))
    print(f"alright,lets subtract {b} and {c}")
    sub=b-c
    print(f"so the answer is {sub}, {a} Hope that helps!")
#func main for add and sub
def main():
    nme()
    if ans.lower() in ["add","addition"]:
      add()
    
    elif ans.lower() in ["sub","subtraction"]:
      sub()
    
main()