# Lab 2 Task 3 - model based classroom agent
# same thresholds as the manual agent (>26 COOL, <20 WARM, empty room -> ECO first)
# previous_mode stores the last mode so the same command is not sent twice


class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"


class StatefulClassroomAgent(ClassroomAgent):
    def __init__(self):
        self.previous_mode = None   # last mode, None at the start

    def act(self, temp, occupied):
        target = super().act(temp, occupied)  # same rules as the reflex agent
        send_command = target != self.previous_mode  # only send if the mode changed
        self.previous_mode = target  # remember it for next time
        return target, send_command
