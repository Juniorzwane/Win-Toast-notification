from plyer import notification


title = "Notification"
message = "This is the message you want to display."


notification.notify(
    title=title,
    message=message,
    app_name="Appname", 
    timeout=10  # Optional: Time
)
