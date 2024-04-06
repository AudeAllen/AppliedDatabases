## Python Project
## Author: Audrey Allen
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "appdbproj"
)

def main():  

    print ("In Main") 

    countryStr = "Enter Country:"

    while True: 
        display_menu()   
        Choice = input("Choice:")

        if (Choice == "X"):
            break
        elif (Choice == "1"):
            Country = view_cities(countryStr)
            print (Country)
            


def display_menu():
    print ("In Display Menu") 
    print("")
    print("======================================================")
    print("                           Menu                       ") 
    print("======================================================")
    print("1. View Cities by Country")
    print("2. Update City Population") 
    print("3. Add New Person") 
    print("4. Delete Person")
    print("5. View Countries by population")
    print("6. Show Twinned Cities")
    print("7. Twin with Dublin")
    print("X. Exit Application")
   
## View Cities Function
def view_cities(n):  

    
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "appdbproj"
    )

    print ("In view_cities") 
   
    Country = input(n) 
    print(Country)
   
    cursor = db.cursor()

    cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME =%s order by ci.name limit 2", (Country,) )

    if cursor.fetchone():
         print("Yes record found ")
    else :
         print("This Country does not Exist, Please Enter another:")
         error_country()
        


    results= cursor.fetchall() 
    print(results)


    db.close()
    cursor.close()


def sql_Connector():

    print ("In sql_Connector") 

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "appdbproj"
    )

def error_country():

    print ("In error country")

    countryStr = "Enter Country:"

     

    while True: 
        
            Country = view_cities(countryStr)
            print (Country)
            break







if __name__ == '__main__':
   main()
