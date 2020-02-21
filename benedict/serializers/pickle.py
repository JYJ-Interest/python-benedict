# -*- coding: utf-8 -*-

from __future__ import absolute_import

from benedict.serializers.abstract import AbstractSerializer

import base64
import pickle


class PickleSerializer(AbstractSerializer):

    def __init__(self):
        super(PickleSerializer, self).__init__()

    def decode(self, s, **kwargs):
        encoding = kwargs.pop('encoding', 'utf-8')
        return pickle.loads(
            base64.b64decode(s.encode(encoding)), **kwargs)

    def encode(self, d, **kwargs):
        encoding = kwargs.pop('encoding', 'utf-8')
        kwargs.setdefault('protocol', pickle.HIGHEST_PROTOCOL)
        return base64.b64encode(
            pickle.dumps(d, **kwargs)).decode(encoding)
