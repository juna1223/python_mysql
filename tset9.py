import mysql.connector

try :
    # 1.DB에 연결
    connection = mysql.connector.connect(
        host = 'yh-db.c4kkyzo02io2.us-east-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'python_user',
        password = '1223'
    )

    # 2. 쿼리문 만들고
    query = '''delete from test
                where id = %s;'''
    # 파이썬에서, 튜플만들 때, 데이터가 1개인 경우에는 콤마를 꼭 써준다.
    record = [(2,),(5,),(7,)]

    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.executemany(query,record)

    # 5. 커넥션을 커밋한다. => 디비에 영구적으로 반영한다.
    connection.commit()

except mysql.connector.Error as e:
    print('Error', e)
finally :
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connetion is closed')