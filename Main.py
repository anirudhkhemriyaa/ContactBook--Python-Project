print("---- Welcome to Contact book ---- ")


import json 
from json.decoder import JSONDecodeError

 


# ----------Adding contact to json file --------------
def add_contact():

  with open("contact.json" , "r") as file :
    try:
       contact = json.load(file) 
    except JSONDecodeError :
       contact = []

    
    Name = str(input("Enter Name of contact : "))
    Phone = int(input("Enter Phone Number of contact : "))
    if len(str(Phone)) == 10 :
      new_contact = {Name : Phone}
      contact.append(new_contact)

    else:
       print("Please enter correct Phone number")



    with open("contact.json" , "w") as file:
       json.dump(contact , file , indent=4)
    print("Contact added successfully")


    

#-----------Delete  contact----------

def delete_contact(key):
   with open("contact.json" , "r") as file:
      data = json.load(file)

   for contact in data :
      if key in contact:
         contact.pop(key)


   with open('contact.json', 'w') as f:
      json.dump(data, f, indent=4)

   print("contact deleted successfully")
      


#-------- Search for contact ---------

def search_contact(Name):
     with open("contact.json" , "r") as file :
        data = json.load(file)

     for contact in data :
        if Name  in contact :
           print(f"{Name} : {contact[Name]}")
           break
           

     if Name not in contact :
        return 0 
           

      
    
# -------additional feature will be added --------



print("Choose any one for further process  : ")
print("1 for add-contact\n2 for Search for contact\n3 for delete contact")


ans = int(input("Enter for further process : "))
   
if ans == 1:
   add_contact()

if ans == 2:
   search_contact(str(input("Enter Name to search : ")))

if ans == 3 :
   delete_contact(str(input("Enter contact Name : ")))


