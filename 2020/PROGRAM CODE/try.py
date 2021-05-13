# import mysql.connector

# def database():
#     conn = mysql.connector.connect (user='root', password='', host='localhost', buffered=True)
#     cursor = conn.cursor()
#     databases = ("show databases")
#     cursor.execute(databases)


#     for (databases) in cursor:
#         print(databases[0])

# database()



from covid import Covid

covid = Covid()
# input("Country name  ")
cname = "canada"
cname = covid.get_status_by_country_name(cname)

# print(covid.list_countries())

data = {
    key: cname[key]
    for key in cname.keys() and{
        'confirmed',
        'active',
        'deaths',
        'recovered'
    }
}
# print(str(data))

temp = str(data)
# print(temp)

# opening a file in 'w'
file = open('savedData.txt', 'a')
# writing data using the write() method
file.write(temp+'\n')
# closing the file
file.close()








# sec1 = temp.split(':')
# print("Confirmed: "+sec1[1])
# # sec2 = sec1[0].split('{', 1)
# # print(sec2[1])