# from django import forms
# from .models import StaffMetting, StaffUser

# class StaffMeetingForm(forms.ModelForm):
#     """
#     Formulaire pour créer un rendez-vous avec un membre du staff.
#     """

#     staff = forms.ModelChoiceField(
#         queryset=StaffUser.objects.all(),
#         label="Choisir un membre du staff",
#         help_text="Sélectionnez le membre du staff avec qui vous souhaitez prendre rendez-vous."
#     )

#     class Meta:
#         model = StaffMetting
#         fields = ['staff', 'start_time', 'end_time', 'subject', 'notes']
#         widgets = {
#             'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#             'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }
#         labels = {
#             'start_time': "Date et heure de début",
#             'end_time': "Date et heure de fin",
#             'subject': "Sujet du rendez-vous",
#             'notes': "Notes supplémentaires",
#         }

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)  # Récupération de l'utilisateur passé en paramètre
#         super().__init__(*args, **kwargs)

#         # Empêcher les utilisateurs staff de créer des rendez-vous (facultatif)
#         if user and user.is_staff:
#             self.fields['staff'].queryset = StaffUser.objects.none()

#     def clean_end_time(self):
#         start_time = self.cleaned_data.get('start_time')
#         end_time = self.cleaned_data.get('end_time')

#         if start_time and end_time and end_time <= start_time:
#             raise forms.ValidationError("L'heure de fin doit être postérieure à l'heure de début.")
        
#         return end_time