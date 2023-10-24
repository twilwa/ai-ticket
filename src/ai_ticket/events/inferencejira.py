# ai_ticket.events.jira_inference

import ai_ticket.backends.pyjira
ai_ticket.backends.pyjira.load_env() #setup standard env

def get_existing_ticket(event):
    return get_backend().get_existing_ticket(event)

def get_backend():
    return ai_ticket.backends.pyjira

def create_new_ticket(event):
    return get_backend().create_new_ticket(event)

def create_new_comment(ticket, event):
    return get_backend().create_new_comment(ticket, event)

def on_event(event):
    ticket = get_existing_ticket(event)
     
    if not ticket:
         # No existing ticket found, create a new one
         ticket = create_new_ticket(event)

    return create_new_comment(ticket, event )