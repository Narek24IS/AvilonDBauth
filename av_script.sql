# drop table  Position, Brand, Car, Company_Results, Employee, Salary_payment, Sales;
-- Создание таблицы "Должность"
CREATE TABLE `Position`
(
    `Title`            VARCHAR(255)   NOT NULL,
    `Description`      TEXT           NOT NULL,
    `Salary`           DECIMAL(10, 2) NOT NULL,
    `Requirements`     TEXT           NOT NULL,
    `Responsibilities` TEXT           NOT NULL,
    PRIMARY KEY (`Title`)
);

-- Создание таблицы "Сотрудники"
CREATE TABLE `Employee`
(
    `ID`            INT(11)      NOT NULL AUTO_INCREMENT,
    `FIO`           VARCHAR(255) NOT NULL,
    `Position`      VARCHAR(255) NOT NULL,
    `Birth_Date`    DATE         NOT NULL,
    `Passport_Data` VARCHAR(255) NOT NULL,
    `Contact_Phone` VARCHAR(255) NOT NULL,
    `Email`         VARCHAR(255) NOT NULL,
    `Address`       VARCHAR(255) NOT NULL,
    PRIMARY KEY (`ID`),
    FOREIGN KEY (`Position`) REFERENCES `Position` (`Title`)
);

-- Создание таблицы "Выплата зарплаты"
CREATE TABLE `Salary_payment`
(
    `ID`           INT(11)        NOT NULL AUTO_INCREMENT,
    `Employee_ID`  INT(11)        NOT NULL,
    `Date`         DATE           NOT NULL,
    `Payment_size` DECIMAL(10, 2) NOT NULL,
    `Sales`        DECIMAL(10, 2) NOT NULL,
    `Bonus`        DECIMAL(10, 2) NOT NULL,
    `Rating`       INT(11)        NOT NULL,
    PRIMARY KEY (`ID`),
    FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`ID`)
);

-- Создание таблицы "Итоги компании"
CREATE TABLE `Company_Results`
(
    `Year`                INT           NOT NULL,
    `Profit`              DECIMAL(10, 2) NOT NULL,
    `Revenue`             DECIMAL(10, 2) NOT NULL,
    `Market_Share`        DECIMAL(5, 2)  NOT NULL,
    `Number_of_Customers` INT(11)        NOT NULL,
    PRIMARY KEY (`Year`)
);

-- Создание таблицы "Марка"
CREATE TABLE `Brand`
(
    `Name`              VARCHAR(255) NOT NULL,
    `Manufacturer`      VARCHAR(255) NOT NULL,
    `Country_of_Origin` VARCHAR(255) NOT NULL,
    `Year_Established`  INT         NOT NULL,
    `Logo`              VARCHAR(255) NOT NULL,
    PRIMARY KEY (`Name`)
);

-- Создание таблицы "Машина"
CREATE TABLE `Car`
(
    `ID`            INT(11)        NOT NULL AUTO_INCREMENT,
    `Brand`         VARCHAR(255)   NOT NULL,
    `Model`         VARCHAR(255)   NOT NULL,
    `Complectation` VARCHAR(255)   NOT NULL,
    `Fuel`          VARCHAR(255)   NOT NULL,
    `Year`          INT           NOT NULL,
    `Price`         DECIMAL(10, 2) NOT NULL,
    `Color`         VARCHAR(255)   NOT NULL,
    PRIMARY KEY (`ID`),
    FOREIGN KEY (Brand) REFERENCES Brand(Name)
);

-- Создание таблицы "Продажи"
CREATE TABLE `Sales`
(
    `Transaction_ID` INT(11)        NOT NULL AUTO_INCREMENT,
    `Car_ID`         INT(11)        NOT NULL,
    `Employee_ID`    INT(11)        NOT NULL,
    `Amount`         DECIMAL(10, 2) NOT NULL,
    `Date`           DATE           NOT NULL,
    `Status`         VARCHAR(255)   NOT NULL,
    `Comment`        TEXT           NOT NULL,
    PRIMARY KEY (`Transaction_ID`),
    FOREIGN KEY (`Car_ID`) REFERENCES `Car` (`ID`),
    FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`ID`)
);

-- Заполнение таблицы "Должность" данными
INSERT INTO `Position` (`Title`, `Description`, `Salary`, `Requirements`, `Responsibilities`)
VALUES ('Продавец-консультант', 'Описание должности продавца-консультанта', 40000.00,
        'Требования к продавцу-консультанту', 'Обязанности продавца-консультанта'),
       ('Механик', 'Описание должности механика', 45000.00, 'Требования к механику', 'Обязанности механика'),
       ('Менеджер по продажам', 'Описание должности менеджера по продажам', 55000.00,
        'Требования к менеджеру по продажам', 'Обязанности менеджера по продажам'),
       ('Автомеханик', 'Описание должности автомеханика', 50000.00, 'Требования к автомеханику',
        'Обязанности автомеханика');

