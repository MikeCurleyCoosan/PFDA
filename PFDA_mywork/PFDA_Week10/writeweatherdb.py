import mysql.connector

class weatherDAO:

    def __init__(self): 
        #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="weather"
    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    
    def insertTable(self):
        cursor = self.getCursor()
        sql="Create table weather (id, INT AUTO_INCREMENT PRIMARY KEY, date VARCHAR(255), ind INT, rain FLOAT, ind2 INT, temp FLOAT, ind3 INT, wetb FLOAT, dewpt FLOAT, vappr FLOAT, rhum FLOAT, msl FLOAT,ind4 INT, wdsp FLOAT,ind5 INT, wddir FLOAT, height FLOAT, latitude FLOAT, longitude FLOAT)"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()
        self.closeAll()
        return 

    def findByDate(self, date):
        cursor = self.getCursor()
        sql="select * from weather where date like %s%"
        values = (date,)

        cursor.execute(sql, values)
        result = cursor.fetchall()
        self.closeAll()
        return self.convertToDict(result)
    
    def create(self, student):
        cursor = self.getCursor()
        sql="insert into weather ((id, date, ind, rain, ind2, temp, ind3, wetb, dewpt, vappr, rhum, msl ,ind4 , wdsp ,ind5, wddir , height , latitude , longitude )) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (student.get("name"), student.get("age"))
        cursor.execute(sql, values )

        self.connection.commit()
        newid = cursor.lastrowid
        student["id"] = newid
        self.closeAll()
        return student


    def update(self, id,  student):
        cursor = self.getCursor()
        sql="update student set name= %s, age=%s  where id = %s"
    
        values = (student.get("name"), student.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        
        self.closeAll()
        return student

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        #print("delete done")
        return True

    def convertToDict(self,resultLine):
        studentKeys = ["id", "name", "age"]
        currentkey = 0
        student = {}
        for attrib in resultLine:
            student[studentKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return student

