import psycopg2

def createdb(c):
    conn = psycopg2.connect(database=c, user='<>', password='<>')
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS client(
        client_id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        surname VARCHAR(150),
        email VARCHAR(200),
        telephone_number VARCHAR(200)
        );
        ''')
    conn.commit()
    conn.close()

def add_client(c, name, surname, email, telephone_number=None):
    conn = psycopg2.connect(database=c, user='<>', password='<>')
    with conn.cursor() as cur:
        if telephone_number == None:
            cur.execute(f'''
                INSERT INTO client(name, surname, email, telephone_number) VALUES({repr(name)}, {repr(surname)}, {repr(email)}, {repr('None')})
                ''')
        else:
            cur.execute(f'''
                    INSERT INTO client(name, surname, email, telephone_number) VALUES({repr(name)}, {repr(surname)}, {repr(email)}, {repr(telephone_number)})
                            ''')
    conn.commit()
    conn.close()
def add_phone(c, client_id, phone):
    conn = psycopg2.connect(database=c, user='<>', password='<>')
    with conn.cursor() as cur:
        cur.execute(f'''
    UPDATE client
    SET telephone_number = {repr(phone)}
    where client_id = {client_id}
''')
    conn.commit()
    conn.close()
def change_client(c, client_id, first_name=None, last_name=None, email=None, phones=None):
    conn = psycopg2.connect(database=c, user='<>', password='<>')
    with conn.cursor() as cur:
        if first_name != None:
            cur.execute(f'''
    UPDATE client
    SET name = {repr(first_name)}
    where client_id = {client_id}
''')
        if last_name != None:
                cur.execute(f'''
            UPDATE client
            SET surname = {repr(last_name)}
            where client_id = {client_id}
        ''')
        if email != None:
                    cur.execute(f'''
                    UPDATE client
                    SET email = {repr(email)}
                    where client_id = {client_id}
                ''')
        if phones != None:
                        cur.execute(f'''
                        UPDATE client
                        SET telephone_number = {repr(phones)}
                        where client_id = {client_id}
                    ''')
    conn.commit()
    conn.close()

def delete_phone(c, client_id, phone=None):
    conn = psycopg2.connect(database=c, user='<>', password='<>')
    with conn.cursor() as cur:
        cur.execute(f'''
        UPDATE client
        SET telephone_number = {repr('None')}
        where client_id = {client_id}
                            ''')
    conn.commit()
    conn.close()
def delete_client(c, client_id):
    conn = psycopg2.connect(database=c, user='<>', password='<>')
    with conn.cursor() as cur:
        cur.execute(f'''
    DELETE from client
    where client_id = {client_id}
''')
    conn.commit()
    conn.close()

def find_client(c, first_name=None, last_name=None, email=None, phone=None):
    conn = psycopg2.connect(database=c, user='<>', password='<>')
    with conn.cursor() as cur:
        if first_name != None:
            cur.execute(f'''
SELECT * FROM client
where name = {repr(first_name)};''')
        if last_name != None:
            cur.execute(f'''
            SELECT * FROM client
            where surname = {repr(last_name)};''')
        if email != None:
            cur.execute(f'''
                        SELECT * FROM client
                        where email = {repr(email)};''')
        if phone != None:
            cur.execute(f'''
SELECT * from client
where telephone_number = {repr(phone)}
''')
    conn.commit()
    conn.close()