
import json
import csv
import argparse
import math
from datetime import datetime
from collections import Counter, defaultdict
from pathlib import Path


GALAXY_NAME_BY_HUMAN_NUMBER = {
    1: "Euclid",
    2: "Hilbert Dimension",
    3: "Calypso",
    4: "Hesperius Dimension",
    5: "Hyades",
    6: "Ickjamatew",
    7: "Budullangr",
    8: "Kikolgallr",
    9: "Eltiensleen",
    10: "Eissentam",
    11: "Elkupalos",
    12: "Aptarkaba",
    13: "Ontiniangp",
    14: "Odiwagiri",
    15: "Ogtialabi",
    16: "Muhacksonto",
    17: "Hitonskyer",
    18: "Rerasmutul",
    19: "Isdoraijung",
    20: "Doctinawyra",
    21: "Loychazinq",
    22: "Zukasizawa",
    23: "Ekwathore",
    24: "Yeberhahne",
    25: "Twerbetek",
    26: "Sivarates",
    27: "Eajerandal",
    28: "Aldukesci",
    29: "Wotyarogii",
    30: "Sudzerbal",
    31: "Maupenzhay",
    32: "Sugueziume",
    33: "Brogoweldian",
    34: "Ehbogdenbu",
    35: "Ijsenufryos",
    36: "Nipikulha",
    37: "Autsurabin",
    38: "Lusontrygiamh",
    39: "Rewmanawa",
    40: "Ethiophodhe",
    41: "Urastrykle",
    42: "Xobeurindj",
    43: "Oniijialdu",
    44: "Wucetosucc",
    45: "Ebyeloof",
    46: "Odyavanta",
    47: "Milekistri",
    48: "Waferganh",
    49: "Agnusopwit",
    50: "Teyaypilny",
    51: "Zalienkosm",
    52: "Ladgudiraf",
    53: "Mushonponte",
    54: "Amsentisz",
    55: "Fladiselm",
    56: "Laanawemb",
    57: "Ilkerloor",
    58: "Davanossi",
    59: "Ploehrliou",
    60: "Corpinyaya",
    61: "Leckandmeram",
    62: "Quulngais",
    63: "Nokokipsechl",
    64: "Rinblodesa",
    65: "Loydporpen",
    66: "Ibtrevskip",
    67: "Elkowaldb",
    68: "Heholhofsko",
    69: "Yebrilowisod",
    70: "Husalvangewi",
    71: "Ovna'uesed",
    72: "Bahibusey",
    73: "Nuybeliaure",
    74: "Doshawchuc",
    75: "Ruckinarkh",
    76: "Thorettac",
    77: "Nuponoparau",
    78: "Moglaschil",
    79: "Uiweupose",
    80: "Nasmilete",
    81: "Ekdaluskin",
    82: "Hakapanasy",
    83: "Dimonimba",
    84: "Cajaccari",
    85: "Olonerovo",
    86: "Umlanswick",
    87: "Henayliszm",
    88: "Utzenmate",
    89: "Umirpaiya",
    90: "Paholiang",
    91: "Iaereznika",
    92: "Yudukagath",
    93: "Boealalosnj",
    94: "Yaevarcko",
    95: "Coellosipp",
    96: "Wayndohalou",
    97: "Smoduraykl",
    98: "Apmaneessu",
    99: "Hicanpaav",
    100: "Akvasanta",
    101: "Tuychelisaor",
    102: "Rivskimbe",
    103: "Daksanquix",
    104: "Kissonlin",
    105: "Aediabiel",
    106: "Ulosaginyik",
    107: "Roclaytonycar",
    108: "Kichiaroa",
    109: "Irceauffey",
    110: "Nudquathsenfe",
    111: "Getaizakaal",
    112: "Hansolmien",
    113: "Bloytisagra",
    114: "Ladsenlay",
    115: "Luyugoslasr",
    116: "Ubredhatk",
    117: "Cidoniana",
    118: "Jasinessa",
    119: "Torweierf",
    120: "Saffneckm",
    121: "Thnistner",
    122: "Dotusingg",
    123: "Luleukous",
    124: "Jelmandan",
    125: "Otimanaso",
    126: "Enjaxusanto",
    127: "Sezviktorew",
    128: "Zikehpm",
    129: "Bephembah",
    130: "Broomerrai",
    131: "Meximicka",
    132: "Venessika",
    133: "Gaiteseling",
    134: "Zosakasiro",
    135: "Drajayanes",
    136: "Ooibekuar",
    137: "Urckiansi",
    138: "Dozivadido",
    139: "Emiekereks",
    140: "Meykinunukur",
    141: "Kimycuristh",
    142: "Roansfien",
    143: "Isgarmeso",
    144: "Daitibeli",
    145: "Gucuttarik",
    146: "Enlaythie",
    147: "Drewweste",
    148: "Akbulkabi",
    149: "Homskiw",
    150: "Zavainlani",
    151: "Jewijkmas",
    152: "Itlhotagra",
    153: "Podalicess",
    154: "Hiviusauer",
    155: "Halsebenk",
    156: "Puikitoac",
    157: "Gaybakuaria",
    158: "Grbodubhe",
    159: "Rycempler",
    160: "Indjalala",
    161: "Fontenikk",
    162: "Pasycihelwhee",
    163: "Ikbaksmit",
    164: "Telicianses",
    165: "Oyleyzhan",
    166: "Uagerosat",
    167: "Impoxectin",
    168: "Twoodmand",
    169: "Hilfsesorbs",
    170: "Ezdaranit",
    171: "Wiensanshe",
    172: "Ewheelonc",
    173: "Litzmantufa",
    174: "Emarmatosi",
    175: "Mufimbomacvi",
    176: "Wongquarum",
    177: "Hapirajua",
    178: "Igbinduina",
    179: "Wepaitvas",
    180: "Sthatigudi",
    181: "Yekathsebehn",
    182: "Ebedeagurst",
    183: "Nolisonia",
    184: "Ulexovitab",
    185: "Iodhinxois",
    186: "Irroswitzs",
    187: "Bifredait",
    188: "Beiraghedwe",
    189: "Yeonatlak",
    190: "Cugnatachh",
    191: "Nozoryenki",
    192: "Ebralduri",
    193: "Evcickcandj",
    194: "Ziybosswin",
    195: "Heperclait",
    196: "Sugiuniam",
    197: "Aaseertush",
    198: "Uglyestemaa",
    199: "Horeroedsh",
    200: "Drundemiso",
    201: "Ityanianat",
    202: "Purneyrine",
    203: "Dokiessmat",
    204: "Nupiacheh",
    205: "Dihewsonj",
    206: "Rudrailhik",
    207: "Tweretnort",
    208: "Snatreetze",
    209: "Iwundaracos",
    210: "Digarlewena",
    211: "Erquagsta",
    212: "Logovoloin",
    213: "Boyaghosganh",
    214: "Kuolungau",
    215: "Pehneldept",
    216: "Yevettiiqidcon",
    217: "Sahliacabru",
    218: "Noggalterpor",
    219: "Chmageaki",
    220: "Veticueca",
    221: "Vittesbursul",
    222: "Nootanore",
    223: "Innebdjerah",
    224: "Kisvarcini",
    225: "Cuzcogipper",
    226: "Pamanhermonsu",
    227: "Brotoghek",
    228: "Mibittara",
    229: "Huruahili",
    230: "Raldwicarn",
    231: "Ezdartlic",
    232: "Badesclema",
    233: "Isenkeyan",
    234: "Iadoitesu",
    235: "Yagrovoisi",
    236: "Ewcomechio",
    237: "Inunnunnoda",
    238: "Dischiutun",
    239: "Yuwarugha",
    240: "Ialmendra",
    241: "Reponudrle",
    242: "Rinjanagrbo",
    243: "Zeziceloh",
    244: "Oeileutasc",
    245: "Zicniijinis",
    246: "Dugnowarilda",
    247: "Neuxoisan",
    248: "Ilmenhorn",
    249: "Rukwatsuku",
    250: "Nepitzaspru",
    251: "Chcehoemig",
    252: "Haffneyrin",
    253: "Uliciawai",
    254: "Tuhgrespod",
    255: "Iousongola",
    256: "Odyalutai",
}

