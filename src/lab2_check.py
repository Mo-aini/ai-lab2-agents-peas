# Lab 2 - test cases for the model based agent
try:
    from .lab2_model import ClassroomAgent, StatefulClassroomAgent
    from .lab2_percepts import percepts as SUPPLIED_PERCEPTS
except ImportError:                      # so it also runs as: python src/lab2_check.py
    from lab2_model import ClassroomAgent, StatefulClassroomAgent
    from lab2_percepts import percepts as SUPPLIED_PERCEPTS

# (percept, scenario label, expected target, expected send_command)
SCENARIO = [
    ((29, True), "first percept, hot and occupied", "COOL", True),
    ((29, True), "repeated percept", "COOL", False),
    ((26, True), "exact upper boundary 26 C (not > 26); transition COOL->IDLE", "IDLE", True),
    ((20, True), "exact lower boundary 20 C (not < 20); same mode", "IDLE", False),
    ((19, True), "mode transition IDLE->WARM", "WARM", True),
    ((19, False), "empty room: occupancy priority over cold reading", "ECO", True),
    ((29, False), "empty room again, hot: still ECO, no repeat", "ECO", False),
    ((24, True), "room re-occupied, comfortable", "IDLE", True),
]

NOISY = [(26.4, True), (25.8, True), (26.2, True), (25.9, True), (26.1, True), (26.3, True)]


def trace(agent, sequence):
    rows = []
    for step, percept in enumerate(sequence, 1):
        prev = agent.previous_mode
        target, send = agent.act(*percept)
        rows.append((step, prev, percept, target, send))
    return rows


def fmt_prev(p):
    return "-" if p is None else p


def run_scenario():
    print("Required scenario (repeated percepts, both boundaries, transition, empty room):")
    print("step | previous mode | percept (temp C, occupied) | target | command | check | scenario")
    agent = StatefulClassroomAgent()
    passed = 0
    for (step, prev, percept, target, send), (_, label, exp_t, exp_s) in zip(trace(agent, [s[0] for s in SCENARIO]), SCENARIO):
        ok = (target, send) == (exp_t, exp_s)
        passed += ok
        print(step, fmt_prev(prev), percept, target, "SEND" if send else "no command",
              "PASS" if ok else "FAIL", label, sep=" | ")
    print("Checks passed: %d/%d" % (passed, len(SCENARIO)))
    return passed


def run_reflex_vs_stateful():
    print("Reflex vs stateful on the manual's supplied percept list:")
    print("step | percept | reflex target | reflex sends | stateful previous | stateful target | stateful command")
    reflex, stateful = ClassroomAgent(), StatefulClassroomAgent()
    sent_reflex = sent_state = 0
    for step, percept in enumerate(SUPPLIED_PERCEPTS, 1):
        r = reflex.act(*percept)
        prev = stateful.previous_mode
        t, s = stateful.act(*percept)
        sent_reflex += 1
        sent_state += s
        print(step, percept, r, "SEND", fmt_prev(prev), t, "SEND" if s else "no command", sep=" | ")
    print("Commands sent: reflex %d, stateful %d (targets identical at every step)." % (sent_reflex, sent_state))


def run_noisy():
    print("Noisy sequence around 26 C (Section 2.7): memory alone is not hysteresis")
    print("step | previous mode | percept | target | command")
    rows = trace(StatefulClassroomAgent(), NOISY)
    for step, prev, percept, target, send in rows:
        print(step, fmt_prev(prev), percept, target, "SEND" if send else "no command", sep=" | ")
    print("Commands sent: %d of %d steps; the mode flips every time the reading crosses 26 C."
          % (sum(r[4] for r in rows), len(rows)))


def main():
    print("=" * 72)
    print("LAB 2 / Task 3  lab2_model.py + lab2_check.py  (stateful agent)")
    print("=" * 72)
    run_scenario()
    print()
    run_reflex_vs_stateful()
    print()
    run_noisy()


if __name__ == "__main__":
    main()
