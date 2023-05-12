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
    "conf-year": "2023",
    "conf-location": "Florence, Italy",
}

conf_data = {
    "golab": {
        "conf-name": "GoLab",
        "conf-hostname": "golab.io",
        "conf-lang": "Go",
        "conf-fist-year": "2015",
    },
    "rustlab": {
        "conf-name": "RustLab",
        "conf-hostname": "rustlab.it",
        "conf-lang": "Rust",
        "conf-fist-year": "2019",
    },
}

for conf in conf_data:
    conf_data[conf]["conf-slug"] = conf+base["conf-year"]

for this, other in [("golab", "rustlab"), ("rustlab", "golab")]:
    for key in list(conf_data[this]):
        if key.startswith("conf-"):
             conf_data[this]["other-"+key] = conf_data[other][key]


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
