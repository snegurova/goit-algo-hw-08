"""Module providing a function merging lists."""
import heapq

def merge_k_lists(lists):
    """Function merging lists"""
    # Створюємо мін-купу
    min_heap = []

    # Ініціалізуємо купу першим елементом кожного списку
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []

    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)

        # Якщо є наступний елемент у цьому списку, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))

    return result

if __name__ == "__main__":
    # Приклад використання
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
