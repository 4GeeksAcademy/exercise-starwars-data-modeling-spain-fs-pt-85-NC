import os
import sys
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column
from datetime import datetime, timezone

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = mapped_column(Integer, primary_key=True)
    usuario = mapped_column(String(40), nullable=False, unique=True)
    contraseña = mapped_column(String(40), nullable=False)
    nombre = mapped_column(String(200), nullable=False)
    email = mapped_column(String(100), nullable=False, unique=True)
    creado = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    
    favorito = relationship('Favorite', backref='user', lazy=True)

class Planeta(Base):
    __tablename__ = 'planeta'
    
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(100), nullable=False)
    diametro = mapped_column(String(100), nullable=False)
    rotacion = mapped_column(String(100), nullable=False)
    orbita = mapped_column(String(100), nullable=False)
    gravedad = mapped_column(String(100), nullable=False)
    poblacion = mapped_column(String(100), nullable=False)
    clima = mapped_column(String(100), nullable=False)
    terreno = mapped_column(String(100), nullable=False)
    creado = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    editado = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    favorito = relationship('Favorite', backref='planet', lazy=True)

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(100), nullable=False)
    modelo = mapped_column(String(100), nullable=False)
    tipo_vehiculo = mapped_column(String(100), nullable=False)
    fabricante = mapped_column(String(100), nullable=False)
    longitud = mapped_column(String(100), nullable=False)
    precio = mapped_column(String(100), nullable=False)
    velocidad_maxima = mapped_column(String(100), nullable=False)
    carga_maxima = mapped_column(String(100), nullable=False)
    consumibles = mapped_column(String(100), nullable=False)
    url = mapped_column(String(200), nullable=False)
    creado = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    editado = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    favorito = relationship('Favorite', backref='vehicle', lazy=True)

class Personajes(Base):
    __tablename__ = 'personajes'
    
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(100), nullable=False)
    cumpleaños = mapped_column(String(100), nullable=False)
    color_ojos = mapped_column(String(100), nullable=False)
    genero = mapped_column(String(100), nullable=False)
    color_pelo = mapped_column(String(100), nullable=False)
    altura = mapped_column(String(20), nullable=False)
    color_piel = mapped_column(String(20), nullable=False)
    planeta_origen = mapped_column(String(40), nullable=False)
    url = mapped_column(String(100), nullable=False)
    creado = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    editado = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    favorito = relationship('Favorite', backref='people', lazy=True)

class Favorite(Base):
    __tablename__ = 'favoritos'
    
    id = mapped_column(Integer, primary_key=True)
    usuario_id = mapped_column(Integer, ForeignKey('usuario.id'), nullable=False)
    personajes_id = mapped_column(Integer, ForeignKey('personajes.id'), nullable=True)
    vehiculo_id = mapped_column(Integer, ForeignKey('vehiculo.id'), nullable=True)
    planeta_id = mapped_column(Integer, ForeignKey('planeta.id'), nullable=True)

# Generate a diagram for the database schema
render_er(Base, 'diagram.png')