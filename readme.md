# install

```
docker-compose up
```

# install db alembic

```
1. alembic revision --autogenerate -m "name_ver" (optional)
2. alembic upgrade head
2.1 alembic downgrade -1