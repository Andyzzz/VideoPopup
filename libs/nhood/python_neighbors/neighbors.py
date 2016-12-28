# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_neighbors', [dirname(__file__)])
        except ImportError:
            import _neighbors
            return _neighbors
        if fp is not None:
            try:
                _mod = imp.load_module('_neighbors', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _neighbors = swig_import_helper()
    del swig_import_helper
else:
    import _neighbors
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import numpy as np

def nhood_old(measurement_matrix, visibility_matrix,
              velocity_weight, neighbors_num,
              top_k, pframe_thresh,
              max_occ, occ_penalty,
              bottom_vector, top_vector,
              distances, neighbors):

    measurement_matrix = measurement_matrix.astype(np.double)
    visibility_matrix = visibility_matrix.astype(np.int32)

    bottom_vector = bottom_vector.astype(np.int32)
    top_vector = top_vector.astype(np.int32)

    distances = distances.astype(np.double)
    neighbors = neighbors.astype(np.int32)

    get_nhood_old(measurement_matrix, visibility_matrix,
                  velocity_weight, neighbors_num,
                  top_k, pframe_thresh, max_occ,
                  occ_penalty, bottom_vector, top_vector,
                  distances, neighbors)

    return distances, neighbors

def nhood(measurement_matrix, visibility_matrix,
          velocity_weight, neighbors_num,
          top_k, pframe_thresh,
          max_occ, occ_penalty,
          bottom_vector, top_vector,
          distances, neighbors,
          color_matrix, color_weight):

    measurement_matrix = measurement_matrix.astype(np.double)
    visibility_matrix = visibility_matrix.astype(np.int32)

    color_matrix = color_matrix.astype(np.double)

    bottom_vector = bottom_vector.astype(np.int32)
    top_vector = top_vector.astype(np.int32)

    distances = distances.astype(np.double)
    neighbors = neighbors.astype(np.int32)

    get_nhood(measurement_matrix, visibility_matrix,
              velocity_weight, neighbors_num,
              top_k, pframe_thresh, max_occ,
              occ_penalty, bottom_vector, top_vector,
              distances, neighbors,
              color_matrix, color_weight)

    return distances, neighbors



def get_nhood_old(*args):
  return _neighbors.get_nhood_old(*args)
get_nhood_old = _neighbors.get_nhood_old

def get_nhood(*args):
  return _neighbors.get_nhood(*args)
get_nhood = _neighbors.get_nhood
# This file is compatible with both classic and new-style classes.


