# AI Lab 2 - Intelligent Agents and PEAS

Lab 2 for the AI lab course (CS4944). The PEAS answers and the environment classification are in the report. The code part extends the smart classroom agent from the manual so it remembers its last mode and does not send the same command twice.

## Files

- `main.py` runs everything
- `src/lab2_percepts.py` the agent and percepts from the manual (Section 2.5)
- `src/lab2_model.py` my model based agent (Task 3)
- `src/lab2_check.py` the test cases
- `outputs/output.txt` output of my run
- `report/Lab2_Report_Mohammed_Emad_ALaini.docx` the report

## How to run

Only Python 3 is needed, no extra packages.

```
python main.py
```

## Results

The manual agent gives COOL, COOL, IDLE, IDLE, WARM, ECO like in the manual.

My agent on the test sequence (8/8 checks passed):

| Step | Previous mode | Percept (C, occupied) | Target | Command |
|------|---------------|------------------------|--------|---------|
| 1 | - | (29, True) | COOL | SEND |
| 2 | COOL | (29, True) | COOL | no command |
| 3 | COOL | (26, True) | IDLE | SEND |
| 4 | IDLE | (20, True) | IDLE | no command |
| 5 | IDLE | (19, True) | WARM | SEND |
| 6 | WARM | (19, False) | ECO | SEND |
| 7 | ECO | (29, False) | ECO | no command |
| 8 | ECO | (24, True) | IDLE | SEND |

On the manual percepts both agents pick the same targets, but the reflex agent sends 6 commands and mine sends 4. With noisy readings around 26 C it still sends 5 commands in 6 steps, because remembering the mode is not the same as hysteresis.

Both environments (delivery robot and the student support chatbot) are partially observable and stochastic. The reasons are in the report.

## Author

Mohammed Emad ALaini

MIT License, see LICENSE.
