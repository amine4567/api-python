from pydantic import BaseModel


def custom_to_pascal(snake: str, dont_alias: list[str] | None = None):
    if dont_alias and snake in dont_alias:
        return snake
    parts = snake.split("_")
    converted_parts = [part.capitalize() if part != "id" else "ID" for part in parts]
    pascal_case_string = "".join(converted_parts)
    return pascal_case_string


class RAAPIResponse(BaseModel):
    class Config:
        alias_generator = custom_to_pascal
        extra = "forbid"
