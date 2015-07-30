__author__ = 'x433165'


import bitstring
import pandas
import numpy


class BinaryFrame:
    def __init__(self, data):
        assert isinstance(data, pandas.DataFrame)
        self.data = data
        self.bin_data = {}
        self.columns = self.data.columns

    def convert(self):
        for c in self.data.columns:
            cbin_data = ""
            for i in range(len(self.data[c])):
                bin_r = bitstring.BitArray(float=self.data[c][i], length=64)
                cbin_data += str(bin_r._getbin())
            self.bin_data[c] = cbin_data

    def discretize(self):
        for c in self.data.columns:
            cbin_data = ""
            for i in range(len(self.data[c])):
                if self.data[c][i] >= 0.0:
                    cbin_data += '1'
                else:
                    cbin_data += '0'
            self.bin_data[c] = cbin_data