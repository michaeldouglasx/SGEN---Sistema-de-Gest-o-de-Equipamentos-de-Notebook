from django import forms
from accounts.models import User

class CadastroForm(forms.Form):
    fullname = forms.CharField(max_length=150)
    email_pessoal = forms.EmailField(max_length=150)
    email_academico = forms.EmailField( max_length=150 )
    phone = forms.CharField(max_length=15)
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Crie sua Senha",
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirme sua senha",
        min_length=8)

    def save(self):
        user = User(
            fullname = self.cleaned_data['fullname'],
            email_pessoal = self.cleaned_data['email_pessoal'],
            email_academico = self.cleaned_data['email_academico'],
            phone = self.cleaned_data['phone'],
            username =self.cleaned_data['email_academico']
        )
        senha = self.cleaned_data.get("password")
        user.set_password(senha)
        user.save()
        return user

        
    
    def clean_email_academico(self):
        email = self.cleaned_data.get('email_academico')
        if User.objects.filter(email_academico=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado no SGEN')
        return email
    
    def clean(self):
        senha_digitada = self.cleaned_data.get("password")
        confirmacao_de_senha_digitada = self.cleaned_data.get("confirm_password")

        if senha_digitada != confirmacao_de_senha_digitada:
            raise forms.ValidationError("Senhas não são idênticas")
        else:
            return self.cleaned_data
        