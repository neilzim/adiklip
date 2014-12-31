#! /usr/bin/env python
"""

Carry out PSF subtraction on LMIRcam GJ504 data using principal
component analysis/K-L.

"""

import numpy as np
from adiklip import *
import time as time
import sys
import os
import cPickle as pickle
import matplotlib.pyplot as plt
import matplotlib.colors

N_proc = 4
diagnos_stride = 100
#N_proc = 2

dataset_label = 'gj504_nb8-mar13'
#data_dir = os.path.expanduser('/disk1/zimmerman/GJ504/mar13_nb8/reduc')
#result_dir = os.path.expanduser('/disk1/zimmerman/GJ504/mar13_nb8/klipsub_results')
data_dir = os.path.expanduser('/Volumes/MacDataHDD/GJ504/2014mar13/sat/reduc')
result_dir = os.path.expanduser('/Volumes/MacDataHDD/GJ504/2014mar13/sat/klipsub_results')
#
# source PCA search zone config
#
fwhm = 4.
R_inner = 212
R_out = [252]

parang_fname = '%s/%s_parang.sav' % (data_dir, dataset_label)
parang_seq = readsav(parang_fname).master_parang_arr
az_margin_psffit = 15.

PA_guess = 324.6
DPhi = [ np.round(np.abs(parang_seq[-1] - parang_seq[0]) + 2*az_margin_psffit) ]
Phi_0 = [ np.round((PA_guess + 90. - parang_seq[-1] - az_margin_psffit + DPhi[0]/2) % 360.) ]

test_mode = False
store_results = True
store_psf = False
store_archv = True
use_svd = True
coadd_full_overlap_only = True

mode_cut = [15]
min_refgap_fac = [1.0]
result_label = 'gj504_nb8-mar13_src_K%d_refgap%02d' % (mode_cut[0], round(10*min_refgap_fac[0]))

klip_config, klip_data,\
coadd_img, med_img,\
annular_rms, zonal_rms = klip_subtract(dataset_label, data_dir, result_dir, R_inner, R_out, mode_cut, DPhi, Phi_0,
                                       fwhm, min_refgap_fac, op_fr=None, N_proc=N_proc, diagnos_stride=diagnos_stride,
                                       fake_planets=None, synth_psf_img=None, test_mode=test_mode, use_svd=use_svd,
                                       coadd_full_overlap_only=coadd_full_overlap_only, store_results=store_results,
                                       store_psf=store_psf, store_archv=store_archv)

if store_archv:
    klipsub_archv_fname = "%s/%s_klipsub_archv.pkl" % (result_dir, result_label)
    if os.path.exists(klipsub_archv_fname):
        os.remove(klipsub_archv_fname)
    if store_archv:
       klipsub_archv = open(klipsub_archv_fname, 'wb') 
       pickle.dump((klip_config, klip_data), klipsub_archv, protocol=2)
       klipsub_archv.close()
       print "Wrote KLIP reduction (%.3f Mb) archive to %s" % (os.stat(klipsub_archv_fname).st_size/10.**6, klipsub_archv_fname)
