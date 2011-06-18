class DataField(object):
    
    def __init__(self, obj, field, defaults, only_defaults=False):
        self._obj = obj
        self._field = field
        self._def_settings = defaults
        self._only_defaults = only_defaults
        if only_defaults:
            try:
                allowed_settings = dict([(key, value) for (key, value) in self.iteritems() if key in self._defaults.keys()])
                self._defaults.update(allowed_settings)
            except (TypeError, AttributeError): 
                pass
        else:
            settings = self._settings
            if settings is not None:
                self._defaults.update(self._settings)
        self._settings = self._defaults
    
    @property
    def _defaults(self):
        return self._def_settings
    
    @property
    def _settings(self):
        return getattr(self._obj, self._field)
    
    def iteritems(self):
        return self._settings.iteritems()
    
    def __repr__(self):
        return str(self._settings)
    
    def __call__(self):
        return self._settings
    
    def __dir__(self):
        return self._settings.keys()
    
    def __getattr__(self, name):
        try:
            if self._only_defaults:
                if name in self._defaults:
                    return self._settings[name]
                else:
                    raise AttributeError("Attribute '%s' does not exist" % name)
            else:
                return self._settings[name]
        except KeyError:
            return None 
    
    def __setattr__(self, name, value):
        if name in ('_obj', '_field', '_def_settings', '_settings', '_only_defaults'):
            if name == '_settings':
                setattr(self._obj, self._field, value)
            else:
                self.__dict__[name] = value
        else:
            if self._only_defaults:
                if name in self._defaults:
                    self._settings[name] = value
                else:
                    raise AttributeError("Creation of new attributes ('%s') not allowed" % name)
            else:
                self._settings[name] = value

    def __getitem__(self, name):
        return self.__getattr__(name)
    
    def __setitem__(self, name, value):
        return self.__setattr__(name, value)