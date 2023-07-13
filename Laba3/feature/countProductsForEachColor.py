from data.SQLiteConnector import SQLiteConnector


def countProductsForEachColor(
        connector: SQLiteConnector) -> list[tuple[str, int]]:
    '''посчитать количество товаров для каждого цвета'''
    conn = connector.connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            c.color_name as 'color_name', 
            count(1) AS 'count' 
        FROM product p
        JOIN color c ON p.color_id = c.id
        GROUP BY c.color_name
    """)
    return cur.fetchall()