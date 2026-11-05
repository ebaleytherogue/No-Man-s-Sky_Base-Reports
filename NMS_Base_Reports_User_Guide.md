# No Man's Sky Base Reports
## User Guide

**Platform:** Windows  
**Required software:** Python 3 and a save editor capable of exporting the full save as readable JSON  
**Script files:**

- `extract_nms_bases.py`
- `Generate Reports.bat`

## Current version: ownership and part counts

The reports include bases from the player-facing `BaseContext` list only when the record's `Owner` matches the player configured in the script. Foreign, missing, and conflicting ownership records are excluded. The script currently targets the owner configured for this release; change the owner UID and username constants in `extract_nms_bases.py` before using it with a different player.

Both CSV files include **Base Parts** for each reported base. The summary includes **Total base parts** across those bases. A part count is the number of entries in the saved `Objects` array, including the base computer when present. It may differ from the game's construction-limit accounting.

## Biome Type

Both CSV reports include **Biome Type** after **Base Type**. It comes from planet discovery records matched to the complete saved address, including the galaxy. Multiple distinct saved types are joined with ` or ` (for example, `Blue or Swamp`). Missing or unrecognized types are `Unknown`; nonplanetary bases are `Not applicable`. These are saved classifications and may reflect earlier game versions. Pet and egg data are not used.

## Table of Contents

