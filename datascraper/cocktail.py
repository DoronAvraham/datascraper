import dataclasses

@dataclasses.dataclass
class Cocktail:
    id: str
    name: str
    ingredients: list[str]
    measures: list[str]
    instructions: str
    thumbnail_url: str
    image_url: str
