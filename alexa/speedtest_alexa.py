# -*- coding: utf-8 -*-
import logging

from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement

import subprocess

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

TYPE_KEY = "Type"

@ask.launch
def launch():
    card_title = render_template('card_title')
    question_text = render_template('welcome')
    reprompt_text = render_template('welcome_reprompt')
    return question(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)

@ask.intent('CurrentSpeedIntent', mapping={'type': 'Type'})
def my_type_is(type):
    card_title = render_template('card_title')
    if type is not None:
        session.attributes[TYPE_KEY] = type
        shellCall = './speedtest.sh ' + type
        speed_text = render_template('known_type', currentSpeed=subprocess.check_output([shellCall], shell=True), type=type);
        return statement(speed_text).simple_card(card_title, speed_text)
    else:
        question_text = render_template('unknown_type')
        reprompt_text = render_template('unknown_type_reprompt')
        return statement(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)

@ask.session_ended
def session_ended():
    return "", 200

if __name__ == '__main__':
    app.run(debug=True)
