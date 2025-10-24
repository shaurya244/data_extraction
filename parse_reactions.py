from chemdataextractor import Document

def extract_reactions_from_text(text):
    doc = Document(text)
    reactions = []
    for record in doc.records:
        if hasattr(record, 'serialize'):
            reactions.append(record.serialize())
    return reactions
