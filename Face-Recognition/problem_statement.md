# Goal:

## Given:
    user is able to get event photos from their selfie
    user is able to identify the related people photos


## Detailed goals:

Upload-Photo-Batch:
     - user is able to upload photos
     - System should identify the faces in the photo and tag it to respective person (based on confidence level!)
     - Photo must be categorized and tagged for the person identified in that
     - k images can be uploaded at max
     - Define image size (min quality, max quality, min size, max size, image formats supported)
     - 

Recognize-Photo-Real-time:
   - For given photo, identify the face in the photo
   - If one face
        - Show user name
        - Give link for more pictures
   - If multiple faces
        - Show user names
        - Give link for more pictures


## Constraints:
    User will at max 10k images in single request

