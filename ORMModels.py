from sqlalchemy import Column, Integer, Text, Float, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# class Image(Base):
#     __tablename__ = 'Image'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(Text, nullable=False)
#
#
# class Topic(Base):
#     __tablename__ = 'Topic'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(Text, nullable=False)
#     image_id = Column(Integer, ForeignKey('Image.id'), nullable=False)
#
#     rl_image = relationship(Image, backref='topics')  # innerjoin=True для JOIN

class Position(Base):
    __tablename__ = 'Position'

    title = Column(Text, primary_key=True, nullable=False)
    description = Column(Text, nullable=False)
    salary = Column(Float, nullable=False)
    requirements = Column(Text, nullable=False)
    responsibilities = Column(Text, nullable=False)

class Employee(Base):
    __tablename__ = 'Employee'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fio = Column(Text, nullable=False)
    position_title = Column(Text, ForeignKey('Position.title'), nullable=False)
    birth_date = Column(Date, nullable=False)
    passport_data = Column(Text, nullable=False)
    contact_phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    address = Column(Text, nullable=False)

    rl_position = relationship(Position, backref='employees')


class Salary_payment(Base):
    __tablename__ = 'Salary payment'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    employee_id = Column(Integer, ForeignKey('Employee.id'), nullable=False)
    year = Column(Date, nullable=False)
    payment_size = Column(Float, nullable=False)
    sales = Column(Float, nullable=False)
    bonus = Column(Float, nullable=False)
    rating = Column(Integer, nullable=False)

    rl_employee = relationship(Employee, backref='payments')

    
class Company_Results(Base):
    __tablename__ = 'Company Results'

    year = Column(Date, primary_key=True, nullable=False)
    profit = Column(Float, nullable=False)
    revenue = Column(Float, nullable=False)
    market_share = Column(Float, nullable=False)
    number_of_customers = Column(Integer, nullable=False)
    
class Brand(Base):
    __tablename__ = 'Brand'
    
    name = Column(Text, primary_key=True, nullable=False)
    manufacturer = Column(Text, nullable=False)
    country_of_origin = Column(Text, nullable=False)
    year_established = Column(Date, nullable=False)
    logo = Column(Text, nullable=False)

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



