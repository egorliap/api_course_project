from datetime import date

class RBTask:
    def __init__(self,
                 id: int | None = None,
                 lesson_id: int | None = None,
                 given: date | None = None):
        self.id = id
        self.lesson_id = lesson_id
        self.given = given
        
    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "lesson_id": self.lesson_id,
            "given": self.given,
            }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
                         }
        return filtered_data