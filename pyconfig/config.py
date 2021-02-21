import os
import json
from collections.abc import MutableMapping
    
class Config(MutableMapping):
    def __init__(self, filepath, do_write_automatically=True, sort_keys=True, indent=4):
        self.store = dict()
        self.do_write_automatically = do_write_automatically

        self.sort_keys = sort_keys
        self.indent = indent

        self.filepath = filepath
        if os.path.isfile(self.filepath):
            self.read()
        else:
            self.write()
    
    def write(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.store, f, sort_keys=self.sort_keys, indent=self.indent)
    
    def read(self):
        with open(self.filepath, 'r') as f:
            self.store = json.load(f)

    def update(self, other):
        self.store.update(other)
        self.write()

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value
        if self.do_write_automatically:
            self.write()

    def __delitem__(self, key):
        del self.store[key]
        if self.do_write_automatically:
            self.write()

    def __iter__(self):
        return iter(self.store)
    
    def __len__(self):
        return len(self.store)
    
    def __repr__(self):
        return repr(self.store)
    
    def __str__(self):
        return str(self.store)
    
    def __contains__(self, key):
        return key in self.store


from pprint import pprint
def main():
    config = Config('config.json')
    for key, value in config.items():
        print(str(key) + ': ' + str(value))
    
    d = {
        'one': 2,
        'three': 4
    }
    d['d'] = d.copy()
    pprint(d)
    config.update(d)

if __name__ == '__main__':
    main()