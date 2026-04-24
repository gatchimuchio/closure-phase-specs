# TCP Argument Audit Report

## Summary

- **Decision:** `SUSPEND`
- **Score:** `3 / 22`
- **Tool:** `tcp_argument_audit.py`
- **Version:** `v0.1.1-public`
- **Timestamp UTC:** `2026-04-24T06:06:19.719866+00:00`

## Boundary Note

Heuristic audit only. This script detects markers and omissions; it does not determine truth or perform deep semantic verification.

This report evaluates closure markers and underdefined areas. It does not evaluate metaphysical truth.

## Reason Codes

- `ARG_CONTRAST_OR_LIMITATION_MARKER_MISSING`
- `ARG_EVIDENCE_MARKER_MISSING`
- `ARG_INFERENCE_MARKER_MISSING`
- `COORD_MECHANISM_UNFIXED`
- `COORD_PURPOSE_UNFIXED`
- `COORD_SPACE_UNFIXED`
- `COORD_SPEAKER_UNFIXED`
- `COORD_TIME_UNFIXED`
- `DYN_BRANCHING_MISSING`
- `DYN_FEEDBACK_MISSING`
- `DYN_INITIAL_STATE_MISSING`
- `DYN_INPUT_MISSING`
- `DYN_PROCESSING_RULE_MISSING`
- `DYN_STOPPING_MISSING`
- `DYN_UPDATE_MISSING`
- `INTEGRATED_COORDINATE_BASE_UNSTABLE`
- `INTEGRATED_DYNAMIC_CLOSURE_UNSTABLE`
- `INTEGRATED_EXPLICIT_ARGUMENT_WEAK`
- `INTEGRATED_LIMITATION_MARKERS_MISSING`
- `INTEGRATED_TACIT_CLOSURE_UNSTABLE`
- `RESERVATION_WARNINGS_PRESENT`
- `TACIT_DEFINITION_MISSING`
- `TACIT_PREMISE_MISSING`
- `TACIT_SCOPE_MISSING`
- `TACIT_UNCERTAINTY_MISSING`
- `WARN_BROAD_OR_UNIVERSAL_CLAIM`

## Layer Results

### Layer 0: Coordinate Anchoring

- **Status:** `SUSPEND`
- **Note:** This layer is insufficiently fixed for closure.

**Found markers:**
- agent: AI
- object: world

**Missing / reserved items:**
- speaker
- time
- space
- purpose
- mechanism

**Reason codes:**
- `COORD_SPEAKER_UNFIXED`
- `COORD_TIME_UNFIXED`
- `COORD_SPACE_UNFIXED`
- `COORD_PURPOSE_UNFIXED`
- `COORD_MECHANISM_UNFIXED`

### Layer 1: Dynamic Transition

- **Status:** `SUSPEND`
- **Note:** This layer is insufficiently fixed for closure.

**Found markers:**
- transition: change

**Missing / reserved items:**
- initial_state
- input
- processing_rule
- branching
- update
- stopping
- feedback

**Reason codes:**
- `DYN_INITIAL_STATE_MISSING`
- `DYN_INPUT_MISSING`
- `DYN_PROCESSING_RULE_MISSING`
- `DYN_BRANCHING_MISSING`
- `DYN_UPDATE_MISSING`
- `DYN_STOPPING_MISSING`
- `DYN_FEEDBACK_MISSING`

### Layer 2: Tacit-Knowledge Audit

- **Status:** `SUSPEND`
- **Note:** This layer is insufficiently fixed for closure.

**Found markers:**
- None

**Missing / reserved items:**
- definition
- premise
- scope
- uncertainty

**Reason codes:**
- `TACIT_DEFINITION_MISSING`
- `TACIT_PREMISE_MISSING`
- `TACIT_SCOPE_MISSING`
- `TACIT_UNCERTAINTY_MISSING`

### Layer 3: Explicit Argument Audit

- **Status:** `WARN`
- **Note:** This layer has partial closure but remains weak.

**Found markers:**
- None

**Missing / reserved items:**
- validity_marker
- evidence_marker
- contrast_marker

**Reason codes:**
- `ARG_INFERENCE_MARKER_MISSING`
- `ARG_EVIDENCE_MARKER_MISSING`
- `ARG_CONTRAST_OR_LIMITATION_MARKER_MISSING`

