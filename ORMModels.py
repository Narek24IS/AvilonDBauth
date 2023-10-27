from sqlalchemy import Column, Integer, Text, Float, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Position(Base):
    __tablename__ = 'Position'

    title = Column(Text, primary_key=True, nullable=False)
    description = Column(Text, nullable=False)
    salary = Column(Float, nullable=False)
    requirements = Column(Text, nullable=False)
    responsibilities = Column(Text, nullable=False)

    def get_info(self):
        return [self.title, self.description, self.salary, self.requirements, self.responsibilities]

    @staticmethod
    def get_headers():
        return ['Title', 'Description', 'Salary', 'Requirements', 'Responsibilities']

class Employee(Base):
    __tablename__ = 'Employee'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fio = Column(Text, nullable=False)
    position = Column(Text, ForeignKey('Position.title'), nullable=False)
    birth_date = Column(Date, nullable=False)
    passport_data = Column(Text, nullable=False)
    contact_phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    address = Column(Text, nullable=False)

    rl_position = relationship(Position, backref='employees')

    def get_info(self):
        return [self.id, self.fio, self.position, self.birth_date, self.passport_data,
                self.contact_phone, self.email, self.address]

    @staticmethod
    def get_headers():
        return ['Id', 'FIO', 'Position', 'Birth date', 'Passport data', 'Contact phone',
                'Email', 'Address']


class Salary_payment(Base):
    __tablename__ = 'Salary_payment'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    employee_id = Column(Integer, ForeignKey('Employee.id'), nullable=False)
    date = Column(Date, nullable=False)
    payment_size = Column(Float, nullable=False)
    sales = Column(Float, nullable=False)
    bonus = Column(Float, nullable=False)
    rating = Column(Integer, nullable=False)

    rl_employee = relationship(Employee, backref='payments')

    def get_info(self):
        return [self.id, self.employee_id, self.date, self.payment_size, self.sales,
                self.bonus, self.rating]

    @staticmethod
    def get_headers():
        return ['Id', 'Employee ID', 'Date', 'Payment size', 'Sales', 'Bonus', 'Rating']

    
class Company_Results(Base):
    __tablename__ = 'Company_Results'

    year = Column(Date, primary_key=True, nullable=False)
    profit = Column(Float, nullable=False)
    revenue = Column(Float, nullable=False)
    market_share = Column(Float, nullable=False)
    number_of_customers = Column(Integer, nullable=False)

    def get_info(self):
        return [self.year, self.profit, self.revenue, self.market_share, self.number_of_customers]

    @staticmethod
    def get_headers():
        return ['Year', 'Profit', 'Revenue', 'Market share', 'Number of customers']

class Brand(Base):
    __tablename__ = 'Brand'
    
    name = Column(Text, primary_key=True, nullable=False)
    manufacturer = Column(Text, nullable=False)
    country_of_origin = Column(Text, nullable=False)
    year_established = Column(Date, nullable=False)
    logo = Column(Text, nullable=False)

    def get_info(self):
        return [self.name, self.manufacturer, self.country_of_origin,
                self.year_established, self.logo]

    @staticmethod
    def get_headers():
        return ['Name', 'Manufacturer', 'Country of origin', 'Year established', 'Sales',
                'Bonus', 'Rating']

class Car(Base):
    __tablename__ = 'Car'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    brand = Column(Text, ForeignKey('Brand.name'), nullable=False)
    model = Column(Text, nullable=False)
    complectation = Column(Text, nullable=False)
    fuel = Column(Text, nullable=False)
    year = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
    color = Column(Text, nullable=False)

    rl_brand = relationship(Brand, backref='cars')

    def get_info(self):
        return [self.id, self.brand, self.model, self.complectation, self.fuel, self.year,
                self.price, self.color]

    @staticmethod
    def get_headers():
        return ['Id', 'Brand', 'Model', 'Complectation', 'Fuel', 'Year', 'Price', 'Color']


class Sales(Base):
    __tablename__ = 'Sales'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    car_id = Column(Integer, ForeignKey('Car.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('Employee.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Text, nullable=False)
    comment = Column(Text, nullable=False)

    car = relationship(Car, backref='sales')
    employee = relationship(Employee, backref='sales')

    def get_info(self):
        return [self.transaction_id, self.car_id, self.employee_id, self.amount, self.date,
                self.status, self.comment]

    @staticmethod
    def get_headers():
        return ['Transaction ID', 'Car ID', 'Employee ID', 'Amount', 'Date', 'Status', 'Comment']
