#coding:utf-8
import matplotlib
matplotlib.use('Qt5Agg')
import webbrowser
import sys
import sklearn as sk
import scipy.stats as st
import requests
import re
import random
import pandas as pd
import os
import os
import numpy as np
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib import path
import matplotlib.patches as patches
import matplotlib.image as mpimg
import matplotlib.font_manager as font_manager
import math
import csv
from xml.dom import minidom
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, Binarizer, OneHotEncoder, Imputer,  PolynomialFeatures, FunctionTransformer
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2
from sklearn.decomposition import PCA, FastICA
from sklearn import datasets
from scipy.stats import mode
from scipy.spatial.distance import *
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy as hc
from PyQt5.QtWidgets import QMainWindow, QMenu, QSizePolicy, QMessageBox, QWidget, QFileDialog, QAction, QLineEdit,    QApplication, QPushButton, QSlider, QLabel, QHBoxLayout, QVBoxLayout,QProxyStyle,QStyle,qApp,QCheckBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import vstack, array, nan, mean, median, ptp, var, std, cov, corrcoef, arange, sin, pi
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.font_manager import ttfFontProperty
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib import ft2font
from bs4 import BeautifulSoup
from geopytool.TabelViewer import TabelViewer


LocationOfMySelf=os.path.dirname(__file__)

print(LocationOfMySelf,'Import Denpendence')

fpath = LocationOfMySelf+('/wqy.ttf')

font = ft2font.FT2Font(fpath)
fprop = font_manager.FontProperties(fname=fpath)

ttfFontProp = ttfFontProperty(font)
fontprop = font_manager.FontProperties(family='sans-serif',
                            size=9,
                            fname=ttfFontProp.fname,
                            stretch=ttfFontProp.stretch,
                            style=ttfFontProp.style,
                            variant=ttfFontProp.variant,
                            weight=ttfFontProp.weight)


'''
fontprop = font_manager.FontProperties(family='sans-serif',
                            size=9,
                            fname=ttfFontProp.fname,
                            stretch=ttfFontProp.stretch,
                            style=ttfFontProp.style,
                            variant=ttfFontProp.variant,
                            weight=ttfFontProp.weight)
'''

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['pdf.fonttype'] = 'truetype'
plt.rcParams['axes.unicode_minus']=False


_translate = QtCore.QCoreApplication.translate