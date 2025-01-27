from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class StaffRequiredMixin(UserPassesTestMixin):
    """
    Vérifie que l'utilisateur est une licorne et redirige vers le profil sinon
    """
    def test_func(self):
        print("C'est lààààààààààààààààààààààààààààà !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('profil') 