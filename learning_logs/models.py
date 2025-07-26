from django.db import models
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# defining the entry model
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for the Entry model."""
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"Entry for {self.topic}: {self.text[:50]}..."
