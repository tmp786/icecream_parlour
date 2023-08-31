from datetime import datetime

mobile = int(input("Enter Phone Number : "))
name = input("Enter Your Name : ")

#list of items 
Lists ="""
venillacup                         Rs  15/each
choclatecup                        Rs  15/each
strawberrycup                      Rs  15/each
butterscothcup                     Rs  15/each
blackcurrentcup                    Rs  15/each
venillaminicone                    Rs  30/each
choclateminicone                   Rs  30/each
strawberryminicone                 Rs  30/each
butterscothminicone                Rs  30/each
blackcurrentminicone               Rs  30/each
dubbledarkchoclateminicone         Rs  30/each
venillalargecone                   Rs  45/each
choclatelargecone                  Rs  45/each
strawberrylargecone                Rs  45/each
butterscothlargecone               Rs  45/each
blackcurrentlargecone              Rs  50/each
dubbledarkchoclatelargecone        Rs  65/each
venillacake1/2kg                   Rs  200/1/2kg
choclatecake1/2kg                  Rs  240/1/2kg
strawberrycake1/2kg                Rs  220/1/2kg
butterscothcake1/2kg               Rs  240/1/2kg
blackcurrentcake1/2kg              Rs  260/1/2kg
dubbledarkchoclatecake1/2kg        Rs  290/1/2kg
venillacake1kg                     Rs  400/kg
choclatecake1kg                    Rs  450/kg
strawberrycake1kg                  Rs  400/kg
butterscothcake1kg                 Rs  460/kg
blackcurrentcake1kg                Rs  500/kg
dubbledarkchoclatecake1kg          Rs  560/kg
"""




# declaration
Price = 0
Price_List = []
Total_Price = 0
Final_Price = 0
I_List = []
Q_List = []
P_List = []


# rates of items
items = {"venillacup": 15, 
         "choclatecup": 15,
         "strawberrycup": 15,
         "butterscothcup": 15, 
         "blackcurrentcup": 15,
         "venillaminicone": 30, 
         "choclateminicone": 30, 
         "strawberryminicone": 30, 
         "butterscothminicone": 30, 
         "blackcurrentminicone": 30,
         "dubbledarkchoclateminicone": 30,
         "venillalargecone": 45,
         "choclatelargecone ": 45,
         "strawberrylargecone": 45, 
         "butterscothlargecone": 45, 
         "blackcurrentlargecone": 50,
         "dubbledarkchoclatelargecone": 65,
         "venillacake": 200,
         "choclatecake": 240, 
         "strawberrycake": 220,
         "butterscothcake": 240,
         "blackcurrentcake": 260, 
         "dubbledarkchoclatecake": 290, 
         "venillacake": 400,
         "choclatecake": 450,
         "strawberrycake": 400, 
         "butterscothcake": 460,
         "blackcurrentcake": 500, 
         "dubbledarkchoclatecake": 560 }
         
option = input("For list of items press Enter")

if option == 1:
    print(Lists)
for k in range(len(items)):
    buyer1 = int(input("If You Want Buy Press1 or 2 For Exit : "))
    if buyer1 == 2:
        break
    if buyer1 == 1:
        item = input("Enter Your items : ")
        quantity = int(input("Enter Quantity : "))
        if item in items.keys():
            Price = quantity*(items[item])
            Price_List.append(items[item])
            Total_Price = Total_Price + Price
            I_List.append(item)
            Q_List.append(quantity)
            P_List.append(Price)
            gst = (Total_Price*5)/100
            final_price = gst+Total_Price
        else:
            ("Sorry you entered item is not available")
    else:
        print("You Entered Wrong Number")
    buyer = input("Can i Bill the items yes or no : ")
    if buyer== "yes":
        pass
        if final_price!=0:
         print(25* "=","p4 market",25*"=")
         print(28* "=","Cold Weather",25*"=")
         print("name:", name, 30* " ", "date:", datetime.now())
         print(75* "_")
         print("sno", 8* " ", "items", 8*" ", "quantity", 3* " ", "price")
         for k in range(len(Price_List)):
             print(k, 4* " ",5* ' ', I_List[k],  10* " ", Q_List[k],  8* " ",  P_List[k] )
        print(75* "_")
        print(50* " ", "TotalAmount:", "RS", Total_Price )
        print("gst amount", 50* " ", "Rs", gst)
        print(75*"-")
        print(50* " ", "FinalAmount:", "Rs", Final_Price)
        print(75*"-")


           
    



