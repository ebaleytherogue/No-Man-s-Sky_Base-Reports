# No-Man-s-Sky_Base-Reports

This Python script analyzes a No Man’s Sky save exported as JSON and generates reports for the player’s bases, including portal locations that make it easy to share a base with other players.

## Reports

Run `Generate Reports.bat` from the repository folder, or run the script directly:

```text
python extract_nms_bases.py <path-to-exported-save.json>
```

The reports are written to the `nms_base_reports` folder by default. To choose another output folder, add `-o <folder>`.

- `nms_bases_master.csv` contains the detailed base list, including a **Base Parts** count for every base.
- `nms_bases_grouped.csv` contains the grouped, easy-to-scan base list and the same **Base Parts** count.
- `nms_bases_summary.txt` reports the number of bases and the combined **Total base parts**, along with the existing counts by base type and galaxy and other summary details.

Part counts are the number of object entries stored in each base’s `Objects` array. This count includes the base computer when it is present; it describes objects recorded in the save and may differ from the game’s construction-limit accounting.

## Ownership filtering

The report uses the player-facing `BaseContext` persistent-base list. It includes a base only when the base record’s `Owner` identifies the configured player by UID or username. If both identifiers are present, both must agree. Bases with foreign, missing, or conflicting ownership information are excluded, so recently visited bases belonging to other players do not inflate the reports or part totals.

The script is configured for the save owner used for this release. To use it for another player, update the configured owner UID and username in `extract_nms_bases.py` to match that player’s save.
