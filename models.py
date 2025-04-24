from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DNASequence(Base):
    __tablename__ = "dna_sequences"
    id = Column(Integer, primary_key=True, index=True)
    sequence = Column(Text, nullable=False)
