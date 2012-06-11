from sqlalchemy import create_engine, MetaData, Table

DATABASE_URI = 'postgresql://webadmin@/teamstarter'

engine = create_engine(DATABASE_URI, convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('users', metadata, autoload=True)