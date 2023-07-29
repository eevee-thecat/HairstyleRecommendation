import face_recognition


def get_face_shape(file_path):
    image = face_recognition.load_image_file(file_path)
    face_locations = face_recognition.face_locations(image)
    if not face_locations:
        print("Could not find face in picture, please choose another picture!")
        exit(1)
    elif len(face_locations) > 1:
        print("Found more than one face in picture, please crop the picture to one face!")
        exit(1)

    face_location = face_locations[0]
    top, right, bottom, left = face_location
    height = bottom - top
    width = right - left

    # Oval face if height >= 1.2x width
    if height >= 1.2 * width:
        return "oval"
    else:
        return "round"


def main():
    file_path = input("Please enter the file path to your selfie:\n")
    face_shape = get_face_shape(file_path)
    recommended_styles(face_shape)

def recommended_styles(face_shape):
    if face_shape == "round":
        print("""You have a round face. This means that you have prominent round cheeks and the width and length of your face is similar.
        
To best highlight your features, we recommend you get a haircut with angles to help elongate the face. Examples of good hairstyles for your face shape include: 
    - Soft waves to add body and volume 
    - Lob or a blunt cut
    - Pixie cut
    - Medium-length shaggy hair
    - Long hair with side bangs
    - Face-framing layers""")
    elif face_shape == "oval":
        print("""You have an oval face. This means that the length of your face is approximately 1.5x the width of your face.

The oval face shape is the most versatile when it comes to hairstyles! Examples of good hairstyles for your face shape include: 
    - Short bob
    - Curtain bangs or long side-swept bangs
    - Side parts
    - Straight cut
    - Long waves""")


if __name__ == "__main__":
    main()
