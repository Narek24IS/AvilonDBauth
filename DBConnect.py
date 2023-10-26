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

    def get_cars(self) -> list[Car]:
        with self.__session_scope() as s:
            result:list[Car] = s.query(Car).all()
            return result

    def get_positions(self) -> list[Position]:
        with self.__session_scope() as s:
            result:list[Position] = s.query(Position).all()
            return result

if __name__ == '__main__':
    db = DBConnect('hikinari', '68ee3e138', 'AvilonN')
    results = db.get_positions()

    print(results[0].get_info())
