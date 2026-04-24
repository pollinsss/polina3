favorite_notes = []

def add_favorite_note(note):
    if not note.strip():
        return "Заметка не может быть пустой!"

    note_id = len(favorite_notes) + 1
    favorite_notes.append({
        'id': note_id,
        'text': note.strip()
    })
    return f"Заметка добавлена в избранное (ID: {note_id})"


def show_all_notes():
    if not favorite_notes:
        print(" У вас пока нет избранных заметок")
        return

    for note in favorite_notes:
        print(f"{note['id']}. {note['text']}")

