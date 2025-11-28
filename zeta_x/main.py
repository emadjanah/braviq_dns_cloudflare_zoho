# main.py
import argparse
import json
from pathlib import Path

from zeta_engine import ZetaEngine
from core.logger import get_logger

log = get_logger(__name__)

def load_config(path: str = "zeta_config.yaml"):
    """
    Load configuration from YAML when available, otherwise fall back to JSON.

    This keeps the CLI runnable even in restricted environments where PyYAML
    cannot be installed (e.g., offline or behind a proxy).
    """
    path_obj = Path(path)

    if path_obj.exists() and path_obj.suffix in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore

            with path_obj.open("r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        except ModuleNotFoundError:
            log.warning("PyYAML not installed; falling back to JSON config if present.")

    json_path = path_obj.with_suffix(".json") if path_obj.suffix in {".yaml", ".yml"} else path_obj
    if json_path.exists():
        with json_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    raise FileNotFoundError(f"No configuration file found at {path_obj} or {json_path}")


def main():
    parser = argparse.ArgumentParser(description="ZETA-X Dominion Core CLI")
    parser.add_argument("--module", "-m", required=True, help="Module name (recon, ops, leads, fin, vault)")
    parser.add_argument("--action", "-a", required=True, help="Action name (scan_market, plan_visit, ...)")
    parser.add_argument("--country", help="Country")
    parser.add_argument("--city", help="City")
    parser.add_argument("--sector", help="Sector")
    parser.add_argument("--name", help="Name")
    parser.add_argument("--channel", help="Channel")
    parser.add_argument("--notes", help="Notes")
    parser.add_argument("--title", help="Title")
    parser.add_argument("--content", help="Content")
    parser.add_argument("--exw_cost", type=float)
    parser.add_argument("--freight", type=float)
    parser.add_argument("--misc", type=float)
    parser.add_argument("--sale_price", type=float)

    args = parser.parse_args()
    config = load_config()
    engine = ZetaEngine(config)

    # نحول args إلى dict ونحذف المفاتيح الفارغة
    kw = {k: v for k, v in vars(args).items() if k not in ("module", "action") and v is not None}

    result = engine.run(args.module, args.action, **kw)
    print(result)


if __name__ == "__main__":
    main()
