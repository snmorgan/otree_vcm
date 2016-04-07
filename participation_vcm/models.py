# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

import itertools

author = 'Stephen Morgan'

doc = """
DRAFT Participation and Compliance Game
"""

class Constants(BaseConstants):
    name_in_url = 'participation_vcm'
    players_per_group = 5
    num_rounds = 5

    endowment = c(25)
    efficiency_factor = .4


class Subsession(BaseSubsession):

    # summary indicator for player's type
    type = models.CharField()

    def before_session_starts(self):

        # in first round number, randomly assign people to roles at the rate of A, B, C, D, E
        if self.round_number == 1:
            players = self.get_players()
            random.shuffle(players)
            treatments = itertools.cycle(['A', 'B', 'C', 'D', 'E'])
            for p in players:
                p.participant.vars['type'] = next(treatments)

            players = self.get_players()
            random.shuffle(players)

            A_players = [p for p in players if p.participant.vars['type'] == 'A']
            B_players = [p for p in players if p.participant.vars['type'] == 'B']
            C_players = [p for p in players if p.participant.vars['type'] == 'C']
            D_players = [p for p in players if p.participant.vars['type'] == 'D']
            E_players = [p for p in players if p.participant.vars['type'] == 'E']


            group_matrix = []
            num_groups = int(len(players) / 5)

            # Note that by this construction everyone who is an A player will have a playerID of 1,
            # B is 2,
            # C is 3,
            # D is 4
            # E is 5

            for i in range(num_groups):
                new_group = [
                    A_players.pop(),
                    B_players.pop(),
                    C_players.pop(),
                    D_players.pop(),
                    E_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_groups(group_matrix)


        elif self.round_number == 2:

            players = self.get_players()
            random.shuffle(players)

            A_players = [p for p in players if p.participant.vars['type'] == 'A']
            B_players = [p for p in players if p.participant.vars['type'] == 'B']
            C_players = [p for p in players if p.participant.vars['type'] == 'C']
            D_players = [p for p in players if p.participant.vars['type'] == 'D']
            E_players = [p for p in players if p.participant.vars['type'] == 'E']

            group_matrix = []
            num_groups = int(len(players) / 5)

            for i in range(num_groups):
                new_group = [
                    E_players.pop(),
                    A_players.pop(),
                    B_players.pop(),
                    C_players.pop(),
                    D_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_groups(group_matrix)

        elif self.round_number == 3:

            players = self.get_players()
            random.shuffle(players)

            A_players = [p for p in players if p.participant.vars['type'] == 'A']
            B_players = [p for p in players if p.participant.vars['type'] == 'B']
            C_players = [p for p in players if p.participant.vars['type'] == 'C']
            D_players = [p for p in players if p.participant.vars['type'] == 'D']
            E_players = [p for p in players if p.participant.vars['type'] == 'E']

            group_matrix = []
            num_groups = int(len(players) / 5)

            for i in range(num_groups):
                new_group = [
                    D_players.pop(),
                    E_players.pop(),
                    A_players.pop(),
                    B_players.pop(),
                    C_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_groups(group_matrix)

        elif self.round_number == 4:

            players = self.get_players()
            random.shuffle(players)

            A_players = [p for p in players if p.participant.vars['type'] == 'A']
            B_players = [p for p in players if p.participant.vars['type'] == 'B']
            C_players = [p for p in players if p.participant.vars['type'] == 'C']
            D_players = [p for p in players if p.participant.vars['type'] == 'D']
            E_players = [p for p in players if p.participant.vars['type'] == 'E']

            group_matrix = []
            num_groups = int(len(players) / 5)

            for i in range(num_groups):
                new_group = [
                    C_players.pop(),
                    D_players.pop(),
                    E_players.pop(),
                    A_players.pop(),
                    B_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_groups(group_matrix)

        elif self.round_number == 5:

            players = self.get_players()
            random.shuffle(players)

            A_players = [p for p in players if p.participant.vars['type'] == 'A']
            B_players = [p for p in players if p.participant.vars['type'] == 'B']
            C_players = [p for p in players if p.participant.vars['type'] == 'C']
            D_players = [p for p in players if p.participant.vars['type'] == 'D']
            E_players = [p for p in players if p.participant.vars['type'] == 'E']

            group_matrix = []
            num_groups = int(len(players) / 5)

            for i in range(num_groups):
                new_group = [
                    B_players.pop(),
                    C_players.pop(),
                    D_players.pop(),
                    E_players.pop(),
                    A_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_groups(group_matrix)

    pass


class Group(BaseGroup):

    total_contribution = models.CurrencyField()
    total_contribution2 = models.CurrencyField()
    total_contribution3 = models.CurrencyField()
    total_contribution4 = models.CurrencyField()
    total_contribution5 = models.CurrencyField()

    individual_share = models.CurrencyField()
    individual_share2 = models.CurrencyField()
    individual_share3 = models.CurrencyField()
    individual_share4 = models.CurrencyField()
    individual_share5 = models.CurrencyField()

    minimum_contribution_rule = models.CurrencyField(min=0, max=Constants.endowment)

    def group_comments(self):
        return list(p.comment for p in self.get_players())

    def set_payoffs(self):

        for p in self.get_players():
            if p.contribution is None:
                p.contribution = 0

        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor

        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share

        rulemaker =  self.get_player_by_role('Rulemaker')
        rulemaker.payoff = 25

    pass

    def set_payoffs2(self):

        for p in self.get_players():
            if p.contribution2 is None:
                p.contribution2 = 0

        self.total_contribution2 = sum([p.contribution2 for p in self.get_players()])
        self.individual_share2 = self.total_contribution2 * Constants.efficiency_factor

        for p in self.get_players():
            p.payoff2 = Constants.endowment - p.contribution2 + self.individual_share2

        rulemaker = self.get_player_by_role('Rulemaker')
        rulemaker.payoff2 = 25

    pass

    def set_payoffs3(self):

        for p in self.get_players():
            if p.contribution3 is None:
                p.contribution3 = 0

        self.total_contribution3 = sum([p.contribution3 for p in self.get_players()])
        self.individual_share3 = self.total_contribution3 * Constants.efficiency_factor

        for p in self.get_players():
            p.payoff3 = Constants.endowment - p.contribution3 + self.individual_share3

        rulemaker = self.get_player_by_role('Rulemaker')
        rulemaker.payoff3 = 25

    pass

    def set_payoffs4(self):

        for p in self.get_players():
            if p.contribution4 is None:
                p.contribution4 = 0

        self.total_contribution4 = sum([p.contribution4 for p in self.get_players()])
        self.individual_share4 = self.total_contribution4 * Constants.efficiency_factor

        for p in self.get_players():
            p.payoff4 = Constants.endowment - p.contribution4 + self.individual_share4

        rulemaker = self.get_player_by_role('Rulemaker')
        rulemaker.payoff4 = 25

    pass

    def set_payoffs5(self):

        for p in self.get_players():
            if p.contribution5 is None:
                p.contribution5 = 0

        self.total_contribution5 = sum([p.contribution5 for p in self.get_players()])
        self.individual_share5 = self.total_contribution5 * Constants.efficiency_factor

        for p in self.get_players():
            p.payoff5 = Constants.endowment - p.contribution5 + self.individual_share5

        rulemaker = self.get_player_by_role('Rulemaker')
        rulemaker.payoff5 = 25

    pass

class Player(BasePlayer):

    contribution = models.CurrencyField(min=0, max=Constants.endowment)
    contribution2 = models.CurrencyField(min=0, max=Constants.endowment)
    contribution3 = models.CurrencyField(min=0, max=Constants.endowment)
    contribution4 = models.CurrencyField(min=0, max=Constants.endowment)
    contribution5 = models.CurrencyField(min=0, max=Constants.endowment)

    comment = models.CharField()

    payoff2 = models.CurrencyField()
    payoff3 = models.CurrencyField()
    payoff4 = models.CurrencyField()
    payoff5 = models.CurrencyField()

    def role(self):
        if self.id_in_group == 1:
            return 'Participant'
        if self.id_in_group == 2:
            return 'Participant'
        if self.id_in_group == 3:
            return 'Participant'
        if self.id_in_group == 4:
            return 'Participant'
        if self.id_in_group == 5:
            return 'Rulemaker'

    pass
