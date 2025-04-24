from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from models import Base, DNASequence

app = FastAPI()
Base.metadata.create_all(bind=engine)

class DNASequenceCreate(BaseModel):
    sequence: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dna_sequences")
def create_dna_sequence(seq: DNASequenceCreate, db: Session = Depends(get_db)):
    db_seq = DNASequence(sequence=seq.sequence)
    db.add(db_seq)
    db.commit()
    db.refresh(db_seq)
    return {"id": db_seq.id, "sequence": db_seq.sequence}

@app.get("/dna_sequences")
def read_dna_sequences(db: Session = Depends(get_db)):
    sequences = db.query(DNASequence).all()
    return {"sequences": [s.sequence for s in sequences]}
