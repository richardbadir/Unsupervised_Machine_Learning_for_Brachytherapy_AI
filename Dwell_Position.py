#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:06:37 2021

@author: sebquet
"""

import os

import pydicom as dicom

import numpy


class Dwell (object):
    
    def __init__(self, CT_folder):
        
        self.CT_folder = CT_folder
        dwell_file_path = self.get_dwell_file()
        self.dwell_file = dicom.read_file(dwell_file_path, force=True)
        self.list_dwell = []
        
        
    def get_dwell_file(self):
        dwell_file_path = ''
        for file in os.listdir(self.CT_folder):
            if  file[:2] == "RP":
                dwell_file_path = os.path.join(self.CT_folder, file)
                self.dwell_file_path = dwell_file_path
                break
            
        return dwell_file_path
    
    
    def get_reference_abosrbed_dose(self):
        file = self.dwell_file
        for ROI in file.DoseReferenceSequence:
            print('hi')
            
            
        
    def get_dwell_list (self):
        
        file = self.dwell_file
        list_dwell = []
        for sets_of_dwell in file.ApplicationSetupSequence[0].ChannelSequence:
            for dwell_pos in sets_of_dwell.BrachyControlPointSequence:
                if dwell_pos.CumulativeTimeWeight is not None:
                    if dwell_pos.ControlPoint3DPosition not in list_dwell:
                        list_dwell.append(dwell_pos.ControlPoint3DPosition)
                    
        self.list_dwell = list_dwell
        return self.list_dwell



if __name__ == "__main__" :
    
    from CT import CT
    import numpy as np
    ct_folder="/home/sebquet/EngerLab/Patient_Data/Breast_Data/test-data/3728_Anon"

     
    att = {"ct_folder" : ct_folder}
    my_Ct_object = CT(att)
    rescaled_grid = np.moveaxis(my_Ct_object.get_whole_grid(),0,2)
    
    My_dwells = Dwell(ct_folder )
    
    list_dwell_positions = My_dwells.get_dwell_list()
    print(len(list_dwell_positions))


    test2 = dicom.read_file( os.path.join(ct_folder, "RP93.dcm"), force=True)

    