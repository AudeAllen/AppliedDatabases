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
        elif (Choice == "3"):                               
            add_newperson()            
            break
        elif (Choice == "4"):                               
            delete_person()            
            break
        elif (Choice == "5"):                               
            show_population()            
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
    
   
    cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME =%s order by ci.name limit %s, 3",(Country ,rownum))
    
    results= cursor.fetchall() 
    print(results) 

    if cursor.rowcount > 0: 
         print ("Record Found")  
         next_two_rows(rownum, Country)                              
    else :
         print("This Country does not Exist, Please enter another:")  
         view_cities(n)
     
    main()   
       
    db.close()
    cursor.close()
    
         

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
    
    results= cursor.fetchall() 
    print(results)  

    NumRows = cursor.rowcount   
    print (NumRows)   
  

    if cursor.rowcount > 0: 
         print ("Record Found")                                
    else :
         print("This City does not Exist, Please go back to main menu and enter another:")  
         update_population(m)
    
    while True:
        IncreaseorDecrease = input("Enter I if you want to increase population, D for decrease : ")
        if IncreaseorDecrease not in ('I', 'D'):
                print("Not an appropriate choice. Please choose again")
        else:
                break  
        
    while True:
        Amount = float(input(" Please enter Amount:"))
        if not isinstance(Amount, float):
                print("Must be an integer value")
        elif (IncreaseorDecrease == "I"):
            IncreasePop = increase_population(cityid,Amount) 
            break   
        elif (IncreaseorDecrease == "D"):
            IncreasePop = decrease_population(cityid,Amount) 
            break          
        else: 
            break    
                   
         
    db.close()
    cursor.close()

def increase_population(cityid,Amount):

    print ("In increase population")

    import mysql.connector
      
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "appdbproj",
        autocommit=True
    )

    cursor = db.cursor()

    print (cityid)
    print(Amount)

    
    cursor.execute("UPDATE citycopy SET population = population + %s where id =%s",(Amount,cityid,))
    

    Rownumber =cursor.rowcount 
    print(Rownumber)
    results= cursor.fetchall() 
    print(results)  

    print('Just about to close out')
    db.close()
    cursor.close()

    main()

def decrease_population(cityid,Amount):

    print ("In decrease population")

    import mysql.connector
      
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "appdbproj",
        autocommit=True
    )

    cursor = db.cursor()

    print (cityid)
    print(Amount)

    
    cursor.execute("UPDATE citycopy SET population = population - %s where id =%s",(Amount,cityid,))
    

    Rownumber =cursor.rowcount 
    print(Rownumber)
    results= cursor.fetchall() 
    print(results)  

    print('Just about to close out')
    db.close()
    cursor.close()
   
    main()

def add_newperson():  
    import mysql.connector
    sql_Connector()

    global userid
    global firstlastname
    global Age
    global salary
    global personcityid
    
    while True:
         try:
              userid = int(input("Please Enter a UserID: ")) 
              break              
         except ValueError:
              print("Invalid input. Please enter a valid integer.")

    while True:
         try:
              firstlastname = input("Please Enter your First and Last Name: ") 
              int(firstlastname)               
              print("Invalid input. Please enter a string value.")                                         
         except ValueError:
              break
         
    while True:
         try:
              Age = int(input("Please Enter the Persons Age: ")) 
              break              
         except ValueError:
              print("Invalid input. Please enter a valid integer.")
     
    while True:
         try:
              salary = float(input("Please Enter the Persons Salary: ")) 
              break              
         except ValueError:
              print("Invalid input. Please enter a valid integer.")     

    while True:
         try:
              personcityid = int(input("Please Enter the CityID: ")) 
              break              
         except ValueError:
              print("Invalid input. Please enter a valid integer.")                           

    print(f"You have chosen the following to add to the database, userid = {userid}  Fullname = {firstlastname}  Age ={Age} Salary = {salary} CityID = {personcityid}!")

    cursor = db.cursor()

    cursor.execute("select PersonID from person where PersonID =%s",(userid,))
            
    results= cursor.fetchall() 
    print(results)  

    NumRows = cursor.rowcount   
    print (NumRows)   
        

    if cursor.rowcount > 0: 
            print (f"This user id {userid} already exists you will be returned to Main Menu")
            main()                                       
    else :
        print("User ID does not exist, Good job!!")  

    cursor = db.cursor()

    cursor.execute("select ID from citycopy where id =%s",(personcityid,))
            
    results= cursor.fetchall() 
    print(results)  

    NumRows = cursor.rowcount   
    print (NumRows)   
        

    if cursor.rowcount > 0: 
            print (f"This city id {personcityid}  exists")                                                     
    else :
        print (f"This city id {personcityid} does not exist you will be returned to Main Menu")
        main() 
              


    cursor = db.cursor()

    cursor.execute("Insert into person (personid, personname, age, salary, city)VALUES (%s,%s, %s, %s,%s)",(userid,firstlastname,Age,salary,personcityid,))

    Rownumber =cursor.rowcount 
    print(Rownumber)
    results= cursor.fetchall() 
    print(results) 


    db.close()
    cursor.close()

