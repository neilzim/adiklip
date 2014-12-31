#! /usr/bin/env python
"""

Implement KLIP point source forward model on LMIRcam kappa And ADI data.

"""
import numpy as np
import astropy.io.fits as pyfits
from adiklip import *

data_dir = '/disk1/zimmerman/GJ504/apr21_longL'
klipsub_result_dir = '%s/klipsub_results_fall2014' % data_dir
klipmod_result_dir = '%s/klipmod_results' % data_dir
template_img_fname = '%s/gj504_longL_octcanon_globalklip_rad215-255_mode020-020_res_coadd.fits'  % klipsub_result_dir
synthpsf_fname = '%s/reduc/gj504_longL_psf_model.fits' % data_dir
N_proc = 22
synthpsf_rolloff = 20.

mode_cut = 5
refgap_fac = 0.5
result_label = 'gj504_nb7_modecut%03d_refgap%02d' % (mode_cut, round(10*refgap_fac))
klipsub_archv_fname = "%s/gj504_nb7_src_K%02d_refgap%d_klipsub_archv.pkl" % (klipsub_result_dir, mode_cut, round(10*refgap_fac))
psol_octcanon = klipmod(ampguess=0.5, posguess_rho=235., posguess_theta=-33., klipsub_archv_fname=klipsub_archv_fname,
                        klipsub_result_dir=klipsub_result_dir, klipmod_result_dir=klipmod_result_dir,
                        template_img_fname=template_img_fname, synthpsf_fname=synthpsf_fname,
                        synthpsf_rolloff=synthpsf_rolloff, result_label=result_label, N_proc=N_proc,
                        mode_cut=mode_cut, do_MLE=True)

#mode_cut = 20
#refgap_fac = 1.
#result_label = 'gj504_nb7_modecut%03d_refgap%02d' % (mode_cut, round(10*refgap_fac))
#klipsub_archv_fname = "%s/gj504_nb7_src_K%02d_refgap%d_klipsub_archv.pkl" % (klipsub_result_dir, mode_cut, round(10*refgap_fac))
#psol_octcanon = klipmod(ampguess=0.5, posguess_rho=235., posguess_theta=-33., klipsub_archv_fname=klipsub_archv_fname,
#                        klipsub_result_dir=klipsub_result_dir, klipmod_result_dir=klipmod_result_dir,
#                        template_img_fname=template_img_fname, synthpsf_fname=synthpsf_fname,
#                        synthpsf_rolloff=synthpsf_rolloff, result_label=result_label, N_proc=N_proc,
#                        mode_cut=mode_cut, do_MLE=True)
#mode_cut = 30
#refgap_fac = 1.
#result_label = 'gj504_nb7_modecut%03d_refgap%02d' % (mode_cut, round(10*refgap_fac))
#klipsub_archv_fname = "%s/gj504_nb7_src_K%02d_refgap%d_klipsub_archv.pkl" % (klipsub_result_dir, mode_cut, round(10*refgap_fac))
#psol_octcanon = klipmod(ampguess=0.5, posguess_rho=235., posguess_theta=-33., klipsub_archv_fname=klipsub_archv_fname,
#                        klipsub_result_dir=klipsub_result_dir, klipmod_result_dir=klipmod_result_dir,
#                        template_img_fname=template_img_fname, synthpsf_fname=synthpsf_fname,
#                        synthpsf_rolloff=synthpsf_rolloff, result_label=result_label, N_proc=N_proc,
#                        mode_cut=mode_cut, do_MLE=True)
#mode_cut = 50
#refgap_fac = 1.
#result_label = 'gj504_nb7_modecut%03d_refgap%02d' % (mode_cut, round(10*refgap_fac))
#klipsub_archv_fname = "%s/gj504_nb7_src_K%02d_refgap%d_klipsub_archv.pkl" % (klipsub_result_dir, mode_cut, round(10*refgap_fac))
#psol_octcanon = klipmod(ampguess=0.5, posguess_rho=235., posguess_theta=-33., klipsub_archv_fname=klipsub_archv_fname,
#                        klipsub_result_dir=klipsub_result_dir, klipmod_result_dir=klipmod_result_dir,
#                        template_img_fname=template_img_fname, synthpsf_fname=synthpsf_fname,
#                        synthpsf_rolloff=synthpsf_rolloff, result_label=result_label, N_proc=N_proc,
#                        mode_cut=mode_cut, do_MLE=True)