GALAXY_NAME_BY_SAVE_INDEX = {
    human_num - 1: name
    for human_num, name in GALAXY_NAME_BY_HUMAN_NUMBER.items()
}

GLYPH_NAME_BY_HEX = {
    "0": "Sunrise",
    "1": "Bird",
    "2": "Face",
    "3": "Diplo",
    "4": "Eclipse",
    "5": "Balloon",
    "6": "Boat",
    "7": "Bug",
    "8": "Dragonfly",
    "9": "Galaxy",
    "A": "Octagon",
    "B": "Fish",
    "C": "Tent",
    "D": "Rocket",
    "E": "Tree",
    "F": "Atlas",
}


# --- Helpers ---




def format_timestamp_local(ts):
    if ts in (None, ""):
        return ""
    try:
        ts = int(ts)
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return ""



def galaxy_name_from_save_index(save_index):
    if isinstance(save_index, int):
        return GALAXY_NAME_BY_SAVE_INDEX.get(save_index, "")
    return ""


def human_number_from_save_index(save_index):
    if isinstance(save_index, int):
        return save_index + 1
    return ""


def load_json_with_backslash_fix(path: Path):
    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        print("Standard JSON parse failed.")
        print(f"Reason: {e}")
        print("Attempting automatic repair of invalid backslashes inside strings...")

    repaired_chars = []
    in_string = False
    escape = False
    i = 0

    while i < len(raw):
        ch = raw[i]
        if in_string:
            if escape:
                if ch in '"\\/bfnrt':
                    repaired_chars.append("\\")
                    repaired_chars.append(ch)
                elif ch == "u":
                    hex_part = raw[i + 1:i + 5]
                    if len(hex_part) == 4 and all(c in "0123456789abcdefABCDEF" for c in hex_part):
                        repaired_chars.append("\\")
                        repaired_chars.append("u")
                    else:
                        repaired_chars.append("\\\\")
                        repaired_chars.append("u")
                else:
                    repaired_chars.append("\\\\")
                    repaired_chars.append(ch)
                escape = False
            else:
                if ch == "\\":
                    escape = True
                elif ch == '"':
                    in_string = False
                    repaired_chars.append(ch)
                else:
                    repaired_chars.append(ch)
        else:
            repaired_chars.append(ch)
            if ch == '"':
                in_string = True
        i += 1

    if escape:
        repaired_chars.append("\\\\")
    return json.loads("".join(repaired_chars))


