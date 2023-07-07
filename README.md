# PypeDreams
PypeDreams generates animal-based hash digests meant to be memorable
and human-readable. Pype Dreams is apt for anthropomorphizing project
names, crypto addresses, UUIDs, or any complex string of characters that
needs to be displayed in a user interface.

## Example

```
from PypeDreams import pype_dreamer

digest = pype_dreamer('my ugly input string', style='lowercase')
print(digest)
# => virtual pear wombat wearing a caftan

digest = pype_dreamer('addr1q9f082s3z98tq258ezp20v9pvcdwe4a55n2lxx54sywv9j8vq4tslucax99h9k8a9k2qykdgj4e3xa8a5fqrrl5v7xgqvhdpwx')
print(digest)
# => Zesty Amethyst Ostrich Wearing a Palazzo Pants

# Tests
from test_tool import test_tool

# Demo
from examples import demo

```

Original Helium Network Javascript library here: https://github.com/helium/angry-purple-tiger

Brought to you by https://TheMorphium.io
-Huth S0lo

## License
Apache 2.0 ©