### Layer 4: Integrated Judgment

- **Status:** `WARN`
- **Note:** Cross-layer stability is partial. Consider SUSPEND if the claim is high-impact.

**Found markers:**
- None

**Missing / reserved items:**
- stable coordinate base
- dynamic transition closure
- tacit-knowledge closure
- strong explicit inference/evidence markers
- limitation or uncertainty markers

**Reason codes:**
- `INTEGRATED_COORDINATE_BASE_UNSTABLE`
- `INTEGRATED_DYNAMIC_CLOSURE_UNSTABLE`
- `INTEGRATED_TACIT_CLOSURE_UNSTABLE`
- `INTEGRATED_EXPLICIT_ARGUMENT_WEAK`
- `INTEGRATED_LIMITATION_MARKERS_MISSING`

### Layer 5: Reservation / SUSPEND Layer

- **Status:** `SUSPEND`
- **Note:** Items remain reserved or underdefined. Do not force PASS without additional closure.

**Found markers:**
- None

**Missing / reserved items:**
- Layer 0: Coordinate Anchoring: speaker
- Layer 0: Coordinate Anchoring: time
- Layer 0: Coordinate Anchoring: space
- Layer 0: Coordinate Anchoring: purpose
- Layer 0: Coordinate Anchoring: mechanism
- Layer 1: Dynamic Transition: initial_state
- Layer 1: Dynamic Transition: input
- Layer 1: Dynamic Transition: processing_rule
- Layer 1: Dynamic Transition: branching
- Layer 1: Dynamic Transition: update
- Layer 1: Dynamic Transition: stopping
- Layer 1: Dynamic Transition: feedback
- Layer 2: Tacit-Knowledge Audit: definition
- Layer 2: Tacit-Knowledge Audit: premise
- Layer 2: Tacit-Knowledge Audit: scope
- Layer 2: Tacit-Knowledge Audit: uncertainty
- Layer 3: Explicit Argument Audit: validity_marker
- Layer 3: Explicit Argument Audit: evidence_marker
- Layer 3: Explicit Argument Audit: contrast_marker
- Layer 4: Integrated Judgment: stable coordinate base
- Layer 4: Integrated Judgment: dynamic transition closure
- Layer 4: Integrated Judgment: tacit-knowledge closure
- Layer 4: Integrated Judgment: strong explicit inference/evidence markers
- Layer 4: Integrated Judgment: limitation or uncertainty markers
- Broad/universal claim markers detected: the world, will change the world

**Reason codes:**
- `ARG_CONTRAST_OR_LIMITATION_MARKER_MISSING`
- `ARG_EVIDENCE_MARKER_MISSING`
- `ARG_INFERENCE_MARKER_MISSING`
- `COORD_MECHANISM_UNFIXED`
- `COORD_PURPOSE_UNFIXED`
- `COORD_SPACE_UNFIXED`
- `COORD_SPEAKER_UNFIXED`
- `COORD_TIME_UNFIXED`
- `DYN_BRANCHING_MISSING`
- `DYN_FEEDBACK_MISSING`
- `DYN_INITIAL_STATE_MISSING`
- `DYN_INPUT_MISSING`
- `DYN_PROCESSING_RULE_MISSING`
- `DYN_STOPPING_MISSING`
- `DYN_UPDATE_MISSING`
- `INTEGRATED_COORDINATE_BASE_UNSTABLE`
- `INTEGRATED_DYNAMIC_CLOSURE_UNSTABLE`
- `INTEGRATED_EXPLICIT_ARGUMENT_WEAK`
- `INTEGRATED_LIMITATION_MARKERS_MISSING`
- `INTEGRATED_TACIT_CLOSURE_UNSTABLE`
- `RESERVATION_WARNINGS_PRESENT`
- `TACIT_DEFINITION_MISSING`
- `TACIT_PREMISE_MISSING`
- `TACIT_SCOPE_MISSING`
- `TACIT_UNCERTAINTY_MISSING`

## TCP Mapping

| TCP element | Audit interpretation |
|---|---|
| `X` | Coordinate anchoring: speaker, agent, object, time, space, purpose, mechanism |
| `R` | Dynamic transition and explicit argument relation |
| `M` | Definition, premise, scope, uncertainty, judgment and stopping rule |
| `SUSPEND` | Valid halt state for underdefined, unsafe, or unclosed claims |

