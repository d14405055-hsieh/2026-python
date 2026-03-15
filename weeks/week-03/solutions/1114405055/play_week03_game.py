from __future__ import annotations

from uva100_3n1 import solve as solve_100
from uva118_mutant_flatworld import solve as solve_118
from uva272_tex_quotes import solve as solve_272
from uva299_train_swapping import solve as solve_299
from uva490_rotating_sentences import solve as solve_490
from robot_game import main as robot_game_main


DEMO_INPUTS = {
    "1": (
        "UVA 100 - 3n + 1",
        "1 10\n100 200\n201 210\n900 1000\n",
        solve_100,
    ),
    "2": (
        "UVA 118 - Mutant Flatworld Explorers",
        "5 3\n1 1 E\nRFRFRFRF\n3 2 N\nFRRFLLFFRRFLL\n0 3 W\nLLFFFLFLFL\n",
        solve_118,
    ),
    "3": (
        "UVA 272 - TEX Quotes",
        '"To be or not to be," quoth the bard, "that is the question."\n',
        solve_272,
    ),
    "4": (
        "UVA 299 - Train Swapping",
        "3\n3\n1 3 2\n4\n4 3 2 1\n2\n2 1\n",
        solve_299,
    ),
    "5": (
        "UVA 490 - Rotating Sentences",
        'Rene Decartes once said,\n"I think, therefore I am."\n',
        solve_490,
    ),
}


def print_menu() -> None:
    print("\n=== Week 03 Mini Game ===")
    print("1) Play UVA 100 demo")
    print("2) Play UVA 118 demo")
    print("3) Play UVA 272 demo")
    print("4) Play UVA 299 demo")
    print("5) Play UVA 490 demo")
    print("6) Custom input mode")
    print("7) Score challenge mode")
    print("8) Robot Lost 星圖巡航遊戲")
    print("q) Quit")


def read_multiline() -> str:
    print("Paste your input. Type a single line END to finish:")
    lines: list[str] = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    return "\n".join(lines) + ("\n" if lines else "")


def normalize_output(text: str) -> str:
    lines = text.rstrip("\n").split("\n")
    return "\n".join(line.rstrip() for line in lines).strip()


def run_demo(choice: str) -> None:
    title, sample_input, solver = DEMO_INPUTS[choice]
    print(f"\n--- {title} ---")
    print("[Sample Input]")
    print(sample_input, end="")
    print("[Output]")
    print(solver(sample_input))


def run_custom() -> None:
    print("Choose problem: 1=100, 2=118, 3=272, 4=299, 5=490")
    target = input("Problem number: ").strip()
    if target not in DEMO_INPUTS:
        print("Invalid problem number.")
        return

    title, _, solver = DEMO_INPUTS[target]
    print(f"\n--- Custom Mode: {title} ---")
    text = read_multiline()
    print("[Output]")
    print(solver(text))


def run_score_challenge() -> None:
    print("\n=== Score Challenge ===")
    print("Rules: 5 questions, each 1 point.")
    print("For each question, read sample input and type expected output.")
    print("Finish each answer with a single line END.")

    total = 0
    score = 0

    for key in ["1", "2", "3", "4", "5"]:
        total += 1
        title, sample_input, solver = DEMO_INPUTS[key]
        expected = normalize_output(solver(sample_input))

        print(f"\nQ{total}: {title}")
        print("[Input]")
        print(sample_input, end="")
        print("Type your expected output, then END:")
        user_answer = normalize_output(read_multiline())

        if user_answer == expected:
            score += 1
            print("Correct!")
        else:
            print("Not quite.")
            print("[Expected]")
            print(expected)

    print(f"\nFinal Score: {score}/{total}")
    if score == total:
        print("Perfect score!")
    elif score >= 3:
        print("Nice work. Keep going!")
    else:
        print("Good try. Replay to improve your score!")


def main() -> None:
    while True:
        print_menu()
        choice = input("Select: ").strip().lower()

        if choice == "q":
            print("Bye. Have fun!")
            return
        if choice in DEMO_INPUTS:
            run_demo(choice)
            continue
        if choice == "6":
            run_custom()
            continue
        if choice == "7":
            run_score_challenge()
            continue
        if choice == "8":
            robot_game_main()
            continue

        print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
