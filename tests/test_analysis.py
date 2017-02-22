# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:36:11 2017

@author: Shengyuan
"""

import pytest
import floodsystem.analysis as analysis

def test_polyfit():
    assert type(analysis.polyfit()) == numpy.poly1d