## Python Project
## Author: Audrey Allen
import mysql.connector



def main():  
    sql_Connector()

    print ("In Main") 

    countryStr = "Enter Country:"
    display_menu() 
    while True: 
        print("In main Code")
        sql_Connector()
           
        Choice = input("Choice:")

        if (Choice == "X"):
            break
        elif (Choice == "1"):
            Country = view_cities(countryStr)
            print (Country)
            break
            


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
    
    sql_Connector()
    print ("In view_cities") 
   
    Country = input(n) 
    print(Country)
   
    
    cursor = db.cursor()
    
    cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME =%s order by ci.name limit 2", (Country,) )

    if cursor.fetchone():
         print("Yes record found ") 
       # break                
    else :
         print("This Country does not Exist, Please go back to main menu and enter another:")  
         main()       
         
   
 
    results= cursor.fetchall() 
    print(results)   
    main()   


    db.close()
    cursor.close()



def sql_Connector():
    import mysql.connector
    print ("In sql_Connector") 

    global db
    global host
    global User
    global password
    global database

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "appdbproj"
    )

    cursor = db.cursor()

    return db, cursor


if __name__ == '__main__':
   main()
