

def show_all_notes():
    if not favorite_notes:
        print(" У вас пока нет избранных заметок")
        return

    for note in favorite_notes:
        print(f"{note['id']}. {note['text']}")

