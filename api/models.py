from sqlalchemy import  create_engine, Column, Integer, BigInteger, String, Enum, TIMESTAMP, text 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from enum import Enum

class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
        


class User(Base):
    __tablename__ = "user"

    # Primary Key
    id = Column(BigInteger, primary_key=True, index=True)
    
    # Foreign Keys / Relations
    organization_id = Column(BigInteger, nullable=True)
    
    # Standard Columns
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    
    # Enum Column
    #status = Column(Enum(UserStatus), server_default="active")
    
    # Timestamps with Automatic Defaults
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    created_by = Column(BigInteger, nullable=True)
     # Updated_at with 'ON UPDATE' logic
    updated_at = Column(
        TIMESTAMP, 
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
    updated_by = Column(BigInteger, nullable=True)
    
