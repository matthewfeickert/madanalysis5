################################################################################
#  
#  Copyright (C) 2012-2020 Jack Araz, Eric Conte & Benjamin Fuks
#  The MadAnalysis development team, email: <ma5team@iphc.cnrs.fr>
#  
#  This file is part of MadAnalysis 5.
#  Official website: <https://launchpad.net/madanalysis5>
#  
#  MadAnalysis 5 is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  MadAnalysis 5 is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with MadAnalysis 5. If not, see <http://www.gnu.org/licenses/>
#  
################################################################################

from __future__ import absolute_import
import logging

class JetConfiguration:
    
    userVariables = ['antikt','cambridge',
                     'genkt','gridjet','kt',
                     'cdfjetclu','cdfmidpoint','siscone']

    def __init__(self,JetID='Ma5Jet', algorithm='', options={}):
        """
            Parameters
            ----------
            JetID : STR
                Jet identification =>  event.rec()->jet("MA5Jet")
            algorithm: STR
                Clustering algorithm
            options: DICT
                options such as radius, ptmin etc.

            The instance names are used directly in C++ implementation
            hence change in instance name will require change in C++ portion 
            as well.
        """
        self.JetID     = JetID

        # Main Jet Configurations
        if algorithm in self.userVariables:
            self.SetDefaultAlgorithm(algorithm, options)


    def SetDefaultAlgorithm(self,algorithm, options):
        if   algorithm == 'antikt'      : self.DefaultAntikT(options)
        elif algorithm == 'cambridge'   : self.DefaultCambridgeAchen(options)
        elif algorithm == 'genkt'       : self.DefaultGenkT(options)
        elif algorithm == 'kt'          : self.DefaultkT(options)
        elif algorithm == 'gridjet'     : self.DefaultGridJet(options)
        elif algorithm == 'cdfjetclu'   : self.DefaultCDF(options)
        elif algorithm == 'cdfmidpoint' : self.DefaultCDFMidPoint(options)
        elif algorithm == 'siscone'     : self.DefaultSisCone(options)

    def DefaultAntikT(self,kwargs):
        self.algorithm = 'antikt'
        self.radius    = kwargs.get('radius',          0.4)
        self.ptmin     = kwargs.get('ptmin',           5.)

    def DefaultkT(self,kwargs):
        self.algorithm = 'kt'
        self.radius    = kwargs.get('radius',          0.4)
        self.ptmin     = kwargs.get('ptmin',           5.)
        self.exclusive = kwargs.get('exclusive',       False)

    def DefaultCambridgeAchen(self,kwargs):
        self.algorithm = 'cambridge'
        self.radius    = kwargs.get('radius',          0.4)
        self.ptmin     = kwargs.get('ptmin',           5.)

    def DefaultGenkT(self,kwargs):
        self.algorithm = 'genkt'
        self.radius    = kwargs.get('radius',          0.4)
        self.ptmin     = kwargs.get('ptmin',           5.)
        self.exclusive = kwargs.get('exclusive',       False)
        self.p         = kwargs.get('p',               -1)

    def DefaultGridJet(self,kwargs):
        self.algorithm = 'gridjet'
        self.ymax      = kwargs.get('ymax',            3.)
        self.ptmin     = kwargs.get('ptmin',           5.)

    def DefaultSisCone(self,kwargs):
        self.algorithm   = 'siscone'
        self.radius      = kwargs.get('radius',        0.4)
        self.ptmin       = kwargs.get('ptmin',         5.)
        self.input_ptmin = kwargs.get('input_ptmin',   5.)
        self.overlap     = kwargs.get('overlap',       0.5)
        self.npassmax    = kwargs.get('npassmax',      1.)

    def DefaultCDF(self,kwargs):
        self.algorithm = 'cdfjetclu'
        self.radius    = kwargs.get('radius',          0.4)
        self.ptmin     = kwargs.get('ptmin',           5.)
        self.overlap   = kwargs.get('overlap',         0.5)
        self.seed      = kwargs.get('seed',            1.)
        self.iratch    = kwargs.get('iratch',          0.)

    def DefaultCDFMidPoint(self,kwargs):
        self.algorithm    = 'cdfmidpoint'
        self.radius       = kwargs.get('radius',       0.4)
        self.ptmin        = kwargs.get('ptmin',        5.)
        self.overlap      = kwargs.get('overlap',      0.5)
        self.seed         = kwargs.get('seed',         1.)
        self.iratch       = kwargs.get('iratch',       0.)
        self.areafraction = kwargs.get('areafraction', 1.)

    def GetJetAlgorithms(self):
        return self.userVariables

    def user_GetValues(self,parameter):
        if parameter == 'algorithm':
            return self.GetJetAlgorithms()
        else:
            return [str(self.__dict__[parameter])]

    def user_SetParameter(self,parameter,value):
        if parameter not in ['algorithm','JetID']:
            if parameter not in self.__dict__.keys():
                logging.getLogger('MA5').error("Option '"+parameter+"' is not available for "+self.algorithm+' algorithm.')
                logging.getLogger('MA5').error("Available options are : "+\
                                               ', '.join([x for x in self.__dict__.keys() if x!='JetID']))
                return
            try:
                # Except exclusive rets of the parameters are floats!!
                if parameter == 'exclusive':
                    if value.lower() in ['true','t']:
                        self.exclusive = True
                    elif value.lower() in ['false','f']:
                        self.exclusive = False
                    else:
                        raise ValueError
                else:
                    tmp = float(value)
                    self.__dict__[parameter] = tmp
                return 
            except ValueError:
                if parameter == 'exclusive':
                    logging.getLogger('MA5').error("The "+parameter+" value must be True or False.")
                else:
                    logging.getLogger('MA5').error("The "+parameter+" value must be float.")
                return
        elif parameter == 'algorithm':
            if value not in self.userVariables:
                logging.getLogger('MA5').error("The clustering algorithm '"+value+"' is not available.")
                logging.getLogger('MA5').error("Available algorithms are : "+ ', '.join(self.userVariables))
                return
            else:
                # Keep all the relevant options for the new algorithm throw the rest
                options = {}
                previous_keys = list(self.__dict__.keys())
                for key in previous_keys:
                    if key != 'JetID': 
                        options[key] = self.__dict__[key]
                        self.__dict__.pop(key)
                self.SetDefaultAlgorithm(value,options)
                # logging.getLogger('MA5').warning(self.JetID+' has been reset.')
        return

    def user_GetParameters(self):
        return [x for x in self.__dict__.keys() if x != 'JetID']


    def Display(self):
        key_order  = ['JetID','algorithm']+[x for x in ['radius','ptmin'] if x in self.__dict__.keys()]
        key_order += [x for x in self.__dict__.keys() if x not in key_order]
        for key in key_order:
            if key=='JetID':
                continue
            else:
                logging.getLogger('MA5').info('      - '+key.ljust(15,' ')+' : '+str(self.__dict__[key]))