def walk(node):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from walk(value)
    elif isinstance(node, list):
        for item in node:
            yield from walk(item)


# --- Helpers ---

def format_timestamp_local(ts):
    if ts in (None, ""):
        return ""
    try:
        ts = int(ts)
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return ""


def normalize_name(value):
    return " ".join(str(value or "").strip().lower().split())


def build_portal_fields(planet_index, system_index, voxel_x, voxel_y, voxel_z):
    if any(v is None for v in [planet_index, system_index, voxel_x, voxel_y, voxel_z]):
        return {
            "Portal Hex (Grouped)": "",
            "Glyph String (No Spaces)": "",
            "Glyph Digits": "",
            "Glyph Names": "",
        }

    p = f"{planet_index & 0xF:X}"
    sss = f"{system_index & 0xFFF:03X}"
    yy = f"{voxel_y & 0xFF:02X}"
    zzz = f"{voxel_z & 0xFFF:03X}"
    xxx = f"{voxel_x & 0xFFF:03X}"

    compact = f"{p}{sss}{yy}{zzz}{xxx}"
    grouped = f"{p} {sss} {yy} {zzz} {xxx}"
    glyph_digits = " ".join(compact)
    glyph_names = " | ".join(GLYPH_NAME_BY_HEX[d] for d in compact)

    return {
        "Portal Hex (Grouped)": grouped,
        "Glyph String (No Spaces)": compact,
        "Glyph Digits": glyph_digits,
        "Glyph Names": glyph_names,
    }


def decode_packed_galactic_address(value):
    if value is None:
        return None

    if isinstance(value, str):
        text = value.strip()
        if text.lower().startswith("0x"):
            value = int(text, 16)
        else:
            value = int(text, 16) if all(c in "0123456789abcdefABCDEF" for c in text) else int(text)

    return {
        "VoxelX": (value >> 0) & 0xFFF,
        "VoxelZ": (value >> 12) & 0xFFF,
        "VoxelY": (value >> 24) & 0xFF,
        "Unknown": (value >> 32) & 0xFF,
        "SolarSystemIndex": (value >> 40) & 0xFFF,
        "PlanetIndex": (value >> 52) & 0xF,
    }


def signed_from_bits(value, bits):
    sign_bit = 1 << (bits - 1)
    return value - (1 << bits) if value & sign_bit else value


def decode_packed_galactic_address_signed(value):
    decoded = decode_packed_galactic_address(value)
    if not decoded:
        return None

    return {
        "VoxelX": signed_from_bits(decoded["VoxelX"], 12),
        "VoxelY": signed_from_bits(decoded["VoxelY"], 8),
        "VoxelZ": signed_from_bits(decoded["VoxelZ"], 12),
        "SolarSystemIndex": decoded["SolarSystemIndex"],
        "PlanetIndex": decoded["PlanetIndex"],
        "Unknown": decoded["Unknown"],
    }


def add_vectors(a, b):
    return [a[i] + b[i] for i in range(3)]


def format_planetary_coordinates_from_world_position(pos):
    if not isinstance(pos, list) or len(pos) != 3:
        return ""

    x, y, z = pos
    radius = math.sqrt((x * x) + (y * y) + (z * z))
    if radius == 0:
        return ""

    latitude = math.degrees(math.asin(y / radius))
    longitude = math.degrees(math.atan2(x, z))

    if longitude > 180:
        longitude -= 360
    elif longitude <= -180:
        longitude += 360

    return f"{latitude:+.2f}, {longitude:+.2f}"


def parse_coordinate_string(coord_text):
    if not coord_text or "," not in str(coord_text):
        return None
    try:
        lat_text, lon_text = [p.strip() for p in str(coord_text).split(",", 1)]
        return (float(lat_text), float(lon_text))
    except Exception:
        return None


def angular_distance(coord_a, coord_b):
    if coord_a is None or coord_b is None:
        return None
    lat_diff = coord_a[0] - coord_b[0]
    lon_diff = coord_a[1] - coord_b[1]
    return math.sqrt((lat_diff * lat_diff) + (lon_diff * lon_diff))


def iter_persistent_player_bases(data):
    for context_key in ("BaseContext", "ExpeditionContext"):
        context = data.get(context_key, {}) or {}
        player_state = context.get("PlayerStateData", {}) or {}
        for base in player_state.get("PersistentPlayerBases", []) or []:
            if isinstance(base, dict):
                yield context_key, base


def infer_primary_owner_uid(data):
    counts = Counter()
    for _, base in iter_persistent_player_bases(data):
        owner = base.get("Owner", {}) or {}
        uid = str(owner.get("UID", "")).strip()
        if uid:
            counts[uid] += 1
    if not counts:
        return ""
    return counts.most_common(1)[0][0]


def infer_primary_owner_username(data):
    counts = Counter()
    primary_uid = infer_primary_owner_uid(data)
    for _, base in iter_persistent_player_bases(data):
        owner = base.get("Owner", {}) or {}
        if str(owner.get("UID", "")).strip() != primary_uid:
            continue
        username = str(owner.get("USN", "")).strip()
        if username:
            counts[username] += 1
    if counts:
        return counts.most_common(1)[0][0]
    return ""


