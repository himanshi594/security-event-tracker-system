events=[]

def add_event():
    print("1.Login_failed")
    print("2.USB_connected")
    print("3.Files_deleted")

    choice=input("Enter the choice ")

    if choice=="1":
        name="Login_failed"
        severity="HIGH"

    if choice=="2":
        name="USB_connected"
        severity="LOW"
        
    if choice=="3":
        name="Files_deleted"
        severity="HIGH"
        
    account_name=input("Enter the name of the user")
    
    event={
        "user":account_name,
        "name":name,
        "severity":severity
    }

    events.append(event)

def show_events():
    for event in events:
        print(event["user"] + "\n") 
        print(event["name"] + "\n") 
        print(event["severity"] + "\n")   

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
# shortcut is better in small program , structure is better in complex
#one function = one job
#If I can understand whole logic in 10–15 lines → don’t split
#If it starts feeling messy → then split

def severity_filter_view():
    high_s=[]
    for event in events:
        if event["severity"]=="HIGH":
            high_s.append(event)
    return high_s

def freq_tracker():
    login_f=[]
    usb=[]
    files_del=[]

    for event in events:
        if event["name"]=="Login_failed":
            login_f.append(event)
            
        elif event["name"]=="USB_connected":
            usb.append(event)
        elif event["name"]=="Files_deleted":
            files_del.append(event)

    result= {
        "login failed":len(login_f),
        "usb_connected":len(usb),
        "files deleted":len(files_del)
    }

              

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


    




            



