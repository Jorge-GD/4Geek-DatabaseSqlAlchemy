import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name=Column(String, nullable= False)
    _password=Column(String, nullable=False)
    nickname=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    fav = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet")
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship("People")
    starship_id = Column(Integer, ForeignKey('starship.id'))
    starship = relationship("Starship")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    name=Column(String, nullable=False)
    diameter=Column(Numeric, nullable=False)
    rotation_period=Column(Numeric, nullable=False)
    orbital_period=Column(Numeric, nullable=False)
    gravity=Column(Numeric, nullable=False)
    population=Column(Numeric, nullable=False)
    climate=Column(String, nullable=False)
    terrain=Column(String, nullable=False)
    surface_water=Column(Numeric, nullable=False)
    create=Column(String, nullable=True)
    edited=Column(String, nullable=True)
    description=Column(String, nullable=False)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    name=Column(String, nullable=True)
    height=Column(Numeric, nullable=True)
    mass=Column(Numeric, nullable=True)
    hair_color=Column(String, nullable=True)
    skin_color=Column(String, nullable=True)
    eyes_color=Column(String, nullable=True)
    birth_year=Column(Date, nullable=True)
    create=Column(String, nullable=True)
    edited=Column(String, nullable=True)
    homeworld=Column(String, nullable=True)



class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    name=Column(String, nullable=False)
    model=Column(String, nullable=False)
    straship_class=Column(String, nullable=False)
    manufacture=Column(String, nullable=False)
    incredit=Column(Numeric, nullable=False)
    lenght=Column(Numeric, nullable=False)
    grew=Column(String, nullable=False)
    passenger=Column(Numeric, nullable=False)
    max_atmospheric_speed=Column(Numeric, nullable=False)
    hyperdrive_rating=Column(Numeric, nullable=False)
    mglt=Column(Numeric, nullable=False)
    cargo_capacity=Column(Numeric, nullable=False)
    consumables=Column(Numeric, nullable=False)
    pilot=Column(String, nullable=False)
    create=Column(String, nullable=True)
    edited=Column(String, nullable=True)
    




def get_all(): 
    user = User.query.all()   #Select * from customer
    return user


def get_by_id(id): #Select * from customer where id = id
    user = User.query.get(id).one_or_None()
    #customer = Customer.query.filter_by(id = id)
    return user


def get_by_nick(nick):
    user = User.query.filter_by(nick = nick).one_or_None() #Select * from customer where nick = nick
    return user

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')