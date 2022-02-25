from django.views.generic import ListView
from django.forms.models import model_to_dict
from django.contrib import messages
from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from django.forms import modelformset_factory

from .models import Cdchanger
from . import forms


class CdchangerListView(ListView):
    model = Cdchanger


# multistep wizard form for cdchanger -----------------------------------BEGIN
class CdchangerWizard(SessionWizardView):
    # forms
    FORMS = [
        ("step1", forms.CdchangerWizardForm1),
        ("step2", forms.CdchangerWizardForm2),
    ]
    # form templates
    TEMPLATES = {
        "step1": "cdchanger/cdchanger_wizard/step1.html",
        "step2": "cdchanger/cdchanger_wizard/step2.html",
    }

    def get_template_names(self):
        return [CdchangerWizard.TEMPLATES[self.steps.current]]

    def get_form(self, step=None, data=None, files=None):
        form = super(CdchangerWizard, self).get_form(step, data, files)

        if step is None:
            step = self.steps.current

        if step == 'step1':
            pass
        elif step == 'step2':
            print('------get_form---')
            pass

        return form

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)

        if self.steps.current == 'step1':
            pass
        elif self.steps.current == 'step2':
            context['disks']= forms.DiskFormSet(
                self.storage.get_step_data('step2')
            )
        print('----get_context_data---')
        return context

    def get_form_initial(self, step):
        if 'pk' in self.kwargs:
            cdchanger_id = self.kwargs['pk']
            cdchanger = Cdchanger.objects.get(pk=cdchanger_id)
            return model_to_dict(cdchanger)
        else:
            if step == 'step1':
                pass
            elif step == 'step2':
                pass
            return self.initial_dict.get(step, {})

    def get_form_instance(self, step):
        if 'pk' in self.kwargs:
            pass
        else:
            if step == 'step1':
                pass
            elif step == 'step2':
                # return self.instance_dict.get(step, Disk())
                pass
        return self.instance_dict.get(step, None)

    def post(self, *args, **kwargs):
        go_to_step = self.request.POST.get('wizard_goto_step', None)  # get the step name
        form = self.get_form(data=self.request.POST)
        current_index = self.get_step_index(self.steps.current)
        goto_index = self.get_step_index(go_to_step)

        if current_index > goto_index:
            if form.is_valid():
                self.storage.set_step_data(self.steps.current, self.process_step(form))

        if form.is_valid():
            pass
        else:
            # print('-- form errors:', form.errors)
            # print('-- form total_error_count:', form.total_error_count())
            pass

        return super(CdchangerWizard, self).post(*args, **kwargs)

    def done(self, form_list, form_dict, **kwargs):
        print('-----------done--------------')
        for form in form_list:
            if form.is_valid():
                # import pdb; pdb.set_trace()
                pass

        # save data from all of the steps
        cdchanger = Cdchanger(
            name=form_dict['step1'].cleaned_data['name'],
            capacity=form_dict['step1'].cleaned_data['capacity'],
        )
        # if pk exists then it is UPDATE mode
        if 'pk' in self.kwargs:
            cdchanger.id = self.kwargs['pk']

        cdchanger.save()

        # # disks set
        # disk_forms = form_dict['form2'].cleaned_data['disks']

        # for disk_form in disk_forms:
        #     disk = Disk(
        #         cdchanger=cdchanger,
        #         title=disk_form.form_dict['form2'].cleaned_data['title'],
        #         default=disk_form.form_dict['form2'].cleaned_data['default'],
        #     )
        #     disk.save()

        # cdchanger.save()
        success_message = 'Cdchanger successfully saved.'

        messages.success(self.request, success_message)
        return redirect('cdchangers')
# multistep wizard form for cdchanger -----------------------------------END
