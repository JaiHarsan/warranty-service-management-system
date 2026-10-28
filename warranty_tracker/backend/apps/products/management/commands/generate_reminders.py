
from django.core.management.base import BaseCommand
from apps.warranties.models import Warranty
from apps.notifications.models import Notification
from apps.warranties.views import calculate_status

class Command(BaseCommand):
    help = 'Generate reminders for expiring warranties'

    def handle(self, *args, **kwargs):
        warranties = Warranty.objects.all()
        for w in warranties:
            status, days = calculate_status(w.end_date)
            if status == "EXPIRING_SOON":
                user = w.product_id.user_id
                title = "Warranty Expiring Soon"
                msg = f"Warranty for {w.product_id.brand} {w.product_id.product_name} expires in {days} days."
                if not Notification.objects(user_id=user, related_product_id=str(w.product_id.id), title=title).first():
                    Notification(user_id=user, type="warranty", title=title, message=msg, related_product_id=str(w.product_id.id)).save()
                    self.stdout.write(f"Generated reminder for {w.product_id.brand} {w.product_id.product_name}")
        self.stdout.write(self.style.SUCCESS('Reminders generated'))

