from source.gateway.sqlite_client import SQLiteClient, SQLiteBase

if __name__ == "__main__":
    sqlite_client = SQLiteClient()
    SQLiteBase.metadata.create_all(bind=sqlite_client._engine)