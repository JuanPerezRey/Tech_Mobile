from fastapi import APIRouter, Depends, HTTPException, Request, Form, Path
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates
from app.database.connection import db
from app.models.estudiante import Estudiante

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])
templates = Jinja2Templates(directory="app/templates")

# Dependencia para obtener sesión de BD
def get_session():
    with Session(db.engine) as session:
        yield session

# Ruta para listar celulares
@router.get("/")
def listar_celulares(request: Request, session: Session = Depends(get_session)):
    celulares = session.exec(select(Estudiante)).all()
    return templates.TemplateResponse("estudiante/listar.html", {"request": request, "celulares": celulares})

# Ruta para mostrar formulario de agregar celular
@router.get("/agregar")
def mostrar_formulario_agregar(request: Request):
    return templates.TemplateResponse("estudiante/agregar.html", {"request": request})

# Ruta para procesar agregar celular
@router.post("/agregar")
def agregar_celular(
    request: Request,
    id: str = Form(...),
    marca: str = Form(...),
    modelo: str = Form(...),
    almacenamientogb: int = Form(...),
    precio: int = Form(...),
    stock: int = Form(...),
    session: Session = Depends(get_session)
):
    nuevo_celular = Estudiante(
        id=id,
        marca=marca,
        modelo=modelo,
        almacenamientogb=almacenamientogb,
        precio=precio,
        stock=stock
    )

    session.add(nuevo_celular)
    session.commit()
    session.refresh(nuevo_celular)

    return templates.TemplateResponse("estudiante/agregar.html", {"request": request, "mensaje": "Celular agregado exitosamente"})

# Ruta para mostrar formulario de edición
@router.get("/editar/{id}")
def mostrar_formulario_editar(request: Request, id: int = Path(...), session: Session = Depends(get_session)):
    celular = session.get(Estudiante, id)
    if not celular:
        raise HTTPException(status_code=404, detail="Celular no encontrado")
    return templates.TemplateResponse("estudiante/editar.html", {"request": request, "celular": celular})

# Ruta para procesar actualización de celular
@router.post("/editar/{id}")
def actualizar_celular(
    request: Request,
    id: int = Path(...),
    marca: str = Form(...),
    modelo: str = Form(...),
    almacenamientogb: int = Form(...),
    precio: int = Form(...),
    stock: int = Form(...),
    session: Session = Depends(get_session)
):
    celular = session.get(Estudiante, id)
    if not celular:
        raise HTTPException(status_code=404, detail="Celular no encontrado")

    # Actualizar datos del celular
    celular.marca = marca
    celular.modelo = modelo
    celular.almacenamientogb = almacenamientogb
    celular.precio = precio
    celular.stock = stock

    session.add(celular)
    session.commit()
    session.refresh(celular)

    return templates.TemplateResponse("estudiante/editar.html", {"request": request, "celular": celular, "mensaje": "Celular actualizado exitosamente"})

# Ruta para mostrar confirmación de eliminación
@router.get("/eliminar/{id}")
def mostrar_confirmacion_eliminar(request: Request, id: int = Path(...), session: Session = Depends(get_session)):
    celular = session.get(Estudiante, id)
    if not celular:
        raise HTTPException(status_code=404, detail="Celular no encontrado")
    return templates.TemplateResponse("estudiante/eliminar.html", {"request": request, "celular": celular})

# Ruta para eliminar celular
@router.post("/eliminar/{id}")
def eliminar_celular(id: int = Path(...), session: Session = Depends(get_session)):
    celular = session.get(Estudiante, id)
    if not celular:
        raise HTTPException(status_code=404, detail="Celular no encontrado")

    session.delete(celular)
    session.commit()
    return templates.TemplateResponse("estudiante/listar.html", {"request": {}, "mensaje": "Celular eliminado exitosamente"})