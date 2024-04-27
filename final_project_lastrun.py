#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.1),
    on April 27, 2024, at 00:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.1'
expName = 'final_project'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'age': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\sophi\\OneDrive\\文档\\9.60 Experiment\\final_project_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[-1.0000, -1.0000, -0.6863], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -0.6863]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp_welcome') is None:
        # initialise key_resp_welcome
        key_resp_welcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_welcome',
        )
    if deviceManager.getDevice('key_resp_intro') is None:
        # initialise key_resp_intro
        key_resp_intro = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_intro',
        )
    if deviceManager.getDevice('key_resp_instructions') is None:
        # initialise key_resp_instructions
        key_resp_instructions = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_instructions',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='Welcome and thank you for taking the time to do the experiment!\n\nThe following page will be providing the instructions to complete each task. Your email will be asked at the end of the experiment to enter the boba raffle.\n\nPress SPACEBAR to begin.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_welcome = keyboard.Keyboard(deviceName='key_resp_welcome')
    
    # --- Initialize components for Routine "Intro_Bongard" ---
    textIntro = visual.TextStim(win=win, name='textIntro',
        text='Bongard are geometric puzzles that consists of two sets of six images. Traditionally, in order to solve the puzzle you are required to identify the rule that differentiate the images on the left from those on the right. For example, for the hypothetical Bongard problem below the rule that separates the two set is "left are all white images and right are all black images."',
        font='Open Sans',
        units='norm', pos=(0, 0.55), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageBongardExample = visual.ImageStim(
        win=win,
        name='imageBongardExample', units='norm', 
        image='example_bongard.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.75, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    textSPACEBARContinue = visual.TextStim(win=win, name='textSPACEBARContinue',
        text='Press SPACEBAR to continue.',
        font='Open Sans',
        pos=(0, -0.325), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_intro = keyboard.Keyboard(deviceName='key_resp_intro')
    
    # --- Initialize components for Routine "Instructions" ---
    textInstructions = visual.TextStim(win=win, name='textInstructions',
        text='For this experiment, instead of asking you to identify the rule, we will ask you to group images you believe belong together. We will randomize the image order and ask you to use a slider to indicate if each image belongs to the left or right. Images in the same group should be assigned the same orientation. For the last Bongard problem example, both of the following answers would be considered correct.',
        font='Open Sans',
        units='norm', pos=(0, 0.55), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_correct_1 = visual.ImageStim(
        win=win,
        name='image_correct_1', 
        image='File (4).jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.05), size=(0.4, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_correct_2 = visual.ImageStim(
        win=win,
        name='image_correct_2', 
        image='File (5).jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.05), size=(0.4, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    textFinalInstructions = visual.TextStim(win=win, name='textFinalInstructions',
        text='Now you are ready for the experiment! Simply press on the slide bar for the red dot to appear and drag to change its location. Have fun and press SPACEBAR to begin!',
        font='Open Sans',
        pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp_instructions = keyboard.Keyboard(deviceName='key_resp_instructions')
    
    # --- Initialize components for Routine "trial" ---
    t_1 = visual.ImageStim(
        win=win,
        name='t_1', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.9, 0.9), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    t_2 = visual.ImageStim(
        win=win,
        name='t_2', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.48, 0.9), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    t_3 = visual.ImageStim(
        win=win,
        name='t_3', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.06, 0.9), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    t_4 = visual.ImageStim(
        win=win,
        name='t_4', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(0.36, 0.9), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    t_5 = visual.ImageStim(
        win=win,
        name='t_5', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.9, 0.27), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    t_6 = visual.ImageStim(
        win=win,
        name='t_6', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.48, 0.27), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    t_7 = visual.ImageStim(
        win=win,
        name='t_7', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.06, 0.27), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    t_8 = visual.ImageStim(
        win=win,
        name='t_8', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(0.36, 0.27), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    t_9 = visual.ImageStim(
        win=win,
        name='t_9', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.9, -0.35), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    t_10 = visual.ImageStim(
        win=win,
        name='t_10', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.48, -0.35), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    t_11 = visual.ImageStim(
        win=win,
        name='t_11', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(-0.06, -0.35), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    t_12 = visual.ImageStim(
        win=win,
        name='t_12', units='norm', 
        image='default.png', mask=None, anchor='top-left',
        ori=0.0, pos=(0.36, -0.35), size=(0.35, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(0.05, 0.025), pos=(-0.725, 0.35), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-12, readOnly=False)
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=None, size=(0.05, 0.025), pos=(-0.305, 0.35), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-13, readOnly=False)
    slider_3 = visual.Slider(win=win, name='slider_3',
        startValue=None, size=(0.05, 0.025), pos=(0.115, 0.35), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-14, readOnly=False)
    slider_4 = visual.Slider(win=win, name='slider_4',
        startValue=None, size=(0.05, 0.025), pos=(0.535, 0.35), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-15, readOnly=False)
    slider_5 = visual.Slider(win=win, name='slider_5',
        startValue=None, size=(0.05, 0.025), pos=(-0.725, -0.28), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-16, readOnly=False)
    slider_6 = visual.Slider(win=win, name='slider_6',
        startValue=None, size=(0.05, 0.025), pos=(-0.305, -0.28), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-17, readOnly=False)
    slider_7 = visual.Slider(win=win, name='slider_7',
        startValue=None, size=(0.05, 0.025), pos=(0.115, -0.28), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-18, readOnly=False)
    slider_8 = visual.Slider(win=win, name='slider_8',
        startValue=None, size=(0.05, 0.025), pos=(0.535, -0.28), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-19, readOnly=False)
    slider_9 = visual.Slider(win=win, name='slider_9',
        startValue=None, size=(0.05, 0.025), pos=(-0.725, -0.9), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-20, readOnly=False)
    slider_10 = visual.Slider(win=win, name='slider_10',
        startValue=None, size=(0.05, 0.025), pos=(-0.305, -0.9), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-21, readOnly=False)
    slider_11 = visual.Slider(win=win, name='slider_11',
        startValue=None, size=(0.05, 0.025), pos=(0.115, -0.9), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-22, readOnly=False)
    slider_12 = visual.Slider(win=win, name='slider_12',
        startValue=None, size=(0.05, 0.025), pos=(0.535, -0.9), units='norm',
        labels=None, ticks=(0, 1), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[1.0000, 1.0000, 1.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-23, readOnly=False)
    imageNext = visual.ImageStim(
        win=win,
        name='imageNext', units='norm', 
        image='next.png', mask=None, anchor='center-right',
        ori=0.0, pos=(0.95, 0), size=(0.2, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-24.0)
    mouseNext = event.Mouse(win=win)
    x, y = [None, None]
    mouseNext.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "ThankYou" ---
    textThankYou = visual.TextStim(win=win, name='textThankYou',
        text='Thank you for participating in the experiment! Please enter your email below to enter the boba raffle.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textboxEmail = visual.TextBox2(
         win, text='email', placeholder=None, font='Arial',
         pos=(0, -0.3),units='norm',     letterHeight=0.05,
         size=(0.35, 0.1), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textboxEmail',
         depth=-1, autoLog=True,
    )
    textSpaceExit = visual.TextStim(win=win, name='textSpaceExit',
        text='Press SPACEBAR to exit the experiment.',
        font='Open Sans',
        units='norm', pos=(0, -0.5), height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Welcome.started', globalClock.getTime(format='float'))
    key_resp_welcome.keys = []
    key_resp_welcome.rt = []
    _key_resp_welcome_allKeys = []
    # keep track of which components have finished
    WelcomeComponents = [textWelcome, key_resp_welcome]
    for thisComponent in WelcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_welcome* updates
        waitOnFlip = False
        
        # if key_resp_welcome is starting this frame...
        if key_resp_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_welcome.frameNStart = frameN  # exact frame index
            key_resp_welcome.tStart = t  # local t and not account for scr refresh
            key_resp_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_welcome.started')
            # update status
            key_resp_welcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_welcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_welcome.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_welcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_welcome_allKeys.extend(theseKeys)
            if len(_key_resp_welcome_allKeys):
                key_resp_welcome.keys = _key_resp_welcome_allKeys[-1].name  # just the last key pressed
                key_resp_welcome.rt = _key_resp_welcome_allKeys[-1].rt
                key_resp_welcome.duration = _key_resp_welcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Welcome.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_welcome.keys in ['', [], None]:  # No response was made
        key_resp_welcome.keys = None
    thisExp.addData('key_resp_welcome.keys',key_resp_welcome.keys)
    if key_resp_welcome.keys != None:  # we had a response
        thisExp.addData('key_resp_welcome.rt', key_resp_welcome.rt)
        thisExp.addData('key_resp_welcome.duration', key_resp_welcome.duration)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Intro_Bongard" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Intro_Bongard.started', globalClock.getTime(format='float'))
    key_resp_intro.keys = []
    key_resp_intro.rt = []
    _key_resp_intro_allKeys = []
    # keep track of which components have finished
    Intro_BongardComponents = [textIntro, imageBongardExample, textSPACEBARContinue, key_resp_intro]
    for thisComponent in Intro_BongardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Intro_Bongard" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textIntro* updates
        
        # if textIntro is starting this frame...
        if textIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textIntro.frameNStart = frameN  # exact frame index
            textIntro.tStart = t  # local t and not account for scr refresh
            textIntro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textIntro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textIntro.started')
            # update status
            textIntro.status = STARTED
            textIntro.setAutoDraw(True)
        
        # if textIntro is active this frame...
        if textIntro.status == STARTED:
            # update params
            pass
        
        # *imageBongardExample* updates
        
        # if imageBongardExample is starting this frame...
        if imageBongardExample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageBongardExample.frameNStart = frameN  # exact frame index
            imageBongardExample.tStart = t  # local t and not account for scr refresh
            imageBongardExample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageBongardExample, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageBongardExample.started')
            # update status
            imageBongardExample.status = STARTED
            imageBongardExample.setAutoDraw(True)
        
        # if imageBongardExample is active this frame...
        if imageBongardExample.status == STARTED:
            # update params
            pass
        
        # *textSPACEBARContinue* updates
        
        # if textSPACEBARContinue is starting this frame...
        if textSPACEBARContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textSPACEBARContinue.frameNStart = frameN  # exact frame index
            textSPACEBARContinue.tStart = t  # local t and not account for scr refresh
            textSPACEBARContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textSPACEBARContinue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textSPACEBARContinue.started')
            # update status
            textSPACEBARContinue.status = STARTED
            textSPACEBARContinue.setAutoDraw(True)
        
        # if textSPACEBARContinue is active this frame...
        if textSPACEBARContinue.status == STARTED:
            # update params
            pass
        
        # *key_resp_intro* updates
        waitOnFlip = False
        
        # if key_resp_intro is starting this frame...
        if key_resp_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_intro.frameNStart = frameN  # exact frame index
            key_resp_intro.tStart = t  # local t and not account for scr refresh
            key_resp_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_intro.started')
            # update status
            key_resp_intro.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_intro.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_intro.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_intro.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_intro_allKeys.extend(theseKeys)
            if len(_key_resp_intro_allKeys):
                key_resp_intro.keys = _key_resp_intro_allKeys[-1].name  # just the last key pressed
                key_resp_intro.rt = _key_resp_intro_allKeys[-1].rt
                key_resp_intro.duration = _key_resp_intro_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intro_BongardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro_Bongard" ---
    for thisComponent in Intro_BongardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Intro_Bongard.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_intro.keys in ['', [], None]:  # No response was made
        key_resp_intro.keys = None
    thisExp.addData('key_resp_intro.keys',key_resp_intro.keys)
    if key_resp_intro.keys != None:  # we had a response
        thisExp.addData('key_resp_intro.rt', key_resp_intro.rt)
        thisExp.addData('key_resp_intro.duration', key_resp_intro.duration)
    thisExp.nextEntry()
    # the Routine "Intro_Bongard" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime(format='float'))
    key_resp_instructions.keys = []
    key_resp_instructions.rt = []
    _key_resp_instructions_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [textInstructions, image_correct_1, image_correct_2, textFinalInstructions, key_resp_instructions]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstructions* updates
        
        # if textInstructions is starting this frame...
        if textInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructions.frameNStart = frameN  # exact frame index
            textInstructions.tStart = t  # local t and not account for scr refresh
            textInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructions.started')
            # update status
            textInstructions.status = STARTED
            textInstructions.setAutoDraw(True)
        
        # if textInstructions is active this frame...
        if textInstructions.status == STARTED:
            # update params
            pass
        
        # *image_correct_1* updates
        
        # if image_correct_1 is starting this frame...
        if image_correct_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_correct_1.frameNStart = frameN  # exact frame index
            image_correct_1.tStart = t  # local t and not account for scr refresh
            image_correct_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_correct_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_correct_1.started')
            # update status
            image_correct_1.status = STARTED
            image_correct_1.setAutoDraw(True)
        
        # if image_correct_1 is active this frame...
        if image_correct_1.status == STARTED:
            # update params
            pass
        
        # *image_correct_2* updates
        
        # if image_correct_2 is starting this frame...
        if image_correct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_correct_2.frameNStart = frameN  # exact frame index
            image_correct_2.tStart = t  # local t and not account for scr refresh
            image_correct_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_correct_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_correct_2.started')
            # update status
            image_correct_2.status = STARTED
            image_correct_2.setAutoDraw(True)
        
        # if image_correct_2 is active this frame...
        if image_correct_2.status == STARTED:
            # update params
            pass
        
        # *textFinalInstructions* updates
        
        # if textFinalInstructions is starting this frame...
        if textFinalInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textFinalInstructions.frameNStart = frameN  # exact frame index
            textFinalInstructions.tStart = t  # local t and not account for scr refresh
            textFinalInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textFinalInstructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textFinalInstructions.started')
            # update status
            textFinalInstructions.status = STARTED
            textFinalInstructions.setAutoDraw(True)
        
        # if textFinalInstructions is active this frame...
        if textFinalInstructions.status == STARTED:
            # update params
            pass
        
        # *key_resp_instructions* updates
        waitOnFlip = False
        
        # if key_resp_instructions is starting this frame...
        if key_resp_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_instructions.frameNStart = frameN  # exact frame index
            key_resp_instructions.tStart = t  # local t and not account for scr refresh
            key_resp_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_instructions.started')
            # update status
            key_resp_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_instructions.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_instructions_allKeys.extend(theseKeys)
            if len(_key_resp_instructions_allKeys):
                key_resp_instructions.keys = _key_resp_instructions_allKeys[-1].name  # just the last key pressed
                key_resp_instructions.rt = _key_resp_instructions_allKeys[-1].rt
                key_resp_instructions.duration = _key_resp_instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_instructions.keys in ['', [], None]:  # No response was made
        key_resp_instructions.keys = None
    thisExp.addData('key_resp_instructions.keys',key_resp_instructions.keys)
    if key_resp_instructions.keys != None:  # we had a response
        thisExp.addData('key_resp_instructions.rt', key_resp_instructions.rt)
        thisExp.addData('key_resp_instructions.duration', key_resp_instructions.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('data_randomized.xlsx', selection=random(12)*393),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime(format='float'))
        t_1.setImage(image1)
        t_2.setImage(image2)
        t_3.setImage(image3)
        t_4.setImage(image4)
        t_5.setImage(image5)
        t_6.setImage(image6)
        t_7.setImage(image7)
        t_8.setImage(image8)
        t_9.setImage(image9)
        t_10.setImage(image10)
        t_11.setImage(image11)
        t_12.setImage(image12)
        slider_1.reset()
        slider_2.reset()
        slider_3.reset()
        slider_4.reset()
        slider_5.reset()
        slider_6.reset()
        slider_7.reset()
        slider_8.reset()
        slider_9.reset()
        slider_10.reset()
        slider_11.reset()
        slider_12.reset()
        # setup some python lists for storing info about the mouseNext
        mouseNext.x = []
        mouseNext.y = []
        mouseNext.leftButton = []
        mouseNext.midButton = []
        mouseNext.rightButton = []
        mouseNext.time = []
        mouseNext.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        trialComponents = [t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9, t_10, t_11, t_12, slider_1, slider_2, slider_3, slider_4, slider_5, slider_6, slider_7, slider_8, slider_9, slider_10, slider_11, slider_12, imageNext, mouseNext]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *t_1* updates
            
            # if t_1 is starting this frame...
            if t_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_1.frameNStart = frameN  # exact frame index
                t_1.tStart = t  # local t and not account for scr refresh
                t_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_1.started')
                # update status
                t_1.status = STARTED
                t_1.setAutoDraw(True)
            
            # if t_1 is active this frame...
            if t_1.status == STARTED:
                # update params
                pass
            
            # *t_2* updates
            
            # if t_2 is starting this frame...
            if t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_2.frameNStart = frameN  # exact frame index
                t_2.tStart = t  # local t and not account for scr refresh
                t_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_2.started')
                # update status
                t_2.status = STARTED
                t_2.setAutoDraw(True)
            
            # if t_2 is active this frame...
            if t_2.status == STARTED:
                # update params
                pass
            
            # *t_3* updates
            
            # if t_3 is starting this frame...
            if t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_3.frameNStart = frameN  # exact frame index
                t_3.tStart = t  # local t and not account for scr refresh
                t_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_3.started')
                # update status
                t_3.status = STARTED
                t_3.setAutoDraw(True)
            
            # if t_3 is active this frame...
            if t_3.status == STARTED:
                # update params
                pass
            
            # *t_4* updates
            
            # if t_4 is starting this frame...
            if t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_4.frameNStart = frameN  # exact frame index
                t_4.tStart = t  # local t and not account for scr refresh
                t_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_4.started')
                # update status
                t_4.status = STARTED
                t_4.setAutoDraw(True)
            
            # if t_4 is active this frame...
            if t_4.status == STARTED:
                # update params
                pass
            
            # *t_5* updates
            
            # if t_5 is starting this frame...
            if t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_5.frameNStart = frameN  # exact frame index
                t_5.tStart = t  # local t and not account for scr refresh
                t_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_5.started')
                # update status
                t_5.status = STARTED
                t_5.setAutoDraw(True)
            
            # if t_5 is active this frame...
            if t_5.status == STARTED:
                # update params
                pass
            
            # *t_6* updates
            
            # if t_6 is starting this frame...
            if t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_6.frameNStart = frameN  # exact frame index
                t_6.tStart = t  # local t and not account for scr refresh
                t_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_6.started')
                # update status
                t_6.status = STARTED
                t_6.setAutoDraw(True)
            
            # if t_6 is active this frame...
            if t_6.status == STARTED:
                # update params
                pass
            
            # *t_7* updates
            
            # if t_7 is starting this frame...
            if t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_7.frameNStart = frameN  # exact frame index
                t_7.tStart = t  # local t and not account for scr refresh
                t_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_7.started')
                # update status
                t_7.status = STARTED
                t_7.setAutoDraw(True)
            
            # if t_7 is active this frame...
            if t_7.status == STARTED:
                # update params
                pass
            
            # *t_8* updates
            
            # if t_8 is starting this frame...
            if t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_8.frameNStart = frameN  # exact frame index
                t_8.tStart = t  # local t and not account for scr refresh
                t_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_8.started')
                # update status
                t_8.status = STARTED
                t_8.setAutoDraw(True)
            
            # if t_8 is active this frame...
            if t_8.status == STARTED:
                # update params
                pass
            
            # *t_9* updates
            
            # if t_9 is starting this frame...
            if t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_9.frameNStart = frameN  # exact frame index
                t_9.tStart = t  # local t and not account for scr refresh
                t_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_9.started')
                # update status
                t_9.status = STARTED
                t_9.setAutoDraw(True)
            
            # if t_9 is active this frame...
            if t_9.status == STARTED:
                # update params
                pass
            
            # *t_10* updates
            
            # if t_10 is starting this frame...
            if t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_10.frameNStart = frameN  # exact frame index
                t_10.tStart = t  # local t and not account for scr refresh
                t_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_10.started')
                # update status
                t_10.status = STARTED
                t_10.setAutoDraw(True)
            
            # if t_10 is active this frame...
            if t_10.status == STARTED:
                # update params
                pass
            
            # *t_11* updates
            
            # if t_11 is starting this frame...
            if t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_11.frameNStart = frameN  # exact frame index
                t_11.tStart = t  # local t and not account for scr refresh
                t_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_11.started')
                # update status
                t_11.status = STARTED
                t_11.setAutoDraw(True)
            
            # if t_11 is active this frame...
            if t_11.status == STARTED:
                # update params
                pass
            
            # *t_12* updates
            
            # if t_12 is starting this frame...
            if t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                t_12.frameNStart = frameN  # exact frame index
                t_12.tStart = t  # local t and not account for scr refresh
                t_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(t_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_12.started')
                # update status
                t_12.status = STARTED
                t_12.setAutoDraw(True)
            
            # if t_12 is active this frame...
            if t_12.status == STARTED:
                # update params
                pass
            
            # *slider_1* updates
            
            # if slider_1 is starting this frame...
            if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_1.frameNStart = frameN  # exact frame index
                slider_1.tStart = t  # local t and not account for scr refresh
                slider_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.started')
                # update status
                slider_1.status = STARTED
                slider_1.setAutoDraw(True)
            
            # if slider_1 is active this frame...
            if slider_1.status == STARTED:
                # update params
                pass
            
            # *slider_2* updates
            
            # if slider_2 is starting this frame...
            if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_2.frameNStart = frameN  # exact frame index
                slider_2.tStart = t  # local t and not account for scr refresh
                slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_2.started')
                # update status
                slider_2.status = STARTED
                slider_2.setAutoDraw(True)
            
            # if slider_2 is active this frame...
            if slider_2.status == STARTED:
                # update params
                pass
            
            # *slider_3* updates
            
            # if slider_3 is starting this frame...
            if slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_3.frameNStart = frameN  # exact frame index
                slider_3.tStart = t  # local t and not account for scr refresh
                slider_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_3.started')
                # update status
                slider_3.status = STARTED
                slider_3.setAutoDraw(True)
            
            # if slider_3 is active this frame...
            if slider_3.status == STARTED:
                # update params
                pass
            
            # *slider_4* updates
            
            # if slider_4 is starting this frame...
            if slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_4.frameNStart = frameN  # exact frame index
                slider_4.tStart = t  # local t and not account for scr refresh
                slider_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_4.started')
                # update status
                slider_4.status = STARTED
                slider_4.setAutoDraw(True)
            
            # if slider_4 is active this frame...
            if slider_4.status == STARTED:
                # update params
                pass
            
            # *slider_5* updates
            
            # if slider_5 is starting this frame...
            if slider_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_5.frameNStart = frameN  # exact frame index
                slider_5.tStart = t  # local t and not account for scr refresh
                slider_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_5.started')
                # update status
                slider_5.status = STARTED
                slider_5.setAutoDraw(True)
            
            # if slider_5 is active this frame...
            if slider_5.status == STARTED:
                # update params
                pass
            
            # *slider_6* updates
            
            # if slider_6 is starting this frame...
            if slider_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_6.frameNStart = frameN  # exact frame index
                slider_6.tStart = t  # local t and not account for scr refresh
                slider_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_6.started')
                # update status
                slider_6.status = STARTED
                slider_6.setAutoDraw(True)
            
            # if slider_6 is active this frame...
            if slider_6.status == STARTED:
                # update params
                pass
            
            # *slider_7* updates
            
            # if slider_7 is starting this frame...
            if slider_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_7.frameNStart = frameN  # exact frame index
                slider_7.tStart = t  # local t and not account for scr refresh
                slider_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_7.started')
                # update status
                slider_7.status = STARTED
                slider_7.setAutoDraw(True)
            
            # if slider_7 is active this frame...
            if slider_7.status == STARTED:
                # update params
                pass
            
            # *slider_8* updates
            
            # if slider_8 is starting this frame...
            if slider_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_8.frameNStart = frameN  # exact frame index
                slider_8.tStart = t  # local t and not account for scr refresh
                slider_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_8.started')
                # update status
                slider_8.status = STARTED
                slider_8.setAutoDraw(True)
            
            # if slider_8 is active this frame...
            if slider_8.status == STARTED:
                # update params
                pass
            
            # *slider_9* updates
            
            # if slider_9 is starting this frame...
            if slider_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_9.frameNStart = frameN  # exact frame index
                slider_9.tStart = t  # local t and not account for scr refresh
                slider_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_9.started')
                # update status
                slider_9.status = STARTED
                slider_9.setAutoDraw(True)
            
            # if slider_9 is active this frame...
            if slider_9.status == STARTED:
                # update params
                pass
            
            # *slider_10* updates
            
            # if slider_10 is starting this frame...
            if slider_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_10.frameNStart = frameN  # exact frame index
                slider_10.tStart = t  # local t and not account for scr refresh
                slider_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_10.started')
                # update status
                slider_10.status = STARTED
                slider_10.setAutoDraw(True)
            
            # if slider_10 is active this frame...
            if slider_10.status == STARTED:
                # update params
                pass
            
            # *slider_11* updates
            
            # if slider_11 is starting this frame...
            if slider_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_11.frameNStart = frameN  # exact frame index
                slider_11.tStart = t  # local t and not account for scr refresh
                slider_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_11.started')
                # update status
                slider_11.status = STARTED
                slider_11.setAutoDraw(True)
            
            # if slider_11 is active this frame...
            if slider_11.status == STARTED:
                # update params
                pass
            
            # *slider_12* updates
            
            # if slider_12 is starting this frame...
            if slider_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_12.frameNStart = frameN  # exact frame index
                slider_12.tStart = t  # local t and not account for scr refresh
                slider_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_12.started')
                # update status
                slider_12.status = STARTED
                slider_12.setAutoDraw(True)
            
            # if slider_12 is active this frame...
            if slider_12.status == STARTED:
                # update params
                pass
            
            # *imageNext* updates
            
            # if imageNext is starting this frame...
            if imageNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imageNext.frameNStart = frameN  # exact frame index
                imageNext.tStart = t  # local t and not account for scr refresh
                imageNext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageNext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNext.started')
                # update status
                imageNext.status = STARTED
                imageNext.setAutoDraw(True)
            
            # if imageNext is active this frame...
            if imageNext.status == STARTED:
                # update params
                pass
            # *mouseNext* updates
            
            # if mouseNext is starting this frame...
            if mouseNext.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseNext.frameNStart = frameN  # exact frame index
                mouseNext.tStart = t  # local t and not account for scr refresh
                mouseNext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseNext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouseNext.started', t)
                # update status
                mouseNext.status = STARTED
                mouseNext.mouseClock.reset()
                prevButtonState = mouseNext.getPressed()  # if button is down already this ISN'T a new click
            if mouseNext.status == STARTED:  # only update if started and not finished!
                buttons = mouseNext.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(imageNext, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseNext):
                                gotValidClick = True
                                mouseNext.clicked_name.append(obj.name)
                        x, y = mouseNext.getPos()
                        mouseNext.x.append(x)
                        mouseNext.y.append(y)
                        buttons = mouseNext.getPressed()
                        mouseNext.leftButton.append(buttons[0])
                        mouseNext.midButton.append(buttons[1])
                        mouseNext.rightButton.append(buttons[2])
                        mouseNext.time.append(mouseNext.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime(format='float'))
        trials.addData('slider_1.response', slider_1.getRating())
        trials.addData('slider_1.rt', slider_1.getRT())
        trials.addData('slider_2.response', slider_2.getRating())
        trials.addData('slider_2.rt', slider_2.getRT())
        trials.addData('slider_3.response', slider_3.getRating())
        trials.addData('slider_3.rt', slider_3.getRT())
        trials.addData('slider_4.response', slider_4.getRating())
        trials.addData('slider_4.rt', slider_4.getRT())
        trials.addData('slider_5.response', slider_5.getRating())
        trials.addData('slider_5.rt', slider_5.getRT())
        trials.addData('slider_6.response', slider_6.getRating())
        trials.addData('slider_6.rt', slider_6.getRT())
        trials.addData('slider_7.response', slider_7.getRating())
        trials.addData('slider_7.rt', slider_7.getRT())
        trials.addData('slider_8.response', slider_8.getRating())
        trials.addData('slider_8.rt', slider_8.getRT())
        trials.addData('slider_9.response', slider_9.getRating())
        trials.addData('slider_9.rt', slider_9.getRT())
        trials.addData('slider_10.response', slider_10.getRating())
        trials.addData('slider_10.rt', slider_10.getRT())
        trials.addData('slider_11.response', slider_11.getRating())
        trials.addData('slider_11.rt', slider_11.getRT())
        trials.addData('slider_12.response', slider_12.getRating())
        trials.addData('slider_12.rt', slider_12.getRT())
        # store data for trials (TrialHandler)
        trials.addData('mouseNext.x', mouseNext.x)
        trials.addData('mouseNext.y', mouseNext.y)
        trials.addData('mouseNext.leftButton', mouseNext.leftButton)
        trials.addData('mouseNext.midButton', mouseNext.midButton)
        trials.addData('mouseNext.rightButton', mouseNext.rightButton)
        trials.addData('mouseNext.time', mouseNext.time)
        trials.addData('mouseNext.clicked_name', mouseNext.clicked_name)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "ThankYou" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ThankYou.started', globalClock.getTime(format='float'))
    textboxEmail.reset()
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ThankYouComponents = [textThankYou, textboxEmail, textSpaceExit, key_resp]
    for thisComponent in ThankYouComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ThankYou" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textThankYou* updates
        
        # if textThankYou is starting this frame...
        if textThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textThankYou.frameNStart = frameN  # exact frame index
            textThankYou.tStart = t  # local t and not account for scr refresh
            textThankYou.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textThankYou, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textThankYou.started')
            # update status
            textThankYou.status = STARTED
            textThankYou.setAutoDraw(True)
        
        # if textThankYou is active this frame...
        if textThankYou.status == STARTED:
            # update params
            pass
        
        # *textboxEmail* updates
        
        # if textboxEmail is starting this frame...
        if textboxEmail.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxEmail.frameNStart = frameN  # exact frame index
            textboxEmail.tStart = t  # local t and not account for scr refresh
            textboxEmail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxEmail, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxEmail.started')
            # update status
            textboxEmail.status = STARTED
            textboxEmail.setAutoDraw(True)
        
        # if textboxEmail is active this frame...
        if textboxEmail.status == STARTED:
            # update params
            pass
        
        # *textSpaceExit* updates
        
        # if textSpaceExit is starting this frame...
        if textSpaceExit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textSpaceExit.frameNStart = frameN  # exact frame index
            textSpaceExit.tStart = t  # local t and not account for scr refresh
            textSpaceExit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textSpaceExit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textSpaceExit.started')
            # update status
            textSpaceExit.status = STARTED
            textSpaceExit.setAutoDraw(True)
        
        # if textSpaceExit is active this frame...
        if textSpaceExit.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThankYouComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ThankYou" ---
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ThankYou.stopped', globalClock.getTime(format='float'))
    thisExp.addData('textboxEmail.text',textboxEmail.text)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
