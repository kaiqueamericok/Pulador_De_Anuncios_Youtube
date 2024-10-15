from cx_Freeze import setup, Executable

setup(
    name="Pulador_Anuncios",
    version="1.0",
    description="Pular Anuncios de youtube",
    executables=[Executable("app.py")],
)