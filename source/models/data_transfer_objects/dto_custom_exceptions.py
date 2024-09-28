from http import HTTPStatus
from typing import List

ENTITY_MAP = {
    "Title": "Já existe um produto com o mesmo título no banco de dados!",
    "Barcode": "Já existe um produto com o mesmo código de barras no banco de dados!",
    "Email": "Já existe um usuário com o mesmo email no banco de dados!",
    "Username": "Já existe um usuário com o mesmo username no banco de dados!",
    "Chat": "Já existe um chat com o mesmo id no banco de dados!",
    "Whatsapp": "Já existe um chat com o mesmo id no banco de dados!"
}


class EntityAlreadyExistsException(Exception):
    def __init__(self, entity_tag: str, entity):
        self.message = f"Conflict on Entity [{entity}]"
        self.description = ENTITY_MAP[entity_tag]
        self.error_type = "EntityAlreadyExistsException"
        self.status_code = HTTPStatus.BAD_REQUEST
        super().__init__(self.message)


class ChatAlreadyExistsException(Exception):
    def __init__(self, system_user_id: int, customer_user_id: int):
        self.message = f"Conflict on Chat [{system_user_id}, {customer_user_id}]"
        self.description = (f"Já existe um chat atrelado ao [SystemUser #{system_user_id}] "
                            f"e ao [CustomerUser #{customer_user_id}]")
        self.error_type = "ChatAlreadyExistsException"
        self.status_code = HTTPStatus.BAD_REQUEST
        super().__init__(self.message)


class EntityNotFoundException(Exception):
    def __init__(self, entity_type: str, entity_name: str):
        self.message = "Operation not performed! Contact the system administrator!"
        self.description = f"{entity_type} [{entity_name}] não foi encontrado no banco de dados!"
        self.error_type = "EntityNotFoundException"
        self.status_code = HTTPStatus.NOT_FOUND
        super().__init__(self.message)


class InvalidFileTypeException(Exception):
    def __init__(self, input_message: str = None, input_description: str = None):
        self.message = "Operation not performed! Contact the system administrator!"
        self.description = "Tipo de arquivo inválido!"
        self.error_type = "InvalidFileTypeException"
        self.status_code = HTTPStatus.BAD_REQUEST
        if input_message:
            self.message = input_message
        if input_description:
            self.description = input_description
        super().__init__(self.message)


class PermissionDeniedException(Exception):
    def __init__(self, input_message: str = None, input_description: str = None):
        self.message = "Operation not performed! Contact the system administrator!"
        self.description = "Permissão negada!"
        self.error_type = "PermissionDeniedException"
        self.status_code = HTTPStatus.FORBIDDEN
        if input_message:
            self.message = input_message
        if input_description:
            self.description = input_description
        super().__init__(self.message)


class TokenNotAvailableException(Exception):
    def __init__(self, input_message: str = None, input_description: str = None):
        self.message = "The token is not available anymore. Please log in again and get a new token."
        self.description = "O token não está mais disponível. Por favor, faça login novamente e obtenha um novo token."
        self.error_type = "TokenNotAvailableException"
        self.status_code = HTTPStatus.BAD_REQUEST
        if input_message:
            self.message = input_message
        if input_description:
            self.description = input_description
        super().__init__(self.message)


class MissingBodyException(Exception):
    def __init__(self, input_message: str = None, inputDescription: str = None):
        self.message = "The request body is missing or empty!"
        self.description = "Corpo da requisição está faltando ou vazio!"
        self.error_type = "MissingBodyException"
        self.status_code = HTTPStatus.BAD_REQUEST
        if input_message:
            self.message = input_message
        if inputDescription:
            self.description = inputDescription
        super().__init__(self.message)


class MissingBodyParameterException(Exception):
    def __init__(self, parameter_name: str, all_parameters: List[str]):
        self.message = f"Missing required parameter: {parameter_name}"
        self.description = f"Essa requisição requer os seguintes parâmetros: {all_parameters}"
        self.error_type = "MissingBodyParameterException"
        self.status_code = HTTPStatus.BAD_REQUEST
        super().__init__(self.message)


class InvalidStatusValueException(Exception):
    def __init__(self, invalid_status: str, valid_statuses: List[str]):
        self.message = f"Invalid status value: '{invalid_status}'"
        self.description = f"Valores de status válidos são: {valid_statuses}"
        self.error_type = "InvalidStatusValueException"
        self.status_code = HTTPStatus.BAD_REQUEST
        super().__init__(self.message)


class SQLIntegrityErrorException(Exception):
    def __init__(self, input_message: str, sql_parameters: str):
        self.error_type = "SQLIntegrityErrorException"
        self.status_code = HTTPStatus.BAD_REQUEST
        self.message = input_message
        self.description = sql_parameters
        super().__init__(self.message)


class InvalidLoginCredentialsException(Exception):
    def __init__(self):
        self.error_type = "InvalidLoginCredentialsException"
        self.status_code = HTTPStatus.UNAUTHORIZED
        self.message = "Invalid login credentials!"
        self.description = "Nome de usuário ou senha incorretos! Por favor, tente novamente"
        super().__init__(self.message)