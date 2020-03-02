        #OUTPUT
        message = client.messages.create(
            to = output_number, 
            from_= twilio_number,
            body = 'New tag detected on ' + str(page_link))
        current_count = page_count
    time.sleep(time_wait)
