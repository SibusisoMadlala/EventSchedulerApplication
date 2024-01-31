# 30 January 2024
# Sibusiso Madlala
# Event Scheduler Application version 1
import unittest


class Event:
    
    def __init__(self, title, description, date, time):
        
        self.title = title
        self.description = description
        self.date = date
        self.time = time
    
    ''' setters ''' 
    def set_title(self,title):
        self.title = title
        
    def set_description(self, description):
        self.description = description
    
    def set_date(self,date):
        self.date = date
    
    def set_time(self,time):
        self.time = time
        
    ''' getters '''
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_date(self):
        return self.date
    
    def get_time(self):
        return self.time
    
    ''' compares two events , returns 1 if greater than, returns 0 is equal, and -1 if less'''
    def compare_dates(self, event):
        thisdate = self.get_date()
        thatdate = event.get_date()
        
        thisdaytimeyear = thisdate.split("-")
        thatdaytimeyear = thatdate.split("-")
        
        ''' compare years months and days '''
        if int(thisdaytimeyear[0])==int(thatdaytimeyear[0]):
            
            if int(thisdaytimeyear[1])==int(thatdaytimeyear[1]):
                
                if int(thisdaytimeyear[2])==int(thatdaytimeyear[2]):
                    return 0
                
                elif int(thisdaytimeyear[2])>int(thatdaytimeyear[2]):
                    return 1
                
                else:
                    return -1
            
            elif int(thisdaytimeyear[1])>int(thatdaytimeyear[1]):
                return 1
            
            else:
                return -1
            
        elif int(thisdaytimeyear[0])>int(thatdaytimeyear[0]):
            return 1
        
        else : 
            return -1


    def display_event(self):
        print("title: "+self.title + " "+"description: "+ self.description+" "+"date: "+self.date+" "+"time: "+self.time)
        

global event_list
event_list = []  
    
global valid_time
global valid_date
global valid_title



def insertion_sort(event_list):
    n = len(event_list)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = event_list[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key.compare_dates(event_list[j])==-1:  # Move elements greater than key one position ahead
            event_list[j+1] = event_list[j]  # Shift elements to the right
            j -= 1
        event_list[j+1] = key   

def binary_search(val, array,start, end):
    if start < end:
     
        mid = (start + end) // 2
    
 
        # If element is present at the middle itself
        if array[mid].compare_dates(val)==0 :
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif array[mid].compare_dates(val)==1:
            return binary_search(val, array,start, mid - 1)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(val,array, mid+1, end)
     
    else:    
        return -1
    
    
    
def valid_time(time):
    
    if len(time) ==len("HH:MM"):
        timelist = time.split(":")
        timeformat = "HH:MM".split(":")
        
        if len(timeformat) == len(timelist):
            
            if len(timeformat[0]) == len(timelist[0]) and len(timeformat[1]) == len(timelist[1]):
                
                if timelist[0].isnumeric() and timelist[1].isnumeric():
                    return True
                 
                else:
                    return False
            
            else:
                return False
        
        else:
            return False
        
            
def valid_date(date):
    ''' check length of date '''
    if len(date) == len("YYYY-MM-DD"):
    
        datelist = date.split("-")
        formatlist = "YYYY-MM-DD".split("-")
    
        if len(datelist) == len(formatlist):
            
            if len(datelist[0]) == len(formatlist[0]) and len(datelist[1]) == len(formatlist[1]) and len(datelist[2]) == len(formatlist[2]):
                
                if datelist[0].isnumeric() and datelist[1].isnumeric() and datelist[2].isnumeric:
                    
                    return True
                
                else:
                    return False
            
            else:
                return False
            
        else:
            return False
    
        
  
def create_event(): 
        
    ''' adding event infomation '''
    
        
    ''' check if title exists '''
    title = input("title: ")
    
    ''' verifying date format '''
    date = input("date(YYYY-MM-DD): ")
    while not valid_date(date):
        date = input("Enter date format (YYYY-MM-DD): ")
    
        
    description = input("description: ")
    
            
    '''verifying time format '''    
    time = input("time(HH:MM) :")
    while not valid_time(time):
        time = input("Enter time format (HH:MM): ")
        
    ''' adding event to the list '''
    event_list.append(Event(title,description,date,time))
    insertion_sort(event_list)
    
    print("\nevent created\n")
        
        
def view_event():
    viewprompt = input("insert ALL to view all events, or ONE to view one event\ninsert: ")
        
    if viewprompt.upper() == "ALL":
        for event in event_list:
            event.display_event()
                
    elif viewprompt.upper() == "ONE":
        date = input("please enter date of event: ")
        
        while not valid_date(date):
            date = input("Enter date format (YYYY-MM-DD):")  
            
        event = binary_search(Event("","",date,""),event_list,0,len(event_list))
        
        if event==-1:
            print("event not found")
        else:
            event_list[event].display_event()
    else:
        print("incorrect option")
            
def delete_event():
    deletedate = input("please enter date of the event you wish to delete: ")
    
    while not valid_date(deletedate):
        deletedate = input("Enter date format (YYYY-MM-DD):")
        
    index = binary_search(Event("","",deletedate,""),event_list,0,len(event_list))
    
    if index==-1:
        print("title not found")
    
    else:
        event_list.remove(event_list[index])
        print("event deleted succesfully\n")
        
def edit_event():
    eventdate = input("please enter date of the event you wish to edit: ")
    
    ''' verifying date format '''
    while not valid_date(eventdate):
        eventdate = input("Enter date format (YYYY-MM-DD): ")    
        
    index = binary_search(Event("","",eventdate,""), event_list,0,len(event_list))
    
    if index==-1:
        print("event does not exist")
        
    newtitle = input("Edit title: ")
    newdescription = input("Edit description: ")
        
    newdate = input("Edit date: ")
    while not valid_date(newdate):
        newdate = input("Enter date format (YYYY-MM-DD): ")
            
    newtime = input("Edit time: ")
    while not valid_time(newtime):
        newtime = input("Enter time format (HH:MM): ")
            
    event_list[index].set_title(newtitle)
    event_list[index].set_description(newdescription)
    event_list[index].set_date(newdate)
    event_list[index].set_time(newtime)
    
    event_list[index].display_event()
    insertion_sort(event_list)
    print("Event edited succesfully")
        
def main():   
    while True:
        prompt = input("insert CREATE to add an event, VIEW to view event/s, DELETE to delete an/or event/s, EDIT to edit an event\ninsert: ")
            
        if prompt.upper() == "CREATE":
            create_event()
                
        elif prompt.upper() == "VIEW":
            view_event()
                
        elif prompt.upper() == "DELETE":
            delete_event()
                
        elif prompt.upper() == "EDIT":
            edit_event()
                
        else:
            print("please choose the given options\n")



if __name__ == '__main__':
    main()