def iter_authoritative_persistent_bases(data):
    """
    Yield the player-facing / teleporter-facing bases.

    Field testing in May 2026 showed that the visible Terminus > My Bases
    list follows the FIRST PersistentPlayerBases section, which is located at:

        BaseContext.PlayerStateData.PersistentPlayerBases

    The SECOND section, found under ExpeditionContext in this export shape,
    appears to contain persistence/sync/internal records and does not control
    visible teleporter ordering.

    Yield format:
        (context_key, teleporter_order, base_dict)

    teleporter_order is 1-based and reflects the raw array position in the
    player-facing list before any report sorting is applied.
    """
    context_key = "BaseContext"
    context = data.get(context_key, {}) or {}
    player_state = context.get("PlayerStateData", {}) or {}
    bases = player_state.get("PersistentPlayerBases", []) or []

    for index, base in enumerate(bases, start=1):
        if isinstance(base, dict):
            yield context_key, index, base

def extract_base_object_positions(base):
    base_world_pos = base.get("Position")
    objects = base.get("Objects", []) or []

    computer_world_pos = None
    first_object_world_pos = None
    object_count = 0

    object_timestamps = []
    base_computer_timestamp_raw = None

    for obj in objects:
        if not isinstance(obj, dict):
            continue

        object_count += 1

        ts = obj.get("Timestamp")
        try:
            if ts not in (None, ""):
                object_timestamps.append(int(ts))
        except Exception:
            pass

        local_pos = obj.get("Position")
        world_pos = None
        if isinstance(base_world_pos, list) and len(base_world_pos) == 3 and isinstance(local_pos, list) and len(local_pos) == 3:
            world_pos = add_vectors(base_world_pos, local_pos)

        if first_object_world_pos is None and world_pos is not None:
            first_object_world_pos = world_pos

        if obj.get("ObjectID") == "^BUILDSAVE":
            if world_pos is not None:
                computer_world_pos = world_pos
            if base_computer_timestamp_raw is None and ts not in (None, ""):
                base_computer_timestamp_raw = ts

    earliest_object_timestamp_raw = min(object_timestamps) if object_timestamps else ""
    latest_object_timestamp_raw = max(object_timestamps) if object_timestamps else ""

    return {
        "base_world_pos": base_world_pos if isinstance(base_world_pos, list) and len(base_world_pos) == 3 else None,
        "computer_world_pos": computer_world_pos,
        "first_object_world_pos": first_object_world_pos,
        "object_count": object_count,
        "has_base_computer": computer_world_pos is not None,
        "earliest_object_timestamp_raw": earliest_object_timestamp_raw,
        "latest_object_timestamp_raw": latest_object_timestamp_raw,
        "base_computer_timestamp_raw": base_computer_timestamp_raw or "",
        "object_timestamp_count": len(object_timestamps),
    }


BASE_TYPE_LABELS = {
    "HomePlanetBase": "Planetary Base",
    "PlayerSpaceBase": "Orbital / Space Base",
    "PlayerSpaceStationBase": "Space Station",
    "PlayerShipBase": "Corvette / Ship Base",
    "FreighterBase": "Freighter Base",
}


def extract_raw_base_type(base):
    """Return the PersistentBaseTypes enum value from old or new save shapes."""
    base_type = base.get("BaseType", "")
    if isinstance(base_type, dict):
        return str(base_type.get("PersistentBaseTypes", "")).strip()
    return str(base_type).strip()


def friendly_base_type(raw_base_type):
    return BASE_TYPE_LABELS.get(raw_base_type, raw_base_type or "Unknown")

def build_teleporter_lookup(data):
    lookup = defaultdict(list)

    for node in walk(data):
        if not isinstance(node, dict):
            continue
        if node.get("TeleporterType") != "Base":
            continue

        ua = node.get("UniverseAddress", {}) or {}
        ga = ua.get("GalacticAddress", {}) or {}

        key = (
            ga.get("VoxelX"),
            ga.get("VoxelY"),
            ga.get("VoxelZ"),
            ga.get("SolarSystemIndex"),
            ga.get("PlanetIndex"),
        )

        lookup[key].append({
            "reality_index": ua.get("RealityIndex"),
            "teleporter_name": str(node.get("Name", "")).strip(),
            "teleporter_coordinates": format_planetary_coordinates_from_world_position(node.get("Position")),
            "is_favourite": bool(node.get("IsFavourite", False)),
            "is_featured": bool(node.get("IsFeatured", False)),
        })

    return lookup


def choose_best_teleporter_candidate(persistent_name, reference_coordinates, candidates, require_name_match=False):
    if not candidates:
        return None

    target_name = normalize_name(persistent_name)
    reference_point = parse_coordinate_string(reference_coordinates)

    scored = []
    for candidate in candidates:
        candidate_name = normalize_name(candidate.get("teleporter_name", ""))
        exact_name_match = 1 if target_name and candidate_name == target_name else 0
        contains_name_match = 1 if target_name and candidate_name and (target_name in candidate_name or candidate_name in target_name) else 0
        if require_name_match and not (exact_name_match or contains_name_match):
            continue
        candidate_point = parse_coordinate_string(candidate.get("teleporter_coordinates", ""))
        distance = angular_distance(reference_point, candidate_point)
        scored.append((
            exact_name_match,
            contains_name_match,
            1 if candidate.get("is_favourite") else 0,
            1 if candidate.get("is_featured") else 0,
            -(distance if distance is not None else 999999.0),
            -len(candidate.get("teleporter_name", "")),
            candidate,
        ))

    if not scored:
        return None

    scored.sort(reverse=True)
    return scored[0][-1]


