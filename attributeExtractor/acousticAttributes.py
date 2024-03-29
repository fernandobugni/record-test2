from textgrid import TextGrid, Tier
import mfccExtractor as mfccExt
import phraseToAccents as phToAcc
import attributes as att
import numpy as np
import re
import logging

logger = logging.getLogger('acousticAttributes: ')

mfcc_len = 33 #33

#=======================================================================
# La 'c' antes de la 't' no suena
def _foundPattern(wordPattern, syllablePattern, textgrid, mfcc):

    # buquemos si esta es la frase con 'CT'
    wordInterval = []

    for i, tier in enumerate(textgrid):
        if tier.nameid == 'words':
            for row in tier.simple_transcript:
                if re.search(wordPattern, str(row[2])):
                    interval = {}
                    interval['xmin'] = row[0]
                    interval['xmax'] = row[1]
                    wordInterval += [interval]

    logger.debug('wordInterval: '+str(wordInterval))

    # busquemos en ese intervalo la 'k'
    syllableIntervals = []
    for i, tier in enumerate(textgrid):
        if tier.nameid == 'phones':

            prevRow = (0,0,'')
            for row in tier.simple_transcript:

                # guardo la letra previa sino es
                if re.search(syllablePattern, str(prevRow[2])+str(row[2])):

                    for interval in wordInterval:
                        if interval['xmin'] < prevRow[0] and prevRow[1] < interval['xmax']:
                            interval1 = {}
                            interval1['xmin'] = prevRow[0]
                            interval1['xmax'] = prevRow[1]
                            syllableIntervals += [interval1]
                
                prevRow = row

    if syllableIntervals:
        mfccs = ()
        for interval in syllableIntervals:

            tuplee = mfcc[float(interval['xmin']):float(interval['xmax'])]
            mfccs = mfccs + tuplee
        logger.debug('syllableIntervals: '+str(syllableIntervals))
        return mfccs
    else:
        return '?'

#=======================================================================

KT = {'wordPattern': r'.CT.', 'syllablePattern': r'kt' } 

def ACU_AverageKT(textgrid, mfcc):
    logger.debug('mfccAverageKT: ')
    mfccTemp = _foundPattern(KT['wordPattern'], KT['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.average(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])

def ACU_MaxKT(textgrid, mfcc):
    logger.debug('mfccMaxKT: ')
    mfccTemp = _foundPattern(KT['wordPattern'], KT['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amax(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])

def ACU_MinKT(textgrid, mfcc):
    logger.debug('mfccMinKT: ')
    mfccTemp = _foundPattern(KT['wordPattern'], KT['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amin(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])
#=======================================================================

LL = {'wordPattern': r'LL.', 'syllablePattern': r'Z.'}

def ACU_AverageLL(textgrid, mfcc):
    logger.debug('mfccAverageLL: ')
    mfccTemp = _foundPattern(LL['wordPattern'], LL['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.average(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])        

def ACU_MaxLL(textgrid, mfcc):
    logger.debug('mfccMaxLL: ')
    mfccTemp = _foundPattern(LL['wordPattern'], LL['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amax(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])        

def ACU_MinLL(textgrid, mfcc):
    logger.debug('mfccMinLL: ')
    mfccTemp = _foundPattern(LL['wordPattern'], LL['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amin(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)]) 
#=======================================================================

# TODO: Para la RR hacer el extractor de atributos para la longitud
    
RR = {'wordPattern': r'.RR.', 'syllablePattern': r'R.'}

def ACU_AverageRR(textgrid, mfcc):
    logger.debug('mfccAverageRR: ')
    mfccTemp = _foundPattern(RR['wordPattern'], RR['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.average(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)]) 

def ACU_MaxRR(textgrid, mfcc):
    logger.debug('mfccMaxRR: ')
    mfccTemp = _foundPattern(RR['wordPattern'], RR['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amax(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)]) 

def ACU_MinRR(textgrid, mfcc):
    logger.debug('mfccMinRR: ')
    mfccTemp = _foundPattern(RR['wordPattern'], RR['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amin(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)]) 

#=======================================================================

SC = {'wordPattern': r'.SC.', 'syllablePattern': r'hk'}

def ACU_AverageSC(textgrid, mfcc):
    logger.debug('mfccAverageSC: ')
    mfccTemp = _foundPattern(SC['wordPattern'], SC['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.average(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])         

def ACU_MaxSC(textgrid, mfcc):
    logger.debug('mfccMaxSC: ')
    mfccTemp = _foundPattern(SC['wordPattern'], SC['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amax(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])         

def ACU_MinSC(textgrid, mfcc):
    logger.debug('mfccMinSC: ')
    mfccTemp = _foundPattern(SC['wordPattern'], SC['syllablePattern'], textgrid, mfcc)
    if isinstance(mfccTemp, tuple):
        mfccTemp = np.around(mfccTemp, decimals=2)
        return np.amin(mfccTemp, axis=0)
    else:
        return np.array([None for i in range(mfcc_len)])         

def _dummy(textgrid, mfcc):
    return '8'