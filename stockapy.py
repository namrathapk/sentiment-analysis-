import requests
import sqlite3

base_url= "https://www.alphavantage.co/query"
apikey= "T4TTN6HP5SI0Q92M"

connection = sqlite3.connect('Rohans Database')
cursor = connection.cursor()
create_table_query = ''' 
CREATE TABLE IF NOT EXISTS stock (
ticker  TEXT, 
price  INTEGER

);
'''


cursor .execute(create_table_query)

connection.commit()


print ("Table made!")


def stock(base_url):

    params = {

        "function" :"GLOBAL_QUOTE",
        "symbol" : ["TSLA","PEP"],
        "apikey" : apikey

}

    response= requests.get(base_url, params= params)
    data= response.json()

    return data 

data = stock(base_url)

ticker = data["Global Quote"]["01. symbol"]
price = data["Global Quote"]["05. price"]


print(data)  


insert_query = '''

INSERT INTO stock (ticker, price)
VALUES (?,?)
'''

cursor .execute(insert_query,(ticker, price))
connection.commit()


