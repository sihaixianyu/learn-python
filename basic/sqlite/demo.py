import sqlite3

db_file = 'demo.db'
db_name = "direct_repay_stock"


def create_table(conn: sqlite3.Connection):
    c = conn.cursor()

    c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='direct_repay_stock'")
    if c.fetchone()[0] == 1:
        print("Table exists!")
        return

    sql = """
        CREATE TABLE {}(
            id              integer     primary key autoincrement,
            acct_type       varchar(50) not null,
            acct            varchar(50) not null,
            symbol          varchar(50) not null,
            qty             integer     not null,
            compact         varchar(50) not null,
            cash_group_prop integer     not null);
        """.format(db_name)
    conn.execute(sql)

    conn.commit()


def insert_data(conn: sqlite3.Connection):
    cursor = conn.cursor()

    triples = [
        ("SHHTSC", "2204278", 11, 1000, "123456", 1),
        ("SHHTSC", "2204278", 12, 1000, "123456", 2),
        ("SHHTSC", "2204278", 13, 1000, "123456", 1),
    ]
    sqls = [
        (
            "insert into {} (acct_type, acct, symbol, qty, compact, cash_group_prop) "
            "values ('{}', '{}', {}, {}, '{}', {})"
        ).format(
            db_name,
            triple[0],
            triple[1],
            triple[2],
            triple[3],
            triple[4],
            triple[5],
        )
        for triple in triples
    ]

    for sql in sqls:
        # print(sql)
        cursor.execute(sql)

    conn.commit()


def select_data(conn: sqlite3.Connection):
    cursor = conn.cursor()

    sql = "select * from {}".format(db_name)
    cursor.execute(sql)

    for row in cursor:
        print(
            "id: {}, acct_type: {}, acct: {}, symbol: {}, qty: {}, compact: {}, cash_group_prop: {}".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            )
        )

    conn.commit()


def delete_data(conn: sqlite3.Connection):
    cursor = conn.cursor()

    sql = "delete from {}".format(db_name)
    cursor.execute(sql)

    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect(db_file)

    create_table(conn)
    insert_data(conn)
    select_data(conn)
    delete_data(conn)

    conn.close()
