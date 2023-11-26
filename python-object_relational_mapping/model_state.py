#!/usr/bin/python3
"""
Module define the state class.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Creating declarative_base instance called Base.
Base = declarative_base()


class state(Base):
    """
    Defining state class mapped to cities table in database hbtn_0e_14_usa.

    Attributes:
        __tablename__: Name of table mapped to State class.
        id: Column representing primary key.
        name: Column representing name.
        state_id: Column representing foreign key to states table.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
