from django import forms

from cdchanger.utils.formsetcustomlayout import SimpleFormset
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Submit, HTML, Div, \
        Fieldset
from .models import Cdchanger, Disk


# wizard forms - for Cdchanger ----------------------------------BEGIN

# step1
class CdchangerWizardForm1(forms.ModelForm):
    class Meta:
        model = Cdchanger
        fields = ('name', 'capacity')


class CdchangerWizardForm2(forms.ModelForm):
    class Meta:
        model = Disk
        fields = ('title', 'default')

    def __init__(self, *args, **kwargs):
        super(CdchangerWizardForm2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Fieldset('Add disks', SimpleFormset('disks')),
            ),
            HTML('<hr>'),
            Row(
                HTML('<button class="btn btn-secondary btnPrevious" ' +
                     'name="wizard_goto_step" type="submit" ' +
                     'id="goto_step1_id" ' +
                     'value="{{ wizard.steps.prev }}">Back</button>'),
                HTML('&nbsp;'),
                Submit('submit', 'Submit', css_id='next_submit_btn'),
                css_class='form-group'
            ),
        )


class DiskForm(forms.ModelForm):
    class Meta:
        model = Disk
        fields = ['title', 'default']


DiskFormSet = forms.modelformset_factory(Disk, form=DiskForm, extra=1)
