# Para iniciar el docker de todo el proyecto, siga estos pasos:

- tambien se documento con swagger http://127.0.0.1:8000/docs

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

```
docker run --name mysql -v /home/homero/mysql-db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=users -p 3306:3306 -d mysql
```

# Finalmente, inicie todos los servicios definidos en el archivo docker-compose con el siguiente comando:

```
docker compose up -d
```
