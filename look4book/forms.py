from django import forms

class FormsBook(forms.Form):
    
    name_opt = forms.BooleanField(initial=True, required=False, label='By Name')
    author_opt = forms.BooleanField(initial=False, required=False, label='By Author')
    # options = forms.MultipleChoiceField(label='some label',  choices=(('happy','Happy'),('sad','Sad')),
    #   widget=forms.CheckboxSelectMultiple(attrs={'checked' : 'checked'}))
    
    book_name = forms.CharField(initial="The lord of the rings", required=True, label="Write the book's name separated by pipe '|'")
    author_name = forms.CharField(required=False, label="Write the author's name separated by pipe '|'")
    
    def clean_terms(self):
         if self.cleaned_data["name_opt"] == True:
             raise forms.ValidationError(
                 "You have to accept terms&conditions to complete registration"
             )