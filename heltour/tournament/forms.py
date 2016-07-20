from django import forms

from .models import PREVIOUS_SEASON_ALTERNATE_OPTIONS, ALTERNATE_PREFERENCE_OPTIONS

YES_NO_OPTIONS = (
    (True, 'Yes'),
    (False, 'No'),
)

class RegistrationForm(forms.Form):
    lichess_username = forms.CharField(label='Your Lichess Username', max_length=255)
    slack_username = forms.CharField(label='Your Slack Username (Please, it should be the same). If you aren\'t on our Slack yet, please fill in N/A.', max_length=255)
    email = forms.EmailField(label='Your email', max_length=255)
    
    classical_rating = forms.IntegerField(label='Your Lichess Classical Rating. (####)')
    peak_classical_rating = forms.IntegerField(label='Your highest peak Lichess Classical Rating (####)')
    has_played_20_games = forms.TypedChoiceField(label='Have you played more than 20 games of classical chess on Lichess? (If no, this must be fulfilled ASAP).', choices=YES_NO_OPTIONS, widget=forms.RadioSelect, coerce=lambda x: x == 'True')
    already_in_slack_group = forms.TypedChoiceField(label='Are you on our Slack group?', choices=YES_NO_OPTIONS, widget=forms.RadioSelect, coerce=lambda x: x == 'True')
    previous_season_alternate = forms.ChoiceField(label='Were you an alternate for the previous season?', choices=PREVIOUS_SEASON_ALTERNATE_OPTIONS, widget = forms.RadioSelect)
    can_commit = forms.TypedChoiceField(label='Are you able to commit to 1 Long Time Control Game (45|45, currently) of Classical Chess on Lichess.org per week?', choices=YES_NO_OPTIONS, widget=forms.RadioSelect, coerce=lambda x: x == 'True')
    friends = forms.CharField(required=False, label='Are there any friends you would like to be paired with? (Note: All players must register. All players must join Slack. All players should also request each other).', max_length=1023)
    agreed_to_rules = forms.TypedChoiceField(label='Do you agree to the rules of the 45|45 League? https://docs.google.com/document/d/1nRzexE_dNmqc-XiE48JxkVeW3oZjAPqUAmYltVPEbrU/edit', choices=YES_NO_OPTIONS, widget=forms.RadioSelect, coerce=lambda x: x == 'True')
    alternate_preference = forms.ChoiceField(label='Are you interested in being an alternate or a full time player?', choices=ALTERNATE_PREFERENCE_OPTIONS, widget = forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        season = kwargs.pop('season')
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        weeks = [(i, 'Week %s' % i) for i in range(1, season.rounds + 1)]
        self.fields['weeks_unavailable'] = forms.MultipleChoiceField(required=False, label='Are there any weeks you would be unable to play?', choices=weeks, widget=forms.CheckboxSelectMultiple)
        self.fields['season_id'] = forms.IntegerField(widget=forms.HiddenInput)
        self.fields['season_id'].initial = season.id