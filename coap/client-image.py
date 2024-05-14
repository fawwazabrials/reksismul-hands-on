import cv2
import numpy as np
import asyncio
from aiocoap import Context, Message, POST

async def capture_and_send_image():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is captured correctly
    if not ret:
        print("Error: Could not capture frame")
        return

    # Release the webcam
    cap.release()

    # Encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', frame)

    # Convert numpy array to bytes
    img_bytes = img_encoded.tobytes()

    # Create CoAP context
    context = await Context.create_client_context()

    # Create CoAP message
    request = Message(code=POST, payload=img_bytes)
    request.set_request_uri('coap://127.0.0.1/capture_image')

    try:
        response = await context.request(request).response
        print("Image sent to server successfully!")
        print("Response: %s\n%r" % (response.code, response.payload))
    except Exception as e:
        print("Failed to send image to server: %s" % e)

if __name__ == "__main__":
    asyncio.run(capture_and_send_image())
