# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Comment(Page):

    form_model = models.Player
    form_fields = ['comment']

    def is_displayed(self):
        return self.player.id_in_group < 5

class Rulemaking(Page):

    form_model = models.Group
    form_fields = ['minimum_contribution_rule']

    def is_displayed(self):
        return self.player.id_in_group == 5

class Contribute(Page):

    form_model = models.Player
    form_fields = ['contribution']

    def is_displayed(self):
        return self.player.id_in_group < 5

class WaitforPlayers(WaitPage):
    pass

class WaitforRule(WaitPage):
    pass

class ResultsWaitPage(WaitPage):

    title_text = "Waiting For All Group Member Input"
    body_text = ""

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass

class Contribute2(Page):

    form_model = models.Player
    form_fields = ['contribution2']

    def is_displayed(self):
        return self.player.id_in_group < 5

class ResultsWaitPage2(WaitPage):
    title_text = "Waiting For All Group Member Input"
    body_text = ""

    def after_all_players_arrive(self):
        self.group.set_payoffs2()

class Results2(Page):
    pass

class Contribute3(Page):

    form_model = models.Player
    form_fields = ['contribution3']

    def is_displayed(self):
        return self.player.id_in_group < 5

class ResultsWaitPage3(WaitPage):
    title_text = "Waiting For All Group Member Input"
    body_text = ""

    def after_all_players_arrive(self):
        self.group.set_payoffs3()

class Results3(Page):
    pass

class Contribute4(Page):

    form_model = models.Player
    form_fields = ['contribution4']

    def is_displayed(self):
        return self.player.id_in_group < 5

class ResultsWaitPage4(WaitPage):
    title_text = "Waiting For All Group Member Input"
    body_text = ""

    def after_all_players_arrive(self):
        self.group.set_payoffs4()

class Results4(Page):
    pass

class Contribute5(Page):

    form_model = models.Player
    form_fields = ['contribution5']

    def is_displayed(self):
        return self.player.id_in_group < 5

class ResultsWaitPage5(WaitPage):
    title_text = "Waiting For All Group Member Input"
    body_text = ""

    def after_all_players_arrive(self):
        self.group.set_payoffs5()

class Results5(Page):
    pass

page_sequence = [
    Comment,
    WaitforPlayers,
    Rulemaking,
    WaitforRule,
    Contribute,
    ResultsWaitPage,
    Results,
    Contribute2,
    ResultsWaitPage2,
    Results2,
    Contribute3,
    ResultsWaitPage3,
    Results3,
    Contribute4,
    ResultsWaitPage4,
    Results4,
    Contribute5,
    ResultsWaitPage5,
    Results5,
]
