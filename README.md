# MedSchedule Microservice API 

Using Django Rest Framework, Django Socio Grpc with PostgreSQL

## Running the app 

```
$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py

$ python manage.py grpcrunaioserver --dev

```

## Generate files GRPC

```

$ python manage.py generateproto

```

## Routes
### Appointments
```
GET /appointments -> Retorna todos os agendamentos registrados.
POST /appointments -> Cria um novo agendamento.
GET /appointments/:id -> Retorna o agendamento com o ID especificado.
PUT /appointments/:id -> Atualiza o agendamento com o ID especificado.
DELETE /appointments/:id -> Deleta o agendamento com o ID especificado.
```
