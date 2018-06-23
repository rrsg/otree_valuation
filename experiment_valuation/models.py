from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Non-market valuation experiment
"""

class Constants(BaseConstants):
    name_in_url = 'experiment_valuation'
    players_per_group = None
    num_rounds = 1

    endowment = c(100)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    code = models.IntegerField(max=999999)

    ## Voluntary contribution - Single
    contributionVS1 = models.CurrencyField(min=0, max=Constants.endowment)

    ## Voluntary contribution - Joint
    contributionVJ1 = models.CurrencyField(min=0, max=Constants.endowment)
    contributionVJ2 = models.CurrencyField(min=0, max=Constants.endowment)

    ## Compulsory Contribution - Single
    contributionCS1 = models.CurrencyField(choices=currency_range(c(0), c(Constants.endowment), c(10)))

    ## Compulsory Contribution - Joint
    contributionCJ1 = models.CurrencyField(choices=currency_range(c(0), c(Constants.endowment), c(10)))
    contributionCJ2 = models.CurrencyField(choices=currency_range(c(0), c(Constants.endowment), c(10)))

    ## Joint Choice
    contributionJC1 = models.IntegerField(
        choices=[
            [1, 'Program A'],
            [2, 'Program B'],
        ]
    )
    ## Learning Check
    check1 = models.IntegerField(
        choices=[
            [1, '(A) Seaweeds are edible raw while seagrasses will need to be cooked first'],
            [2, '(B) Seaweeds are flowering plants while seagrass are not'],
            [3, '(C) Seaweeds have true stems and true leaves while seagrasses do not'],
            [4, '(D) Seaweeds contribute to reducing greenhouse gases while seagrasses do not'],
        ]
    )

    ## Demographic questionnaires
    age = models.IntegerField(
        label='How old are you?',
    )

    sex = models.IntegerField(
        choices=[
            [1, 'Male'],
            [2, 'Female'], ],
        label='What is your sex?',
        )

    degree = models.StringField(
        label='What is your degree program? [Please do not abbreviate, i.e. Bachelors of Science in Marine Science)',
    )

    residence = models.StringField(
        label='Where do you currently live? (City/Municipality, Province)',
    )

    born = models.StringField(
        label='Where were you born? (City/Municipality, Province)',
    )

    educ = models.IntegerField(
        label='How many years have you been studying? (excluding Nursery/Pre-K12)',
    )

    held = models.IntegerField(
        label='Have you ever repeated a grade or held back a grade?',
        choices=[
            [1, 'Yes'],
            [2, 'No'], ],
        )

    educfather = models.IntegerField(
        label='What was the highest educational attainment of your father?',
        choices=[
            [1, 'No formal schooling'],
            [2, 'Primary school attended but not completed (Grade 1 -- Grade 6)'],
            [3, 'Primary school completed (Finished Grade 6)'],
            [4, 'Lower secondary education attended (1st Year to 2nd Year High school)'],
            [5, 'Upper secondary education attended (3rd Year to 4th Year High school)'],
            [6, 'Post secondary education (technical/vocational)'],
            [7, 'University education -- undergraduate/bachelors'],
            [7, 'Post-graduate - masters/doctorate/professional school (law, medicine, dentistry'],
        ])

    educmother = models.IntegerField(
        label='What was the highest educational attainment of your mother?',
        choices=[
            [1, 'No formal schooling'],
            [2, 'Primary school attended but not completed (Grade 1 -- Grade 6)'],
            [3, 'Primary school completed (Finished Grade 6)'],
            [4, 'Lower secondary education attended (1st Year to 2nd Year High school)'],
            [5, 'Upper secondary education attended (3rd Year to 4th Year High school)'],
            [6, 'Post secondary education (technical/vocational)'],
            [7, 'University education -- undergraduate/bachelors'],
            [7, 'Post-graduate - masters/doctorate/professional school (law, medicine, dentistry'],
        ])

    job = models.IntegerField(
        label='Do you have a part-time job?',
        choices=[
            [1, 'Yes'],
            [2, 'No'],
        ])

    jobhrs = models.IntegerField(
        label='How many hours a week do you work?',
    )
    headhh = models.IntegerField(
        label='Who is the head of the household?',
        choices=[
            [1, 'Mother'],
            [2, 'Father'],
            [3, 'Older/Younger Sibling'],
            [4, 'Self'],
            [5, 'Other'],
        ])

    headworking = models.IntegerField(
        label='Has the head of the household been employed in the last six months?',
        choices=[
            [1, 'Yes'],
            [2, 'No'],
        ])

    headmembers = models.IntegerField(
        label='Including the household head, how many members of your family have been employed in the last six months?',
    )

    jobfather = models.StringField(
        label='What is your fathers occupation?',
    )
    jobmother = models.StringField(
        label='What is your mothers occupation?',
    )

    expdaily = models.IntegerField(
        label='On average, how much do you spend on your needs and wants per day?',
    )
    expdailyfood = models.IntegerField(
        label='On average, how much do you spend on food per day?',
    )

    expdailytrans = models.IntegerField(
        label='On average, how much do you spend on transportation per day?',
    )

    expdailyhousing = models.IntegerField(
        label='On average, how much do you spend on housing per day?',
    )

    def make_field(label):
        return models.IntegerField(
            choices=[
                [1, 'Never'],
                [2, 'Seldom'],
                [3, 'Sometimes'],
                [4, 'Often'],
                [5, 'Always'], ],
            label=label,
            widget=widgets.RadioSelectHorizontal,
        )

    trust1 = make_field('[D7.A.1 Trust in government] How much do you trust the local government of New Washington to do what is best for its citizens?')
    trust2 = make_field('[D7.A.2 Trust in government] How much do you trust the local government of New Washington to make decisions in a fair way?')
    trust3 = make_field('[D7.A.3 Trust in government] How much do you trust the local government of New Washington to do what is best for its citizens?')
    trust4 = make_field('[D7.A.4 Trust in government]  How much do you trust the government of New Washington to use tax revenues for the welfare of the community?')