def teleporter_name_matches(persistent_name, candidate):
    target_name = normalize_name(persistent_name)
    candidate_name = normalize_name(candidate.get("teleporter_name", ""))
    return bool(
        target_name
        and candidate_name
        and (target_name == candidate_name or target_name in candidate_name or candidate_name in target_name)
    )


def extract_base_rows(data):
    rows = []
    teleporter_lookup = build_teleporter_lookup(data)
    primary_owner_uid = infer_primary_owner_uid(data)
    primary_owner_username = infer_primary_owner_username(data)

    for context_key, teleporter_order, base in iter_authoritative_persistent_bases(data):
        decoded = decode_packed_galactic_address_signed(base.get("GalacticAddress"))
        if not decoded:
            continue

        coords = extract_base_object_positions(base)
        raw_base_type = extract_raw_base_type(base)
        persistent_name = str(base.get("Name", "")).strip()
        persistent_last_update_raw = base.get("LastUpdateTimestamp")
        persistent_last_update = format_timestamp_local(persistent_last_update_raw)

        earliest_object_timestamp_raw = coords["earliest_object_timestamp_raw"]
        latest_object_timestamp_raw = coords["latest_object_timestamp_raw"]
        base_computer_timestamp_raw = coords["base_computer_timestamp_raw"]

        earliest_object_timestamp = format_timestamp_local(earliest_object_timestamp_raw)
        latest_object_timestamp = format_timestamp_local(latest_object_timestamp_raw)
        base_computer_timestamp = format_timestamp_local(base_computer_timestamp_raw)

        computer_coordinates = format_planetary_coordinates_from_world_position(coords["computer_world_pos"])
        base_position_coordinates = format_planetary_coordinates_from_world_position(coords["base_world_pos"])
        first_object_coordinates = format_planetary_coordinates_from_world_position(coords["first_object_world_pos"])
        reference_coordinates = computer_coordinates or base_position_coordinates or first_object_coordinates

        key = (
            decoded["VoxelX"],
            decoded["VoxelY"],
            decoded["VoxelZ"],
            decoded["SolarSystemIndex"],
            decoded["PlanetIndex"],
        )

        candidates = teleporter_lookup.get(key, [])
        eligible_candidates = (
            [candidate for candidate in candidates if teleporter_name_matches(persistent_name, candidate)]
            if decoded["PlanetIndex"] == 0
            else candidates
        )
        chosen_candidate = choose_best_teleporter_candidate(
            persistent_name=persistent_name,
            reference_coordinates=reference_coordinates,
            candidates=eligible_candidates,
            # Several Cosmos objects can share one system-level Planet-0
            # address.  Only accept a name-related teleporter entry there so
            # ships, freighters, orbital bases and stations cannot borrow one
            # another's supplemental metadata.
            require_name_match=decoded["PlanetIndex"] == 0,
        )

        reality_index = chosen_candidate.get("reality_index") if chosen_candidate else ""
        teleporter_name = chosen_candidate.get("teleporter_name", "") if chosen_candidate else ""
        teleporter_coordinates = chosen_candidate.get("teleporter_coordinates", "") if chosen_candidate else ""
        is_favourite = bool(chosen_candidate.get("is_favourite", False)) if chosen_candidate else False
        is_featured = bool(chosen_candidate.get("is_featured", False)) if chosen_candidate else False

        portal_fields = build_portal_fields(
            planet_index=decoded["PlanetIndex"],
            system_index=decoded["SolarSystemIndex"],
            voxel_x=decoded["VoxelX"],
            voxel_y=decoded["VoxelY"],
            voxel_z=decoded["VoxelZ"],
        )

        row = {
            "Teleporter Order": teleporter_order,
            "Base Name": persistent_name,
            "Base Type": friendly_base_type(raw_base_type),
            "Base Type (Raw)": raw_base_type,
            "Galaxy": galaxy_name_from_save_index(reality_index),
            "Galaxy Number (Save)": reality_index,
            "Galaxy Number (Human)": human_number_from_save_index(reality_index) if isinstance(reality_index, int) else "",
            "VoxelX": decoded["VoxelX"],
            "VoxelY": decoded["VoxelY"],
            "VoxelZ": decoded["VoxelZ"],
            "SystemIndex": decoded["SolarSystemIndex"],
            "Planet": decoded["PlanetIndex"],
            "Computer Coordinates": computer_coordinates,
            "Teleporter Coordinates": teleporter_coordinates,
            "Teleporter Base Name": teleporter_name,
            "Persistent Base Name": persistent_name,
            "Persistent Last Update Timestamp": persistent_last_update,
            "Persistent Last Update Timestamp Raw": persistent_last_update_raw if persistent_last_update_raw not in (None, "") else "",
            "Earliest Object Timestamp": earliest_object_timestamp,
            "Earliest Object Timestamp Raw": earliest_object_timestamp_raw,
            "Latest Object Timestamp": latest_object_timestamp,
            "Latest Object Timestamp Raw": latest_object_timestamp_raw,
            "Base Computer Timestamp": base_computer_timestamp,
            "Base Computer Timestamp Raw": base_computer_timestamp_raw,
            "Object Timestamp Count": coords["object_timestamp_count"],
            "Persistent Match": "Yes",
            "IsFavourite": is_favourite,
            "IsFeatured": is_featured,
            "System (Coords)": f"({decoded['VoxelX']}, {decoded['VoxelY']}, {decoded['VoxelZ']}) | {decoded['SolarSystemIndex']}",
            "Notes": "",
            "Context": context_key,
            "Owner UID": primary_owner_uid,
            "Owner Username": primary_owner_username,
            "Teleporter Candidate Count": len(eligible_candidates),
            "Base Position Coordinates": base_position_coordinates,
            "First Object Coordinates": first_object_coordinates,
            "Object Count": coords["object_count"],
            "Has Base Computer": "Yes" if coords["has_base_computer"] else "No",
            **portal_fields,
        }
        rows.append(row)

    return rows


