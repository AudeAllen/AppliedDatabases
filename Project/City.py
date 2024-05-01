## Python Project
## Author: Audrey Allen
## Course: Applied Databases
## Lecturer: Gerard Harrison
## Due Date: May 6th 2024

import mysql.connector
import mysql.connector.errorcode
# The python package rich can change the font colour for the output
from rich.console import Console
console = Console()


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
                        
        Choice = input("Choice:")

        if (Choice == "X"):
            console.print('[bright_green]Goodbye!!! You are now exiting the program!!! [/bright_green]', highlight=False) 
            exit()            
        elif (Choice == "x"):
            console.print('[bright_green]Goodbye!!! You are now exiting the program!!! [/bright_green]', highlight=False)
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
    print("")
    print("======================================================")
  #  print("                           Menu                       ") 
    console.print('[green]                           Menu                       [/green]', highlight=False)
    print("======================================================")  
    console.print('[blue]1. View Cities by Country[/blue]', highlight=False)    
    console.print('[chartreuse2]2. Update City Population[/chartreuse2]', highlight=False)    
    console.print('[orchid]3. Add New Person[/orchid]', highlight=False)    
    console.print('[gold1]4. Delete Person[/gold1]', highlight=False)    
    console.print('[dark_olive_green2]5. View Countries by population[/dark_olive_green2]', highlight=False)    
    console.print('[light_steel_blue]6. Show Twinned Cities[/light_steel_blue]', highlight=False)    
    console.print('[dark_slate_gray1]7. Twin with Dublin[/dark_slate_gray1]', highlight=False)   
    console.print('[bright_red]X. Exit Application[/bright_red]', highlight=False)
   
## View Cities Function
def view_cities(n):  

# This function returns country name, city name, district and city population of the country that is input
# Can either enter full country name or a partial name
# If a country name is entered that does not exist then an error message will appear to the user        
      
    sql_Connector()
   
    global Country 
        
    Country = input(n) 

    console.print('[blue]'+Country+'[/blue]', highlight=False) 
   

    cursor = db.cursor()
    
    cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME like %s order by ci.name limit %s, 3",("{}%".format(Country),rownum))
    
    # This returns the result from the mysql query   
    results= cursor.fetchall()       
    print(results) 
    
    if cursor.rowcount > 0:  
        def get_first_element_using_map(tuples_list):
            first_elements = list(map(lambda x: x[0], tuples_list))
            Country =  first_elements[0]  
           # print(Country)
            cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME like %s order by ci.name limit %s, 3",("{}%".format(Country),rownum)) 
            results= cursor.fetchall() 
            print(results) 
            next_two_rows(rownum, Country)
            print(f"The first elements of the list are: {get_first_element_using_map(results)}")             
            print  (first_elements[0])                            
            return first_elements[0]   
                                       
    # the function next_two_rows is called here and if any key other than 'q' (returns to main menu)  the 
    # next two cities from that country is shown      
              
        next_two_rows(rownum, Country)                                      
    else :
         print("Your country does not exist please choose again but be more specific!!!:")  
         view_cities(n)
     
    main()   

    # Close out the connection to the database
   
    db.close()
    cursor.close()
    
      

def next_two_rows(rownum,Country):
  
  # Add 2 onto the variable rownum as the next two rows must be shown 
      
    rownum = rownum + 2
  
    cursor = db.cursor()


    print ("If you press q you will return to main menu, any other key will return next two cities of the country you entered")

    while True: 
      
        rownum = rownum + 2
                   
        Choice = input("Choice:")
      
## If option is q user will be returned to main menu otherwise next two cities of that country will be shown to the user

        if (Choice == "q"):
            main()
        elif (Choice != "q"):          
           
            cursor.execute("SELECT CO.NAME AS 'Country Name', ci.name as 'City Name', ci.district as 'City District', ci.population as 'City Population' FROM COUNTRY CO INNER JOIN CITY CI ON CO.CODE = CI.COUNTRYCODE  where CO.NAME like %s order by ci.name limit %s, 2",("{}%".format(Country),rownum))
            results= cursor.fetchall() 
            print(results) 

        if cursor.rowcount == 0:   
             main()
        else:  
           results= cursor.fetchall() 
          # print(results)           
                   
