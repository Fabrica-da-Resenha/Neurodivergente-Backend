from django.db import models
from django.contrib.auth.models import User

class Gender(models.TextChoices):
    feminino = "F", "Feminino"
    masculino = "M", "Masculino"
    alienigina = "A", "Alienigina"

class Profile(models.Model):
    #Usuario a qual o perfil pertence
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(null=False, blank=False)

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.alienigina,
        blank=True
    )
    
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True
    )

    @property
    def followers(self):
        return User.objects.filter(
            following__user_followed=self.user
        )

    @property
    def following(self):
        return User.objects.filter(
            followers__user_follow=self.user
        )
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return f"Perfil de {self.user.username}"