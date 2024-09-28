from models.data_transfer_objects.dto_custom_exceptions import EntityNotFoundException, InvalidFileTypeException, \
    PermissionDeniedException, EntityAlreadyExistsException, TokenNotAvailableException, MissingBodyException, \
    MissingBodyParameterException, InvalidStatusValueException, SQLIntegrityErrorException, \
    InvalidLoginCredentialsException, ChatAlreadyExistsException

EXCEPTIONS = [
    EntityNotFoundException, InvalidFileTypeException, PermissionDeniedException,
    EntityAlreadyExistsException, TokenNotAvailableException, MissingBodyException,
    MissingBodyParameterException, InvalidStatusValueException, SQLIntegrityErrorException,
    InvalidLoginCredentialsException, ChatAlreadyExistsException
]