def dedupe_exact_rows(rows):
    seen = set()
    deduped = []

    for row in rows:
        key = (
            row["Base Name"],
            row["VoxelX"],
            row["VoxelY"],
            row["VoxelZ"],
            row["SystemIndex"],
            row["Planet"],
            row["Persistent Last Update Timestamp"],
        )
        if key not in seen:
            seen.add(key)
            deduped.append(row)

    return deduped


def annotate_notes(rows):
    name_counts = Counter(row["Base Name"] for row in rows if row["Base Name"])

    for row in rows:
        notes = []
        if row["IsFavourite"]:
            notes.append("Favourite")
        if row["IsFeatured"]:
            notes.append("Featured")
        if row["Base Name"] and name_counts[row["Base Name"]] > 1:
            notes.append("Repeated base name")
        if row["Planet"] == 0 and row.get("Base Type (Raw)") == "HomePlanetBase":
            notes.append("PlanetIndex 0 (portal will error-correct to planet 1)")
        if not row.get("Teleporter Base Name"):
            notes.append("No teleporter match")
        elif row.get("Teleporter Base Name") and row.get("Persistent Base Name") and row["Teleporter Base Name"] != row["Persistent Base Name"]:
            notes.append("Teleporter name differed from persistent base name")
        if row.get("Teleporter Candidate Count", 0) > 1:
            notes.append(f"Multiple teleporter candidates ({row['Teleporter Candidate Count']})")
        if not row.get("Computer Coordinates") and row.get("Base Type (Raw)") == "HomePlanetBase":
            notes.append("No base computer object found")
        row["Notes"] = "; ".join(notes)

    return rows


def sort_rows(rows):
    return sorted(
        rows,
        key=lambda r: (
            r["Galaxy Number (Save)"] if r["Galaxy Number (Save)"] not in ("", None) else 999999,
            r["VoxelX"] if r["VoxelX"] is not None else 999999,
            r["VoxelY"] if r["VoxelY"] is not None else 999999,
            r["VoxelZ"] if r["VoxelZ"] is not None else 999999,
            r["SystemIndex"] if r["SystemIndex"] is not None else 999999,
            str(r["Base Name"]).lower(),
            r["Planet"] if r["Planet"] is not None else 999999,
        ),
    )


def write_csv(rows, output_path: Path, fieldnames):
    with output_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def build_grouped_rows(rows):
    grouped = []
    for row in rows:
        grouped.append({
            "Teleporter Order": row["Teleporter Order"],
            "Galaxy": row["Galaxy"],
            "Galaxy Number (Human)": row["Galaxy Number (Human)"],
            "Base Name": row["Base Name"],
            "Base Type": row["Base Type"],
            "Teleporter Coordinates": row["Teleporter Coordinates"],
            "Computer Coordinates": row["Computer Coordinates"],
            "Planet": row["Planet"],
            "Glyph Names": row["Glyph Names"],
            "Galaxy Number (Save)": row["Galaxy Number (Save)"],
            "Persistent Last Update Timestamp": row["Persistent Last Update Timestamp"],
            "Persistent Last Update Timestamp Raw": row["Persistent Last Update Timestamp Raw"],
            "Earliest Object Timestamp": row["Earliest Object Timestamp"],
            "Earliest Object Timestamp Raw": row["Earliest Object Timestamp Raw"],
            "Latest Object Timestamp": row["Latest Object Timestamp"],
            "Latest Object Timestamp Raw": row["Latest Object Timestamp Raw"],
            "Base Computer Timestamp": row["Base Computer Timestamp"],
            "Base Computer Timestamp Raw": row["Base Computer Timestamp Raw"],
            "Object Timestamp Count": row["Object Timestamp Count"],
            "System (Coords)": row["System (Coords)"],
            "Portal Hex (Grouped)": row["Portal Hex (Grouped)"],
            "Glyph String (No Spaces)": row["Glyph String (No Spaces)"],
            "Teleporter Base Name": row["Teleporter Base Name"],
            "Persistent Base Name": row["Persistent Base Name"],
            "Persistent Match": row["Persistent Match"],
            "Notes": row["Notes"],
        })
    return grouped


