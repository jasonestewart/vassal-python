from VASSAL.counters import Decorator, Embellishment, BasicPiece

# 1 (activateCommand)	            'Activate',	     'Activate',
# 2 (activateModifiers)	            '128',	         '128',
# 3 (activateKey)	                'A',	         'A',
# 4 (upCommand)	                    '',	             'fooIncR',
# 5 (upModifiers)	                '128',	         '128',
# 6 (upKey)	                        '',	             '',
# 7 (downCommand)	                '',	             'fooDecD',
# 8 (downModifiers)	                '128',	         '128',
# 9 (downKey)	                    '',	             '',
# 10 (resetCommand)	                '',	             'fooResetF',
# 11 (resetKey)	                    '',	             '70,130',
# 12 (resetLevel.getFormat())	    '1',	         '1',
# 13 (drawUnderneathWhenSelected)   'false',         'false',
# 14 (xOff)	                        '0',	         '0',
# 15 (yOff)	                        '0',		     '0',
# 16 (imageName)	                '',	  	         '',
# 17 (commonName)    	            '',	 	         '',
# 18 (loopLevels)	                'true',		     'false',
# 19 (name)	                        'foo name',	     '',
# 20 (rndKey)   // rnd 	            '',	 	         '',
# 21 (rndText)  // rnd 	            '',	 	         '',
# 22 (followProperty)	            'true',		     'false',
# 23 (propertyName)	                '{fooValue}',	 '',
# 24 (firstLevelValue)	            '1',	         '1',
# 25 (version)	  	                '1',		     '1',
# 26 (alwaysActive)	 	            'true',	         'true',
# 27 (activateKeyStroke)            '65,130',	     '65,130',
# 28 (increaseKeyStroke)            '',	         	 '82,130',
# 29 (decreaseKeyStroke)            '',	         	 '68,130',
# 30 (description)	                'foo desc',    	 '',
# 31 (scale);	 	                '1.0'	       	 '1.0'

class Layer:
    _layer_class = Embellishment().getClass()
    _NAME             = 19
    _FOLLOW_PROP_BOOL = 22
    _FOLLOW_PROP_EXPR = 23
    _FIRST_LEVEL_VAL  = 24


    def __init__(self, emb):
        self._array = [str(x) for x in emb.myGetType().split(';')]
        self._emb = emb

    def __setitem__(self, key, value):
        self._array[key] = value

    def set_follow_expression(self, expr):
        self.__setitem__(key=Layer._FOLLOW_PROP_EXPR, value=expr)
        self.__setitem__(key=Layer._FOLLOW_PROP_BOOL, value="true")
        self.__setitem__(key=Layer._FIRST_LEVEL_VAL , value="1")

    def set_name(self, name):
        self.__setitem__(key=Layer._NAME, value=name)

    @staticmethod
    def rename_piece_layer(piece, old_layer_name, new_layer_name):
        emb = Layer.find_layer(piece, old_layer_name)
        if emb:
            layer = Layer(emb)
            layer.set_name(new_layer_name)
            layer.set_layer()
            return layer
        else:
            return None


    @staticmethod
    def find_layer(piece, layer_name):
        while not isinstance(piece, BasicPiece):
            layer = Decorator.getDecorator(piece, Layer._layer_class)
            if layer.getLayerName() == layer_name:
                return layer
            piece = layer.getInner()
        return None

    @staticmethod
    def layer_to_array(layer):
        return list(layer.getType().split(';'))

    def set_layer(self):
        type_str = ';'.join(self._array)
        self._emb.mySetType(type_str)

    def set_piece_layer_from_layer(self, piece, layer_name):
        type_str = ';'.join(self._array)
        layer = Layer.find_layer(piece, layer_name)
        if layer:
            layer.mySetType(type_str)
