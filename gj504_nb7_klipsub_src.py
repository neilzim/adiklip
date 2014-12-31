#! /usr/bin/env python
"""

Carry out PSF subtraction on LMIRcam GJ504 data using principal
component analysis/K-L.

"""

import numpy as np
from adiklip import *
import astropy.io.fits as pyfits
import sys
import os
import cPickle as pickle

N_proc = 12 
diagnos_stride = 100

dataset_label = 'gj504_longL_octcanon'
data_dir = '/disk1/zimmerman/GJ504/apr21_longL/reduc'
result_dir = '/disk1/zimmerman/GJ504/apr21_longL/klipsub_results_fall2014'
#
# PCA search zone config
#
fwhm = 4.
R_inner = 215
R_out = [255.]
DPhi = [90.]
Phi_0 = [53.]

mode_cut = [5]
min_refgap_fac = [0.5]
result_label = 'gj504_nb7_src_K%02d_refgap%d' % (mode_cut[0], round(10*min_refgap_fac[0]))

klip_config, klip_data,\
coadd_img, med_img,\
annular_rms, zonal_rms = klip_subtract(dataset_label, data_dir, result_dir, R_inner, R_out, mode_cut, DPhi, Phi_0,
                                       fwhm, min_refgap_fac, op_fr=None, N_proc=N_proc, diagnos_stride=diagnos_stride,
                                       fake_planets=None, synth_psf_img=None, test_mode=False, use_svd=True,
                                       coadd_full_overlap_only=True, store_results=True,
                                       store_psf=False, store_archv=True)
klipsub_archv_fname = "%s/%s_klipsub_archv.pkl" % (result_dir, result_label)
if os.path.exists(klipsub_archv_fname):
    os.remove(klipsub_archv_fname)
klipsub_archv = open(klipsub_archv_fname, 'wb') 
pickle.dump((klip_config, klip_data), klipsub_archv, protocol=2)
klipsub_archv.close()
print "Wrote KLIP reduction (%.3f Mb) archive to %s" % (os.stat(klipsub_archv_fname).st_size/10.**6, klipsub_archv_fname)

mode_cut = [10]
min_refgap_fac = [0.5]
result_label = 'gj504_nb7_src_K%02d_refgap%d' % (mode_cut[0], round(10*min_refgap_fac[0]))

klip_config, klip_data,\
coadd_img, med_img,\
annular_rms, zonal_rms = klip_subtract(dataset_label, data_dir, result_dir, R_inner, R_out, mode_cut, DPhi, Phi_0,
                                       fwhm, min_refgap_fac, op_fr=None, N_proc=N_proc, diagnos_stride=diagnos_stride,
                                       fake_planets=None, synth_psf_img=None, test_mode=False, use_svd=True,
                                       coadd_full_overlap_only=True, store_results=True,
                                       store_psf=False, store_archv=True)
klipsub_archv_fname = "%s/%s_klipsub_archv.pkl" % (result_dir, result_label)
if os.path.exists(klipsub_archv_fname):
    os.remove(klipsub_archv_fname)
klipsub_archv = open(klipsub_archv_fname, 'wb') 
pickle.dump((klip_config, klip_data), klipsub_archv, protocol=2)
klipsub_archv.close()
print "Wrote KLIP reduction (%.3f Mb) archive to %s" % (os.stat(klipsub_archv_fname).st_size/10.**6, klipsub_archv_fname)

mode_cut = [15]
min_refgap_fac = [0.5]
result_label = 'gj504_nb7_src_K%02d_refgap%d' % (mode_cut[0], round(10*min_refgap_fac[0]))

klip_config, klip_data,\
coadd_img, med_img,\
annular_rms, zonal_rms = klip_subtract(dataset_label, data_dir, result_dir, R_inner, R_out, mode_cut, DPhi, Phi_0,
                                       fwhm, min_refgap_fac, op_fr=None, N_proc=N_proc, diagnos_stride=diagnos_stride,
                                       fake_planets=None, synth_psf_img=None, test_mode=False, use_svd=True,
                                       coadd_full_overlap_only=True, store_results=True,
                                       store_psf=False, store_archv=True)
klipsub_archv_fname = "%s/%s_klipsub_archv.pkl" % (result_dir, result_label)
if os.path.exists(klipsub_archv_fname):
    os.remove(klipsub_archv_fname)
klipsub_archv = open(klipsub_archv_fname, 'wb') 
pickle.dump((klip_config, klip_data), klipsub_archv, protocol=2)
klipsub_archv.close()
print "Wrote KLIP reduction (%.3f Mb) archive to %s" % (os.stat(klipsub_archv_fname).st_size/10.**6, klipsub_archv_fname)

#mode_cut = [12]
#min_refgap_fac = [1.]
#result_label = 'gj504_nb7_src_K%02d_refgap%d' % (mode_cut[0], round(10*min_refgap_fac[0]))
#
#klip_config, klip_data,\
#coadd_img, med_img,\
#annular_rms, zonal_rms = klip_subtract(dataset_label, data_dir, result_dir, R_inner, R_out, mode_cut, DPhi, Phi_0,
#                                       fwhm, min_refgap_fac, op_fr=None, N_proc=N_proc, diagnos_stride=diagnos_stride,
#                                       fake_planets=None, synth_psf_img=None, test_mode=False, use_svd=True,
#                                       coadd_full_overlap_only=True, store_results=True,
#                                       store_psf=False, store_archv=True)
#klipsub_archv_fname = "%s/%s_klipsub_archv.pkl" % (result_dir, result_label)
#if os.path.exists(klipsub_archv_fname):
#    os.remove(klipsub_archv_fname)
#klipsub_archv = open(klipsub_archv_fname, 'wb') 
#pickle.dump((klip_config, klip_data), klipsub_archv, protocol=2)
#klipsub_archv.close()
#print "Wrote KLIP reduction (%.3f Mb) archive to %s" % (os.stat(klipsub_archv_fname).st_size/10.**6, klipsub_archv_fname)
#
#mode_cut = [15]
#min_refgap_fac = [1.]
#result_label = 'gj504_nb7_src_K%02d_refgap%d' % (mode_cut[0], round(10*min_refgap_fac[0]))
#
#klip_config, klip_data,\
#coadd_img, med_img,\
#annular_rms, zonal_rms = klip_subtract(dataset_label, data_dir, result_dir, R_inner, R_out, mode_cut, DPhi, Phi_0,
#                                       fwhm, min_refgap_fac, op_fr=None, N_proc=N_proc, diagnos_stride=diagnos_stride,
#                                       fake_planets=None, synth_psf_img=None, test_mode=False, use_svd=True,
#                                       coadd_full_overlap_only=True, store_results=True,
#                                       store_psf=False, store_archv=True)
#klipsub_archv_fname = "%s/%s_klipsub_archv.pkl" % (result_dir, result_label)
#if os.path.exists(klipsub_archv_fname):
#    os.remove(klipsub_archv_fname)
#klipsub_archv = open(klipsub_archv_fname, 'wb') 
#pickle.dump((klip_config, klip_data), klipsub_archv, protocol=2)
#klipsub_archv.close()
#print "Wrote KLIP reduction (%.3f Mb) archive to %s" % (os.stat(klipsub_archv_fname).st_size/10.**6, klipsub_archv_fname)