def build_duplicate_rows(rows):
    by_name = defaultdict(list)
    for row in rows:
        if row["Base Name"]:
            by_name[row["Base Name"]].append(row)

    duplicate_rows = []
    for base_name, entries in sorted(by_name.items(), key=lambda kv: kv[0].lower()):
        if len(entries) < 2:
            continue

        sorted_entries = sorted(
            entries,
            key=lambda r: (
                r["Galaxy Number (Save)"] if r["Galaxy Number (Save)"] not in ("", None) else 999999,
                r["VoxelX"] if r["VoxelX"] is not None else 999999,
                r["VoxelY"] if r["VoxelY"] is not None else 999999,
                r["VoxelZ"] if r["VoxelZ"] is not None else 999999,
                r["SystemIndex"] if r["SystemIndex"] is not None else 999999,
                r["Planet"] if r["Planet"] is not None else 999999,
            )
        )

        for idx, entry in enumerate(sorted_entries, start=1):
            duplicate_rows.append({
                "Teleporter Order": entry["Teleporter Order"],
                "Base Name": entry["Base Name"],
                "Occurrence": idx,
                "Total Occurrences": len(entries),
                "Galaxy": entry["Galaxy"],
                "Galaxy Number (Human)": entry["Galaxy Number (Human)"],
                "Galaxy Number (Save)": entry["Galaxy Number (Save)"],
                "System (Coords)": entry["System (Coords)"],
                "Planet": entry["Planet"],
                "Computer Coordinates": entry["Computer Coordinates"],
                "Teleporter Coordinates": entry["Teleporter Coordinates"],
                "Teleporter Base Name": entry["Teleporter Base Name"],
                "Persistent Base Name": entry["Persistent Base Name"],
                "Persistent Match": entry["Persistent Match"],
                "Portal Hex (Grouped)": entry["Portal Hex (Grouped)"],
                "Glyph String (No Spaces)": entry["Glyph String (No Spaces)"],
                "Persistent Last Update Timestamp": entry["Persistent Last Update Timestamp"],
                "Earliest Object Timestamp": entry["Earliest Object Timestamp"],
                "Latest Object Timestamp": entry["Latest Object Timestamp"],
                "Base Computer Timestamp": entry["Base Computer Timestamp"],
                "Notes": entry["Notes"],
            })

    return duplicate_rows



def split_valid_and_filtered_rows(rows):
    valid_rows = []
    filtered_rows = []

    for row in rows:
        planet = row.get("Planet")
        voxel_x = row.get("VoxelX")
        voxel_y = row.get("VoxelY")
        voxel_z = row.get("VoxelZ")
        galaxy = row.get("Galaxy")
        base_name = str(row.get("Base Name", "")).strip()
        timestamp = str(row.get("Persistent Last Update Timestamp", "")).strip()
        object_count = row.get("Object Count") or 0
        has_base_computer = row.get("Has Base Computer") == "Yes"
        base_position = str(row.get("Base Position Coordinates", "")).strip()
        first_object_position = str(row.get("First Object Coordinates", "")).strip()
        computer_coordinates = str(row.get("Computer Coordinates", "")).strip()

        address_looks_invalid = (
            planet == 0
            or (voxel_x == 0 and voxel_y == 0 and voxel_z == 0)
            or not galaxy
        )

        has_real_base_signals = any([
            base_name,
            timestamp,
            object_count > 0,
            has_base_computer,
            base_position,
            first_object_position,
            computer_coordinates,
        ])

        if address_looks_invalid and not has_real_base_signals:
            reasons = []
            if planet == 0:
                reasons.append("PlanetIndex 0")
            if voxel_x == 0 and voxel_y == 0 and voxel_z == 0:
                reasons.append("Zero voxel address")
            if not galaxy:
                reasons.append("Blank galaxy")

            filtered = dict(row)
            existing_notes = filtered.get("Notes", "")
            extra = "Filtered out: " + ", ".join(reasons)
            filtered["Notes"] = f"{existing_notes}; {extra}".strip("; ").strip()
            filtered_rows.append(filtered)
        else:
            valid_rows.append(row)

    return valid_rows, filtered_rows

def write_summary(rows, summary_path: Path, filtered_rows=None):
    total_bases = len(rows)
    filtered_count = len(filtered_rows) if filtered_rows is not None else 0
    by_galaxy = Counter(
        (row["Galaxy Number (Save)"], row["Galaxy"], row["Galaxy Number (Human)"])
        for row in rows
    )
    by_name = Counter(row["Base Name"] for row in rows if row["Base Name"])

    repeated_name_count = sum(1 for _, count in by_name.items() if count > 1)
    favourite_count = sum(1 for row in rows if row["IsFavourite"])
    featured_count = sum(1 for row in rows if row["IsFeatured"])
    base_type_counts = Counter(row["Base Type"] for row in rows)
    planetary_planet_zero_count = sum(
        1 for row in rows
        if row["Planet"] == 0 and row.get("Base Type (Raw)") == "HomePlanetBase"
    )
    teleporter_match_count = sum(1 for row in rows if row["Teleporter Base Name"])
    unmatched_count = total_bases - teleporter_match_count
    planetary_no_computer_count = sum(
        1 for row in rows
        if not row["Computer Coordinates"] and row.get("Base Type (Raw)") == "HomePlanetBase"
    )

    with summary_path.open("w", encoding="utf-8") as f:
        f.write("No Man's Sky Base Extraction Summary\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Total report rows: {total_bases}\n")
        f.write(f"Filtered-out rows: {filtered_count}\n")
        f.write(f"Rows with teleporter match: {teleporter_match_count}\n")
        f.write(f"Rows without teleporter match: {unmatched_count}\n")
        f.write(f"Bases marked Favourite: {favourite_count}\n")
        f.write(f"Bases marked Featured: {featured_count}\n")
        f.write(f"Distinct repeated base names: {repeated_name_count}\n")
        f.write(f"Planetary bases with PlanetIndex 0: {planetary_planet_zero_count}\n")
        f.write(f"Planetary bases without base computer object: {planetary_no_computer_count}\n\n")

        f.write("Counts by base type:\n")
        for base_type, count in sorted(base_type_counts.items()):
            f.write(f"  {base_type}: {count}\n")
        f.write("\n")

        f.write("Counts by galaxy:\n")
        for save_num, galaxy_name, human_num in sorted(
            by_galaxy.keys(),
            key=lambda x: x[0] if x[0] not in ("", None) else 999999
        ):
            count = by_galaxy[(save_num, galaxy_name, human_num)]
            display_name = galaxy_name if galaxy_name else f"Unknown Galaxy"
            f.write(f"  {display_name} | Human {human_num} | Save {save_num}: {count}\n")

        f.write("\nRepeated base names:\n")
        any_repeats = False
        for base_name, count in sorted(by_name.items(), key=lambda kv: (-kv[1], kv[0].lower())):
            if count > 1:
                any_repeats = True
                f.write(f"  {base_name}: {count}\n")
        if not any_repeats:
            f.write("  None\n")


