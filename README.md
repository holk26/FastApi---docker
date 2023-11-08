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
![Screenshot](https://github.com/holk26/FastApi/assets/23020718/faea7a6b-74ac-4abf-b642-262984e029cb)

![Screenshot-2](https://github.com/holk26/FastApi/assets/23020718/3790cc8a-2654-4032-9c2e-451b4ee591bd)

![Screenshot-4](https://github.com/holk26/FastApi/assets/23020718/5da2b164-4b5f-468c-ba8e-1aa4f333ddb1)

![Screenshot-5](https://github.com/holk26/FastApi/assets/23020718/77ef6978-a470-4674-a1f4-c31bcf297e96)