-- Заполнение таблицы "Сотрудники" данными
INSERT INTO `Employee` (`FIO`, `Position`, `Birth_Date`, `Passport_Data`, `Contact_Phone`, `Email`, `Address`)
VALUES ('Иванов Иван Иванович', 'Продавец-консультант', '1990-01-01', '1234567890', '1234567890', 'ivanov@example.com',
        'г. Москва, ул. Ленина, д. 1'),
       ('Петров Петр Петрович', 'Механик', '1995-02-02', '0987654321', '0987654321', 'petrov@example.com',
        'г. Санкт-Петербург, ул. Пушкина, д. 2'),
       ('Сидоров Сидор Сидорович', 'Менеджер по продажам', '1988-03-03', '5678901234', '5678901234',
        'sidorov@example.com', 'г. Екатеринбург, ул. Гагарина, д. 3'),
       ('Смирнова Анна Ивановна', 'Автомеханик', '1992-04-04', '4321098765', '4321098765', 'smirnova@example.com',
        'г. Новосибирск, ул. Ленина, д. 4'),
       ('Ковалев Алексей Петрович', 'Менеджер по продажам', '1988-05-05', '6789012345', '6789012345',
        'kovalev@example.com', 'г. Казань, ул. Кирова, д. 5'),
       ('Морозова Екатерина Александровна', 'Автомеханик', '1993-06-06', '5432109876', '5432109876',
        'morozova@example.com', 'г. Ростов-на-Дону, ул. Горького, д. 6');

-- Заполнение таблицы "Выплата зарплаты" данными
INSERT INTO `Salary_payment` (`Employee_ID`, `Date`, `Payment_size`, `Sales`, `Bonus`, `Rating`)
VALUES (1, '2022-03-03', 40000.00, 700000.00, 7000.00, 3),
       (2, '2022-03-03', 45000.00, 600000.00, 6000.00, 2),
       (3, '2022-03-03', 55000.00, 900000.00, 9000.00, 4),
       (4, '2022-03-03', 50000.00, 750000.00, 7500.00, 3),
       (5, '2022-03-03', 55000.00, 900000.00, 9000.00, 4),
       (6, '2022-03-03', 50000.00, 750000.00, 7500.00, 3);

-- Заполнение таблицы "Итоги компании" данными
INSERT INTO `Company_Results` (`Year`, `Profit`, `Revenue`, `Market_Share`, `Number_of_Customers`)
VALUES (2020, 1000000.00, 5000000.00, 10.00, 1000),
       (2021, 1500000.00, 6000000.00, 12.50, 1200),
       (2022, 2000000.00, 7000000.00, 15.00, 1500);

-- Заполнение таблицы "Машина" данными
INSERT INTO `Brand` (`Name`, `Manufacturer`, `Country_of_Origin`, `Year_Established`, `Logo`)
VALUES ('Toyota', 'Toyota Motor Corporation', 'Japan', 1937, 'toyota_logo.png'),
       ('Honda', 'Honda Motor Co., Ltd.', 'Japan', 1948, 'honda_logo.png'),
       ('BMW', 'Bayerische Motoren Werke AG', 'Germany', 1916, 'bmw_logo.png'),
       ('Mercedes-Benz', 'Mercedes-Benz AG', 'Germany', 1926, 'mercedes_logo.png'),
       ('Audi', 'Audi AG', 'Germany', 1909, 'audi_logo.png'),
       ('Volkswagen', 'Volkswagen AG', 'Germany', 1937, 'volkswagen_logo.png');

-- Заполнение таблицы "Марка" данными
INSERT INTO `Car` (`Brand`, `Model`, `Complectation`, `Fuel`, `Year`, `Price`, `Color`)
VALUES ('Toyota', 'Camry', 'Standard', 'Petrol', 2022, 25000.00, 'Black'),
       ('Honda', 'Civic', 'Sport', 'Petrol', 2022, 22000.00, 'White'),
       ('BMW', 'X5', 'Premium', 'Diesel', 2022, 50000.00, 'Silver'),
       ('Mercedes-Benz', 'E-Class', 'Luxury', 'Petrol', 2022, 45000.00, 'Blue'),
       ('Audi', 'A4', 'S-Line', 'Petrol', 2022, 35000.00, 'Red'),
       ('Volkswagen', 'Golf', 'Comfort', 'Petrol', 2022, 20000.00, 'Gray');

-- Заполнение таблицы "Продажи" данными
INSERT INTO `Sales` (`Car_ID`, `Employee_ID`, `Amount`, `Date`, `Status`, `Comment`)
VALUES (1, 1, 25000.00, '2022-03-03', 'Оплачено', 'Комментарий к продаже'),
       (2, 2, 22000.00, '2022-04-04', 'Оплачено', 'Комментарий к продаже'),
       (3, 3, 50000.00, '2022-05-05', 'Оплачено', 'Комментарий к продаже'),
       (4, 4, 45000.00, '2022-06-06', 'Оплачено', 'Комментарий к продаже'),
       (5, 5, 35000.00, '2022-07-07', 'Оплачено', 'Комментарий к продаже'),
       (6, 6, 20000.00, '2022-08-08', 'Оплачено', 'Комментарий к продаже');