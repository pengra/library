from django import forms


class KioskForm(forms.Form):
    "A form for /dashboard/kiosk/ editing"
    name = forms.CharField()
    school = forms.CharField()
    active = forms.CharField()
    auth_code = forms.CharField()
    pk = forms.IntegerField()
    proxy_method = forms.CharField(required=False)


class LoginForm(forms.Form):
    "A form for an AJAX hit from a kiosk."
    mode = forms.CharField()
    return_value = forms.CharField()
    log_pk = forms.IntegerField(required=False)

    def is_valid_card_number(self):
        "Is this a card number the user just typed in?"
        is_valid = self.is_valid()
        is_box = self.cleaned_data.get('mode') == '_box'
        is_numeric = self.cleaned_data.get('return_value', '').isdigit()
        return is_valid and is_box and is_numeric

    def is_valid_email(self):
        "Is this an email this person just typed in?"
        is_valid = self.is_valid()
        is_box = self.cleaned_data.get('mode') == '_box'
        contains_at = "@" in self.cleaned_data.get('return_value', '')
        contains_period = '.' in self.cleaned_data.get('return_value', '')
        return is_valid and is_box and contains_at and contains_period

    def is_valid_name(self):
        "Is this a valid name this person just typed in?"
        is_one_space_min = len(self.cleaned_data.get(
            'return_value', '').split(' ')) > 1
        return self.is_valid_nickname() and is_one_space_min

    def is_valid_nickname(self):
        "is this a valid nickname this person just yped in?"
        is_valid = self.is_valid()
        is_box = self.cleaned_data.get('mode') == '_box'
        is_text = self.cleaned_data.get('return_value', '1').replace(
            ' ', '').replace('-', '').isalpha()
        return is_valid and is_box and is_text

    def is_valid_poll(self):
        "Is this a valid poll option coming through?"
        is_valid = self.is_valid()
        is_poll = self.cleaned_data.get('mode') == '_poll'
        contains_pk = 'log_pk' in self.data
        return is_valid and is_poll and contains_pk


class PollMangementForm(forms.Form):
    "Form for librarian/teacher managing the polls."
    question = forms.CharField()
    answers = forms.CharField()
    pk = forms.IntegerField()
    method_proxy = forms.CharField()


class BugSplatForm(forms.Form):
    "Form for bug reports/questions."
    report_type = forms.CharField()
    title = forms.CharField()
    content = forms.CharField(required=False)


class XMLFileUploadForm(forms.Form):
    "Form for XML uploads."
    spreadsheet = forms.FileField()
    xml_studentid = forms.CharField()
    xml_fname = forms.CharField()
    xml_lname = forms.CharField()
    xml_grade = forms.CharField(required=False)
    xml_teacher = forms.CharField(required=False)
    xml_nickname = forms.CharField(required=False)
    xml_email = forms.CharField(required=False)


class StudentLogOutForm(forms.Form):
    "Form for student logouts"
    student_id = forms.IntegerField()


class StudentCreationForm(forms.Form):
    "Form for creating students."
    crud_studentid = forms.IntegerField()
    crud_fname = forms.CharField()
    crud_lastname = forms.CharField()
    crud_nickname = forms.CharField(required=False)
    crud_teacher = forms.CharField(required=False)
    crud_grade = forms.CharField(required=False)
    crud_email = forms.EmailField(required=False)