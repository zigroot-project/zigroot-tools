#!/usr/bin/env python3
"""Generate index.json from */metadata.toml and versions/*.toml"""

import json
import tomllib
from datetime import datetime, timezone
from pathlib import Path

def main():
    tools = []
    for meta_path in sorted(Path(".").glob("*/metadata.toml")):
        tool_dir = meta_path.parent
        with open(meta_path, "rb") as f:
            meta = tomllib.load(f)

        tool = meta.get("tool", {})
        versions = sorted(
            [v.stem for v in (tool_dir / "versions").glob("*.toml")],
            reverse=True
        )

        tools.append({
            "name": tool.get("name", tool_dir.name),
            "description": tool.get("description", ""),
            "license": tool.get("license", ""),
            "versions": versions,
            "latest": versions[0] if versions else ""
        })

    index = {
        "version": 1,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tools": tools
    }

    with open("index.json", "w") as f:
        json.dump(index, f, indent=2)

    print(f"Generated index.json with {len(tools)} tools")

if __name__ == "__main__":
    main()
