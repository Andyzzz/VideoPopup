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
            fp, pathname, description = imp.find_module('_segmentation', [dirname(__file__)])
        except ImportError:
            import _segmentation
            return _segmentation
        if fp is not None:
            try:
                _mod = imp.load_module('_segmentation', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _segmentation = swig_import_helper()
    del swig_import_helper
else:
    import _segmentation
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

def allgc(unary, overlap_nbor, pairwise_nbor, pairwise_cost,
          interior_labels, lambda_weight, label_costs, ppthresh,
          pbthresh, overlap_cost):

    """ Newest graph-cut segmentation algorithm that supports edge-breaking and sparsity in overlapping models.
        unary: [points * models] unary cost, overlap_nbor: [overlap_nbor_num * points] neighborhood, pairwise_nbor:
        [pairwise_nbor_num * points], pairwise_cost: [pairwise_nbor_num * points ] pairwise cost, interior_labels:
        [1*points] vector current interior labeling, lambda: overlapping parameter, label_costs: [1*points] vector mdl label costs,
        ppthresh: [1*points] vector per point outlier threshold, pbthresh: [overlap_nbor_num * points / 1 * points] 2d array
        edge breaking threshold(per edge or per point, corresponding to different strategies),
        overlap_cost: cost per pairwise overlapping labels.
    """
    from numpy import zeros

    mask_out = zeros(unary.shape)
    labels_out = zeros(unary.shape[0])

    overlap_nbor = overlap_nbor.astype(np.double)
    pairwise_nbor = pairwise_nbor.astype(np.double)
    pairwise_cost = pairwise_cost.astype(np.double)
    interior_labels = interior_labels.astype(np.double)
    label_costs = label_costs.astype(np.double)
    ppthresh = ppthresh.astype(np.double)
    pbthresh = pbthresh.astype(np.double)

    _allgc(mask_out, labels_out, unary, overlap_nbor, pairwise_nbor,
           pairwise_cost, interior_labels, lambda_weight, label_costs, ppthresh,
           pbthresh, overlap_cost)

    return mask_out, labels_out

def expand(unary, pairwise_nbor, pairwise_cost, interior_labels, label_costs, ppthresh):

    from numpy import zeros
    mask_out = zeros(unary.shape)
    labels_out = zeros(unary.shape[0])

    pairwise_nbor = pairwise_nbor.astype(np.double)
    pairwise_cost = pairwise_cost.astype(np.double)
    interior_labels = interior_labels.astype(np.double)
    label_costs = label_costs.astype(np.double)
    ppthresh = ppthresh.astype(np.double)

    _expand(mask_out, labels_out, unary, pairwise_nbor, pairwise_cost,
            interior_labels, label_costs, ppthresh)

    return mask_out, labels_out

def multi(unary, overlap_nbor, interior_labels, lambda_weight, label_costs, ppthresh, pbthresh, overlap_cost):

    from numpy import zeros
    mask_out = zeros(unary.shape)
    labels_out = zeros(unary.shape[0])

    overlap_nbor = overlap_nbor.astype(np.double)
    interior_labels = interior_labels.astype(np.double)
    label_costs = label_costs.astype(np.double)
    ppthresh = ppthresh.astype(np.double)
    pbthresh = pbthresh.astype(np.double)

    _multi(mask_out, labels_out, unary, overlap_nbor, interior_labels,
           lambda_weight, label_costs, ppthresh, pbthresh, overlap_cost)

    return mask_out, labels_out



def _allgc(*args):
  return _segmentation._allgc(*args)
_allgc = _segmentation._allgc

def _expand(*args):
  return _segmentation._expand(*args)
_expand = _segmentation._expand

def _multi(*args):
  return _segmentation._multi(*args)
_multi = _segmentation._multi
# This file is compatible with both classic and new-style classes.

