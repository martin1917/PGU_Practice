CREATE TABLE IF NOT EXISTS color(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color_name nvarchar(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS type_product(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name nvarchar(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS product(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name nvarchar(128) NOT NULL,
    price REAL NOT NULL,
    type_id INTEGER NOT NULL,
    availability INTEGER NOT NULL DEFAULT 0 CHECK(availability = 0 OR availability = 1),
    color_id INTEGER NOT NULL,
    
    FOREIGN KEY (type_id) REFERENCES type_product (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES color (id) ON UPDATE CASCADE ON DELETE CASCADE
);