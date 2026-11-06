# No Man's Sky Base Reports

A Python tool that turns an exported No Man's Sky save JSON into spreadsheet-friendly reports of your bases. Use it to count bases by galaxy, find base and teleporter coordinates, review saved timestamps, count parts, and copy portal addresses to share with other players.

The script uses the player-facing persistent base list as its source, with teleporter records supplying extra information when matched. It filters bases by the configured owner's UID and username, excluding foreign, missing, or conflicting ownership. It reports planetary, orbital, space station, ship, and freighter base types without changing your save or input JSON.

## Reports
The master CSV report includes **Biome Type** after **Base Type**. It comes from planet discovery records matched to the complete saved address, including the galaxy. Multiple distinct saved types are joined with ` or ` (for example, `Blue or Swamp`). Missing or unrecognized types are `Unknown`; nonplanetary bases are `Not applicable`. These are saved classifications and may reflect earlier game versions. Pet and egg data are not used.


The master CSV includes a **Base Parts** count for each base. The summary includes the total number of reported bases and the combined **Total base parts**. Part counts come from each base's saved `Objects` entries, including the base computer when present; they may differ from the game's construction-limit accounting.

**Requirements:** Python 3 and a full save JSON export with readable field names. No additional Python packages are required.

Place `save.hg.json` beside `extract_nms_bases.py` and `Generate Reports.bat`, then double-click the BAT file. It uses the `python` command and writes a master CSV and a Markdown summary to `nms_base_reports`.

To run the script directly, use `python extract_nms_bases.py <path-to-exported-save.json>`. Add `-o <folder>` to choose a different output folder.

The script is configured for the player identity associated with this release. To use it for another player, update the configured owner UID and username in `extract_nms_bases.py`.

See the [User Guide](NMS_Base_Reports_User_Guide.md) for setup, report explanations, and troubleshooting.

## Report layout and inferred galaxies

Normal runs generate only `nms_bases_master.csv` and `nms_bases_summary.md`. The grouped CSV is retired. Existing grouped CSV and text-summary snapshots are left untouched; they are no longer refreshed.

In the master CSV, `Glyph String (No Spaces)` and `Glyph Names` immediately follow `Galaxy Number (Human)`, followed by `Galaxy Number (Save)`. `Teleporter Order` immediately follows `Teleporter Coordinates`. All other master fields are retained.

When no galaxy number can be identified from extracted metadata, a base name beginning with `GXXX-` supplies the human galaxy number, provided XXX is exactly three digits from 001 through 256. The save number is the human number minus one, and the galaxy name comes from the script's mapping. Identified galaxies are never overwritten. `Notes` records `Galaxy inferred from base-name prefix`; names without a valid prefix remain unidentified. Inference does not manufacture a teleporter match or change biome classifications.

The Markdown summary includes inferred and unresolved record counts, compact galaxy and base-type tables, the eight largest builds, and data coverage checks. Its Complete Galaxy Table appendix lists all represented galaxies with human galaxy numbers and record counts; Items to Review is the final section. Network themes are descriptive, not counted classifications. Missing extracted objects do not by themselves establish in-game damage.

View the summary in a Markdown viewer. When using Google Docs, import or convert Markdown with heading and table support to retain its formatting.
