from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/', null=True, blank=True, max_length=500)
    audio_link = models.CharField(max_length=500, null=True, blank=True)  
    image = models.ImageField(upload_to='covers/', null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    
    def get_audio_url(self):
        """Return the audio URL - either from uploaded file or external link"""
        if self.audio_file:
            return self.audio_file.url
        elif self.audio_link:
            return self.audio_link
        return None
    
    def get_image_url(self):
        """Return the cover image URL"""
        if self.image:
            return self.image.url
        return None
    
    def __str__(self):
        return f"{self.title} - {self.artist}"
    
    class Meta:
        ordering = ['title']
        verbose_name = "Song"
        verbose_name_plural = "Songs"