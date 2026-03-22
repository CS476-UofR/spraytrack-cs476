"""
This file will connect the observer pattern to the subjects that we create in the factory.

We will call ready(), after which every call to spray_record_subject.set_state() in our views will trigger update on both observers.
"""
from django.apps import AppConfig


class RecordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #Auto generated primary key 
    name = 'records'                                     #Auto generated app name, must match records 

    def ready(self):
        """
        This is called automatically when Django starts. 
        This just wires everything together.
        """
        from records.observer import (
            spray_record_subject,
            AuditLogObserver,
            LoggingObserver,
        )

        #Now create the observer instances 
        audit_log_observer = AuditLogObserver()
        logging_observer = LoggingObserver()

        #Then register with the subject 
        spray_record_subject.register(audit_log_observer)
        spray_record_subject.register(logging_observer)
