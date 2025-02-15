import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().ident}")

# Testing the execution thread
if __name__ == "__main__":
    print(f"Main execution running in thread: {threading.current_thread().ident}")

    obj = MyModel(name="Test Object")
    obj.save()  # This should trigger the signal
