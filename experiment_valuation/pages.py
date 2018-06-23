from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    form_model = 'player'
    form_fields = ['code']

class Voluntary_Contribution(Page):
    form_model = 'player'
    form_fields = ['contributionVS1']

    def before_next_page(self):
        self.player.payoff = Constants.endowment - self.player.contributionVS1

class Voluntary_Contribution_Joint(Page):
    form_model = 'player'
    form_fields = ['contributionVJ1', 'contributionVJ2']

    def error_message(self, values):
        print('values is', values)
        if values["contributionVJ1"] + values["contributionVJ2"] > 100:
            return 'The total of both amounts must be less than or equal to 100'

class Video(Page):
    pass

class Comprehension(Page):
    form_model = 'player'
    form_fields = ['check1']

class Comp_Contribution_Single(Page):
    form_model = 'player'
    form_fields = ['contributionCS1']

class Comp_Contribution_Joint(Page):
    form_model = 'player'
    form_fields = ['contributionCJ1', 'contributionCJ2']

    def error_message(self, values):
        print('values is', values)
        if values["contributionCJ1"] + values["contributionCJ2"] > 100:
            return 'The total of both amounts must be less than or equal to 100'

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'sex',
                   'degree',
                   'residence',
                   'born',
                   'educ',
                   'held',
                   'educfather',
                   'educmother',
                   'job',
                   'jobhrs',
                   'headhh',
                   'headworking',
                   'headmembers',
                   'jobfather',
                   'jobmother',
                   'expdaily',
                   'expdailyfood',
                   'expdailytrans',
                   'expdailyhousing',
                   'trust1',
                   'trust2',
                   'trust3',
                   'trust4',
                   ]

class Results(Page):
    pass

page_sequence = [
    Instructions,
    Voluntary_Contribution,
    Voluntary_Contribution_Joint,
    Video,
    Comprehension,
    Comp_Contribution_Single,
    Comp_Contribution_Joint,
    Demographics,
    Results
]
