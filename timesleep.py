import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(5)  # Introduce a delay to check synchronous execution
    print("Signal handler finished.")

# Testing the synchronous execution
if __name__ == "__main__":
    print("Creating and saving an object...")
    obj = MyModel(name="Test Object")
    obj.save()  # This should trigger the signal

    print("This line should only print after the signal handler completes.")
