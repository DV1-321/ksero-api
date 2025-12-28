from ksero_payer_rules import extract_fields as base_extract, validate_fields

def extract_fields(text: str) -> dict:
    baseline = base_extract(text)
    validated = validate_fields(baseline)
    return validated