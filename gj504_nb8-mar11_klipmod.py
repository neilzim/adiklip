#! /usr/bin/env python
"""

Implement KLIP point source forward model on LMIRcam ADI data.

"""
import numpy as np
import time as time
import astropy.io.fits as pyfits
from scipy.ndimage.interpolation import *
from scipy.interpolate import *
from scipy.optimize import *
import multiprocessing
import sys
import os
import pdb
import cPickle as pickle
from adiklip import *

#data_dir = '/disk1/zimmerman/GJ504/mar13_nb8'
data_dir = os.path.expanduser('/Volumes/MacDataHDD/GJ504/2014mar11/sat')
klipsub_result_dir = '%s/klipsub_results' % data_dir
klipmod_result_dir = '%s/klipmod_results' % data_dir
#template_img_fname = '%s/gj504_nb8-mar13_2x2bin_globalklip_rad105-130_mode010-010_res_coadd.fits'  % klipsub_result_dir
#template_img_fname = '%s/gj504_nb8-mar13_2x2bin_globalklip_rad105-130_mode001-001_res_coadd.fits'  % klipsub_result_dir
template_img_fname = '%s/gj504_nb8-mar11_klip_rad212-252_mode030-030_res_coadd.fits'  % klipsub_result_dir
synthpsf_fname = '%s/reduc/gj504_nb8-mar11_psf_model.fits' % data_dir
N_proc = 4
synthpsf_rolloff = 20.

print ''
print 'Modeling PSF in KLIP residual'

mode_cut = 30
result_label = 'gj504_nb8-mar13_modecut%03d' % mode_cut
klipsub_archv_fname = "%s/gj504_nb8-mar11_src_K%02d_refgap10_klipsub_archv.pkl" % (klipsub_result_dir, mode_cut)
psol_nb8mar13 = klipmod(ampguess=0.3, posguess_rho=232.5, posguess_theta=-35., klipsub_archv_fname=klipsub_archv_fname,
                        klipsub_result_dir=klipsub_result_dir, klipmod_result_dir=klipmod_result_dir,
                        template_img_fname=template_img_fname, synthpsf_fname=synthpsf_fname,
                        synthpsf_rolloff=synthpsf_rolloff, result_label=result_label, N_proc=N_proc,
                        mode_cut=mode_cut, do_MLE=True)
