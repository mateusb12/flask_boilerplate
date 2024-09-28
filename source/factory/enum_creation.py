from enum import Enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from source.models.enums import database_enums as db_enums


def _create_database_enums(input_db_instance: SQLAlchemy):
    all_enums = [attr for attr in dir(db_enums) if isinstance(getattr(db_enums, attr), type)
                 and issubclass(getattr(db_enums, attr), Enum) and getattr(db_enums, attr) is not Enum]

    # Loop through each Enum class and create a PostgresSQL ENUM type
    for enum_name in all_enums:
        enum_class = getattr(db_enums, enum_name)

        # Generate ENUM type name in PostgresSQL and ENUM options
        enum_type_name = enum_name.lower()  # Example: 'orderstatus' becomes 'orderstatus'
        enum_options = ', '.join(f"'{item.value}'" for item in enum_class)

        # SQL to check if the type already exists
        check_type_exists_sql = f"SELECT EXISTS (SELECT 1 FROM pg_type WHERE typname = '{enum_type_name}');"

        # SQL to create ENUM type
        create_type_sql = f"CREATE TYPE {enum_type_name} AS ENUM ({enum_options});"

        # Execute SQL commands
        with input_db_instance.engine.connect() as connection:
            result = connection.execute(text(check_type_exists_sql)).scalar()
            if result:
                # print(f"Type {enum_type_name} already exists. Dropping and recreating...")
                drop_type_sql = f"DROP TYPE IF EXISTS {enum_type_name};"
                connection.execute(text(drop_type_sql))
            # print(f"Creating Enum [{enum_type_name}] with options [{enum_options}]")
            connection.execute(text(create_type_sql))

