from dataclasses import dataclass

@dataclass
class Planet:
    name: str
    type: str
    mass: float
    lengthOfDay: int
    lengthOfYear: int
    averageDistanceToStar: int
    
    