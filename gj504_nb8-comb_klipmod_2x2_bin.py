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

data_dir_mar11 = '/disk1/zimmerman/GJ504/mar11_nb8'
data_dir_mar13 = '/disk1/zimmerman/GJ504/mar13_nb8'
#klipsub_result_dir = '%s/klipsub_results' % data_dir
klipsub_result_dir_mar11 = '%s/klipsub_results' % data_dir_mar11
klipsub_result_dir_mar13 = '%s/klipsub_results' % data_dir_mar13
klipmod_result_dir_mar11 = '%s/klipmod_results' % data_dir_mar11
klipmod_result_dir_mar13 = '%s/klipmod_results' % data_dir_mar13
#test_res_img_fname_mar11 = '%s/gj504_nb8-mar11_2x2bin_globalklip_rad105-130_mode000-000_res_coadd.fits'  % klipsub_result_dir_mar11
#test_res_img_fname_mar13 = '%s/gj504_nb8-mar13_2x2bin_globalklip_rad105-130_mode000-000_res_coadd.fits'  % klipsub_result_dir_mar13
test_res_img_fname_mar11 = '%s/gj504_nb8-mar11_2x2bin_globalklip_rad105-130_mode020-020_res_coadd.fits'  % klipsub_result_dir_mar11
test_res_img_fname_mar13 = '%s/gj504_nb8-mar13_2x2bin_globalklip_rad105-130_mode020-020_res_coadd.fits'  % klipsub_result_dir_mar13
synthpsf_fname_mar11 = '%s/reduc/gj504_nb8-mar11_2x2bin_psf_model.fits' % data_dir_mar11
synthpsf_fname_mar13 = '%s/reduc/gj504_nb8-mar13_2x2bin_psf_model.fits' % data_dir_mar13
mode_cut_mar11 = 20
mode_cut_mar13 = 20
N_proc = 20
synthpsf_rolloff = 10.

N_tel_mar11 = 1
N_tel_mar13 = 2
expt_mar11 = 0.989726
expt_mar13 = 0.873288
eff_expt_mar11 = N_tel_mar11 * expt_mar11
eff_expt_mar13 = N_tel_mar13 * expt_mar13
flux_scale_fac = eff_expt_mar13 / eff_expt_mar11
test_res_img_hdulist = pyfits.open(test_res_img_fname_mar11, 'readonly')
test_res_img_mar11 = test_res_img_hdulist[0].data
test_res_img_hdulist.close()
test_res_img_hdulist = pyfits.open(test_res_img_fname_mar13, 'readonly')
test_res_img_mar13 = test_res_img_hdulist[0].data
test_res_img_hdulist.close()
xy_src = (test_res_img_mar11.shape[0]/2 - 0.5 + 67.1, test_res_img_mar11.shape[0]/2 - 0.5 + 94.8)
src_rad_map = np.sqrt(get_radius_sqrd(test_res_img_mar11.shape, c = xy_src))
test_ind = np.where( src_rad_map > 4. )
test_rms_mar11 = np.sqrt( nanmean( test_res_img_mar11[test_ind]**2 ) )
test_rms_mar13 = np.sqrt( nanmean( test_res_img_mar13[test_ind]**2 ) )
#test_rms_mar11 = np.sqrt( nanmean( np.ravel(test_res_img_mar11)**2 ) )
#test_rms_mar13 = np.sqrt( nanmean( np.ravel(test_res_img_mar13)**2 ) )
#sd_mar11 = 0.34 # standard deviation of ADI residual image within a 51x51 pixel box surrounding the source
#sd_mar13 = 0.40 # standard deviation of ADI residual image within a 51x51 pixel box surrounding the source
print 'RMS in mar 11 and mar 13 KLIP subtraction test images: %0.2e, %0.2e' % (test_rms_mar11, test_rms_mar13)
#weight_mar11 = 1. / (flux_scale_fac * test_rms_mar11)**2
#weight_mar13 = 1. / test_rms_mar13**2
weight_mar11 = 0.
weight_mar13 = 1.
print 'Weights on mar 11 and mar 13 KLIP model: %0.2e, %0.2e' % (weight_mar11, weight_mar13)

print ''
print 'Modeling PSF in joint Mar11 and Mar13 NB8 KLIP residual'
#result_label = 'gj504_nb8-comb_2x2bin_mar11modecut%03d_mar13modecut%03d_weightsON' % (mode_cut_mar11, mode_cut_mar13)
result_label = 'gj504_nb8-comb_2x2bin_mar11modecut%03d_mar13modecut%03d_weightMar13only' % (mode_cut_mar11, mode_cut_mar13)
#klipsub_archv_fname_mar11 = "%s/gj504_nb8-mar11_src_K10_klipsub_archv.pkl" % klipsub_result_dir_mar11
#klipsub_archv_fname_mar13 = "%s/gj504_nb8-mar13_src_K10_klipsub_archv.pkl" % klipsub_result_dir_mar13
klipsub_archv_fname_mar11 = "%s/gj504_nb8-mar11_src_K20_refgap10_klipsub_archv.pkl" % klipsub_result_dir_mar11
#klipsub_archv_fname_mar13 = "%s/gj504_nb8-mar13_src_K20_refgap10_klipsub_archv.pkl" % klipsub_result_dir_mar13
klipsub_archv_fname_mar13 = "%s/gj504_nb8-mar13_src_K20_refgap05_klipsub_archv.pkl" % klipsub_result_dir_mar13
#psol_nb8 = twoobs_klipmod(ampguess=0.33, posguess_rho=117., posguess_theta=-35.,
psol_nb8 = twoobs_klipmod(ampguess=0.6, posguess_rho=117., posguess_theta=-35.,
                          obs2to1_flux_scale_fac=1/flux_scale_fac, obs1_weight = weight_mar13, obs2_weight = weight_mar11,
                          obs1_klipsub_archv_fname=klipsub_archv_fname_mar13, obs2_klipsub_archv_fname=klipsub_archv_fname_mar11,
                          obs1_klipsub_result_dir=klipsub_result_dir_mar13, obs2_klipsub_result_dir=klipsub_result_dir_mar11,
                          obs1_klipmod_result_dir=klipmod_result_dir_mar13, obs2_klipmod_result_dir=klipmod_result_dir_mar11,
                          obs1_template_img_fname=test_res_img_fname_mar13, obs2_template_img_fname=test_res_img_fname_mar11,
                          obs1_synthpsf_fname=synthpsf_fname_mar13, obs2_synthpsf_fname=synthpsf_fname_mar11,
                          synthpsf_rolloff=synthpsf_rolloff, result_label=result_label, N_proc=N_proc,
                          obs1_mode_cut=mode_cut_mar13, obs2_mode_cut=mode_cut_mar11, do_MLE=True)
