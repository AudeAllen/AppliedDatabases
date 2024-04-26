## Python Project
## Author: Audrey Allen
import mysql.connector

global IncreaseorDecrease

def main():  

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
            exit()
        elif (Choice == "x"):
            exit()
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
        elif (Choice == "6"):                               
            show_twinned_cities()            
            break
        elif (Choice == "7"):                               
            twin_with_dublin()            
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
   
    global Country 
        
    Country = input(n) 
   

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

    cursor.execute("select ID, name, countrycode, population, longitude, latitude from city where id =%s",(cityid,))
    
    results= cursor.fetchall() 
    print(results)  

    NumRows = cursor.rowcount   
     
  

    if cursor.rowcount > 0: 
         print ("Record Found")                                
    else :
         print("This City does not Exist, Please go back to main menu and enter another:")  
         update_population(m)
    
    while True:
        IncreaseorDecrease = input("Enter I or i if you want to increase population, D or d for decrease : ")
        if IncreaseorDecrease not in ('I', 'D','i','d'):
                print("Not an appropriate choice. Please choose again")
        else:
                break  
        
    while True:
        Amount = float(input(" Please enter Amount:"))
        if not isinstance(Amount, float):
                print("Must be an integer value")
        elif (IncreaseorDecrease == "I" or IncreaseorDecrease == "i"):
            IncreasePop = increase_population(cityid,Amount) 
            break   
        elif (IncreaseorDecrease == "D" or IncreaseorDecrease == "d"):
            IncreasePop = decrease_population(cityid,Amount) 
            break          
        else: 
            break    
                   
         
    db.close()
    cursor.close()

def increase_population(cityid,Amount):
    import mysql.connector
      
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "appdbproj",
        autocommit=True
    )

    cursor = db.cursor()

   
    cursor.execute("UPDATE city SET population = population + %s where id =%s",(Amount,cityid,))
    
    Rownumber =cursor.rowcount 
    
    results= cursor.fetchall() 
  

    cursor.execute("select name, population from city where id =%s",(cityid,))

    results= cursor.fetchall() 
   

    # print the results in each row
    for r in results: 
             
        cityname = (r[0])  
        citypop = (r[1])      
     
    
    print(f"You have increased the population of city {cityname}  by  {Amount}! The new population of {cityname} is {citypop} ")
    
    db.close()
    cursor.close()

    main()

def decrease_population(cityid,Amount):

   

    import mysql.connector
      
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "appdbproj",
        autocommit=True
    )

    cursor = db.cursor()
      
    cursor.execute("UPDATE city SET population = population - %s where id =%s",(Amount,cityid,))
    
    Rownumber =cursor.rowcount 
    
    results= cursor.fetchall() 
     

    cursor.execute("select name, population from city where id =%s",(cityid,))

    results= cursor.fetchall() 
    

    # print the results in each row
    for r in results:                   
        cityname = (r[0])  
        citypop = (r[1])      
     
    
    print(f"You have decreased the population of city {cityname}  by  {Amount}! The new population of {cityname} is {citypop} ")
    
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

    cursor.execute("select ID from city where id =%s",(personcityid,))
            
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
       
def show_twinned_cities():
    
    neo4jconnection()

    with driver.session() as session:
        values = session.read_transaction(display_twinned_cities)

    driver.close()    


def display_twinned_cities(tx):

    query = "MATCH(n:City)-[r:TWINNED_WITH]->(C:City) return n.name, r.type, C.name order by n.name"    
    results = tx.run(query)   
    print ("Twinned Cities")
    print ("===============")  
    for result in results:                       
        print  (result['n.name'] + "<------------>" + result['C.name'])

def twin_with_dublin():

    sql_Connector()
    neo4jconnection()
    from neo4j import exceptions

    global cityname
    global neo4jcityid
     
    while True:
         try:
              neo4jcityid = int(input("Please Enter a CityID that you would like to twin with Dublin: ")) 
              break              
         except ValueError:
              print("Invalid input. Please enter a valid integer.") 

    cursor = db.cursor()
    
    cursor.execute("select ID, name from city where id =%s",(neo4jcityid,))
             
    results= cursor.fetchall() 
    print(results) 

    # print the results in each row
    for r in results:        
        print(r[0])
        print(r[1])
        cityname = (r[1])
        print(cityname)
        
    NumRows = cursor.rowcount   
    print (NumRows)  


    if cursor.rowcount > 0: 
            print (f"This city id {neo4jcityid}  exists")                                                     
    else :
        print (f"This city id {neo4jcityid} does not exist please enter another ID")
        twin_with_dublin()  
   
    

    with driver.session() as session:
                values = session.read_transaction(display_does_city_exist,cityname)  

     
    driver.close() 
     


