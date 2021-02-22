from sqlalchemy import Column, Integer, String


from db.database import Base, engine


class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

    def __repr__(self):
        return "<Command(question='%s', answer='%s')>" % (
            self.question, self.answer)


Base.metadata.create_all(engine)
