# TCP Argument Audit Script

A minimal CLI prototype for applying the Trinity Principle (TCP: Three-Term Closure Principle) to natural-language argument audit.

## Status

This script is an application example, not a core implementation.

It does not prove TCP, Closure Phase Ψ, 神の領域原理, or HDS.  
It does not disclose sealed HDS core implementation.  
It does not judge metaphysical truth.

It only checks whether a text contains enough observable markers to be treated as partially closed under a TCP-style audit and whether the claim approaches a 神の領域原理 boundary.

## Usage

Run from this directory:

```bash
python tcp_argument_audit.py input.txt --format markdown
python tcp_argument_audit.py input.txt --format json
python tcp_argument_audit.py --text "AI will change the world."
cat input.txt | python tcp_argument_audit.py --format markdown
```

Run from the repository root:

```bash
python tcp_argument_audit_script_v0_1_1/tcp_argument_audit.py --text "AI will change the world."
```

## Output

The script returns:

```text
PASS
SUSPEND
FAIL
```

Meaning:

- `PASS`: minimum closure markers are present under this heuristic script.
- `SUSPEND`: coordinates, dynamics, closure rules, evidence, uncertainty, or 神域 boundary conditions are underdefined.
- `FAIL`: prohibited-use framing or severe misuse pattern was detected.

## TCP Mapping

| TCP element | Script interpretation |
|---|---|
| `X` | speaker, agent, object, time, place/domain, purpose, mechanism |
| `R` | relation, transition, comparison, update, branch, feedback, evidence |
| `M` | definition, premise, scope, judgment, uncertainty, stopping, boundary |
| `SUSPEND` | valid halt state for underdefined, unsafe, or unclosed claims |
| `神の領域原理` | boundary check against projecting cognition-after models into the pre-cognitive world-itself |

## Limitations

This is a heuristic marker detector. It is not a semantic verifier, theorem prover, LLM judge, peer review substitute, or truth checker.

Broad claims such as “AI will change the world” should normally produce `SUSPEND`, not `FAIL`, unless prohibited-use framing is detected.

## License

Recommended for code:

```text
Apache License 2.0
SPDX-License-Identifier: Apache-2.0
```