1. [What the Tool Does](#1-what-the-tool-does)
2. [Before You Begin](#2-before-you-begin)
3. [Generating Reports](#3-generating-reports)
4. [Using the Report Files](#4-using-the-report-files)
5. [Understanding the Data](#5-understanding-the-data)
6. [Troubleshooting](#6-troubleshooting)
7. [Recommended Workflow](#7-recommended-workflow)

---

## 1. What the Tool Does

Use this tool when you want a list of your bases outside the game, with enough information to find them again or share their locations.

The script:

- Reads a full save JSON export.
- Uses `BaseContext.PlayerStateData.PersistentPlayerBases` as the source of the base list.
- Supplements those records with matching teleporter information when available.
- Reports base names, types, galaxies, portal addresses, coordinates, and saved timestamps.
- Creates two CSV reports and a text summary, including counts by galaxy and base type.
- Leaves your save and input JSON untouched.

This tool produces reports. Changing a CSV does not change your bases or their order in the game's Terminus list.

---

## 2. Before You Begin

### Check Python

Open PowerShell or Command Prompt and enter:

```powershell
python --version
```

You should see a Python 3 version number. The script uses only Python's standard library, so there are no extra packages to install.

If your installation uses `py` instead of `python`, use the manual command in Section 3. The supplied BAT calls `python`.

### Export your save

Use your save editor to export the **full save as JSON with readable field names**. A raw `.hg` save or an individual `.nmsbase` export is not the input this script expects.

The original manual records testing with Vectorcmdr's and Goatfungus' save editors. It mentions NomNom as a possibility, but does not record testing it.

Use a fresh export of the save slot you actually want to report on. The script does not read the running game or automatically locate your saves.

### Prepare the folder

Place the files together, for example:

```text
C:\apps\NMS Base Reports\
    extract_nms_bases.py
    Generate Reports.bat
    save.hg.json
```

Rename your exported JSON to `save.hg.json` when using the BAT. Make sure File Explorer shows filename extensions so you do not accidentally create `save.hg.json.json`.

The repository also includes `extract_nms_bases_2026-09-18.py`. Use the undated `extract_nms_bases.py` for normal operation; that is the file the BAT launches.

---

## 3. Generating Reports

### Step-by-step instructions

**Step 1 — Save your progress and export the JSON.**

Create a fresh full-save export after the changes you want included in the reports.

**Step 2 — Put the JSON in the script folder.**

For the supplied BAT, its name must be `save.hg.json`.

**Step 3 — Double-click `Generate Reports.bat`.**

Run it from the folder containing the script and JSON. Its paths are relative to the working folder.

**Step 4 — Check the completion messages.**

The script prints the paths of the master CSV, grouped CSV, and summary, followed by row counts. The BAT pauses so you can read the results or any error.

**Step 5 — Open `nms_base_reports`.**

The default output folder contains:

```text
nms_base_reports\
    nms_bases_master.csv
    nms_bases_grouped.csv
    nms_bases_summary.txt
```

**Important:** Running again in the same output folder replaces these reports. Copy reports elsewhere first if you want to keep an older snapshot. The script also removes old `nms_bases_duplicate_names.csv` and `nms_bases_filtered_out.csv` files from the selected output folder; those reports are no longer generated.

### Running manually

In File Explorer, open the script folder, type `powershell` in the address bar, and press Enter.

Run:

```powershell
python .\extract_nms_bases.py .\save.hg.json
```

You can use a different input filename without renaming it:

```powershell
python .\extract_nms_bases.py ".\My Save.json"
```

To choose a different output folder:

```powershell
python .\extract_nms_bases.py .\save.hg.json -o ".\Reports November 2"
```

Substitute `py` for `python` if needed. Use `--help` to display the available command options.

---

## 4. Using the Report Files

| File | Use it for |
|---|---|
| `nms_bases_master.csv` | Detailed base information, addresses, coordinates, timestamps, and diagnostic notes. |
| `nms_bases_grouped.csv` | The same base rows with galaxy and frequently useful fields placed near the front. |
| `nms_bases_summary.txt` | Total rows, counts by galaxy and base type, teleporter matches, and other checks. |

Open the CSV files in Excel or LibreOffice Calc, or upload them to Google Drive and open them with Google Sheets. You can then filter and sort them like any other spreadsheet.

Both CSVs are sorted by galaxy, system coordinates, system index, base name, and planet. The grouped file does not combine several bases into one row.

To examine the original saved base-list sequence, sort **Teleporter Order** numerically from smallest to largest. This is the one-based position in the source array before report sorting and filtering; gaps can occur.

### Sharing a location

Find the base and copy its **Glyph String (No Spaces)** value. That is the 12-character hexadecimal portal address. **Glyph Names** provides the corresponding glyph names in order.

Include the **Galaxy** when sharing an address. For planetary bases, include the available computer or teleporter coordinates to help locate the base after arrival.

---

## 5. Understanding the Data

| Field | Meaning |
|---|---|
| Base Type | Distinguishes planetary, orbital / space, space station, Corvette / ship, and freighter bases. |
| Galaxy Number (Human) | The familiar numbering, starting with Euclid as 1. |
| Galaxy Number (Save) | The save's numbering, starting with Euclid as 0. |
| Computer Coordinates | Calculated latitude and longitude when the expected base-computer object is available. |
| Teleporter Coordinates | Calculated coordinates from a matched teleporter record. |
| Persistent Base Name / Teleporter Base Name | The names in the two sources, useful when they disagree. |
| Notes | Flags such as repeated names, missing teleporter matches, or differing names. |

### Dates and times

The reports include the persistent last-update timestamp, earliest and latest object timestamps, and base-computer timestamp when available. Human-readable values use the local time zone of the computer generating the report. Raw timestamp columns preserve the numerical values.

These are saved timestamps, not guaranteed dates of original base creation. Missing values remain blank.

### Space bases and Planet 0

A Planet value of 0 can be legitimate for orbital, station, ship, or freighter records. Do not treat it alone as proof that a base is broken. The script applies the Planet-0 warning and missing-computer diagnostic specifically to planetary bases.

Portal and latitude/longitude fields for space or mobile bases need context; do not use them as though they described an ordinary planetary destination.

### Counts and missing information

The script removes exact duplicate report rows and filters placeholder-like records only when suspicious address data is accompanied by no meaningful base information. Records with undecodable addresses are skipped. It reads the player-facing BaseContext list rather than merging in the ExpeditionContext base list.

Blank coordinates or a missing teleporter match do not automatically mean a base is missing. Review the base type and Notes before drawing conclusions.

---

## 6. Troubleshooting

### Python is not found, or the Microsoft Store opens

Check that Python 3 is installed and available through the command you are using. Try `py --version`. If that works, run the script manually with `py`, or change the BAT's initial `python` command to `py`.

### The script cannot find the JSON or Python file

Check that all three working files are together and that the JSON is named exactly `save.hg.json`. Open PowerShell in that folder and run the manual command to avoid working-folder problems.

### A JSON parsing error appears

Export the full save again. The script attempts to repair certain invalid backslashes in memory, but it cannot repair every malformed export. Look for the three completion messages before assuming the reports finished successfully.

### The report is empty or has fewer bases than expected

Confirm the save slot and export format. The script expects readable keys under `BaseContext.PlayerStateData.PersistentPlayerBases`; it does not fall back to the ExpeditionContext list. Check the summary's filtered-row count as well.

### A base name looks old

First save and export again. Your original manual records a case where uploading a renamed base and generating a fresh export resolved a stale name. Compare the persistent and teleporter name columns; older versions relied more heavily on teleporter names than this script does.

### Some coordinates or dates are blank

Those fields depend on information present in the export. A space base may not contain the traditional planetary base-computer object. A missing value is not a reason to delete or rebuild the base.

---

## 7. Recommended Workflow

1. Save your progress in the correct game slot.
2. Export a fresh full-save JSON.
3. Place it beside the script as `save.hg.json`.
4. Preserve any earlier reports you want to keep.
5. Run `Generate Reports.bat` and check the completion messages.
6. Read the summary, then open a CSV to filter or sort your bases.
7. Share the galaxy and portal address together when giving someone a base location.

**End of User Guide**
