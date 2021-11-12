#!/usr/bin/env python
# coding: utf-8

# In[42]:


#This program saearches and iterates through predifined values of courses/schedules

rooms = {"CS101":3004,"CS102":4501,"CS103":6755,"NT110":1244,"CM241":1411}
instructors = {"CS101":"Haynes","CS102":"Alvarado","CS103":"Rich","NT110":"Burke","CM241":"Lee"}
time = {"CS101":"8:00am", "CS102":"9:00am", "CS103":"10:00am","NT110":"11:00am","CM241":"1:00pm"}

class_c = 1 
instruct = 2
clock = 3

def main():
    again = "Y"                              #search validation
    while again.upper() == "Y":
        choice = menu()
        if choice == class_c:
            user = input("Enter a Class Code: ")
            print()
            room(user)
            print()
            again = input("Search again? (Y/N) ")
        
        elif choice == instruct:
            ask = input("Enter Instructor Last Name: ")
            print()
            instructor(ask)
            print()
            again = input("Search again? (Y/N) ")
        
        elif choice == clock:
            Q = input("Enter Schedule Time (e.g. '2:00pm'): ")
            print()
            tzone(Q)
            print()
            again = input("Search again? (Y/N) ")
        
def room(user):
    if user in rooms:
        print("Class:", user)
        print("Room:", rooms[user])
        print("Instructor:", instructors[user])
        print("Time:", time[user])
    else:
        print("Course not available")
        
def instructor(search):
    instr_lstk = list(instructors.keys())
    instr_lstv = list(instructors.values())
    try:
        position = instr_lstv.index(search)
        c = instr_lstk[position]
        print("Class:", c)
        print("Room:", rooms[c])
        print("Instructor:", search)
        print("Time:", time[c])
        
    except ValueError:
        print("Instructor not found")

def tzone(inp):
    time_lstk = list(time.keys())
    time_lstv = list(time.values())
    try:
        index = time_lstv.index(inp)
        t = time_lstk[index]
        print("Class:", t)
        print("Room:", rooms[t])
        print("Instructor", instructors[t])
        print("Time:", inp)
        
    except ValueError:
        print("Time not available")
        
def menu():
    print("1) Search by Class Code")
    print("2) Search by Instructor Name")
    print("3) Search by Time")
    
    choice = int(input("Enter your choice: "))
    while choice < class_c or choice > clock:
        choice = int(input("Enter a valid choice: "))      #input validation
    return choice
    
main()   


# In[ ]:





# In[ ]:




