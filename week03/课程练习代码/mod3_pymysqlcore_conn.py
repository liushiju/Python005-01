#!/venv1/bin/python
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine(
    "mysql+pymysql://testuser:testpass@192.168.0.168:3306/testdb", echo=True)

metadata = MetaData(engine)

book_table = Table('book', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(20)),
                   )

author_table = Table('author', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('book_id', None, ForeignKey('book.id')),
                     Column('author_name', String(128), nullable=False)
                     )

try:
    metadata.create_all()
except Exception as e:
    print(f"create err {e}")
