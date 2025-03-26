from sqlmodel import SQLModel
from app.database.connection import db
from app.models.estudiante import Estudiante

def create_tables():
    SQLModel.metadata.create_all(db.engine)

if __name__ == "__main__":
    create_tables()
    print("Tablas creadas exitosamente")