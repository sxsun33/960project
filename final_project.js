/********************** 
 * Final_Project *
 **********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'final_project';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'age': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 0.6863)]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(Intro_BongardRoutineBegin());
flowScheduler.add(Intro_BongardRoutineEachFrame());
flowScheduler.add(Intro_BongardRoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(ThankYouRoutineBegin());
flowScheduler.add(ThankYouRoutineEachFrame());
flowScheduler.add(ThankYouRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'data_randomized.xlsx', 'path': 'data_randomized.xlsx'},
    {'name': 'example_bongard.png', 'path': 'example_bongard.png'},
    {'name': 'File (4).jpg', 'path': 'File (4).jpg'},
    {'name': 'File (5).jpg', 'path': 'File (5).jpg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'next.png', 'path': 'next.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeClock;
var textWelcome;
var key_resp_welcome;
var Intro_BongardClock;
var textIntro;
var imageBongardExample;
var textSPACEBARContinue;
var key_resp_intro;
var InstructionsClock;
var textInstructions;
var image_correct_1;
var image_correct_2;
var textFinalInstructions;
var key_resp_instructions;
var trialClock;
var t_1;
var t_2;
var t_3;
var t_4;
var t_5;
var t_6;
var t_7;
var t_8;
var t_9;
var t_10;
var t_11;
var t_12;
var slider_1;
var slider_2;
var slider_3;
var slider_4;
var slider_5;
var slider_6;
var slider_7;
var slider_8;
var slider_9;
var slider_10;
var slider_11;
var slider_12;
var imageNext;
var mouseNext;
var ThankYouClock;
var textThankYou;
var textboxEmail;
var textSpaceExit;
var key_resp;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Welcome and thank you for taking the time to do the experiment!\n\nThe following page will be providing the instructions to complete each task. Your email will be asked at the end of the experiment to enter the boba raffle.\n\nPress SPACEBAR to begin.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_welcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Intro_Bongard"
  Intro_BongardClock = new util.Clock();
  textIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'textIntro',
    text: 'Bongard are geometric puzzles that consists of two sets of six images. Traditionally, in order to solve the puzzle you are required to identify the rule that differentiate the images on the left from those on the right. For example, for the hypothetical Bongard problem below the rule that separates the two set is "left are all white images and right are all black images."',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0, 0.55], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageBongardExample = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageBongardExample', units : 'norm', 
    image : 'example_bongard.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.1)], size : [0.75, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  textSPACEBARContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSPACEBARContinue',
    text: 'Press SPACEBAR to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.325)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_intro = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  textInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstructions',
    text: 'For this experiment, instead of asking you to identify the rule, we will ask you to group images you believe belong together. We will randomize the image order and ask you to use a slider to indicate if each image belongs to the left or right. Images in the same group should be assigned the same orientation. For the last Bongard problem example, both of the following answers would be considered correct.',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0, 0.55], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_correct_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_correct_1', units : undefined, 
    image : 'File (4).jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.05)], size : [0.4, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_correct_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_correct_2', units : undefined, 
    image : 'File (5).jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.05)], size : [0.4, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  textFinalInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'textFinalInstructions',
    text: 'Now you are ready for the experiment! Simply press on the slide bar for the red dot to appear and drag to change its location. Have fun and press SPACEBAR to begin!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  key_resp_instructions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  t_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_1', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.9), 0.9], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  t_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_2', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.48), 0.9], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  t_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_3', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.06), 0.9], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  t_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_4', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [0.36, 0.9], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  t_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_5', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.9), 0.27], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  t_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_6', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.48), 0.27], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  t_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_7', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.06), 0.27], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  t_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_8', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [0.36, 0.27], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  t_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_9', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.9), (- 0.35)], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  t_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_10', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.48), (- 0.35)], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  t_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_11', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [(- 0.06), (- 0.35)], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  t_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_12', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'top-left',
    ori : 0.0, pos : [0.36, (- 0.35)], size : [0.35, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -11.0 
  });
  slider_1 = new visual.Slider({
    win: psychoJS.window, name: 'slider_1',
    startValue: undefined,
    size: [0.05, 0.025], pos: [(- 0.725), 0.35], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -12, 
    flip: false,
  });
  
  slider_2 = new visual.Slider({
    win: psychoJS.window, name: 'slider_2',
    startValue: undefined,
    size: [0.05, 0.025], pos: [(- 0.305), 0.35], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -13, 
    flip: false,
  });
  
  slider_3 = new visual.Slider({
    win: psychoJS.window, name: 'slider_3',
    startValue: undefined,
    size: [0.05, 0.025], pos: [0.115, 0.35], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -14, 
    flip: false,
  });
  
  slider_4 = new visual.Slider({
    win: psychoJS.window, name: 'slider_4',
    startValue: undefined,
    size: [0.05, 0.025], pos: [0.535, 0.35], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -15, 
    flip: false,
  });
  
  slider_5 = new visual.Slider({
    win: psychoJS.window, name: 'slider_5',
    startValue: undefined,
    size: [0.05, 0.025], pos: [(- 0.725), (- 0.28)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -16, 
    flip: false,
  });
  
  slider_6 = new visual.Slider({
    win: psychoJS.window, name: 'slider_6',
    startValue: undefined,
    size: [0.05, 0.025], pos: [(- 0.305), (- 0.28)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -17, 
    flip: false,
  });
  
  slider_7 = new visual.Slider({
    win: psychoJS.window, name: 'slider_7',
    startValue: undefined,
    size: [0.05, 0.025], pos: [0.115, (- 0.28)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -18, 
    flip: false,
  });
  
  slider_8 = new visual.Slider({
    win: psychoJS.window, name: 'slider_8',
    startValue: undefined,
    size: [0.05, 0.025], pos: [0.535, (- 0.28)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -19, 
    flip: false,
  });
  
  slider_9 = new visual.Slider({
    win: psychoJS.window, name: 'slider_9',
    startValue: undefined,
    size: [0.05, 0.025], pos: [(- 0.725), (- 0.9)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -20, 
    flip: false,
  });
  
  slider_10 = new visual.Slider({
    win: psychoJS.window, name: 'slider_10',
    startValue: undefined,
    size: [0.05, 0.025], pos: [(- 0.305), (- 0.9)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -21, 
    flip: false,
  });
  
  slider_11 = new visual.Slider({
    win: psychoJS.window, name: 'slider_11',
    startValue: undefined,
    size: [0.05, 0.025], pos: [0.115, (- 0.9)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -22, 
    flip: false,
  });
  
  slider_12 = new visual.Slider({
    win: psychoJS.window, name: 'slider_12',
    startValue: undefined,
    size: [0.05, 0.025], pos: [0.535, (- 0.9)], ori: 0.0, units: 'norm',
    labels: undefined, fontSize: 0.05, ticks: [0, 1],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -23, 
    flip: false,
  });
  
  imageNext = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNext', units : 'norm', 
    image : 'next.png', mask : undefined,
    anchor : 'center-right',
    ori : 0.0, pos : [0.95, 0], size : [0.2, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -24.0 
  });
  mouseNext = new core.Mouse({
    win: psychoJS.window,
  });
  mouseNext.mouseClock = new util.Clock();
  // Initialize components for Routine "ThankYou"
  ThankYouClock = new util.Clock();
  textThankYou = new visual.TextStim({
    win: psychoJS.window,
    name: 'textThankYou',
    text: 'Thank you for participating in the experiment! Please enter your email below to enter the boba raffle.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textboxEmail = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxEmail',
    text: 'email',
    placeholder: undefined,
    font: 'Arial',
    pos: [0, (- 0.3)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.35, 0.1],  units: 'norm', 
    color: [(- 1.0), (- 1.0), (- 1.0)], colorSpace: 'rgb',
    fillColor: [1.0, 1.0, 1.0], borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  textSpaceExit = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceExit',
    text: 'Press SPACEBAR to exit the experiment.',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_welcome_allKeys;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Welcome.started', globalClock.getTime());
    key_resp_welcome.keys = undefined;
    key_resp_welcome.rt = undefined;
    _key_resp_welcome_allKeys = [];
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(textWelcome);
    WelcomeComponents.push(key_resp_welcome);
    
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }
    
    
    // *key_resp_welcome* updates
    if (t >= 0.0 && key_resp_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_welcome.tStart = t;  // (not accounting for frame time here)
      key_resp_welcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_welcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_welcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_welcome.clearEvents(); });
    }
    
    if (key_resp_welcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_welcome.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_welcome_allKeys = _key_resp_welcome_allKeys.concat(theseKeys);
      if (_key_resp_welcome_allKeys.length > 0) {
        key_resp_welcome.keys = _key_resp_welcome_allKeys[_key_resp_welcome_allKeys.length - 1].name;  // just the last key pressed
        key_resp_welcome.rt = _key_resp_welcome_allKeys[_key_resp_welcome_allKeys.length - 1].rt;
        key_resp_welcome.duration = _key_resp_welcome_allKeys[_key_resp_welcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    for (const thisComponent of WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_welcome.corr, level);
    }
    psychoJS.experiment.addData('key_resp_welcome.keys', key_resp_welcome.keys);
    if (typeof key_resp_welcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_welcome.rt', key_resp_welcome.rt);
        psychoJS.experiment.addData('key_resp_welcome.duration', key_resp_welcome.duration);
        routineTimer.reset();
        }
    
    key_resp_welcome.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_intro_allKeys;
var Intro_BongardComponents;
function Intro_BongardRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Intro_Bongard' ---
    t = 0;
    Intro_BongardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Intro_Bongard.started', globalClock.getTime());
    key_resp_intro.keys = undefined;
    key_resp_intro.rt = undefined;
    _key_resp_intro_allKeys = [];
    // keep track of which components have finished
    Intro_BongardComponents = [];
    Intro_BongardComponents.push(textIntro);
    Intro_BongardComponents.push(imageBongardExample);
    Intro_BongardComponents.push(textSPACEBARContinue);
    Intro_BongardComponents.push(key_resp_intro);
    
    for (const thisComponent of Intro_BongardComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Intro_BongardRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Intro_Bongard' ---
    // get current time
    t = Intro_BongardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textIntro* updates
    if (t >= 0.0 && textIntro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textIntro.tStart = t;  // (not accounting for frame time here)
      textIntro.frameNStart = frameN;  // exact frame index
      
      textIntro.setAutoDraw(true);
    }
    
    
    // *imageBongardExample* updates
    if (t >= 0.0 && imageBongardExample.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageBongardExample.tStart = t;  // (not accounting for frame time here)
      imageBongardExample.frameNStart = frameN;  // exact frame index
      
      imageBongardExample.setAutoDraw(true);
    }
    
    
    // *textSPACEBARContinue* updates
    if (t >= 0.0 && textSPACEBARContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSPACEBARContinue.tStart = t;  // (not accounting for frame time here)
      textSPACEBARContinue.frameNStart = frameN;  // exact frame index
      
      textSPACEBARContinue.setAutoDraw(true);
    }
    
    
    // *key_resp_intro* updates
    if (t >= 0.0 && key_resp_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_intro.tStart = t;  // (not accounting for frame time here)
      key_resp_intro.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_intro.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_intro.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_intro.clearEvents(); });
    }
    
    if (key_resp_intro.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_intro.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_intro_allKeys = _key_resp_intro_allKeys.concat(theseKeys);
      if (_key_resp_intro_allKeys.length > 0) {
        key_resp_intro.keys = _key_resp_intro_allKeys[_key_resp_intro_allKeys.length - 1].name;  // just the last key pressed
        key_resp_intro.rt = _key_resp_intro_allKeys[_key_resp_intro_allKeys.length - 1].rt;
        key_resp_intro.duration = _key_resp_intro_allKeys[_key_resp_intro_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Intro_BongardComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Intro_BongardRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Intro_Bongard' ---
    for (const thisComponent of Intro_BongardComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Intro_Bongard.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_intro.corr, level);
    }
    psychoJS.experiment.addData('key_resp_intro.keys', key_resp_intro.keys);
    if (typeof key_resp_intro.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_intro.rt', key_resp_intro.rt);
        psychoJS.experiment.addData('key_resp_intro.duration', key_resp_intro.duration);
        routineTimer.reset();
        }
    
    key_resp_intro.stop();
    // the Routine "Intro_Bongard" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_instructions_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    key_resp_instructions.keys = undefined;
    key_resp_instructions.rt = undefined;
    _key_resp_instructions_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(textInstructions);
    InstructionsComponents.push(image_correct_1);
    InstructionsComponents.push(image_correct_2);
    InstructionsComponents.push(textFinalInstructions);
    InstructionsComponents.push(key_resp_instructions);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textInstructions* updates
    if (t >= 0.0 && textInstructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textInstructions.tStart = t;  // (not accounting for frame time here)
      textInstructions.frameNStart = frameN;  // exact frame index
      
      textInstructions.setAutoDraw(true);
    }
    
    
    // *image_correct_1* updates
    if (t >= 0.0 && image_correct_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_correct_1.tStart = t;  // (not accounting for frame time here)
      image_correct_1.frameNStart = frameN;  // exact frame index
      
      image_correct_1.setAutoDraw(true);
    }
    
    
    // *image_correct_2* updates
    if (t >= 0.0 && image_correct_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_correct_2.tStart = t;  // (not accounting for frame time here)
      image_correct_2.frameNStart = frameN;  // exact frame index
      
      image_correct_2.setAutoDraw(true);
    }
    
    
    // *textFinalInstructions* updates
    if (t >= 0.0 && textFinalInstructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textFinalInstructions.tStart = t;  // (not accounting for frame time here)
      textFinalInstructions.frameNStart = frameN;  // exact frame index
      
      textFinalInstructions.setAutoDraw(true);
    }
    
    
    // *key_resp_instructions* updates
    if (t >= 0.0 && key_resp_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_instructions.tStart = t;  // (not accounting for frame time here)
      key_resp_instructions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_instructions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instructions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instructions.clearEvents(); });
    }
    
    if (key_resp_instructions.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_instructions.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_instructions_allKeys = _key_resp_instructions_allKeys.concat(theseKeys);
      if (_key_resp_instructions_allKeys.length > 0) {
        key_resp_instructions.keys = _key_resp_instructions_allKeys[_key_resp_instructions_allKeys.length - 1].name;  // just the last key pressed
        key_resp_instructions.rt = _key_resp_instructions_allKeys[_key_resp_instructions_allKeys.length - 1].rt;
        key_resp_instructions.duration = _key_resp_instructions_allKeys[_key_resp_instructions_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_instructions.corr, level);
    }
    psychoJS.experiment.addData('key_resp_instructions.keys', key_resp_instructions.keys);
    if (typeof key_resp_instructions.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_instructions.rt', key_resp_instructions.rt);
        psychoJS.experiment.addData('key_resp_instructions.duration', key_resp_instructions.duration);
        routineTimer.reset();
        }
    
    key_resp_instructions.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'data_randomized.xlsx', (Math.random(12) * 393)),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var gotValidClick;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    t_1.setImage(image1);
    t_2.setImage(image2);
    t_3.setImage(image3);
    t_4.setImage(image4);
    t_5.setImage(image5);
    t_6.setImage(image6);
    t_7.setImage(image7);
    t_8.setImage(image8);
    t_9.setImage(image9);
    t_10.setImage(image10);
    t_11.setImage(image11);
    t_12.setImage(image12);
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
    // setup some python lists for storing info about the mouseNext
    // current position of the mouse:
    mouseNext.x = [];
    mouseNext.y = [];
    mouseNext.leftButton = [];
    mouseNext.midButton = [];
    mouseNext.rightButton = [];
    mouseNext.time = [];
    mouseNext.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(t_1);
    trialComponents.push(t_2);
    trialComponents.push(t_3);
    trialComponents.push(t_4);
    trialComponents.push(t_5);
    trialComponents.push(t_6);
    trialComponents.push(t_7);
    trialComponents.push(t_8);
    trialComponents.push(t_9);
    trialComponents.push(t_10);
    trialComponents.push(t_11);
    trialComponents.push(t_12);
    trialComponents.push(slider_1);
    trialComponents.push(slider_2);
    trialComponents.push(slider_3);
    trialComponents.push(slider_4);
    trialComponents.push(slider_5);
    trialComponents.push(slider_6);
    trialComponents.push(slider_7);
    trialComponents.push(slider_8);
    trialComponents.push(slider_9);
    trialComponents.push(slider_10);
    trialComponents.push(slider_11);
    trialComponents.push(slider_12);
    trialComponents.push(imageNext);
    trialComponents.push(mouseNext);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *t_1* updates
    if (t >= 0.0 && t_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_1.tStart = t;  // (not accounting for frame time here)
      t_1.frameNStart = frameN;  // exact frame index
      
      t_1.setAutoDraw(true);
    }
    
    
    // *t_2* updates
    if (t >= 0.0 && t_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_2.tStart = t;  // (not accounting for frame time here)
      t_2.frameNStart = frameN;  // exact frame index
      
      t_2.setAutoDraw(true);
    }
    
    
    // *t_3* updates
    if (t >= 0.0 && t_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_3.tStart = t;  // (not accounting for frame time here)
      t_3.frameNStart = frameN;  // exact frame index
      
      t_3.setAutoDraw(true);
    }
    
    
    // *t_4* updates
    if (t >= 0.0 && t_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_4.tStart = t;  // (not accounting for frame time here)
      t_4.frameNStart = frameN;  // exact frame index
      
      t_4.setAutoDraw(true);
    }
    
    
    // *t_5* updates
    if (t >= 0.0 && t_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_5.tStart = t;  // (not accounting for frame time here)
      t_5.frameNStart = frameN;  // exact frame index
      
      t_5.setAutoDraw(true);
    }
    
    
    // *t_6* updates
    if (t >= 0.0 && t_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_6.tStart = t;  // (not accounting for frame time here)
      t_6.frameNStart = frameN;  // exact frame index
      
      t_6.setAutoDraw(true);
    }
    
    
    // *t_7* updates
    if (t >= 0.0 && t_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_7.tStart = t;  // (not accounting for frame time here)
      t_7.frameNStart = frameN;  // exact frame index
      
      t_7.setAutoDraw(true);
    }
    
    
    // *t_8* updates
    if (t >= 0.0 && t_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_8.tStart = t;  // (not accounting for frame time here)
      t_8.frameNStart = frameN;  // exact frame index
      
      t_8.setAutoDraw(true);
    }
    
    
    // *t_9* updates
    if (t >= 0.0 && t_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_9.tStart = t;  // (not accounting for frame time here)
      t_9.frameNStart = frameN;  // exact frame index
      
      t_9.setAutoDraw(true);
    }
    
    
    // *t_10* updates
    if (t >= 0.0 && t_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_10.tStart = t;  // (not accounting for frame time here)
      t_10.frameNStart = frameN;  // exact frame index
      
      t_10.setAutoDraw(true);
    }
    
    
    // *t_11* updates
    if (t >= 0.0 && t_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_11.tStart = t;  // (not accounting for frame time here)
      t_11.frameNStart = frameN;  // exact frame index
      
      t_11.setAutoDraw(true);
    }
    
    
    // *t_12* updates
    if (t >= 0.0 && t_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_12.tStart = t;  // (not accounting for frame time here)
      t_12.frameNStart = frameN;  // exact frame index
      
      t_12.setAutoDraw(true);
    }
    
    
    // *slider_1* updates
    if (t >= 0.0 && slider_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_1.tStart = t;  // (not accounting for frame time here)
      slider_1.frameNStart = frameN;  // exact frame index
      
      slider_1.setAutoDraw(true);
    }
    
    
    // *slider_2* updates
    if (t >= 0.0 && slider_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_2.tStart = t;  // (not accounting for frame time here)
      slider_2.frameNStart = frameN;  // exact frame index
      
      slider_2.setAutoDraw(true);
    }
    
    
    // *slider_3* updates
    if (t >= 0.0 && slider_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_3.tStart = t;  // (not accounting for frame time here)
      slider_3.frameNStart = frameN;  // exact frame index
      
      slider_3.setAutoDraw(true);
    }
    
    
    // *slider_4* updates
    if (t >= 0.0 && slider_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_4.tStart = t;  // (not accounting for frame time here)
      slider_4.frameNStart = frameN;  // exact frame index
      
      slider_4.setAutoDraw(true);
    }
    
    
    // *slider_5* updates
    if (t >= 0.0 && slider_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_5.tStart = t;  // (not accounting for frame time here)
      slider_5.frameNStart = frameN;  // exact frame index
      
      slider_5.setAutoDraw(true);
    }
    
    
    // *slider_6* updates
    if (t >= 0.0 && slider_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_6.tStart = t;  // (not accounting for frame time here)
      slider_6.frameNStart = frameN;  // exact frame index
      
      slider_6.setAutoDraw(true);
    }
    
    
    // *slider_7* updates
    if (t >= 0.0 && slider_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_7.tStart = t;  // (not accounting for frame time here)
      slider_7.frameNStart = frameN;  // exact frame index
      
      slider_7.setAutoDraw(true);
    }
    
    
    // *slider_8* updates
    if (t >= 0.0 && slider_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_8.tStart = t;  // (not accounting for frame time here)
      slider_8.frameNStart = frameN;  // exact frame index
      
      slider_8.setAutoDraw(true);
    }
    
    
    // *slider_9* updates
    if (t >= 0.0 && slider_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_9.tStart = t;  // (not accounting for frame time here)
      slider_9.frameNStart = frameN;  // exact frame index
      
      slider_9.setAutoDraw(true);
    }
    
    
    // *slider_10* updates
    if (t >= 0.0 && slider_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_10.tStart = t;  // (not accounting for frame time here)
      slider_10.frameNStart = frameN;  // exact frame index
      
      slider_10.setAutoDraw(true);
    }
    
    
    // *slider_11* updates
    if (t >= 0.0 && slider_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_11.tStart = t;  // (not accounting for frame time here)
      slider_11.frameNStart = frameN;  // exact frame index
      
      slider_11.setAutoDraw(true);
    }
    
    
    // *slider_12* updates
    if (t >= 0.0 && slider_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_12.tStart = t;  // (not accounting for frame time here)
      slider_12.frameNStart = frameN;  // exact frame index
      
      slider_12.setAutoDraw(true);
    }
    
    
    // *imageNext* updates
    if (t >= 0.0 && imageNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNext.tStart = t;  // (not accounting for frame time here)
      imageNext.frameNStart = frameN;  // exact frame index
      
      imageNext.setAutoDraw(true);
    }
    
    // *mouseNext* updates
    if (t >= 0.0 && mouseNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseNext.tStart = t;  // (not accounting for frame time here)
      mouseNext.frameNStart = frameN;  // exact frame index
      
      mouseNext.status = PsychoJS.Status.STARTED;
      mouseNext.mouseClock.reset();
      prevButtonState = mouseNext.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseNext.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseNext.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [imageNext]) {
            if (obj.contains(mouseNext)) {
              gotValidClick = true;
              mouseNext.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouseNext.getPos();
          mouseNext.x.push(_mouseXYs[0]);
          mouseNext.y.push(_mouseXYs[1]);
          mouseNext.leftButton.push(_mouseButtons[0]);
          mouseNext.midButton.push(_mouseButtons[1]);
          mouseNext.rightButton.push(_mouseButtons[2]);
          mouseNext.time.push(mouseNext.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider_1.response', slider_1.getRating());
    psychoJS.experiment.addData('slider_1.rt', slider_1.getRT());
    psychoJS.experiment.addData('slider_2.response', slider_2.getRating());
    psychoJS.experiment.addData('slider_2.rt', slider_2.getRT());
    psychoJS.experiment.addData('slider_3.response', slider_3.getRating());
    psychoJS.experiment.addData('slider_3.rt', slider_3.getRT());
    psychoJS.experiment.addData('slider_4.response', slider_4.getRating());
    psychoJS.experiment.addData('slider_4.rt', slider_4.getRT());
    psychoJS.experiment.addData('slider_5.response', slider_5.getRating());
    psychoJS.experiment.addData('slider_5.rt', slider_5.getRT());
    psychoJS.experiment.addData('slider_6.response', slider_6.getRating());
    psychoJS.experiment.addData('slider_6.rt', slider_6.getRT());
    psychoJS.experiment.addData('slider_7.response', slider_7.getRating());
    psychoJS.experiment.addData('slider_7.rt', slider_7.getRT());
    psychoJS.experiment.addData('slider_8.response', slider_8.getRating());
    psychoJS.experiment.addData('slider_8.rt', slider_8.getRT());
    psychoJS.experiment.addData('slider_9.response', slider_9.getRating());
    psychoJS.experiment.addData('slider_9.rt', slider_9.getRT());
    psychoJS.experiment.addData('slider_10.response', slider_10.getRating());
    psychoJS.experiment.addData('slider_10.rt', slider_10.getRT());
    psychoJS.experiment.addData('slider_11.response', slider_11.getRating());
    psychoJS.experiment.addData('slider_11.rt', slider_11.getRT());
    psychoJS.experiment.addData('slider_12.response', slider_12.getRating());
    psychoJS.experiment.addData('slider_12.rt', slider_12.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouseNext.x) {  psychoJS.experiment.addData('mouseNext.x', mouseNext.x[0])};
    if (mouseNext.y) {  psychoJS.experiment.addData('mouseNext.y', mouseNext.y[0])};
    if (mouseNext.leftButton) {  psychoJS.experiment.addData('mouseNext.leftButton', mouseNext.leftButton[0])};
    if (mouseNext.midButton) {  psychoJS.experiment.addData('mouseNext.midButton', mouseNext.midButton[0])};
    if (mouseNext.rightButton) {  psychoJS.experiment.addData('mouseNext.rightButton', mouseNext.rightButton[0])};
    if (mouseNext.time) {  psychoJS.experiment.addData('mouseNext.time', mouseNext.time[0])};
    if (mouseNext.clicked_name) {  psychoJS.experiment.addData('mouseNext.clicked_name', mouseNext.clicked_name[0])};
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var ThankYouComponents;
function ThankYouRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ThankYou' ---
    t = 0;
    ThankYouClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ThankYou.started', globalClock.getTime());
    textboxEmail.setText('email');
    textboxEmail.refresh();
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    ThankYouComponents = [];
    ThankYouComponents.push(textThankYou);
    ThankYouComponents.push(textboxEmail);
    ThankYouComponents.push(textSpaceExit);
    ThankYouComponents.push(key_resp);
    
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ThankYouRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ThankYou' ---
    // get current time
    t = ThankYouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textThankYou* updates
    if (t >= 0.0 && textThankYou.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textThankYou.tStart = t;  // (not accounting for frame time here)
      textThankYou.frameNStart = frameN;  // exact frame index
      
      textThankYou.setAutoDraw(true);
    }
    
    
    // *textboxEmail* updates
    if (t >= 0.0 && textboxEmail.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxEmail.tStart = t;  // (not accounting for frame time here)
      textboxEmail.frameNStart = frameN;  // exact frame index
      
      textboxEmail.setAutoDraw(true);
    }
    
    
    // *textSpaceExit* updates
    if (t >= 0.0 && textSpaceExit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpaceExit.tStart = t;  // (not accounting for frame time here)
      textSpaceExit.frameNStart = frameN;  // exact frame index
      
      textSpaceExit.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ThankYouRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ThankYou' ---
    for (const thisComponent of ThankYouComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ThankYou.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textboxEmail.text',textboxEmail.text)
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
