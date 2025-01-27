class RBLesson:
    def __init__(self, 
                 lesson_id:int | None = None,
                 student_id:int | None = None,
                 teacher_id:int | None = None):
        self.id = lesson_id
        self.student_id = student_id
        self.teacher_id = teacher_id
    
    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "student_id": self.student_id,
            "teacher_id": self.teacher_id
            }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
            }
        return filtered_data