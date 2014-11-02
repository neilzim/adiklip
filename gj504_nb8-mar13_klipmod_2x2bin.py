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

data_dir = '/disk1/zimmerman/GJ504/mar13_nb8'
#klipsub_result_dir = '%s/klipsub_results' % data_dir
klipsub_result_dir = '%s/klipsub_results' % data_dir
klipmod_result_dir = '%s/klipmod_results' % data_dir
#template_img_fname = '%s/gj504_nb8-mar13_2x2bin_globalklip_rad105-130_mode010-010_res_coadd.fits'  % klipsub_result_dir
#template_img_fname = '%s/gj504_nb8-mar13_2x2bin_globalklip_rad105-130_mode001-001_res_coadd.fits'  % klipsub_result_dir
template_img_fname = '%s/gj504_nb8-mar13_2x2bin_globalklip_rad105-130_mode020-020_res_coadd.fits'  % klipsub_result_dir
synthpsf_fname = '%s/reduc/gj504_nb8-mar13_2x2bin_psf_model.fits' % data_dir
mode_cut = 20
N_proc = 20
synthpsf_rolloff = 10.

print ''
print 'Modeling PSF in KLIP residual'
result_label = 'gj504_nb8-mar13_2x2bin_modecut%03d' % mode_cut
#klipsub_archv_fname = "%s/gj504_nb8-mar13_src_K10_klipsub_archv.pkl" % klipsub_result_dir
#klipsub_archv_fname = "%s/gj504_nb8-mar13_src_K01_klipsub_archv.pkl" % klipsub_result_dir
#klipsub_archv_fname = "%s/gj504_nb8-mar13_src_K00_klipsub_archv.pkl" % klipsub_result_dir
klipsub_archv_fname = "%s/gj504_nb8-mar13_src_K20_refgap05_klipsub_archv.pkl" % klipsub_result_dir
psol_nb6 = klipmod(ampguess=0.6, posguess_rho=117., posguess_theta=-35., klipsub_archv_fname=klipsub_archv_fname,
                        klipsub_result_dir=klipsub_result_dir, klipmod_result_dir=klipmod_result_dir,
                        template_img_fname=template_img_fname, synthpsf_fname=synthpsf_fname,
                        synthpsf_rolloff=synthpsf_rolloff, result_label=result_label, N_proc=N_proc,
                        mode_cut=mode_cut, do_MLE=True)
