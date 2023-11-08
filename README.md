# Explicacion: 

La API está desarrollada usando FastAPI, y para las operaciones de base de datos se emplea el Object-Relational Mapper (ORM) SQLAlchemy. El servidor es manejado por Uvicorn y las migraciones de la base de datos se realizan con Alembic. La base de datos MySQL se ejecuta en un contenedor Docker, y la API proporciona una funcionalidad para buscar empleos.

La API incluye documentación interactiva generada por Swagger, la cual está disponible en: http://127.0.0.1:8000/docs.

1. crear entorno virtual

```
  python -m venv venv
```

2. Active el entorno virtual venv e instale los requisitos:

   ```
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Inicie el servidor Uvicorn:

   ```
   uvicorn app.main:app --reload
   ```

cuatro. Ejecute el contenedor de MySQL con el siguiente comando:


nota: modifica esta linea por su ubicacion /home/homero/mysql-db
```
docker run --name mysql -v /home/homero/mysql-db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=users -p 3306:3306 -d mysql
```

# Finalmente, inicie todos los servicios definidos en el archivo docker-compose con el siguiente comando:

```
docker compose up -d
```
![Screenshot-5](https://github.com/holk26/FastApi---docker/assets/23020718/0dd24938-fb93-428f-ac4a-78c8e543a428)

![Screenshot-4](https://github.com/holk26/FastApi---docker/assets/23020718/eb93c8a8-ef4a-4750-a7ad-6e73d0f3f7a7)

![Screenshot-2](https://github.com/holk26/FastApi---docker/assets/23020718/b4e472af-3840-4b0a-9e74-0afc23229fa6)

![Screenshot](https://github.com/holk26/FastApi---docker/assets/23020718/8009bdc7-4250-42ac-9440-e5cfa02cc7d2)




