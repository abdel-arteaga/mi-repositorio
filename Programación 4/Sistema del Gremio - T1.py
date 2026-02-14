from __future__ import annotations

from typing import List
from sqlalchemy import (
    create_engine, event,
    String, Integer, ForeignKey,
    CheckConstraint, select
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column,
    relationship, Session, sessionmaker
)

# ----------------------------
# Configuración DB
# ----------------------------

DB_FILE = "gremio.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DATABASE_URL, echo=False)

@event.listens_for(engine, "connect")
def _set_sqlite_pragma(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def init_db():
    Base.metadata.create_all(engine)


# ----------------------------
# Modelos
# ----------------------------

class Heroe(Base):
    __tablename__ = "heroes"

    id_heroe: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    clase: Mapped[str] = mapped_column(String, nullable=False)
    nivel_experiencia: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("nivel_experiencia >= 1", name="ck_heroe_nivel"),
    )

    misiones: Mapped[List["MisionHeroe"]] = relationship(
        back_populates="heroe",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


class Mision(Base):
    __tablename__ = "misiones"

    id_mision: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    nivel_dificultad: Mapped[int] = mapped_column(Integer, nullable=False)
    localizacion: Mapped[str] = mapped_column(String, nullable=False)
    recompensa: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("nivel_dificultad BETWEEN 1 AND 10", name="ck_mision_dificultad"),
        CheckConstraint("recompensa >= 0", name="ck_mision_recompensa"),
    )

    heroes: Mapped[List["MisionHeroe"]] = relationship(
        back_populates="mision",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    monstruos: Mapped[List["MisionMonstruo"]] = relationship(
        back_populates="mision",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


class Monstruo(Base):
    __tablename__ = "monstruos"

    id_monstruo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    tipo: Mapped[str] = mapped_column(String, nullable=False)
    nivel_amenaza: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("nivel_amenaza BETWEEN 1 AND 10", name="ck_monstruo_amenaza"),
    )

    misiones: Mapped[List["MisionMonstruo"]] = relationship(
        back_populates="monstruo",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


# ----------------------------
# Tablas puente (Muchos a Muchos)
# ----------------------------

class MisionHeroe(Base):
    __tablename__ = "misiones_heroes"

    id_mision: Mapped[int] = mapped_column(
        ForeignKey("misiones.id_mision", ondelete="CASCADE"),
        primary_key=True
    )
    id_heroe: Mapped[int] = mapped_column(
        ForeignKey("heroes.id_heroe", ondelete="CASCADE"),
        primary_key=True
    )

    mision: Mapped["Mision"] = relationship(back_populates="heroes")
    heroe: Mapped["Heroe"] = relationship(back_populates="misiones")


class MisionMonstruo(Base):
    __tablename__ = "misiones_monstruos"

    id_mision: Mapped[int] = mapped_column(
        ForeignKey("misiones.id_mision", ondelete="CASCADE"),
        primary_key=True
    )
    id_monstruo: Mapped[int] = mapped_column(
        ForeignKey("monstruos.id_monstruo", ondelete="CASCADE"),
        primary_key=True
    )

    mision: Mapped["Mision"] = relationship(back_populates="monstruos")
    monstruo: Mapped["Monstruo"] = relationship(back_populates="misiones")


# ----------------------------
# CRUD Básico
# ----------------------------

def crear_heroe():
    nombre = input("Nombre: ")
    clase = input("Clase: ")
    nivel = int(input("Nivel experiencia: "))

    with SessionLocal() as s:
        h = Heroe(nombre=nombre, clase=clase, nivel_experiencia=nivel)
        s.add(h)
        s.commit()
        print("Héroe creado con ID:", h.id_heroe)


def crear_mision():
    nombre = input("Nombre misión: ")
    dificultad = int(input("Dificultad (1-10): "))
    localizacion = input("Localización: ")
    recompensa = int(input("Recompensa (oro): "))

    with SessionLocal() as s:
        m = Mision(
            nombre=nombre,
            nivel_dificultad=dificultad,
            localizacion=localizacion,
            recompensa=recompensa
        )
        s.add(m)
        s.commit()
        print("Misión creada con ID:", m.id_mision)


def crear_monstruo():
    nombre = input("Nombre: ")
    tipo = input("Tipo: ")
    amenaza = int(input("Nivel amenaza (1-10): "))

    with SessionLocal() as s:
        mon = Monstruo(nombre=nombre, tipo=tipo, nivel_amenaza=amenaza)
        s.add(mon)
        s.commit()
        print("Monstruo creado con ID:", mon.id_monstruo)


def asignar_heroe_a_mision():
    id_heroe = int(input("ID héroe: "))
    id_mision = int(input("ID misión: "))

    with SessionLocal() as s:
        rel = MisionHeroe(id_heroe=id_heroe, id_mision=id_mision)
        s.add(rel)
        s.commit()
        print("Héroe asignado a misión.")


def asignar_monstruo_a_mision():
    id_monstruo = int(input("ID monstruo: "))
    id_mision = int(input("ID misión: "))

    with SessionLocal() as s:
        rel = MisionMonstruo(id_monstruo=id_monstruo, id_mision=id_mision)
        s.add(rel)
        s.commit()
        print("Monstruo asignado a misión.")


# ----------------------------
# Menú Principal
# ----------------------------

def main():
    init_db()

    while True:
        print("\n=== Gremio de Aventureros ===")
        print("1) Crear Héroe")
        print("2) Crear Misión")
        print("3) Crear Monstruo")
        print("4) Asignar Héroe a Misión")
        print("5) Asignar Monstruo a Misión")
        print("0) Salir")

        op = input("Opción: ")

        if op == "1":
            crear_heroe()
        elif op == "2":
            crear_mision()
        elif op == "3":
            crear_monstruo()
        elif op == "4":
            asignar_heroe_a_mision()
        elif op == "5":
            asignar_monstruo_a_mision()
        elif op == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
