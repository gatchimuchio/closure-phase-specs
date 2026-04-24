# TCP Argument Audit Script

A minimal CLI prototype for applying the Three-Term Closure Principle (TCP) to natural-language argument audit.

## Status

This script is an application example, not a core implementation.

It does not prove TCP, Closure Phase Ψ, DDP, or HDS.  
It does not disclose sealed HDS core implementation.  
It does not judge metaphysical truth.

It only checks whether a text contains enough observable markers to be treated as partially closed under a TCP-style audit.

## Usage

```bash
python tcp_argument_audit.py input.txt --format markdown
python tcp_argument_audit.py input.txt --format json
python tcp_argument_audit.py --text "AI will change the world."
cat input.txt | python tcp_argument_audit.py --format markdown
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
- `SUSPEND`: coordinates, dynamics, tacit knowledge, or judgment rules are underdefined.
- `FAIL`: prohibited-use framing or severe misuse pattern was detected.

## TCP Mapping

| TCP element | Script interpretation |
|---|---|
| `X` | speaker, agent, object, time, space, purpose, mechanism |
| `R` | state transition, relation, branch, update, feedback, explicit inference |
| `M` | definition, premise, scope, uncertainty, judgment, stopping |
| `SUSPEND` | valid halt state for underdefined or risky claims |

## Limitations

This is a heuristic marker detector. Version v0.1.1 fixes broad-claim warnings so that slogans such as “AI will change the world” produce SUSPEND rather than FAIL unless prohibited-use framing is detected.

It cannot perform deep semantic verification.  
It cannot replace human audit.  
It cannot determine truth.  
It may miss implicit context or over-detect shallow markers.

## License

Recommended for code:

```text
Apache License 2.0
SPDX-License-Identifier: Apache-2.0
```
