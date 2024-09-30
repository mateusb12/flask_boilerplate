import re
from typing import Optional, Tuple, List, Any

from models.data_transfer_objects.dto_custom_exceptions import EntityAlreadyExistsException


def extract_violation_details(constraint_message: str) -> list[Any]:
    """
    Extracts the constraint name, field, and value from a PostgreSQL unique constraint violation message.

    Args:
        constraint_message (str): The error message from the IntegrityError exception.

    Returns:
        Optional[Tuple[str, str, str]]: A tuple containing the constraint name, field, and value if matched,
         otherwise None.
    """
    matches = re.findall(r'\"([^\"]+)\"', constraint_message)
    return matches


def handle_integrity_error(error, table_name, unique_fields, entity):
    """
    Handles integrity errors arising from unique constraint violations in PostgreSQL, specifically targeting
    instances where a duplicate value is attempted to be inserted into a column that enforces uniqueness.

    This function parses the error message to identify the specific constraint that was violated and raises
    a custom `EntityAlreadyExistsException` with details about the entity and the field causing the violation.
    If the violated constraint doesn't match any of the fields specified, it re-raises the original error.

    Args:
        error (Exception): The original integrity error exception caught, which contains details about the
            constraint violation.
        table_name (str): The name of the database table involved in the operation that led to the integrity error.
        unique_fields (List[str]): A list of field names that have unique constraints in the table, and are thus
            potential candidates for causing the integrity error.
        entity (Any): An object or identifier representing the entity that was being manipulated or created
            when the error occurred. This is used for reporting in the custom exception.

    Raises:
        EntityAlreadyExistsException: If the error message indicates a unique constraint violation on one of
            the specified fields. The exception includes the field name (capitalized) and the entity involved.
        Exception: If the constraint violation is not related to the specified unique fields, the original
            error is re-raised, preserving the original error context and message.

    Returns:
        None
    """
    constraint_message = str(error.orig).lower()
    constraint_info = extract_violation_details(constraint_message)

    for field in unique_fields:
        tag = f"{table_name}_{field}_key".lower()
        if tag in constraint_info:
            raise EntityAlreadyExistsException(
                entity_tag=field.capitalize(),
                entity=entity)
    raise error