from contextlib import contextmanager
from ORMModels import Car, Brand, Sales, Company_Results, Employee, Position, Salary_payment
from sqlalchemy.orm import sessionmaker, Query
import sqlalchemy as sa

class DBConnect:
    def __init__(self, login, password, db_name, is_echo=False) :
        self.__main_engine = sa.create_engine(
            f'mysql+pymysql://{login}:{password}@localhost/{db_name}',
            echo=is_echo,
        )

        self.__ses_maker = sessionmaker(
            bind=self.__main_engine,
            expire_on_commit=False,
        )

    @contextmanager
    def __session_scope(self):
        """Provides a transactional scope around a series of operations."""
        session = self.__ses_maker()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_full_table(self, table_name:str) -> list[Car]:
        with self.__session_scope() as s:
            match table_name.lower():
                case 'brand' | 'brands':
                    return s.query(Brand).all()
                case 'car' | 'cars':
                    return s.query(Car).all()
                case 'company' | 'result' | 'results' | 'company results' | 'company result':
                    return s.query(Company_Results).all()
                case 'employee' | 'employees':
                    return s.query(Employee).all()
                case 'position' | 'positions':
                    return s.query(Position).all()
                case 'salary' | 'payment' | 'payments' | 'salary payment' | 'salary payments':
                    return s.query(Salary_payment).all()
                case 'sale' | 'sales':
                    return s.query(Sales).all()
                case _:
                    return []

    def test(self):
        with self.__session_scope() as s:
            s.query(Sales).all()

if __name__ == '__main__':
    db = DBConnect('hikinari', '68ee3e138', 'AvilonN')
    results = db.get_full_table('sale')
    # db.test()
    print(results[0].get_info())
