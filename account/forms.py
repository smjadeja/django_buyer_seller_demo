from django.forms import ModelForm, ValidationError,TextInput, EmailInput
from django import forms
from . models import MyUser,Product
from . widget import DatePickerInput,TimePickerInput, DateTimePickerInput
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['name','dob','email', 'mobile','balance','password','address','user_role']
    
    dob = forms.DateField(widget=DatePickerInput,label='Date of birth')
    def clean(self):
    # data from the form is fetched using super function
        super(UserForm, self).clean()   
        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        mobile = self.cleaned_data.get('mobile')
        print(name)
        # conditions to be met for the username length
        if name == None:
            self._errors['name'] = self.error_class(["Invalid name"])
        elif len(name) < 5:
            self._errors['name'] = self.error_class(['Your name is too short'])
        else:
            for i in name:
                if i.isdigit():
                    self._errors['name'] = self.error_class(['Invalid name'])
        if len(str(mobile)) != 10:
            self._errors['mobile'] = self.error_class([
                'Please enter 10 digit number'])
        # return any errors if found
        return self.cleaned_data


class UserUdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['name','dob','mobile','balance','address']

        error_messages = {
        'name': {'required': _('Please enter name'),},
        'dob': {'required': _('Please enter date of birth'),},
        'mobile': {'required': _('Please add mobile'),},
        'balance': {'required': _('Please add balance'),},
        'address': {'required': _('Please enter address'),},
        }
    
    dob = forms.DateField(widget=DatePickerInput,label='Date of birth')
    def clean(self):
        super(UserUdateForm, self).clean()   
        name = self.cleaned_data.get('name')
        mobile = self.cleaned_data.get('mobile')
        if name == None:
            self._errors['name'] = self.error_class(["Invalid name"])
        elif len(name) < 5:
            self._errors['name'] = self.error_class(['Your name is too short'])
        else:
            for i in name:
                if i.isdigit():
                    self._errors['name'] = self.error_class(['Invalid name'])
        if len(str(mobile)) != 10:
            self._errors['mobile'] = self.error_class([
                'Please enter 10 digit number'])

        return self.cleaned_data

class ChangepassForm(forms.Form):
    old_password = forms.CharField(min_length=6,widget=forms.PasswordInput, error_messages={'required':'Please enter old password'})
    new_password = forms.CharField(min_length=6,widget=forms.PasswordInput,error_messages={'required':'Please enter new password'})

    def clean(self):
        old_pass = self.cleaned_data.get('old_password')
        new_pass = self.cleaned_data.get('new_password')
        
        if old_pass != None and new_pass != None:
            if old_pass == new_pass:
                raise ValidationError('password cant be same')

    

class LoginForm(forms.Form):
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput)

        def clean(self):                
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')

            if email != None and password != None:
                try:
                    user = MyUser.objects.get(email=email)   
                    if user.password != password:
                        self.add_error("password", "Incorrect Password")
                except:
                    self.add_error("email", "Email is not registered...")
            
            return self.cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_desc','product_img','prod_sell_price','prod_cost_price','stock_unit','created_by_user']
        
        widgets = {'created_by_user': forms.HiddenInput()}
    
        prod_sell_price = forms.IntegerField(max_value=1000,min_value=1)
        prod_cost_price = forms.IntegerField(max_value=1000,min_value=1)
        # stock_unit = forms.IntegerField(max_value=10,min_value=1)

        error_messages = {
            'product_name': {'required': _('Please enter product name'),},
            'product_desc': {'required': _('Please enter product description'),},
            'product_img': {'required': _('Please upload an image'),},
            'prod_sell_price': {'required': _('Please enter sell price'),},
            'prod_cost_price': {'required': _('Please enter cost price'),},
            'stock_unit': {'required': _('Please enter stock unit'),},
        }
    
class ProdUpdateForm(forms.ModelForm):
    # product_img = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Product
        fields  = ['product_name','product_desc','product_img','prod_sell_price','prod_cost_price','stock_unit']    

