# No Man's Sky Base Reports

A Python tool that turns an exported No Man's Sky save JSON into spreadsheet-friendly reports of your bases. Use it to count bases by galaxy, find base and teleporter coordinates, review saved timestamps, count parts, and copy portal addresses to share with other players.

The script uses the player-facing persistent base list as its source, with teleporter records supplying extra information when matched. It filters bases by the configured owner's UID and username, excluding foreign, missing, or conflicting ownership. It reports planetary, orbital, space station, ship, and freighter base types without changing your save or input JSON.

## Reports
Both CSV reports include **Biome Type** after **Base Type**. It comes from planet discovery records matched to the complete saved address, including the galaxy. Multiple distinct saved types are joined with ` or ` (for example, `Blue or Swamp`). Missing or unrecognized types are `Unknown`; nonplanetary bases are `Not applicable`. These are saved classifications and may reflect earlier game versions. Pet and egg data are not used.


The master and grouped CSV files include a **Base Parts** count for each base. The summary includes the total number of reported bases and the combined **Total base parts**. Part counts come from each base's saved `Objects` entries, including the base computer when present; they may differ from the game's construction-limit accounting.

**Requirements:** Python 3 and a full save JSON export with readable field names. No additional Python packages are required.

Place `save.hg.json` beside `extract_nms_bases.py` and `Generate Reports.bat`, then double-click the BAT file. It uses the `python` command and writes two CSV files and a text summary to `nms_base_reports`.

To run the script directly, use `python extract_nms_bases.py <path-to-exported-save.json>`. Add `-o <folder>` to choose a different output folder.

The script is configured for the player identity associated with this release. To use it for another player, update the configured owner UID and username in `extract_nms_bases.py`.

See the [User Guide](NMS_Base_Reports_User_Guide.md) for setup, report explanations, and troubleshooting.
