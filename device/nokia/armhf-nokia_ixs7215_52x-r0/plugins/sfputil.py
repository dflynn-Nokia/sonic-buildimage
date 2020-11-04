#!/usr/bin/env python

try:
    import os
    import time
    import re
    import sys
    import glob
    import sonic_platform.platform
    import sonic_platform.chassis
    from sonic_sfp.sfputilbase import SfpUtilBase
except ImportError, e:
    raise ImportError (str(e) + "- required module not found")

if sys.version_info[0] < 3:
    import commands as cmd
else:
    import subprocess as cmd

smbus_present = 1

try:
    import smbus
except ImportError, e:
    smbus_present = 0

class SfpUtil(SfpUtilBase):
    """Platform specific sfputil class"""

    _port_start = 49
    _port_end = 52
    ports_in_block = 4

    _port_to_eeprom_mapping = {}
    _changed_ports = [0,0,0,0]


    @property
    def port_start(self):
        return self._port_start

    @property
    def port_end(self):
        return self._port_end

    @property
    def qsfp_ports(self):
        return range(0, 0)
        
    @property
    def port_to_eeprom_mapping(self):
         return self._port_to_eeprom_mapping


    
    
    def __init__(self):
        # print " SfpUtil(SfpUtilBase) re-directed to chassis PMON 2.0  " 
        SfpUtilBase.__init__(self)
        self.chassis = sonic_platform.platform.Platform().get_chassis()

    def reset(self, port_num):
        # print " SfpUtil(SfpUtilBase) re-directed to chassis PMON 2.0 "
        if self.chassis is not None:
            return self.chassis.get_sfp(port_num).reset()
        else:
             print "chassis was None error "


    def set_low_power_mode(self, port_nuM, lpmode):
        # print " SfpUtil(SfpUtilBase) targeted for deprecation " 
        return False

    def get_low_power_mode(self, port_num):
        # print " SfpUtil(SfpUtilBase) targeted for deprecation " 
        return False 

    def get_presence(self, port_num):
        # print " SfpUtil(SfpUtilBase) re-directed to chassis PMON 2.0 "
        if self.chassis is not None:
            return self.chassis.get_sfp(port_num).get_presence()
        else:
             print "chassis was None error "
            

    def get_transceiver_change_event(self, timeout):
        # print " SfpUtil(SfpUtilBase) targeted for deprecation "
        port_dict = {}

        raise NotImplementedError
        
        
