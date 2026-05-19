events=[]
from datetime import datetime

def add_event():
    #Role of this fn:Data creation+storage
    #This fn does not return data/mutate storage
    print("1.Login_failed")
    print("2.USB_connected")
    print("3.Files_deleted")

    choice=input("Enter the choice ")

    if choice=="1":
        name="Login_failed"
        severity="HIGH"

    elif choice=="2":
        name="USB_connected"
        severity="LOW"
        
    elif choice=="3":
        name="Files_deleted"
        severity="HIGH"

    else:
        print("Invalid input")
        return
        
    account_name=input("Enter the name of the user")
    # event variable har iteration me new dictionary ko point karta hai
    # purani value overwrite ho jati hai
    # hum multiple dictionaries create nahi kar rahe
    # variables are references in the python,here event isnt dictionary but object reference of dictionary 

    event={
        "user":account_name,
        "name":name,
        "severity":severity,
        "timestamp":datetime.now()
    }

    events.append(event)

def show_events():
    
    for event in events:
        print(event["user"] + "\n") 
        print(event["name"] + "\n") 
        print(event["severity"] + "\n")
        print(event["timestamp"] + "\n")
        

def search_user():
    value=input("Enter the account user you want to search").lower()
    for event in events:
        if value in event["user"].lower():
            print(event["name"]+"\n"+event["severity"])

def sus_activity():
    n="Login_failed"
    c=0
    for event in events:
        if n in event["name"]:
            c+=1
        
    if c>5:
        print("WARNING!!!")
# structure is better in complex
#one function = one job
#If I can understand whole logic in 10–15 lines → don’t split
#If it starts feeling messy → then split

def severity_filter_view():
    high_s=[]
    for event in events:
        if event["severity"]=="HIGH":
            high_s.append(event)
    result=severity_filter_view()
    #returned value needs to be stored,which can be used outside the fn too
    return high_s
#return has nothing to with parameters



def freq_tracker():
    event_count={
        
    }
  
    #whenever you make list , ask will you need items of it in future or just count
    #if you need count simply use counter,don't waste memory
    #Store only what you need
    #outside loop ->storage structure initialize
    #inside loop-> process data
    #event is a pointer refering to current dictionary,in every iteration it points to new object
    for event in events:
        event_name = event["name"]
        #To access a dictionary value, you must provide the key.
        if event_name in event_count:
            event_count[event_name]+=1
            #if in [] string is written within quotes then it means key name is "string"
            #without quotes it uses variable as key
                     
        else:
            #create new key-value pair,as key doesnt exist in event count
            event_count[event_name]=1
            #update value

    print(event_count)
    
def show_menu():
        #Menu systems are loops Not functions.
        while True:
            print("\n--- EVENT SYSTEM MENU ---")
            print("1. Add Event")
            print("2. Show All Events")
            print("3. Search User")
            print("4.Suspicious activity")
            print("5. Severity Check")
            print("6. Frequency Report")
            print("7. Exit")

            choose=int(input("Enter the number of your choice"))

            if choose==1:
                 add_event()
            elif choose==2:
                show_events()
            elif choose==3:
                search_user()
            elif choose==4:
                sus_activity()
            elif choose==5:
                severity_filter_view()
            elif choose==6:
                freq_tracker()
            elif choose==7: 
                print("Exiting program...")
                break

            else:
                print("Invalid choice")

show_menu()


    




            



