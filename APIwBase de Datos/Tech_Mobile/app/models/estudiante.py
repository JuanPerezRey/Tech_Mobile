# coding: utf-8

from sqlmodel import SQLModel, Field
from typing import Optional

class Estudiante(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    almacenamientogb: int
    precio: int
    stock: int