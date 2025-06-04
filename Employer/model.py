from db.models import DbUser
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Float
from sqlalchemy.orm import relationship

class Employer(DbUser):
    __tablename__ = "employer"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    projects_as_employer = relationship(
        "DbProjects",
        back_populates="employer",
        foreign_keys="DbProjects.employer_id"
    )
    