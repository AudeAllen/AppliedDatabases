    
from neo4j import GraphDatabase

drivr = None

def connect():
    global driver
     
    uri ="neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "Brokercrm123!"), max_connection_lifetime=1000) 

  

#def test_module(tx):
 #   query = "MATCH(n:City)-[r:TWINNED_WITH]->(C:City) return n.name, r.type, C.name order by n.name"
  #  names = []
   # results = tx.run(query)    
    #for result in results:                  
     #   names.append({result['n.name'],  result['C.name']})           
    #return names

def test(tx):
   query = "MATCH(n:City)-[r:TWINNED_WITH]->(C:City) return n.name, r.type, C.name order by n.name"
    # names = []
   results = tx.run(query)    
   for result in results:                  
        print  (result['n.name'] + "<------------>" + result['C.name']) 

def main():
    connect()
    with driver.session() as session:
        values = session.read_transaction(test)
          



if __name__ == '__main__':
   main()
