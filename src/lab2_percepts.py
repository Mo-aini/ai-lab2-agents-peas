# Lab 2 Section 2.5 - supplied percept code from the manual


# code from the manual (Section 2.5)
class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"


percepts = [(29, True), (29, True), (20, True),
            (26, True), (19, True), (29, False)]

EXPECTED = ["COOL", "COOL", "IDLE", "IDLE", "WARM", "ECO"]   # from the manual


def main():
    print("=" * 72)
    print("LAB 2 / Section 2.5  lab2_percepts.py  (supplied reflex agent)")
    print("=" * 72)
    agent = ClassroomAgent()
    got = []
    for step, percept in enumerate(percepts, 1):
        mode = agent.act(*percept)
        got.append(mode)
        print(step, percept, "target mode", mode)
    print("Expected (manual):", ", ".join(EXPECTED))
    print("Matches manual:", got == EXPECTED)
    print("Note: the reflex agent returns COOL at steps 1 and 2. It has no memory, so it would")
    print("re-send the same COOL command although cooling was already requested.")


if __name__ == "__main__":
    main()
