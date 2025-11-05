from collections.abc import AsyncGenerator
import uuid
import datetime
from sqlalchemy import Column, Text, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

class Base(DeclarativeBase):
    pass


# Data Model
class Post(Base):
    __tablename__ = "posts"

    # everytime a new unique id will be generated when we insert into the database which will be randomly generated
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable= False)
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# start db engine and create db and tables
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# get session which will allow us to acess the db and write and read from it asynchronously 
async def get_async_session()->AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