def update_population(m): 
    
    import mysql.connector
    
    global cityid 
            
    cityid = input(m) 
   
   # Connection to mysql database is made

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "appdbproj"
    )

    cursor = db.cursor()
    
    # Extract ID, name, countrycode, population, long and lat from cityid that is entered by the user

    cursor.execute("select ID, name, countrycode, population, longitude, latitude from city where id =%s",(cityid,))
    
    results= cursor.fetchall() 
    print(results)  

    NumRows = cursor.rowcount   
     
  # If the city does not exist go back and enter another city id 

    if cursor.rowcount > 0: 
         print ("Record Found")                                
    else :
         print("This City does not Exist, Please go back and enter another city id please:")  
         update_population(m)
    

    # User is asked whether or not they wish to increase or decrease the population of the city chosen

    while True:
        IncreaseorDecrease = input("Enter I or i if you want to increase population, D or d for decrease : ")
        if IncreaseorDecrease not in ('I', 'D','i','d'):
                print("Not an appropriate choice. Please choose again")
        else:
                break  
        
    # User is asked by how much they wish to increase or decrease the population of that city 
    # Some error handling also in this piece of code
    # Depending on   
    
    while True:
      try:    
        Amount = float(input(" Please enter Amount:"))
        if not isinstance(Amount, float):
                print("Must be an integer value")
        elif (IncreaseorDecrease == "I" or IncreaseorDecrease == "i"):
            IncreasePop = increase_population(cityid,Amount) 
            break   
        elif (IncreaseorDecrease == "D" or IncreaseorDecrease == "d"):
            IncreasePop =   (cityid,Amount) 
            break          
        else: 
            break
      except  ValueError as err: 
           print (f"Error: {err}")   
                   
         
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
   

    # print the results in each row - Get new population of the city after the increase
    for r in results: 
             
        cityname = (r[0])  
        citypop = (r[1])      
     
    # Print output message to show user what has been done - 

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
    

    # print the results in each row - Get new population of the city after the decrease
    for r in results:                   
        cityname = (r[0])  
        citypop = (r[1])      
     
     # Print output message to show user what has been done - 

    print(f"You have decreased the population of city {cityname}  by  {Amount}! The new population of {cityname} is {citypop} ")
    
    # Close mysql connection

    db.close()
    cursor.close()

    main()

def add_newperson():  

# This function adds a new person to the mysql database
    
    import mysql.connector
    sql_Connector()

# Declaring the variables as global variables

    global userid
    global firstlastname
    global Age
    global salary
    global personcityid
    
    while True:
         try:
              userid = int(input("Please Enter a UserID: ")) 
              break              
         except ValueError as err:
                print (f"Error: {err}") 


    while True:
         try:
              firstlastname = input("Please Enter your First and Last Name: ")               
              break                                         
         except ValueError as err:
                print (f"Error: {err}") 
   
         
    while True:
        try:
              Age = int(input("Please Enter the Persons Age: ")) 
              break              
        except ValueError as err:
                    print (f"Error: {err}") 
              
     
    while True:
         try:
              salary = float(input("Please Enter the Persons Salary: ")) 
              break              
         except ValueError as err:
                print (f"Error: {err}") 
         except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))  
                   

    while True:
         try:
              personcityid = int(input("Please Enter the CityID: ")) 
              break              
         except ValueError as err:
                print (f"Error: {err}")                           

    print(f"You have chosen the following to add to the database, userid = {userid}  Fullname = {firstlastname}  Age ={Age} Salary = {salary} CityID = {personcityid}!")

    cursor = db.cursor()

    cursor.execute("select PersonID from person where PersonID =%s",(userid,))
            
    results= cursor.fetchall() 
     
    NumRows = cursor.rowcount   
    
# Check does the userid already exist in the mysql database

    if cursor.rowcount > 0: 
            print (f"This user id {userid} already exists you will be returned to Main Menu")
            main()                                       
    else :
        print("User ID does not exist, Good job!!")  

    cursor = db.cursor()

    cursor.execute("select ID from city where id =%s",(personcityid,))
            
    results= cursor.fetchall() 
   
    NumRows = cursor.rowcount   
          

    if cursor.rowcount > 0: 
            print (f"This city id {personcityid}  exists")                                                     
    else :
        print (f"This city id {personcityid} does not exist you will be returned to Main Menu")
        main() 
              
    sql_Connector()

    cursor = db.cursor()
    
    # Insert the record into the mysql database

    try:
        cursor.execute("Insert into person (personid, personname, age, salary, city)VALUES (%s,%s, %s, %s,%s)",(userid,firstlastname,Age,salary,personcityid,))
     
    except  mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))  

    # Close the mysql connection

    db.close()
    cursor.close()
    
    main()               


def delete_person():

# This function deletes the id of the person you enter from the mysql database
     
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
       
     if cursor.rowcount > 0: 
            print (f"This user id {userid} exists")                                                              
     else :
        print("User ID does not exist so cannot perform delete operation!!") 
        main()
    
     # If person id in question has visited a city then they cannot be deletd from the mysql database
                  
     cursor = db.cursor()
     cursor.execute("select * from person person inner join hasvisitedcity hasvisitedcity on person.personid = hasvisitedcity.personid where  hasvisitedcity.personid =%s",(userid,))
     
     results= cursor.fetchall()     
     if cursor.rowcount > 0: 
            print (f"This user id {userid} exists but has visited a city so cannot be deleted")
            main()                                                  
     else :
        print("User ID can be deleted!!") 
        

 
     cursor = db.cursor()

     cursor.execute("delete from person where personid =%s",(userid,))
                       
     results= cursor.fetchall()     
     print (f"You have deleted userid {userid} from the database!!!!")     
     
     db.close()
     cursor.close() 

     main()

    

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
  

