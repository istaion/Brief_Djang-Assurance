from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class StaffRequiredMixin(UserPassesTestMixin):
    """
    Vérifie que l'utilisateur est une licorne et redirige vers le profil sinon
    """
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('profil') 
    
class UserRequiredMixin(UserPassesTestMixin):
    """
    Vérifie que l'utilisateur n'est pas un membre du staff et redirige vers le profil si c'est le cas.
    """
    def test_func(self):
        return not self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('profil')