def main():
    parser = argparse.ArgumentParser(
        description="Extract an authoritative No Man's Sky base list from PersistentPlayerBases and generate reports, using teleporter data only as supplemental metadata when available."
    )
    parser.add_argument("input_json", help="Path to the exported save JSON file")
    parser.add_argument(
        "-o",
        "--output-dir",
        default="nms_base_reports",
        help="Output directory (default: nms_base_reports)",
    )
    args = parser.parse_args()

    input_path = Path(args.input_json)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    main_csv = output_dir / "nms_bases_master.csv"
    grouped_csv = output_dir / "nms_bases_grouped.csv"
    summary_txt = output_dir / "nms_bases_summary.txt"

    # These reports are no longer useful in normal operation. Remove stale
    # copies from the selected output directory as well as ceasing generation.
    for obsolete_name in ("nms_bases_duplicate_names.csv", "nms_bases_filtered_out.csv"):
        obsolete_path = output_dir / obsolete_name
        if obsolete_path.exists():
            obsolete_path.unlink()

    data = load_json_with_backslash_fix(input_path)

    rows = extract_base_rows(data)
    rows = dedupe_exact_rows(rows)
    rows = annotate_notes(rows)
    rows, filtered_rows = split_valid_and_filtered_rows(rows)
    rows = sort_rows(rows)
    filtered_rows = sort_rows(filtered_rows)

    main_fieldnames = [
        "Teleporter Order",
        "Base Name",
        "Base Type",
        "Galaxy",
        "Galaxy Number (Human)",
        "Galaxy Number (Save)",
        "VoxelX",
        "VoxelY",
        "VoxelZ",
        "SystemIndex",
        "Planet",
        "Computer Coordinates",
        "Teleporter Coordinates",
        "System (Coords)",
        "Portal Hex (Grouped)",
        "Glyph String (No Spaces)",
        "Glyph Names",
        "Teleporter Base Name",
        "Persistent Base Name",
        "Persistent Last Update Timestamp",
        "Persistent Last Update Timestamp Raw",
        "Earliest Object Timestamp",
        "Earliest Object Timestamp Raw",
        "Latest Object Timestamp",
        "Latest Object Timestamp Raw",
        "Base Computer Timestamp",
        "Base Computer Timestamp Raw",
        "Object Timestamp Count",
        "Persistent Match",
        "Notes",
    ]
    write_csv(rows, main_csv, main_fieldnames)

    grouped_rows = build_grouped_rows(rows)
    grouped_fieldnames = [
        "Teleporter Order",
        "Galaxy",
        "Galaxy Number (Human)",
        "Base Name",
        "Base Type",
        "Teleporter Coordinates",
        "Computer Coordinates",
        "Planet",
        "Glyph Names",
        "Galaxy Number (Save)",
        "Persistent Last Update Timestamp",
        "Persistent Last Update Timestamp Raw",
        "Earliest Object Timestamp",
        "Earliest Object Timestamp Raw",
        "Latest Object Timestamp",
        "Latest Object Timestamp Raw",
        "Base Computer Timestamp",
        "Base Computer Timestamp Raw",
        "Object Timestamp Count",
        "System (Coords)",
        "Teleporter Coordinates",
        "Portal Hex (Grouped)",
        "Glyph String (No Spaces)",
        "Teleporter Base Name",
        "Persistent Base Name",
        "Persistent Match",
        "Notes",
    ]
    write_csv(grouped_rows, grouped_csv, grouped_fieldnames)

    write_summary(rows, summary_txt, filtered_rows)

    repeated_groups = sum(
        1 for count in Counter(row["Base Name"] for row in rows if row["Base Name"]).values()
        if count > 1
    )

    print(f"Master CSV written:       {main_csv.resolve()}")
    print(f"Grouped CSV written:      {grouped_csv.resolve()}")
    print(f"Summary written:          {summary_txt.resolve()}")
    print(f"\nTotal report rows: {len(rows)}")
    print(f"Filtered-out rows: {len(filtered_rows)}")
    print(f"Repeated base-name groups: {repeated_groups}")


if __name__ == "__main__":
    main()
