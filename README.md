# Sorting Algorithm Visualizer

A Python tool that visually animates how classic sorting algorithms work,
using `matplotlib` bar charts that update in real time as the array sorts itself.

![Bubble Sort Demo](demo.gif)

## Algorithms Included
- **Bubble Sort**
- **Selection Sort**
- **Quick Sort**

Each algorithm is implemented as a Python **generator**, yielding the array's
state after every comparison/swap — this state is then fed frame-by-frame into
a `matplotlib` animation.

## Tech Used
- Python 3
- `matplotlib` (animation + plotting)

## How to Run
```bash
pip install matplotlib
python sorting_visualizer.py
```

You'll be prompted to choose an algorithm (`bubble`, `selection`, or `quick`),
then a live animated bar chart will open showing the sort happening step by step.

## What This Project Demonstrates
- Strong understanding of core **Data Structures & Algorithms** (sorting, complexity, recursion in Quick Sort)
- Use of **Python generators** for memory-efficient step-by-step state tracking
- Applying programming to **visual/interactive output**, not just console text
- Clean, extensible code structure — new algorithms can be added by writing one generator function and registering it in `ALGORITHMS`

## Possible Extensions
- Add Merge Sort, Insertion Sort, Heap Sort
- Display live comparison/swap counters
- Add a speed slider using `matplotlib.widgets`
