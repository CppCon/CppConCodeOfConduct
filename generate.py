#!/usr/bin/env python3

import os
import glob

base = {
    "emergency-number": "112",
    "conf-chair": "Mena Marotta",
    "conf-staff-list": """
- Mena Marotta (she/her)
- Matteo Bertini (he/him)
- Aurélien Rainone (he/him)
- Niccolò Pieretti (he/him)
""",
}

conf_data = {
    "golab": {
        "conf-name": "GoLab",
        "conf-hostname": "golab.io",
        "conf-lang": "Go"
    },
    "rustlab": {
        "conf-name": "RustLab",
        "conf-hostname": "rustlab.it",
        "conf-lang": "Rust",
    },
}


def generate(conf):
    os.makedirs(conf, exist_ok=True)
    for md in glob.glob("*.md"):
        with open(md) as template:
            data = template.read()
            for key, value in (base | conf_data[conf]).items():
                data = data.replace("{{%s}}" % key, value)
        with open(os.path.join(conf, md), "w+") as target:
            target.write(data)


if __name__ == "__main__":
    generate("golab")
    generate("rustlab")
