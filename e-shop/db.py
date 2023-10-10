import databases
import sqlalchemy

from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()




    
goods = sqlalchemy.Table("goods",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(64)),
                         sqlalchemy.Column("description", sqlalchemy.String(128)),
                         sqlalchemy.Column("price", sqlalchemy.Float))


clients = sqlalchemy.Table("clients",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(64)),
                         sqlalchemy.Column("surname", sqlalchemy.String(64)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(512)))


orders = sqlalchemy.Table("orders",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("client_id", sqlalchemy.ForeignKey('clients.id')),
                         sqlalchemy.Column("item_id", sqlalchemy.ForeignKey('goods.id')),
                         sqlalchemy.Column("created_at", sqlalchemy.Date),
                         sqlalchemy.Column("status", sqlalchemy.String(16)))

engine =  sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)