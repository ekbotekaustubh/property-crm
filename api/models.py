from sqlalchemy import  create_engine, Column, Integer, BigInteger, String, Enum, TIMESTAMP, text 
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()


class UserStatus( enum.Enum):
    active = "active"
    inactive = "inactive"
        


class User(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True, index=True)
    organization_id = Column(BigInteger, nullable=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    status = Column(Enum(UserStatus), default=UserStatus.active, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    created_by = Column(BigInteger, nullable=False)
    updated_at = Column(
        TIMESTAMP, 
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
    updated_by = Column(BigInteger, nullable=False)


    
