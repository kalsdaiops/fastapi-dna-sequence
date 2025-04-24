import random
from models import SessionLocal, DNASequence

# Function to generate a random DNA sequence
def generate_dna_sequence(length=100):
    return ''.join(random.choices('ATCG', k=length))

# Insert DNA sequences into the database
def insert_sequences():
    db = SessionLocal()
    try:
        for _ in range(10):  # Insert 10 random sequences
            seq = generate_dna_sequence()
            new_sequence = DNASequence(sequence=seq)
            db.add(new_sequence)
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    insert_sequences()
    print("DNA sequences inserted into the database.")
