#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:54:18 2017

@author: Christina
"""

def prepro(basedir): #do something cool
    print('Hello data in the path '+basedir)

    
    
def main():
    #load in all the global variables prepro needs, right now this is just the path to the data
    basedir='/Users/desktop/UNC fMRI Workshop/ds000030_R1.0.5'
    prepro(basedir) #call prepro to do cool things
    
    
main() #call main to execute all our globals then run our prepro function
