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


def delete_note(note_id):
    if not favorite_notes:
        return "Нет заметок для удаления"

    for i, note in enumerate(favorite_notes):
        if note['id'] == note_id:
            deleted_note = favorite_notes.pop(i)
            # Перенумерация ID
            for idx, remaining_note in enumerate(favorite_notes, start=1):
                remaining_note['id'] = idx
            return f"✅ Заметка '{deleted_note['text']}' удалена"

    return f" Заметка с ID {note_id} не найдена"


def calculate_taxi_price(distance_km):
    base_price = 100
    price_per_km = 25

    if distance_km > 20:
        price_per_km = 20
    elif distance_km > 10:
        price_per_km = 22

    total = base_price + (distance_km * price_per_km)
    return round(total, 2)


def show_menu():
    print(" ИЗБРАННОЕ: ЗАМЕТКИ И ТАКСИ ")
    print("1.  Добавить заметку в избранное")
    print("2.  Показать все избранные заметки")
    print("3.  Удалить заметку")
    print("4.  Рассчитать стоимость такси")
    print("0.  Выход")

