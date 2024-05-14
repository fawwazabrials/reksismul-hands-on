import asyncio
from aiocoap import Context, Message
from aiocoap.resource import Resource, Site

class CaptureImageResource(Resource):
    async def render_post(self, request):
        # Receive image from client
        img_bytes = request.payload

        # Save image locally (optional)
        with open('received_image.jpg', 'wb') as f:
            f.write(img_bytes)

        print("Image received from client and saved successfully!")

        return Message(payload=b"Image received successfully!")

class CaptureVideoResource(Resource):
    async def render_post(self, request):
        # Receive video from client
        video_data = request.payload

        # Save video locally (optional)
        with open('received_video.avi', 'wb') as f:
            f.write(video_data)

        print("Video received from client and saved successfully!")

        return Message(payload=b"Video received successfully!")

async def main():
    # Create CoAP context
    site=Site()
    site.add_resource(('capture_image',), CaptureImageResource())
    site.add_resource(('capture_video',), CaptureVideoResource())

    bind = ("127.0.0.1", 5683)
    context = await Context.create_server_context(site, bind=bind)

    print("CoAP server started on {}:{}".format(bind[0], bind[1]))

    # Run CoAP server
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
