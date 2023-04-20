CREATE TABLE
    IF NOT EXISTS IS601_S_Items(
        id int AUTO_INCREMENT PRIMARY KEY,
        name varchar(30) UNIQUE,
        description text,
        category text,
        stock int DEFAULT 0,
        unit_price float DEFAULT 99999,
        visibility boolean,
        image text,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (stock >= 0),
        check (unit_price >= 0)
    )