#DESC	1.2 * DESCRIPTOR INFORMATION ***********************
*
*	Dataset Type and Format:
*
DSRC	EXP
BSEQ	BIG
IKKF	REAL
XTYP	IDX
YTYP	NODATA
ZTYP	NODATA
*
*	Item Formats:
*
IRFMT	D
*
*	Data Ranges and Resolutions:
*
XPTS	2048
XMIN	4000.000000
XWID	16000.000000
*
*	Documentational Text:
*
TITL	'GT192_10 Cr7Zn(purple)-Cr7Mn(green) 25dB 34.14179 5Kb'
IRNAM	'Intensity'
XNAM	'Field'
IRUNI	''
XUNI	'G'
*
************************************************************
*
#SPL	1.2 * STANDARD PARAMETER LAYER
*
OPER    xuser
DATE    10/12/10
TIME    16:23:19
CMNT    
SAMP    
SFOR    
STAG    C
EXPT    CW
OXS1    IADC
AXS1    B0VL
AXS2    NONE
AXS3    
A1CT    1.2
A1SW    1.6
MWFQ    3.4058e+10
MWPW    0.0003799
AVGS    1
RESO    Q2
SPTP    0.08192
RCAG    35
RCHM    1
B0MA    0.0003
B0MF    100000
RCPH    0.0
RCOF    0.0
A1RS    2048
RCTC    0.02048
*
************************************************************
*
#DSL	1.0 * DEVICE SPECIFIC LAYER
*

.DVC     acqStart, 1.0


.DVC     fieldCtrl, 1.0

CenterField        12000.00 G
Delay              0.0 s
FieldFlyback       On
FieldWait          Wait LED off
GFactor            2.000000
SetToSampleG       False
SweepDirection     Up
SweepWidth         16000.0 G

.DVC     fieldSweep, 1.0


.DVC     freqCounter, 1.0

FrequencyMon       34.058 GHz
QMonitBridge       On

.DVC     mwBridge, 1.0

AcqFineTuning      Never
Power              0.3799 mW
PowerAtten         25 dB

.DVC     recorder, 1.0

BaselineCorr       Off
NbScansAcc         1
NbScansDone        1
NbScansToDo        1
ReplaceMode        Off

.DVC     scanEnd, 1.0


.DVC     signalChannel, 1.0

AFCTrap            True
Calibrated         True
ConvTime           81.92 ms
DModAFCTrap        True
DModAmp            1.00 G
DModCalibrated     True
DModDetectSCT      First
DModEliDelay       1.0 us
DModExtLockIn      False
DModExtTrigger     False
DModFieldMod       First
DModGain           60 dB
DModHighPass       True
DModIntegrator     True
DModModOutput      Internal
DModSignalInput    Internal
DModTimeConst      1.28 ms
DoubleModFreq      5.00 kHz
DoubleModPhase     0.0
DoubleMode         False
EliDelay           1.0 us
ExtLockIn          False
ExtTrigger         False
Gain               35 dB
Harmonic           1
HighPass           True
Integrator         False
ModAmp             3.00 G
ModFreq            100.00 kHz
ModInput           Internal
ModOutput          Internal
ModPhase           0.0
Offset             0.0 %
QuadMode           False
QuadPhase          90.0
Resolution         2048
Resonator          1
SctNorm            True
SctRevision        DSC2
SignalInput        Internal
SweepTime          167.77 s
TimeConst          20.48 ms
TuneCaps           45

*
************************************************************
