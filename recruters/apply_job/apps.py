from django.apps import AppConfig


class ApplyJobConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apply_job'
    label='apply_job'

    def ready(self):
        import apply_job.update
        apply_job.update.start()
