
# 2D Fractal Generator

A 2D fractal generator made in Python that allows the user to zoom in and out of fractals that are color-coded based on iteration. The program allows exploration of the **Rational**, **Julia**, and **Mandelbrot** sets. It uses **Pygame** for rendering graphics, **NumPy** for computation, and **Numba** to optimize speed, making fractal generation efficient and responsive, even when zoomed in on detailed regions.

---

## Features

- **Fractal Types**: Generate and explore Mandelbrot, Julia, and Rational fractals.
- **Interactive Interface**: Zoom and pan across the fractals for an immersive experience.
- **Efficient Computation**: Uses the Numba library for speed optimization, ensuring fast fractal generation.
- **Color-Coded Iterations**: Colorful rendering of fractals based on the number of iterations.
- **Switch Fractals**: Easily switch between different fractal types using on-screen buttons.
- **Reset Zoom**: Reset the zoom level to return to the initial view with a click of a button.

---

https://github.com/colingalbraith/Fractal-Generator/assets/146497900/74c058b1-f3c5-4a72-abfb-201de4e88fee

![Untitled design (3)](https://github.com/colingalbraith/Fractal-Generator/assets/146497900/67bebf7b-3205-46c7-8451-000eebbb59bc)

![Untitled design (3) copy](https://github.com/colingalbraith/Fractal-Generator/assets/146497900/a01c2cbd-a351-437d-b228-b7ff62955781)

![Untitled design (3) copy 4](https://github.com/colingalbraith/Fractal-Generator/assets/146497900/85d00f3d-5652-4f5a-9f00-beb029324539)

![Untitled design (3) copy 3](https://github.com/colingalbraith/Fractal-Generator/assets/146497900/3c8b3acd-4f70-430b-ad70-478e75c379d7)

![Untitled design (3) copy 2](https://github.com/colingalbraith/Fractal-Generator/assets/146497900/0dbec693-2d12-44cd-8dff-4188a7307f95)

---

## Fractals Explained

### Mandelbrot Set

The Mandelbrot set is defined by iterating the function:

<img width="138" alt="image" src="https://github.com/user-attachments/assets/83c7ec57-1b84-4c28-a373-fc1013461a3a">

- **Initial Conditions**: Start with \( z = 0 \).
- **Iteration**: For each pixel, corresponding to a complex number \( c \), the function is iterated by applying the formula repeatedly: \( z = z^2 + c \).
- **Escape Criterion**: If \( |z| \) (the magnitude of \( z \)) exceeds 2, the point is considered to have escaped. The number of iterations before escaping is used to color the pixel.
- **Coloring**: Points that escape quickly are given brighter colors, while those that take longer to escape are given darker colors. Points that do not escape are colored black, indicating they belong to the Mandelbrot set.

https://en.wikipedia.org/wiki/Mandelbrot_set

### Julia Set

<img width="187" alt="image" src="https://github.com/user-attachments/assets/a9362a2d-f6bf-4ab7-89ee-113e31cbb8e4">

- **Fixed \( c \)**: In the Julia set, \( c \) is fixed, such as \( c = -0.7 + 0.27015i \).
- **Iteration**: For each pixel (corresponding to a complex number \( z \)), the function is iterated as \( z = z^2 + c \).
- **Escape Criterion**: If \( |z| \) exceeds 2, the point escapes, and the iteration count determines the pixel's color.


https://en.wikipedia.org/wiki/Julia_set

### Rational Fractals

- **Iteration**: For each pixel (represented by a complex number \( c \)), the rational formula is applied iteratively.
- **Escape Criterion**: Similar to the Mandelbrot and Julia sets, if \( |z| \) exceeds 2, the point escapes, and the number of iterations is used to determine the pixel color.

<img width="228" alt="image" src="https://github.com/user-attachments/assets/80477323-29a1-47be-932e-14ae351c2c44">


---

## Technical Details

The fractal generation is performed by iterating complex functions at each pixel and determining the escape time (i.e., how many iterations it takes before the point escapes the fractal's boundary). This value is used to color each pixel accordingly.

- **Zooming/Panning**: Zooming is achieved by dynamically adjusting the boundaries of the complex plane that the fractals are drawn on. Panning allows the user to shift these boundaries without changing the zoom level.
- **NumPy Arrays**: All computations are handled with NumPy arrays for efficient memory usage and fast numerical operations.
- **Numba Optimization**: The fractal generation loop is optimized using Numba's Just-In-Time (JIT) compilation, which accelerates Python code by compiling it to machine code at runtime.

---

## Installation

To run the Fractal Generator on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/colingalbraith/Fractal-Generator.git
   pip install -r requirements.txt
   python main.py