def delete_person():
     
     import mysql.connector
     sql_Connector()

    
    
     while True:
         try:
              userid = int(input("Please Enter the UserID of the person you wish to delete: ")) 
              break              
         except ValueError:
              print("Invalid input. Please enter a valid integer.")

    
     print(f"You have chosen to delete the following person from the database, userid = {userid}!")

     cursor = db.cursor()

     cursor.execute("select * from person where personid =%s",(userid,))
                
     results= cursor.fetchall() 
     print(results)  

  
     if cursor.rowcount > 0: 
            print (f"This user id {userid} exists")                                                              
     else :
        print("User ID does not exist so cannot perform delete operation!!") 
        main()
                  

     cursor.execute("select * from person person inner join hasvisitedcity hasvisitedcity on person.personid = hasvisitedcity.personid where  hasvisitedcity.personid =%s",(userid,))
     
     results= cursor.fetchall() 
     print(results)
     if cursor.rowcount > 0: 
            print (f"This user id {userid} exists but has visited a city so cannot be deleted")
            main()                                                  
     else :
        print("User ID can be deleted!!") 
        
        cursor = db.cursor()

        cursor.execute("delete from person where personid =%s",(userid,))
                
        results= cursor.fetchall() 
        print(results)  

        main()

     db.close()
     cursor.close() 

def show_population():
     
    import mysql.connector
    sql_Connector()

    while True:
        populationsymbol = input("Please Enter > OR < or = and you will shown Countries Population in regards to the symbol chosen: ")
        if populationsymbol not in ('>', '<', '='):
                print("Not an appropriate choice. Please choose again")
        else:
                break  

    while True:
         try:
              populationamount = int(input("Please Enter a Population Amount: ")) 
              break              
         except ValueError:
              print("Invalid input. Please enter a valid integer.")             

    cursor = db.cursor()
  


    if populationsymbol == '>':
        print ("going to execute sql statement")
        cursor.execute("select code,name, continent, population from country where population > %s",(populationamount,))
        results= cursor.fetchall() 
        print(results)    
    elif   populationsymbol == '<':  
         cursor.execute("select  code,name, continent, population from country where population < %s",(populationamount,))
         results= cursor.fetchall() 
         print(results)
    elif  populationsymbol == '=':   
         cursor.execute("select  code,name, continent, population from country where population = %s",(populationamount,))
         results= cursor.fetchall() 
         print(results)
    else:
         print("Invalid Option Chosen:")
       
    
    if cursor.rowcount > 0: 
            print (f"The countries with a population {populationsymbol} {populationamount} are ")                                                              
    else :
        print("There are no countries with a population {populationsymbol} {populationamount} !!") 
       


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
    consume_results=True,
    autocommit=True
    )

    cursor = db.cursor()

    return db, cursor


if __name__ == '__main__':
   main()
