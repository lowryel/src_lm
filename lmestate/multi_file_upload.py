# a function to upload multiple images
def handle_uploaded_file(f):
    with open("/img", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