# Error handling to check that the user has entered a valid symbol - > OR < or = If not an error message will appear

    if populationsymbol == '>':
        print (f"The countries with a population {populationsymbol} {populationamount} are ") 
        cursor.execute("select code,name, continent, population from country where population > %s",(populationamount,))
        results= cursor.fetchall() 
        print(results)    
    elif   populationsymbol == '<': 
         print (f"The countries with a population {populationsymbol} {populationamount} are ")  
         cursor.execute("select  code,name, continent, population from country where population < %s",(populationamount,))
         results= cursor.fetchall() 
         print(results)
    elif  populationsymbol == '=': 
         print (f"The countries with a population {populationsymbol} {populationamount} are ")   
         cursor.execute("select  code,name, continent, population from country where population = %s",(populationamount,))
         results= cursor.fetchall() 
         print(results)
    else:
         print("Invalid Option Chosen:")
       
    
    if cursor.rowcount > 0: 
            print (f"The countries with a population {populationsymbol} {populationamount} are above ")                                                              
    else :
           print(f"There are no countries with a population {populationsymbol} {populationamount} !!") 

    db.close()
    cursor.close()   

    main()     
       
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
    

    # print the results in each row
    for r in results:        
        print(r[0])
        print(r[1])
        cityname = (r[1])
        
        
    NumRows = cursor.rowcount   
    


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

        results =  tx.run("MATCH (u:City {name: 'Dublin'}) "
            "WITH COUNT(u) > 0  as dublin_exists "        
            "RETURN dublin_exists")
        for result in results:                       
            print  (result['dublin_exists']) 

        while True:
            if (result['dublin_exists']) == True:
                print('Dublin exists in the Neo4j database so it can be twinned') 
                break
            elif (result['dublin_exists']) == False:
                print("Dublin has been deleted you will be redireced to Main Menu!!") 
                main() 
            else:
                 break                    
       
        results =  tx.run("MATCH (u:City {name: $cityname}) "
           "WITH COUNT(u) > 0  as node_exists "        
           "RETURN node_exists",
            cityname=cityname)
        for result in results:                       
         print  (result['node_exists']) 
    

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
       
 

   
    tx.run("MATCH(u:City {name:'Dublin'}) "
                "CREATE(p:City {name:$cityname, cid:$neo4jcityid})"        
                "CREATE(p)-[w:TWINNED_WITH]->(u)",
                    cityname=cityname, neo4jcityid=neo4jcityid) 
    print (f"{cityname} is now created and is twinned with Dublin")          
           

def create_twinonly_with_dublin(tx,cityname,neo4jcityid):  

        from neo4j import exceptions        
        
        results =  tx.run("OPTIONAL MATCH (c:City{name:'Dublin'})<-[r]->(n:City{name: $cityname}) "                  
            "RETURN c, r IS NOT NULL as isTwinned",
                cityname=cityname)        
        for result in results:                                       
             print  (result['isTwinned']) 
   
                  
       # while True:
        if (result['isTwinned']) == True:                            
                            print("This city already twinned with Dublin so you will return to Main Menu")
                            main()
        elif (result['isTwinned']) == False:                
                with driver.session() as session:
                    try:    
                        session.write_transaction(twin_with_dublin_as_exists, cityname, neo4jcityid)
                        main()    
                    except exceptions.ClientError as e:               
                        print ("Error Parameters are not valid")
                         
                                        
        else:            
            main()            

         
    
def twin_with_dublin_as_exists(tx,cityname, neo4jcityid):
       from neo4j import exceptions

 

       results = tx.run("MATCH(u:City {name:'Dublin'})"
                        "MATCH(c:City {name:$cityname, cid:$neo4jcityid}) "                   
                        "CREATE(u)-[w:TWINNED_WITH]->(c)",
                        cityname=cityname, neo4jcityid=neo4jcityid) 
       
       print (f"Dublin is now twinned with {cityname}") 
       for result in results:                                                 
                        print  (result['w'])    

                                
     
def neo4jconnection():
 
 # Function that connects to the neo4j database
       
 from neo4j import GraphDatabase
 from neo4j import exceptions

 drivr = None

 global driver
     
 uri ="neo4j://localhost:7687" 
 driver = GraphDatabase.driver(uri, auth=("neo4j", "Brokercrm123!"), max_connection_lifetime=1000) 


def sql_Connector():

# Function that calls sql connector and connects to the mysql database with the credentials specified
    
    import mysql.connector
    

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
