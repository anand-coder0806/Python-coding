import mysql.connector
conn=mysql.connector.connect(host="localhost",password="bhagatanand0806@",user="root")

if conn.is_connected():
    print("connectio eastblished...")