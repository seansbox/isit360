# Import necessary components from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.engine import Engine
from sqlalchemy.sql import select
from sqlalchemy.inspection import inspect

# Define the base class for our models using the updated function
Base = declarative_base()

# Association table for the many-to-many relationship between Movies and Celebs
movie_celeb_association = Table(
    "map_movie_celeb",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("movie_id", String, ForeignKey("movies.id")),
    Column("celeb_id", String, ForeignKey("celebs.id")),
)


# Define the Movie model
class Movie(Base):
    __tablename__ = "movies"

    id = Column(String, primary_key=True)
    name = Column(String)
    release = Column(Date, nullable=True)
    meter = Column(Integer)
    score = Column(Integer)
    thumb = Column(String)
    summary = Column(String)

    celebs = relationship("Celeb", secondary=movie_celeb_association, back_populates="movies")

    def __repr__(self):
        return f"<Movie(name={self.name}, release={self.release})>"


# Define the Celeb model
class Celeb(Base):
    __tablename__ = "celebs"

    id = Column(String, primary_key=True)
    name = Column(String)
    # SQLAlchemy caught that my existing birthday field had blank strings in the
    # field ("") instead of being truly empty (NULL) when an actor had no birthday.
    # I ran this on my movie data to resolve:
    #   UPDATE celebs SET birthday = NULL WHERE birthday = ""
    birthday = Column(Date, nullable=True)
    birthplace = Column(String)
    thumb = Column(String)
    summary = Column(String)

    movies = relationship("Movie", secondary=movie_celeb_association, back_populates="celebs")

    def __repr__(self):
        return f"<Celeb(name={self.name}, birthday={self.birthday})>"


# Create an SQLite engine connected to the specified file
engine = create_engine("sqlite:///movies.sqlite3", echo=True)

# Create a Session class and bind it to the engine
Session = sessionmaker(bind=engine)
session = Session()

# Check if tables already exist using the inspection API
inspector = inspect(engine)
if not inspector.has_table("movies") or not inspector.has_table("celebs") or not inspector.has_table("map_movie_celeb"):
    Base.metadata.create_all(engine)

# Insert or query data here
# Note: Be careful with inserting data to avoid duplicates when the script is run multiple times.

# Query data from the database
movies = session.query(Movie).all()
celebs = session.query(Celeb).all()

print(movies)
print(celebs)

# Close the session
session.close()
