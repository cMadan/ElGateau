---
title: 'ElGateau: A Library for Using the Elgato Stream Deck for Experimental Psychology Research'
tags:
  - psychology
  - experiments
  - Python
authors:
  - name: Christopher R. Madan
    orcid: 0000-0003-3228-6501
    affiliation: 1
affiliations:
 - name: School of Psychology, University of Nottingham
   index: 1
date: 23 October 2018
bibliography: paper.bib
---

# Background

A number of open-source packages exist for implementing psychology experiments, particularly in Python, including PsychoPy [@psychopy], OpenSesame [@opensesame], Expyriment [@expyriment], and Neuropsydia [@neuropsydia]. These packages generally use standard computer hardware (monitor, keyboard, mouse) to display stimuli and collect behavioural responses. The use of novel hardware, however, requires novel software packages. This package, ElGateau, has been developed to interact with a 15-key input/output device called the Elgato Stream Deck. This device can be used to present stimuli or key labels, as well as collect button responses.


# Overview

In experimental psychology research, we often ask participants to press specific keys to correspond to responses in the experiment. For instance, one key for 'old' and another for 'new' in an old/new recognition memory test, 'word' and 'nonword' in a lexical decision task, or red/green/blue in a Stroop test. Sometimes we put stickers over keys on a keyboard to remind participants of these key mappings, but often they are merely included as part of the experiment instructions. What if we could easily just write 'old' and 'new' on the keys themselves? This approach could additionally lead to more manageable (and automatically logged) counterbalancing across participants, but we could further readily counterbalance key mappings across trials (or blocks of trials) if desired. In some cases, a whole experiment could be implemented on an LCD keypad. This project is the infrastructure for implementing experiments with an LCD keypad called the Elgato Stream Deck.

The Elgato Stream Deck is effectively a USB interface device with an array of 3x5 keys. Each key has an LCD display (72x72 px resolution) on the face of it, and has physical buttons that can be pressed and released. This project, 'ElGateau' is a Python API for using the Stream Deck device (updating displays, listen for button presses), along with supporting functionality (e.g., writing text to the display, 'preprocessing' images before writing to display, monitoring for specific button presses). On top of this base functionality, the ElGateau also includes higher-level functions to support using this device in experimental psychology research, such as logging display updates and key presses as well as storing internal representations of the current displays on the device. A 'developer mode' is also included to allow for experiment development without needing the Stream Deck device on hand.

![Elgato Stream Deck device, showing memory game demo.](https://raw.githubusercontent.com/cMadan/ElGateau/master/paper/device_photo.png)

# References
