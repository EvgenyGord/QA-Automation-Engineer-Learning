from pydantic import BaseModel, StrictStr


class User_Delete_Response(BaseModel):
    # Модель пустая, так как ответа нет при 204
    pass