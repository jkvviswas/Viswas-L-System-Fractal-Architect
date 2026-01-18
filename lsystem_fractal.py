import tkinter as tk
import turtle

def expand_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string
    return current

def draw_lsystem(t, instructions, angle, step):
    stack = []
    for i, cmd in enumerate(instructions):
        t.pencolor(0, max(0, 0.6 - i / len(instructions)), 0)
        if cmd == "F":
            t.forward(step)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            stack.append((t.position(), t.heading()))
        elif cmd == "]":
            pos, heading = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

def generate():
    canvas.delete("all")
    axiom = axiom_entry.get()
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())
    rules = {}
    raw_rules = rules_entry.get().split(",")
    for rule in raw_rules:
        k, v = rule.split(":")
        rules[k.strip()] = v.strip()
    final_string = expand_lsystem(axiom, rules, iterations)
    screen = turtle.TurtleScreen(canvas)
    screen.tracer(0, 0)
    t = turtle.RawTurtle(screen)
    t.hideturtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    draw_lsystem(t, final_string, angle, 5)
    screen.update()

root = tk.Tk()
root.title("L-System Fractal Architect")

left = tk.Frame(root)
left.pack(side=tk.LEFT, padx=10)

tk.Label(left, text="Axiom").pack()
axiom_entry = tk.Entry(left)
axiom_entry.insert(0, "F")
axiom_entry.pack()

tk.Label(left, text="Rules (F:FF+[+F-F-F]-[-F+F+F])").pack()
rules_entry = tk.Entry(left, width=40)
rules_entry.insert(0, "F:FF+[+F-F-F]-[-F+F+F]")
rules_entry.pack()

tk.Label(left, text="Angle").pack()
angle_entry = tk.Entry(left)
angle_entry.insert(0, "25")
angle_entry.pack()

tk.Label(left, text="Iterations").pack()
iter_entry = tk.Entry(left)
iter_entry.insert(0, "4")
iter_entry.pack()

tk.Button(left, text="Generate", command=generate).pack(pady=10)

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(side=tk.RIGHT)

root.mainloop()