def display_does_city_exist(tx,cityname):
        from neo4j import exceptions
        print("In display_does_city_exist read section")
               
       
        results =  tx.run("MATCH (u:City {name: $cityname}) "
           "WITH COUNT(u) > 0  as node_exists "        
           "RETURN node_exists",
            cityname=cityname)
        for result in results:                       
         print  (result['node_exists']) 
 
        print("error message")     

        while True:
            if (result['node_exists']) == True:
                print("This city already exists so will be just twinned not created")
                with driver.session() as session:
                    try:    
                        session.write_transaction(create_twinonly_with_dublin, cityname, neo4jcityid)
                        main()    
                    except exceptions.ClientError as e:               
                        print (e)               
            elif (result['node_exists']) == False:
                print("City does not exist - YAY!!") 
                with driver.session() as session:
                    try:    
                        session.write_transaction(create_cityandtwin_with_dublin, cityname, neo4jcityid)
                        main()    
                    except exceptions.ClientError as e:               
                        print ("Error Parameters are not valid")
            else:          
                break

    
            driver.close()        

                       

def create_cityandtwin_with_dublin(tx,cityname,neo4jcityid):
   
    from neo4j import exceptions
       
    print("In create_twin_with_dublin section")

   
    tx.run("MATCH(u:City {name:'Dublin'}) "
                "CREATE(p:City {name:$cityname, cid:$neo4jcityid})"        
                "CREATE(p)-[w:TWINNED_WITH]->(u)",
                    cityname=cityname, neo4jcityid=neo4jcityid) 
    print (f"{cityname} is now created and is twinned with Dublin")          
           

def create_twinonly_with_dublin(tx,cityname,neo4jcityid):  

        from neo4j import exceptions
        print("In create_twinonly_with_dublin")
        print(cityname)

   
        results =  tx.run("OPTIONAL MATCH (c:City{name:'Dublin'})<-[r]->(n:City{name: $cityname}) "                  
            "RETURN c, r IS NOT NULL as isTwinned",
                cityname=cityname)        
        for result in results: 
             print("Just printing istwinned")                          
             print  (result['isTwinned']) 
   
        print("Just leaving the section")

        print(cityname)
        print(neo4jcityid)
           
       # while True:
        if (result['isTwinned']) == True:
                            print ("In bit I dont want ")
                            print("This city already twinned with Dublin so you will return to Main Menu")
                            main()
        elif (result['isTwinned']) == False:
                print ("In bit I want ")
                with driver.session() as session:
                    try:    
                        session.write_transaction(twin_with_dublin_as_exists, cityname, neo4jcityid)
                        main()    
                    except exceptions.ClientError as e:               
                        print ("Error Parameters are not valid")
                         
                                        
        else:
            print("Going back to Main Menu")
            main()            

            print("Just leaving the section2")
    
def twin_with_dublin_as_exists(tx,cityname, neo4jcityid):
       from neo4j import exceptions

       print ("in test") 

       results = tx.run("MATCH(u:City {name:'Dublin'})"
                        "MATCH(c:City {name:$cityname, cid:$neo4jcityid}) "                   
                        "CREATE(u)-[w:TWINNED_WITH]->(c)",
                        cityname=cityname, neo4jcityid=neo4jcityid) 
       
       print (f"Dublin is now twinned with {cityname}") 
       for result in results: 
                        print("Just in results")                          
                        print  (result['w'])    

                                
     
def neo4jconnection():
       
 from neo4j import GraphDatabase
 from neo4j import exceptions

 drivr = None

 global driver
     
 uri ="neo4j://localhost:7687" 
 driver = GraphDatabase.driver(uri, auth=("neo4j", "Brokercrm123!"), max_connection_lifetime=1000) 


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
