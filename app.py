"""Aplicación de ejemplo."""
import os


def obtener_ambiente():
    return os.getenv("APP_ENV", "local")


def saludar(nombre):
    if not nombre or not nombre.strip():
        raise ValueError("Nombre vacío")
    env = obtener_ambiente()
    return f"Hola {nombre.strip()}! Ambiente: {env}"


def calcular_promedio(notas):
    """Calcula el promedio de notas."""
    if not notas:
        raise ValueError("Lista vacía")
    return sum(notas) / len(notas)


if __name__ == '__main__':
    print(saludar("Estudiante IU Digital"))
