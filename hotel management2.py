import random
from datetime import datetime
name=[]
phoneno=[]
address=[]
room=[]
price=[]
roomno=[]
cid=[]
i=0
def Home():
    print("-----------VELVET VIBE HOTEL MANANGEMENT-------------")
    print("\t\t 1 ROOM DETAILS \n")
    print("\t\t 2 BOOKING\n")
    print("\t\t 3 ROOM IFORMATION \n")
    print("\t\t 4 ROOM SERVICES \n")
    print("\t\t 5 PAYMENT \n")
    print("\t\t 0 exit\n")

    a=int(input("ENTER YOURS CHOICE :"))
    if(a==2):
          print(" ")
          booking()
    elif(a==3):
          print(" ")
          roominfo()
    elif(a==1):
          print(" ")
          roomdetail()
    elif(a==4):
          print(" ")
          roomserv()
    elif(a==5):
          print(" ")
          payment()
    else:
        exit()       
def booking():
          print("----BOOKING SECTION----")
          name=str(input("ENTER YOUR NAME :"))
          phoneno=int(input("ENTER YOUR PHONE NUMBER :"))
          address=str(input("ENTER YOUR ADDRESS :"))
          date_str=input("enter checkin date (YYYY-MM-DD):")
          date1=datetime.strptime(date_str,'%Y-%m-%d')
          date__str=input("enter checkout date (yyyy-MM-DD):")
          date2=datetime.strptime(date__str,'%Y-%m-%d')
          n=int(input("ENTER 0 TO CONTINUE:\n-->"))
          if n==0:
                roominfo()
          else:
              exit()
def roominfo():
    print("----SELECT ROOM TYPE----")
    b=int(input("Enter 1 for AC-room 0 for NON AC-room -->"))
    if b==1:
          print("1.3-BED")
          print("2.2-BED")
          print("3.1-BED")
          print("press 0 for Room prices")
          c=int(input("-->"))
          if c==0:
              print("1.3-BED # price-->Rs.5000")
              print("2.2-BED # price-->Rs.4000")
              print("3.1-BED # price-->Rs.3000")
              print(" ENTER ROOM TYPE ")
              c=int(input("-->"))
              if c==1:
                  room.append('AC 3-BED')
                  print("ROOM TYPE:AC 3-BED")
                  price.append(5000)
                  print("price--Rs.5000")
              elif c==2:
                  room.append('AC 2-BED')
                  print("ROOM TYPE:AC 2-BED")
                  price.append(4000)
                  print("price--Rs.4000")
              elif c==3:
                  room.append('AC 1-BED')
                  print("ROOM TYPE:AC 1-BED")
                  price.append(3000)
                  print("price--Rs.3000")
              else:
                  print("wrong choice")
                  
    elif b==0:
          print("1.3-BED")
          print("2.2-BED")
          print("3.1-BED")
          print("press 0 for Room prices")
          c=int(input("-->"))
          if c==0:
              print("1.3-BED # price-->Rs.2000")
              print("2.2-BED # price-->Rs.1500")
              print("3.1-BED # price-->Rs.1000")
              print(" ENTER ROOM TYPE ")
              c=int(input("-->"))
              if c==1:
                  room.append('AC 3-BED')
                  print("ROOM TYPE:AC 3-BED")
                  price.append(2000)
                  print("price--Rs.2000")
              elif c==2:
                  room.append('AC 2-BED')
                  print("ROOM TYPE:AC 2-BED")
                  price.append(1500)
                  print("price--Rs.4000")
              elif c==3:
                  room.append('AC 1-BED')
                  print("ROOM TYPE:AC 1-BED")
                  price.append(1000)
                  print("price--Rs.1000")
              else:
                  print("wrong choice")
    else:
        print("wrong choice")
    randnum=random.randrange(40)+300
    custid=random.randrange(40)+5000
    while randnum in roomno or custid in cid:
        randnum=random.randrange(60)+300
        custid=randdom.randrange(60)+300
    print(" \t\t YOUR ROOM BOOKED SUCCESSFULLY\t\t")
    print("your room number -->",randnum)
    print("your customer id -->",custid)
    print("ENTER 0 TO CONTINUE-->")
    n=int(input(""))
    if n==0:
          roomserv()
    else:
        exit()
def roomdetail():
    c=int(input("ENTER 1 FOR DETAILS ABOUT AC ROOM AND 0 FOR NON AC ROOM-->"))
    if c==1:
       print("DETAIL ABOUT AC ROOMS")
       print("Room Size: 400 square feet\nAmenities:\n\n->King-size bed\n->Private balcony\n->Flat-screen TV with cable channels\n->Minibar\n->Coffee maker\n->Air conditioning\n->Free Wi-Fi\n->Work desk\n->In-room safe\n->Iron and ironing board\n->Hairdryer\n->Complimentary bottled water\n->Bathrobes and slippers\n\n----Additional Services:\n->24-hour room service\n->Daily housekeeping\n->Laundry and dry-cleaning services\n->Wake-up call service\n->Concierge assistance\n->Airport shuttle (upon request, additional charges may apply)")
       from PIL import Image
       img_path=r"D:\python project\image\WhatsApp Image 2024-03-20 at 17.52.18_59097c50.jpg"
       img=Image.open(img_path)
       img.show()
    elif c==0:
        print("DETAILS ABOUT NON AC ROOM")
        print("Room Size: 250 square feet\n->Amenities:\n\n->Double bed\n->Window with views of the surrounding area\n->Flat-screen TV with cable channels\n->Air conditioning\n->Free Wi-Fi\n->Work desk\n->In-room safe\n->Iron and ironing board (upon request)\n->Hairdryer\n->Complimentary toiletries\n\n----Additional Services:\n->24-hour room service\n->Daily housekeeping\n->Laundry service (additional charges may apply)\n->Wake-up call service\n->Concierge assistance")
        from PIL import Image
        img_path=r"D:\python project\image\WhatsApp Image 2024-03-20 at 18.03.12_fe13ce2f.jpg"
        img=Image.open(img_path)
        img.show()
    else:
         print("Wrong choice")    
    print("ENTER 0 TO CONTINUE:")
    n=int(input())
    if n==0:
        booking()
    else:
        exit()
                  
                  
Home()          
               
        
          
          
