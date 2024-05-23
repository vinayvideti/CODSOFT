contact={}
def display_contact():
  print("NAME\t\tCONTACT NUMBER")
  for key in contact:
    print('{}\t\t{}'.format(key,contact.get(key)[0]))
while True:
  print("1-add contact\n2-search contact\n3-Display contact\n4-Edit contact\n5-Delete contact\n6-Exit")
  choice=int(input("enter your choice:"))
  if choice==1:
    name=input("enter the name:").lower()
    phone=input("enter the phone number:")
    email=input("enter the email:")
    adress=input("enter the adress:")
    contact[name]=[phone,email,adress]
  elif choice==2:
    search_name=input("enter the search name:").lower()
    if (search_name in contact):
      print(search_name,"'s contact number is",contact[search_name][0])
    else:
      print("Name is not found in the contact book")
  elif choice==3:
    if not contact:
      print("empty contact book")
    else:
      display_contact()
  elif choice==4:
    edit_contact=input("enter the contact to be edited:").lower()
    if edit_contact in contact:
      phone=int(input("enter mobile number"))
      contact[edit_contact][0]=phone
      print("contact updated")
      display_contact()
    else:
      print("Name is not found in contact book")
  elif choice==5:
    del_contact=input("enter the contact to be deleted:").lower()
    if del_contact in contact:
      confirm=input("Do you want to delete the contact:y/n?").lower()
      if confirm=='y':
        contact.pop(del_contact)
      else:
        break
      display_contact()
    else:
       print("Name is not found in contact book")
  else:
    break