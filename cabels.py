"""Module providing a function minimizing consumptions."""
import heapq

def min_cost_to_connect_cables(cables):
    """Function minimizing consumptions"""
    # Перетворюємо список кабелів на мін-купу
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість їх з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо з'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

if __name__ == "__main__":
    # Приклад використання
    cables = [4, 3, 2, 6]
    print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
