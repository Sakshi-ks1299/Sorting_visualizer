import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            yield a.copy()


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
            yield a.copy()
        a[i], a[min_idx] = a[min_idx], a[i]
        yield a.copy()


def quick_sort(arr):
    a = arr.copy()

    def _quick_sort(low, high):
        if low < high:
            pivot = a[high]
            i = low - 1
            for j in range(low, high):
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
                yield a.copy()
            a[i + 1], a[high] = a[high], a[i + 1]
            yield a.copy()
            yield from _quick_sort(low, i)
            yield from _quick_sort(i + 2, high)

    yield from _quick_sort(0, len(a) - 1)
    yield a.copy()


ALGORITHMS = {
    "bubble": ("Bubble Sort", bubble_sort),
    "selection": ("Selection Sort", selection_sort),
    "quick": ("Quick Sort", quick_sort),
}


def visualize(algorithm_key="bubble", size=30, interval=40):
    name, algo_func = ALGORITHMS[algorithm_key]
    data = [random.randint(1, 100) for _ in range(size)]
    generator = algo_func(data)

    fig, ax = plt.subplots()
    bar_container = ax.bar(range(len(data)), data, color="royalblue")
    ax.set_title(f"{name} Visualization")
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, 110)

    def update(frame):
        for bar, val in zip(bar_container, frame):
            bar.set_height(val)
        return bar_container

    anim = animation.FuncAnimation(
        fig, update, frames=generator, interval=interval, repeat=False, save_count=2000
    )
    plt.show()
    return anim


if __name__ == "__main__":
    print("Available algorithms:", ", ".join(ALGORITHMS.keys()))
    choice = input("Choose an algorithm to visualize [bubble]: ").strip().lower() or "bubble"
    visualize(algorithm_key=choice, size=30, interval=40)
