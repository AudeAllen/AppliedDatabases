## Python Project
## Author: Audrey Allen
import mysql.connector

global IncreaseorDecrease

def main():  
 

    print ("In Main") 

    global countryStr 
    global rownum 
    global cityid 

    rownum = 0 
    countryStr = "Enter Country:"     
    cityid = "Enter City ID:"
    


    display_menu() 
    while True: 
        print("In main Code")
                   
        Choice = input("Choice:")

        if (Choice == "X"):
            break
        elif (Choice == "x"):
            break
        elif (Choice == "1"):
            rownum = 0 
            Country = view_cities(countryStr)
            print (Country)
            break
        elif (Choice == "2"):                               
            update_population(cityid)
            print (cityid)
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

    global Country 
        
    Country = input(n) 
   
    print(Country)
   

    cursor = db.cursor()
    
       
    cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME =%s order by ci.name limit %s, 3",(Country,rownum))
    
     

    if cursor.fetchall():
         print("Yes record found ") 
       # break                
    else :
         print("This Country does not Exist, Please go back to main menu and enter another:")  
         main()       
         
   
 
    results= cursor.fetchall() 
    print(results)  

    next_two_rows(rownum, Country) 
    
    db.close()
    cursor.close()
    
    
    main()   

## End of Section    

def next_two_rows(rownum,Country):
  
    print (rownum)
    
    rownum = rownum + 2
  
    cursor = db.cursor()


    print ("If you press q you will return to main menu, any other key will return next two cities of the country you entered")

    while True: 
        print("In next two rows")
        print (rownum)
        print (Country)
        rownum = rownum + 2
                   
        Choice = input("Choice:")
      
## Change the m below to not equal to q before you put live

        if (Choice == "q"):
            break
        elif (Choice != "q"):           
            cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME =%s order by ci.name limit %s, 2",(Country,rownum))
            results= cursor.fetchall() 
            print(results) 
                   
def update_population(m): 
    
    import mysql.connector
    
    global cityid 
            
    cityid = input(m) 

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "appdbproj"
    )

    cursor = db.cursor()

    cursor.execute("select ID, name, countrycode, population, longitude, latitude from citycopy where id =%s",(cityid,))
    


    if cursor.fetchall():
         print("Yes record found ")                        
    else :
         print("This City does not Exist, Please go back to main menu and enter another:")  
         update_population(m)

    results= cursor.fetchall() 
    print(results)     

   
    try:
        #IncreaseorDecrease, Amount = input("Enter I if you want to increase population, D for decrease and also enter amount: ").split()
        IncreaseorDecrease = input("Enter I if you want to increase population, D for decrease : ")
        Amount = input("Enter Amount Please : ")        
        print("Increase or Decrease: ", IncreaseorDecrease)
        print("Amount: ", Amount)
    except UnboundLocalError: 
        print("Please enter two parameters I or D and amount:")    
    except ValueError: 
        print("Please enter two parameters I or D and amount:")        

    
    display_menu() 
    while True:            
        

        if (IncreaseorDecrease == "I"):
            IncreasePop = increase_population(cityid,Amount)
            break
                  
      
    db.close()
    cursor.close()

def increase_population(cityid,Amount):
    
    sql_Connector()

    print (" In Increase pop") 
    print (cityid)
    print (Amount)
        

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
    database = "appdbproj",
    consume_results=True
    )

    cursor = db.cursor()

    return db, cursor


if __name__ == '__main__':
   main()
