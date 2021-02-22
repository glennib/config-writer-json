import os
import json
from collections.abc import MutableMapping
    
class ConfigWriter(MutableMapping):
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
        
        self.dirty = False
    
    def write(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.store, f, sort_keys=self.sort_keys, indent=self.indent)
        self.dirty = False
    
    def read(self):
        with open(self.filepath, 'r') as f:
            self.store = json.load(f)
        self.dirty = False

    def update(self, other):
        self.store.update(other)
        self.write()

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value
        self.dirty = True
        if self.do_write_automatically:
            self.write()

    def __delitem__(self, key):
        del self.store[key]
        self.dirty = True
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
