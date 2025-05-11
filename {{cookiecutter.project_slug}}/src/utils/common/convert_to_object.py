import json
from typing import Type, TypeVar
from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)


def parse_data(schema: Type[T], data: str) -> T:
    """
    Generic function to parse JSON data into a Pydantic schema.

    :param schema: The Pydantic schema class
    :param data: The JSON string to parse
    :return: An instance of the schema
    :raises ValidationError: If the data is invalid
    """
    try:
        # First, convert the JSON string to a Python dictionary
        parsed_dict = json.loads(data)
        # Then, validate using the Pydantic schema
        return schema.model_validate(parsed_dict)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        raise ValueError("Invalid JSON data") from e
    except ValidationError as e:
        print(f"Validation failed for schema {schema.__name__}: {e}")
        raise
