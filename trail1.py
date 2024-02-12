#name func
def nme():
    global a
    print("Hey there new user! Whats your name?")
    a=input("...")
    print(f"Hey!{a} What would you like to do?")

#function add
def add():
    print("so you picked addition uh? alright give me the numbers ")
    b=int(input("..."))
    c=int(input("..."))
    print(f"alright,lets add {b} and {c}")
#function sub
def sub():
    print("so you picked subtraction uh? alright give me the numbers ")
    b=int(input("..."))
    c=int(input("..."))
    print(f"alright,lets subtract {b} and {c}")
#func main for add and sub
def main():
    add()
    sub()
    
main()