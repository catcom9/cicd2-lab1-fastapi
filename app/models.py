from sqlalchemy import Interger,  String
from sqlalchemy.orm import DeclartiveBase, Mapped, mapped_column

class Base(DeclartiveBase):
    pass

class UserDB(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    age: Mapped[int] = mapped_column(Interger, nullable=False)
    student_id: Mapped[str] = mapped_column(
        String(8), unique=True, nullable=False
    )