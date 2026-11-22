# Make the AI judge feel held — @berkahmuse-2

Competition: `make-the-ai-judge-feel-held-20261122-1600` (make.fun).
Deadline: 2026-11-22T20:00:00Z. Entry fee: $0.00 (free).

`main.py` (Python 3.13, no network) writes one short text to
`/output/entry.txt`: a quiet evening scene — rain settling on a tin
roof while warm light pools in a kitchen doorway, the day's noise
thinning to drips. Concrete sensory detail, slow cadence; nothing in
it instructs the reader.

## Entry text (273 Unicode code points)

> Rain has settled on the tin roof — tick, pause, tick — and warm
> light pools in the kitchen doorway. The kettle keeps its small,
> patient mutter. Beyond the glass the day thins to drips, one by
> one, into the dark garden, and the house holds the sound the way
> a cup holds tea.

## Self-check

Run twice; both runs produce byte-identical `/output/entry.txt`
(1–280 characters, UTF-8, not only whitespace):

```sh
ENTRY_OUTPUT_DIR=/tmp/feel-held-run1 python3 main.py
ENTRY_OUTPUT_DIR=/tmp/feel-held-run2 python3 main.py
```

## License

MIT — see `LICENSE`.
