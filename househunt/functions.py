from mysite.settings import DATABASES
import psycopg2
from psycopg2 import sql
from lxml import html
from django.utils import timezone
from django.utils import timezone
import requests
from collections import namedtuple

dbHost     = DATABASES['default']['HOST']
dbName     = DATABASES['default']['NAME']
dbUsername = DATABASES['default']['USER']
dbPassword = DATABASES['default']['PASSWORD']
dbPort     = DATABASES['default']['PORT']
conn_string = "host=%s dbname=%s user=%s password=%s port=%s" % (dbHost,dbName,dbUsername,dbPassword,dbPort)


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def scrapingdata(form):
    page = requests.get(form.cleaned_data['url'])
    tree = html.fromstring(page.content)  ### Start scraping data from html ###
    search_result = tree.xpath('//div[@id="resultsInfo"]/p/text()')  # How many house have found
    search_result = ', '.join(search_result)

    suburb = tree.xpath('//div[@id="searchResultsTbl"]//a[@class="suburbLink"]/text()')
    suburb_name = ', '.join(suburb)[:-10]

    postcode = ', '.join(suburb)[-4:]
    listed_date = timezone.now()
    sold_date = timezone.now()
    create_date = timezone.now()

    search_list = tree.xpath('//article/@id')  # list of properties id

    twodlist = []
    for i in range(0, 1):
        row = []
        for j in range(0, len(search_list)):
            row_id = j + 1
            property_id = search_list[j]

            address = tree.xpath('//article[@id="' + property_id + '" ]//a[@class="name"]/text()')
            address = ', '.join(address)

            price = tree.xpath('//article[@id="' + property_id + '" ]//p[@class="priceText"]/text()')
            price = ', '.join(price)
            sold_price = ""

            agent_name = tree.xpath('//article[@id="' + property_id + '" ]//img[@class="agent-photo"]/@title')
            agent_name = ', '.join(agent_name)

            row.append(
                [search_result, row_id, property_id, address, suburb_name, postcode, listed_date, price, sold_date,
                 sold_price, agent_name, create_date])
        twodlist.append(row)
    return twodlist
def chk_duplicate_data(prop_id, postcode):
    
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM househunt_property WHERE property_id=%s and postcode=%s;", (prop_id,postcode,))
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    if len(records) > 0:
        return 1
    else:
        return 0
def insert_prop(row, seq):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        sql_str = "INSERT INTO househunt_property (property_id, address, suburb_name, postcode," \
                  "price, listed_agent, create_date, modify_date)" \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        # args_str = ("a", "a", "a","a", \
        #             "a", "a", timezone.now(), timezone.now())
        args_str = (row[seq][2], row[seq][3], row[seq][4], row[seq][5],\
                    row[seq][7], row[seq][10],timezone.now(), timezone.now())

        cursor.execute(sql_str, args_str)

        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
    return "Save data successfully"
def search_prop(postcode, address):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        sql = "SELECT * FROM househunt_property"
        args=()
        if postcode != "" and address =="":
            sql += " WHERE postcode=%s ORDER BY postcode;"
            args = (postcode,)
        if postcode == "" and address !="":
            sql += " WHERE address=%s ORDER BY postcode;"
            args = (address,)
        if postcode != "" and address !="":
            sql += " WHERE postcode=%s AND address=%s ORDER BY postcode;"
            args = (postcode, address,)
        if postcode == "" and address =="":
            sql += " ORDER BY postcode;"

        cursor.execute(sql, args)
        # records = cursor.fetchall()
        records = namedtuplefetchall(cursor)

        cursor.close()
        conn.close()

        return records
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()